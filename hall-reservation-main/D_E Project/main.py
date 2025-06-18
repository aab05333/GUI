# ===== Main Application =====
# -*- coding: utf-8 -*-
import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QApplication, QDialog, QMessageBox, QTableWidgetItem, QInputDialog, QHeaderView
)

from db_manegar import db_manegar
from window_manager import WindowManager


class MainWindow(QDialog, WindowManager):
    def __init__(self):
        super().__init__()
        self.db = db_manegar("database.db")
        self.current_user_id = None
        self.current_username = None
        self.is_admin = False
        self.init_login_window()
        self.show_login_window()


    # AUTHENTICATION & SIGNUP
    def handle_login(self):
        username = self.login_ui.usernameLineEdit.text()
        password = self.login_ui.passwordLineEdit.text()
        account = self.db.get_account(username)

        if account and account[2] == password:
            self.current_user_id, self.current_username = account[0], account[1]
            self.is_admin = bool(account[3])  # Check is_admin column
            QMessageBox.information(self.login_window, 'Success', 'Login successful!')
            if self.is_admin:
                self.show_admin_main_page()
            else:
                self.show_main_page()
        else:
            QMessageBox.warning(self.login_window, 'Error', 'Invalid username or password')

    def handle_admin_login(self):
        username = self.admin_login_ui.usernameLineEdit.text()
        password = self.admin_login_ui.passwordLineEdit.text()
        account = self.db.get_account(username)

        if account and account[2] == password and bool(account[3]):
            self.current_user_id, self.current_username = account[0], account[1]
            self.is_admin = True
            QMessageBox.information(self.admin_login_window, 'Success', 'Admin login successful!')
            self.show_admin_main_page()
        else:
            QMessageBox.warning(self.admin_login_window, 'Error', 'Invalid admin credentials')

    def handle_signup(self):
        username = self.signup_ui.usernameLineEdit.text()
        password = self.signup_ui.passwordLineEdit.text()
        confirm = self.signup_ui.ConfirmPasswordLineEdit.text()
        is_admin = self.signup_ui.AdminSignUpRadioButton.isChecked()

        if not username or not password or password != confirm:
            QMessageBox.warning(self.signup_window, 'Error', 'Please fill fields correctly')
            return

        # Pass `is_admin` to your account creation method
        if not self.db.add_account(username, password, is_admin=is_admin):
            QMessageBox.warning(self.signup_window, 'Error', 'Username already exists')
            return

        QMessageBox.information(self.signup_window, 'Success',
                                'Admin account created!' if is_admin else 'Account created successfully!')
        self.show_login_window()

    def logout(self):
        self.current_user_id = None; self.current_username = None; self.is_admin = False
        self.show_login_window()

    # HALL MANAGEMENT
    def add_hall(self):
        name, ok1 = QInputDialog.getText(self.manage_halls_page, 'Add Hall', 'Enter Name:')
        if not ok1 or not name: return
        capacity, ok2 = QInputDialog.getInt(self.manage_halls_page, 'Add Hall', 'Capacity:', 100)
        if not ok2: return
        price, ok3 = QInputDialog.getInt(self.manage_halls_page, 'Add Hall', 'Price/hr:', 100)
        if not ok3: return
        self.db.add_hall(name, capacity, price)
        QMessageBox.information(self.manage_halls_page, 'Success', 'Hall added!')
        self.populate_halls_table()

    def edit_hall(self):
        row = self.manage_halls_ui.hallTable.currentRow()
        if row < 0: QMessageBox.warning(self.manage_halls_page,'Error','Select a hall'); return
        hall_id = int(self.manage_halls_ui.hallTable.item(row,0).text())
        name,ok1=QInputDialog.getText(self.manage_halls_page,'Edit Hall','New Name:',text=self.manage_halls_ui.hallTable.item(row,1).text())
        if not ok1: return
        cap,ok2=QInputDialog.getInt(self.manage_halls_page,'Edit Hall','New Capacity:',value=int(self.manage_halls_ui.hallTable.item(row,2).text()))
        if not ok2: return
        price,ok3=QInputDialog.getInt(self.manage_halls_page,'Edit Hall','New Price/hr:',value=int(self.manage_halls_ui.hallTable.item(row,3).text()))
        if not ok3: return
        self.db.update_hall(hall_id,name,cap,price)
        QMessageBox.information(self.manage_halls_page,'Success','Hall updated!')
        self.populate_halls_table()

    def delete_hall(self):
        row=self.manage_halls_ui.hallTable.currentRow()
        if row<0: QMessageBox.warning(self.manage_halls_page,'Error','Select a hall'); return
        if QMessageBox.question(self.manage_halls_page,'Confirm','Delete this hall?',QMessageBox.Yes|QMessageBox.No)==QMessageBox.Yes:
            hid=int(self.manage_halls_ui.hallTable.item(row,0).text())
            self.db.delete_hall(hid)
            QMessageBox.information(self.manage_halls_page,'Success','Hall deleted')
            self.populate_halls_table()

    # RESERVATION MANAGEMENT
    def handle_reservation(self):
        txt=self.make_reservation_ui.hallComboBox.currentText()
        if not txt: QMessageBox.warning(self.make_reservation_page,'Error','No halls'); return
        hall_id=int(txt.split('(ID: ')[1][:-1])
        date=self.make_reservation_ui.dateEdit.date().toString('yyyy-MM-dd')
        dur=self.make_reservation_ui.durationSpinBox.value()
        price_per_hour=next((h[3] for h in self.db.get_halls() if h[0]==hall_id),0)
        total=dur*price_per_hour
        self.pending_res={'hall_id':hall_id,'hall_name':next(h[1] for h in self.db.get_halls() if h[0]==hall_id),'date':date,'duration':dur,'total_price':total}
        self.show_payment_page(self.pending_res)

    def delete_reservation(self):
        row=self.view_reservations_ui.reservationsTable.currentRow()
        if row<0: QMessageBox.warning(self.view_reservations_page,'Error','Select reservation'); return
        if QMessageBox.question(self.view_reservations_page,'Confirm','Delete reservation?',QMessageBox.Yes|QMessageBox.No)==QMessageBox.Yes:
            rid=int(self.view_reservations_ui.reservationsTable.item(row,0).text())
            self.db.delete_reservation(rid)
            QMessageBox.information(self.view_reservations_page,'Success','Deleted')
            self.populate_reservations_table()

    def edit_reservation(self):
        row=self.view_reservations_ui.reservationsTable.currentRow()
        if row<0: QMessageBox.warning(self.view_reservations_page,'Error','Select reservation'); return
        rid=int(self.view_reservations_ui.reservationsTable.item(row,0).text())
        old=self.view_reservations_ui.reservationsTable.item(row,2).text()
        new,ok=QInputDialog.getText(self.view_reservations_page,'Edit','New date:',text=old)
        if not ok: return
        self.db.update_reservation(rid,new)
        QMessageBox.information(self.view_reservations_page,'Success','Updated')
        self.populate_reservations_table()

    def admin_cancel_reservation(self):
        row=self.manage_reservations_ui.reservationsTable.currentRow()
        if row<0: QMessageBox.warning(self.manage_reservations_page,'Error','Select reservation'); return
        rid=int(self.manage_reservations_ui.reservationsTable.item(row,0).text())
        self.db.cancel_reservation(rid)
        QMessageBox.information(self.manage_reservations_page,'Success','Canceled')
        self.populate_all_reservations_table()

    def admin_reschedule_reservation(self):
        row=self.manage_reservations_ui.reservationsTable.currentRow()
        if row<0: QMessageBox.warning(self.manage_reservations_page,'Error','Select reservation'); return
        rid=int(self.manage_reservations_ui.reservationsTable.item(row,0).text())
        old=self.manage_reservations_ui.reservationsTable.item(row,3).text()
        new,ok=QInputDialog.getText(self.manage_reservations_page,'Reschedule','New date:',text=old)
        if not ok: return
        self.db.update_reservation(rid,new)
        QMessageBox.information(self.manage_reservations_page,'Success','Rescheduled')
        self.populate_all_reservations_table()

    # PAYMENT PROCESSING
    def process_payment(self):
        QMessageBox.information(self.payment_page,'Processing','Please wait...')
        res_id=self.db.add_reservation(self.current_user_id,self.pending_res['hall_id'],self.pending_res['date'],self.pending_res['duration'],'Confirmed')
        self.db.add_transaction(self.current_user_id,res_id,self.pending_res['total_price'])
        QTimer.singleShot(1500,self.show_payment_confirmation)

    def show_payment_confirmation(self):
        self.payment_ui.confirmationFrame.show()
        QTimer.singleShot(3000,self.show_main_page)

    # TABLE POPULATION
    def populate_halls_combobox(self):
        self.make_reservation_ui.hallComboBox.clear()
        for hid,name,cap,price in self.db.get_halls():
            self.make_reservation_ui.hallComboBox.addItem(f"{name} (ID: {hid})")

    def populate_reservations_table(self):
        rows=self.db.get_reservations_by_user(self.current_user_id)
        table=self.view_reservations_ui.reservationsTable
        table.setRowCount(len(rows)); table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["ID","Hall","Date","Duration","Status","Price"])
        halls={hid:price for hid,_,_,price in self.db.get_halls()}
        for r,rowdata in enumerate(rows):
            rid,hn,date,dur,status=rowdata
            price=dur*halls.get(next(hid for hid,name,_,_ in self.db.get_halls() if name==hn),0)
            table.setItem(r,0,QTableWidgetItem(str(rid)))
            table.setItem(r,1,QTableWidgetItem(hn))
            table.setItem(r,2,QTableWidgetItem(date))
            table.setItem(r,3,QTableWidgetItem(str(dur)))
            table.setItem(r,4,QTableWidgetItem(status))
            table.setItem(r,5,QTableWidgetItem(f"${price:.2f}"))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def populate_halls_table(self):
        rows=self.db.get_halls()
        table=self.manage_halls_ui.hallTable
        table.setRowCount(len(rows)); table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID","Name","Capacity","Price/hr"])
        for r,(hid,name,cap,price) in enumerate(rows):
            for c,val in enumerate((hid,name,cap,price)):
                table.setItem(r,c,QTableWidgetItem(str(val)))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def populate_all_reservations_table(self):
        rows=self.db.get_all_reservations()
        table=self.manage_reservations_ui.reservationsTable
        table.setRowCount(len(rows)); table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["ID","User","HallID","Date","Duration","Status"])
        for r,rowdata in enumerate(rows):
            for c,val in enumerate(rowdata):
                table.setItem(r,c,QTableWidgetItem(str(val)))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def populate_transactions_table(self):
        rows=self.db.get_transactions()
        table=self.payment_transactions_ui.transactionsTable
        table.setRowCount(len(rows)); table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["TxnID","User","ResID","Amount","Date"])
        for r,rowdata in enumerate(rows):
            for c,val in enumerate(rowdata):
                table.setItem(r,c,QTableWidgetItem(str(val)))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setStyle("Fusion")
    window=MainWindow()
    sys.exit(app.exec())
