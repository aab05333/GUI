# ===== Main Application =====
# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QMessageBox, QTableWidgetItem, QInputDialog, QHeaderView
)
from PySide6.QtCore import QTimer, QDate

# Import all the UI files
# Make sure you have run the `pyside6-uic` command on your .ui files
# to generate these Python files.
from PY.AdminLogin import Ui_Dialog as AdminLoginUI
from PY.AdminMainPage import Ui_Dialog as AdminMainUI
from PY.Login import Ui_Dialog as LoginUI
from PY.MainPage import Ui_Dialog as MainPageUI
from PY.MakeReservation import Ui_ReservationView as MakeReservationUI
from PY.ManageHall import Ui_HallView as ManageHallUI
from PY.ManageReservations import Ui_MyReservationsView as ManageReservationsUI
from PY.PaymentPage import Ui_PaymentPage as PaymentPageUI
from PY.PaymentTransactions import Ui_PaymentTransactions as PaymentTransactionsUI
from PY.Signup import Ui_Dialog as SignupUI
from PY.ViewReservations import Ui_ViewReservation as ViewReservationsUI


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.current_user = None  # Store current logged in user
        self.is_admin = False  # Flag for admin status

        # ==================== IN-MEMORY DATA (REPLACE WITH DATABASE) ====================
        # This is placeholder data. A real application would load this from a database.
        self.users_data = {
            "user": "password",
            "admin": "admin123"
        }
        self.halls_data = [
            ["1", "Grand Hall", "200", "150"],
            ["2", "Garden Pavilion", "100", "100"],
            ["3", "Skyline Room", "120", "250"]
        ]  # [ID, Name, Capacity, Price/Hour]

        self.reservations_data = [
            ["1", "user", "1", "2025-07-20", "4", "Confirmed"],
            ["2", "user", "2", "2025-08-15", "6", "Confirmed"],
        ]  # [ID, Username, Hall ID, Date, Duration, Status]

        self.transactions_data = [
            ["TXN-001", "user", "Grand Hall - 2025-07-20", "600.00", "2025-06-10"],
            ["TXN-002", "user", "Garden Pavilion - 2025-08-15", "600.00", "2025-06-12"],
        ]  # [ID, Username, Details, Amount, Date]
        # ==============================================================================

        # Initialize all windows but don't show them yet
        self.init_login_window()
        self.show_login_window()

    # ==============================================================================
    # =========================== INITIALIZE ALL WINDOWS ===========================
    # ==============================================================================

    def init_login_window(self):
        self.login_window = QDialog()
        self.login_ui = LoginUI()
        self.login_ui.setupUi(self.login_window)
        self.login_ui.loginButton.clicked.connect(self.handle_login)
        self.login_ui.AdminLoginPageButton.clicked.connect(self.show_admin_login)
        self.login_ui.SignUpPageButton.clicked.connect(self.show_signup_window)

    def init_admin_login_window(self):
        self.admin_login_window = QDialog()
        self.admin_login_ui = AdminLoginUI()
        self.admin_login_ui.setupUi(self.admin_login_window)
        self.admin_login_ui.loginButton.clicked.connect(self.handle_admin_login)
        self.admin_login_ui.UserLoginPageButton.clicked.connect(self.show_login_window)

    def init_signup_window(self):
        self.signup_window = QDialog()
        self.signup_ui = SignupUI()
        self.signup_ui.setupUi(self.signup_window)
        self.signup_ui.SignupButton.clicked.connect(self.handle_signup)
        self.signup_ui.LoginPageButton.clicked.connect(self.show_login_window)

    def init_main_page(self):
        self.main_page = QDialog()
        self.main_page_ui = MainPageUI()
        self.main_page_ui.setupUi(self.main_page)
        self.main_page_ui.MakeReservationPageButton.clicked.connect(self.show_make_reservation)
        self.main_page_ui.ViewReservationPageButton.clicked.connect(self.show_view_reservations)
        self.main_page_ui.LogoutButton.clicked.connect(self.logout)

    def init_admin_main_page(self):
        self.admin_main_page = QDialog()
        self.admin_main_page_ui = AdminMainUI()
        self.admin_main_page_ui.setupUi(self.admin_main_page)
        self.admin_main_page_ui.ManageHallsButton.clicked.connect(self.show_manage_halls)
        self.admin_main_page_ui.VeiwAllReservationsButton.clicked.connect(self.show_manage_reservations)
        self.admin_main_page_ui.ViewTransactionsButton.clicked.connect(self.show_payment_transactions)
        self.admin_main_page_ui.LogoutButton.clicked.connect(self.logout)

    def init_make_reservation(self):
        self.make_reservation_page = QDialog()
        self.make_reservation_ui = MakeReservationUI()
        self.make_reservation_ui.setupUi(self.make_reservation_page)
        self.make_reservation_ui.reserveButton.clicked.connect(self.handle_reservation)
        self.make_reservation_ui.BackButton.clicked.connect(self.show_main_page)
        self.make_reservation_ui.dateEdit.setDate(QDate.currentDate())
        self.make_reservation_ui.dateEdit.setMinimumDate(QDate.currentDate())

    def init_view_reservations(self):
        self.view_reservations_page = QDialog()
        self.view_reservations_ui = ViewReservationsUI()
        self.view_reservations_ui.setupUi(self.view_reservations_page)
        self.view_reservations_ui.btnBack.clicked.connect(self.show_main_page)
        self.view_reservations_ui.btnDeleteReservation.clicked.connect(self.delete_reservation)
        self.view_reservations_ui.btnEditReservation.clicked.connect(self.edit_reservation)

    def init_manage_halls(self):
        self.manage_halls_page = QDialog()
        self.manage_halls_ui = ManageHallUI()
        self.manage_halls_ui.setupUi(self.manage_halls_page)
        self.manage_halls_ui.backButton.clicked.connect(self.show_admin_main_page)
        self.manage_halls_ui.addHallButton.clicked.connect(self.add_hall)
        self.manage_halls_ui.editHallButton.clicked.connect(self.edit_hall)
        self.manage_halls_ui.deleteHallButton.clicked.connect(self.delete_hall)

    def init_manage_reservations(self):
        self.manage_reservations_page = QDialog()
        self.manage_reservations_ui = ManageReservationsUI()
        self.manage_reservations_ui.setupUi(self.manage_reservations_page)
        self.manage_reservations_ui.backButton.clicked.connect(self.show_admin_main_page)
        self.manage_reservations_ui.cancelButton.clicked.connect(self.admin_cancel_reservation)
        self.manage_reservations_ui.rescheduleButton.clicked.connect(self.admin_reschedule_reservation)

    def init_payment_transactions(self):
        self.payment_transactions_page = QDialog()
        self.payment_transactions_ui = PaymentTransactionsUI()
        self.payment_transactions_ui.setupUi(self.payment_transactions_page)
        self.payment_transactions_ui.backButton.clicked.connect(self.show_admin_main_page)

    def init_payment_page(self):
        self.payment_page = QDialog()
        self.payment_ui = PaymentPageUI()
        self.payment_ui.setupUi(self.payment_page)
        self.payment_ui.payButton.clicked.connect(self.process_payment)
        self.payment_ui.backButton.clicked.connect(self.show_make_reservation)
        self.payment_ui.confirmationFrame.hide()

    # ========================================================================
    # =========================== WINDOW NAVIGATION ==========================
    # ========================================================================

    def show_login_window(self):
        self.close_all_windows()
        if not hasattr(self, 'login_window'): self.init_login_window()
        self.login_window.show()

    def show_admin_login(self):
        self.close_all_windows()
        if not hasattr(self, 'admin_login_window'): self.init_admin_login_window()
        self.admin_login_window.show()

    def show_signup_window(self):
        self.close_all_windows()
        if not hasattr(self, 'signup_window'): self.init_signup_window()
        self.signup_window.show()

    def show_main_page(self):
        self.close_all_windows()
        if not hasattr(self, 'main_page'): self.init_main_page()
        self.main_page.show()

    def show_admin_main_page(self):
        self.close_all_windows()
        if not hasattr(self, 'admin_main_page'): self.init_admin_main_page()
        self.admin_main_page.show()

    def show_make_reservation(self):
        self.close_all_windows()
        if not hasattr(self, 'make_reservation_page'): self.init_make_reservation()
        self.populate_halls_combobox()
        self.make_reservation_page.show()

    def show_view_reservations(self):
        self.close_all_windows()
        if not hasattr(self, 'view_reservations_page'): self.init_view_reservations()
        self.populate_reservations_table()
        self.view_reservations_page.show()

    def show_manage_halls(self):
        self.close_all_windows()
        if not hasattr(self, 'manage_halls_page'): self.init_manage_halls()
        self.populate_halls_table()
        self.manage_halls_page.show()

    def show_manage_reservations(self):
        self.close_all_windows()
        if not hasattr(self, 'manage_reservations_page'): self.init_manage_reservations()
        self.populate_all_reservations_table()
        self.manage_reservations_page.show()

    def show_payment_transactions(self):
        self.close_all_windows()
        if not hasattr(self, 'payment_transactions_page'): self.init_payment_transactions()
        self.populate_transactions_table()
        self.payment_transactions_page.show()

    def show_payment_page(self, reservation_details):
        self.close_all_windows()
        if not hasattr(self, 'payment_page'): self.init_payment_page()
        # Pass details to payment page
        hall_name = reservation_details["hall_name"]
        total_price = reservation_details["total_price"]
        self.payment_ui.reservationInfoLabel.setText(f"Hall: {hall_name}")
        self.payment_ui.amountValueLabel.setText(f"Total: ${total_price:.2f}")
        self.payment_page.show()

    def close_all_windows(self):
        for window in [
            'login_window', 'admin_login_window', 'signup_window',
            'main_page', 'admin_main_page', 'make_reservation_page',
            'view_reservations_page', 'manage_halls_page',
            'manage_reservations_page', 'payment_transactions_page',
            'payment_page'
        ]:
            if hasattr(self, window):
                getattr(self, window).hide()

    # ========================================================================
    # ======================== AUTHENTICATION & LOGOUT =======================
    # ========================================================================

    def handle_login(self):
        username = self.login_ui.usernameLineEdit.text()
        password = self.login_ui.passwordLineEdit.text()

        # DATABASE: Fetch user from the database by username
        if username in self.users_data and self.users_data[username] == password:
            self.current_user = username
            self.is_admin = (username == "admin")  # Simple admin check
            QMessageBox.information(self.login_window, "Success", "Login successful!")
            if self.is_admin:
                self.show_admin_main_page()
            else:
                self.show_main_page()
        else:
            QMessageBox.warning(self.login_window, "Error", "Invalid username or password")

    def handle_admin_login(self):
        username = self.admin_login_ui.usernameLineEdit.text()
        password = self.admin_login_ui.passwordLineEdit.text()

        # DATABASE: Fetch user and check if they have admin privileges
        if username == "admin" and self.users_data.get(username) == password:
            self.current_user = username
            self.is_admin = True
            QMessageBox.information(self.admin_login_window, "Success", "Admin login successful!")
            self.show_admin_main_page()
        else:
            QMessageBox.warning(self.admin_login_window, "Error", "Invalid admin credentials")

    def handle_signup(self):
        username = self.signup_ui.usernameLineEdit.text()
        password = self.signup_ui.passwordLineEdit.text()
        confirm_password = self.signup_ui.ConfirmPasswordLineEdit.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self.signup_window, "Error", "Please fill in all fields")
            return
        if password != confirm_password:
            QMessageBox.warning(self.signup_window, "Error", "Passwords do not match")
            return
        # DATABASE: Check if username already exists in the database
        if username in self.users_data:
            QMessageBox.warning(self.signup_window, "Error", "Username already exists")
            return

        # DATABASE: INSERT the new user into the database. Remember to HASH the password!
        self.users_data[username] = password
        QMessageBox.information(self.signup_window, "Success", "Account created successfully!")
        self.show_login_window()

    def logout(self):
        self.current_user = None
        self.is_admin = False
        self.show_login_window()

    # ========================================================================
    # ========================= HALL MANAGEMENT (Admin) ======================
    # ========================================================================

    def add_hall(self):
        # Get input from admin
        name, ok1 = QInputDialog.getText(self.manage_halls_page, "Add Hall", "Enter Hall Name:")
        if not ok1 or not name: return

        capacity, ok2 = QInputDialog.getInt(self.manage_halls_page, "Add Hall", "Enter Capacity:", 100)
        if not ok2: return

        price, ok3 = QInputDialog.getInt(self.manage_halls_page, "Add Hall", "Enter Price per Hour ($):", 100)
        if not ok3: return

        # Create new hall data
        new_id = str(int(self.halls_data[-1][0]) + 1) if self.halls_data else "1"
        new_hall = [new_id, name, str(capacity), str(price)]

        # DATABASE: INSERT the new_hall data into the 'halls' table
        self.halls_data.append(new_hall)

        QMessageBox.information(self.manage_halls_page, "Success", "Hall added successfully!")
        self.populate_halls_table()

    def edit_hall(self):
        selected_row = self.manage_halls_ui.hallTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.manage_halls_page, "Error", "Please select a hall to edit.")
            return

        # Get the ID of the hall to edit
        hall_id = self.manage_halls_ui.hallTable.item(selected_row, 0).text()

        # Get new data
        name, ok1 = QInputDialog.getText(self.manage_halls_page, "Edit Hall", "Enter New Name:",
                                         text=self.manage_halls_ui.hallTable.item(selected_row, 1).text())
        if not ok1 or not name: return

        capacity, ok2 = QInputDialog.getInt(self.manage_halls_page, "Edit Hall", "Enter New Capacity:",
                                            value=int(self.manage_halls_ui.hallTable.item(selected_row, 2).text()))
        if not ok2: return

        price, ok3 = QInputDialog.getInt(self.manage_halls_page, "Edit Hall", "Enter New Price per Hour ($):",
                                         value=int(self.manage_halls_ui.hallTable.item(selected_row, 3).text()))
        if not ok3: return

        # DATABASE: UPDATE the hall in the database where id = hall_id
        for hall in self.halls_data:
            if hall[0] == hall_id:
                hall[1] = name
                hall[2] = str(capacity)
                hall[3] = str(price)
                break

        QMessageBox.information(self.manage_halls_page, "Success", "Hall updated successfully!")
        self.populate_halls_table()

    def delete_hall(self):
        selected_row = self.manage_halls_ui.hallTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.manage_halls_page, "Error", "Please select a hall to delete.")
            return

        reply = QMessageBox.question(self.manage_halls_page, 'Confirm Delete',
                                     'Are you sure you want to delete this hall?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            hall_id_to_delete = self.manage_halls_ui.hallTable.item(selected_row, 0).text()

            # DATABASE: DELETE from 'halls' table where id = hall_id_to_delete
            self.halls_data = [hall for hall in self.halls_data if hall[0] != hall_id_to_delete]

            self.populate_halls_table()
            QMessageBox.information(self.manage_halls_page, "Success", "Hall deleted.")

    # ========================================================================
    # ======================= RESERVATION MANAGEMENT =========================
    # ========================================================================

    def handle_reservation(self):
        hall_item_text = self.make_reservation_ui.hallComboBox.currentText()
        if not hall_item_text:
            QMessageBox.warning(self.make_reservation_page, "Error", "No halls available for reservation.")
            return

        hall_id = hall_item_text.split(" (ID: ")[1][:-1]
        date = self.make_reservation_ui.dateEdit.date().toString("yyyy-MM-dd")
        duration = self.make_reservation_ui.durationSpinBox.value()

        # Find hall price
        price_per_hour = 100  # default
        hall_name = ""
        for hall in self.halls_data:
            if hall[0] == hall_id:
                price_per_hour = int(hall[3])
                hall_name = hall[1]
                break

        # For now, just show the payment page.
        # A real app would first save the reservation with a "Pending" status.
        reservation_details = {
            "hall_id": hall_id,
            "hall_name": hall_name,
            "date": date,
            "duration": duration,
            "total_price": duration * price_per_hour
        }

        # Store temporary reservation details to be finalized after payment
        self.pending_reservation = reservation_details

        self.show_payment_page(reservation_details)

    def delete_reservation(self):
        selected_row = self.view_reservations_ui.reservationsTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.view_reservations_page, "Error", "Please select a reservation to delete.")
            return

        reply = QMessageBox.question(self.view_reservations_page, 'Confirm Delete',
                                     'Are you sure you want to delete this reservation? This cannot be undone.',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            reservation_id = self.view_reservations_ui.reservationsTable.item(selected_row, 0).text()

            # DATABASE: DELETE from 'reservations' where id = reservation_id
            self.reservations_data = [res for res in self.reservations_data if res[0] != reservation_id]

            self.populate_reservations_table()
            QMessageBox.information(self.view_reservations_page, "Success", "Reservation deleted.")

    def edit_reservation(self):
        selected_row = self.view_reservations_ui.reservationsTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.view_reservations_page, "Error", "Please select a reservation to edit.")
            return

        reservation_id = self.view_reservations_ui.reservationsTable.item(selected_row, 0).text()
        current_date_str = self.view_reservations_ui.reservationsTable.item(selected_row, 2).text()

        # Get new date
        new_date, ok = QInputDialog.getText(self.view_reservations_page, "Edit Reservation",
                                            "Enter new date (YYYY-MM-DD):", text=current_date_str)
        if not ok or not new_date: return

        # DATABASE: UPDATE 'reservations' set date = new_date where id = reservation_id
        for res in self.reservations_data:
            if res[0] == reservation_id:
                res[3] = new_date
                break

        self.populate_reservations_table()
        QMessageBox.information(self.view_reservations_page, "Success", "Reservation date updated.")

    def admin_cancel_reservation(self):
        selected_row = self.manage_reservations_ui.reservationsTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.manage_reservations_page, "Error", "Please select a reservation to cancel.")
            return

        reservation_id = self.manage_reservations_ui.reservationsTable.item(selected_row, 0).text()

        # DATABASE: UPDATE 'reservations' set status = 'Canceled' where id = reservation_id
        for res in self.reservations_data:
            if res[0] == reservation_id:
                res[5] = "Canceled"
                break

        self.populate_all_reservations_table()
        QMessageBox.information(self.manage_reservations_page, "Success", "Reservation has been canceled.")

    def admin_reschedule_reservation(self):
        selected_row = self.manage_reservations_ui.reservationsTable.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.manage_reservations_page, "Error", "Please select a reservation to reschedule.")
            return

        reservation_id = self.manage_reservations_ui.reservationsTable.item(selected_row, 0).text()
        current_date_str = self.manage_reservations_ui.reservationsTable.item(selected_row, 3).text()

        new_date, ok = QInputDialog.getText(self.manage_reservations_page, "Reschedule Reservation",
                                            "Enter new date (YYYY-MM-DD):", text=current_date_str)
        if not ok or not new_date: return

        # DATABASE: UPDATE 'reservations' set date = new_date where id = reservation_id
        for res in self.reservations_data:
            if res[0] == reservation_id:
                res[3] = new_date
                break

        self.populate_all_reservations_table()
        QMessageBox.information(self.manage_reservations_page, "Success", "Reservation has been rescheduled.")

    # ========================================================================
    # ========================== PAYMENT PROCESSING ==========================
    # ========================================================================

    def process_payment(self):
        # In a real app, this would connect to a payment gateway API (Stripe, PayPal, etc.)
        # On success, it would finalize the reservation.

        QMessageBox.information(self.payment_page, "Processing", "Processing payment, please wait...")

        # Finalize reservation after "successful" payment
        new_res_id = str(int(self.reservations_data[-1][0]) + 1) if self.reservations_data else "1"
        res_info = self.pending_reservation
        new_reservation = [
            new_res_id,
            self.current_user,
            res_info["hall_id"],
            res_info["date"],
            str(res_info["duration"]),
            "Confirmed"
        ]

        # DATABASE: INSERT the new_reservation into the 'reservations' table
        self.reservations_data.append(new_reservation)

        # DATABASE: INSERT a new transaction record
        new_txn_id = f"TXN-{len(self.transactions_data) + 1:03d}"
        new_transaction = [
            new_txn_id,
            self.current_user,
            f"{res_info['hall_name']} - {res_info['date']}",
            f"{res_info['total_price']:.2f}",
            QDate.currentDate().toString("yyyy-MM-dd")
        ]
        self.transactions_data.append(new_transaction)

        QTimer.singleShot(1500, self.show_payment_confirmation)

    def show_payment_confirmation(self):
        self.payment_ui.confirmationFrame.show()
        QTimer.singleShot(3000, self.show_main_page)  # Go back to main menu after 3 seconds

    # ========================================================================
    # ======================== TABLE POPULATION ==============================
    # ========================================================================

    def populate_halls_combobox(self):
        self.make_reservation_ui.hallComboBox.clear()
        # DATABASE: SELECT id, name from the 'halls' table
        for hall in self.halls_data:
            self.make_reservation_ui.hallComboBox.addItem(f"{hall[1]} (ID: {hall[0]})")

    def populate_reservations_table(self):
        # DATABASE: SELECT reservations from the database for the self.current_user
        user_reservations = [res for res in self.reservations_data if res[1] == self.current_user]

        table = self.view_reservations_ui.reservationsTable
        table.setRowCount(len(user_reservations))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["ID", "Hall Name", "Date", "Duration (hrs)", "Status", "Price"])

        for row, res_data in enumerate(user_reservations):
            hall_name = "N/A"
            price = 0
            # DATABASE: This would be a JOIN query in a real database
            for hall in self.halls_data:
                if hall[0] == res_data[2]:
                    hall_name = hall[1]
                    price = int(hall[3]) * int(res_data[4])
                    break

            table.setItem(row, 0, QTableWidgetItem(res_data[0]))  # ID
            table.setItem(row, 1, QTableWidgetItem(hall_name))
            table.setItem(row, 2, QTableWidgetItem(res_data[3]))  # Date
            table.setItem(row, 3, QTableWidgetItem(res_data[4]))  # Duration
            table.setItem(row, 4, QTableWidgetItem(res_data[5]))  # Status
            table.setItem(row, 5, QTableWidgetItem(f"${price:.2f}"))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def populate_halls_table(self):
        # DATABASE: SELECT * from the 'halls' table
        table = self.manage_halls_ui.hallTable
        table.setRowCount(len(self.halls_data))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID", "Hall Name", "Capacity", "Price/Hour ($)"])

        for row, hall in enumerate(self.halls_data):
            for col, data in enumerate(hall):
                table.setItem(row, col, QTableWidgetItem(data))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def populate_all_reservations_table(self):
        # DATABASE: SELECT * from the 'reservations' table
        table = self.manage_reservations_ui.reservationsTable
        table.setRowCount(len(self.reservations_data))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(["Res ID", "User", "Hall ID", "Date", "Duration (hrs)", "Status"])

        for row, reservation in enumerate(self.reservations_data):
            for col, data in enumerate(reservation):
                table.setItem(row, col, QTableWidgetItem(data))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def populate_transactions_table(self):
        # DATABASE: SELECT * from the 'transactions' table
        table = self.payment_transactions_ui.transactionsTable
        table.setRowCount(len(self.transactions_data))
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Transaction ID", "User", "Details", "Amount ($)", "Date"])

        for row, transaction in enumerate(self.transactions_data):
            for col, data in enumerate(transaction):
                table.setItem(row, col, QTableWidgetItem(str(data)))
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    sys.exit(app.exec())