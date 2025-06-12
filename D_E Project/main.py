# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QTimer

# Import all the UI files
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

        # Initialize all windows but don't show them yet
        self.init_login_window()
        self.show_login_window()

    def init_login_window(self):
        """Initialize the login window"""
        self.login_window = QDialog()
        self.login_ui = LoginUI()
        self.login_ui.setupUi(self.login_window)

        # Connect buttons
        self.login_ui.loginButton.clicked.connect(self.handle_login)
        self.login_ui.AdminLoginPageButton.clicked.connect(self.show_admin_login)
        self.login_ui.SignUpPageButton.clicked.connect(self.show_signup_window)

    def init_admin_login_window(self):
        """Initialize the admin login window"""
        self.admin_login_window = QDialog()
        self.admin_login_ui = AdminLoginUI()
        self.admin_login_ui.setupUi(self.admin_login_window)

        # Connect buttons
        self.admin_login_ui.loginButton.clicked.connect(self.handle_admin_login)
        self.admin_login_ui.UserLoginPageButton.clicked.connect(self.show_login_window)

    def init_signup_window(self):
        """Initialize the signup window"""
        self.signup_window = QDialog()
        self.signup_ui = SignupUI()
        self.signup_ui.setupUi(self.signup_window)

        # Connect buttons
        self.signup_ui.SignupButton.clicked.connect(self.handle_signup)

    def init_main_page(self):
        """Initialize the main user page"""
        self.main_page = QDialog()
        self.main_page_ui = MainPageUI()
        self.main_page_ui.setupUi(self.main_page)

        # Connect buttons
        self.main_page_ui.MakeReservationPageButton.clicked.connect(self.show_make_reservation)
        self.main_page_ui.ViewReservationPageButton.clicked.connect(self.show_view_reservations)
        self.main_page_ui.LogoutButton.clicked.connect(self.logout)

    def init_admin_main_page(self):
        """Initialize the admin main page"""
        self.admin_main_page = QDialog()
        self.admin_main_page_ui = AdminMainUI()
        self.admin_main_page_ui.setupUi(self.admin_main_page)

        # Connect buttons
        self.admin_main_page_ui.ManageHallsButton.clicked.connect(self.show_manage_halls)
        self.admin_main_page_ui.VeiwAllReservationsButton.clicked.connect(self.show_manage_reservations)
        self.admin_main_page_ui.ViewTransactionsButton.clicked.connect(self.show_payment_transactions)
        self.admin_main_page_ui.LogoutButton.clicked.connect(self.logout)

    def init_make_reservation(self):
        """Initialize the make reservation page"""
        self.make_reservation_page = QDialog()
        self.make_reservation_ui = MakeReservationUI()
        self.make_reservation_ui.setupUi(self.make_reservation_page)

        # Connect buttons
        self.make_reservation_ui.reserveButton.clicked.connect(self.handle_reservation)
        self.make_reservation_ui.BackButton.clicked.connect(self.show_main_page)

        # Dummy data - REPLACE WITH REAL DATA LOADING
        self.make_reservation_ui.hallComboBox.addItems(["Hall A", "Hall B", "Hall C"])

    def init_view_reservations(self):
        """Initialize the view reservations page"""
        self.view_reservations_page = QDialog()
        self.view_reservations_ui = ViewReservationsUI()
        self.view_reservations_ui.setupUi(self.view_reservations_page)

        # Connect buttons
        self.view_reservations_ui.btnBack.clicked.connect(self.show_main_page)
        self.view_reservations_ui.btnDeleteReservation.clicked.connect(self.delete_reservation)
        self.view_reservations_ui.btnEditReservation.clicked.connect(self.edit_reservation)

        # Dummy data - REPLACE WITH REAL DATA LOADING
        self.populate_reservations_table()

    def init_manage_halls(self):
        """Initialize the manage halls page (admin only)"""
        self.manage_halls_page = QDialog()
        self.manage_halls_ui = ManageHallUI()
        self.manage_halls_ui.setupUi(self.manage_halls_page)

        # Connect buttons
        self.manage_halls_ui.backButton.clicked.connect(self.show_admin_main_page)
        self.manage_halls_ui.addHallButton.clicked.connect(self.add_hall)
        self.manage_halls_ui.editHallButton.clicked.connect(self.edit_hall)
        self.manage_halls_ui.deleteHallButton.clicked.connect(self.delete_hall)

        # Dummy data - REPLACE WITH REAL DATA LOADING
        self.populate_halls_table()

    def init_manage_reservations(self):
        """Initialize the manage all reservations page (admin only)"""
        self.manage_reservations_page = QDialog()
        self.manage_reservations_ui = ManageReservationsUI()
        self.manage_reservations_ui.setupUi(self.manage_reservations_page)

        # Connect buttons
        self.manage_reservations_ui.backButton.clicked.connect(self.show_admin_main_page)
        self.manage_reservations_ui.cancelButton.clicked.connect(self.admin_cancel_reservation)
        self.manage_reservations_ui.rescheduleButton.clicked.connect(self.admin_reschedule_reservation)

        # Dummy data - REPLACE WITH REAL DATA LOADING
        self.populate_all_reservations_table()

    def init_payment_transactions(self):
        """Initialize the payment transactions page (admin only)"""
        self.payment_transactions_page = QDialog()
        self.payment_transactions_ui = PaymentTransactionsUI()
        self.payment_transactions_ui.setupUi(self.payment_transactions_page)

        # Connect buttons
        self.payment_transactions_ui.exportButton_2.clicked.connect(self.show_admin_main_page)

        # Dummy data - REPLACE WITH REAL DATA LOADING
        self.populate_transactions_table()

    def init_payment_page(self):
        """Initialize the payment page"""
        self.payment_page = QDialog()
        self.payment_ui = PaymentPageUI()
        self.payment_ui.setupUi(self.payment_page)

        # Connect buttons
        self.payment_ui.payButton.clicked.connect(self.process_payment)
        self.payment_ui.payButton_2.clicked.connect(self.show_make_reservation)

    # ==================== WINDOW NAVIGATION ====================

    def show_login_window(self):
        """Show the login window and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'login_window'):
            self.init_login_window()
        self.login_window.show()

    def show_admin_login(self):
        """Show the admin login window and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'admin_login_window'):
            self.init_admin_login_window()
        self.admin_login_window.show()

    def show_signup_window(self):
        """Show the signup window and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'signup_window'):
            self.init_signup_window()
        self.signup_window.show()

    def show_main_page(self):
        """Show the main user page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'main_page'):
            self.init_main_page()
        self.main_page.show()

    def show_admin_main_page(self):
        """Show the admin main page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'admin_main_page'):
            self.init_admin_main_page()
        self.admin_main_page.show()

    def show_make_reservation(self):
        """Show the make reservation page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'make_reservation_page'):
            self.init_make_reservation()
        self.make_reservation_page.show()

    def show_view_reservations(self):
        """Show the view reservations page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'view_reservations_page'):
            self.init_view_reservations()
        self.view_reservations_page.show()

    def show_manage_halls(self):
        """Show the manage halls page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'manage_halls_page'):
            self.init_manage_halls()
        self.manage_halls_page.show()

    def show_manage_reservations(self):
        """Show the manage all reservations page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'manage_reservations_page'):
            self.init_manage_reservations()
        self.manage_reservations_page.show()

    def show_payment_transactions(self):
        """Show the payment transactions page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'payment_transactions_page'):
            self.init_payment_transactions()
        self.payment_transactions_page.show()

    def show_payment_page(self):
        """Show the payment page and hide others"""
        self.close_all_windows()
        if not hasattr(self, 'payment_page'):
            self.init_payment_page()
        self.payment_page.show()

    def close_all_windows(self):
        """Close all windows except the one we're about to show"""
        windows = [
            'login_window', 'admin_login_window', 'signup_window',
            'main_page', 'admin_main_page', 'make_reservation_page',
            'view_reservations_page', 'manage_halls_page',
            'manage_reservations_page', 'payment_transactions_page',
            'payment_page'
        ]
        for window in windows:
            if hasattr(self, window):
                getattr(self, window).hide()

    # ==================== DUMMY FUNCTIONS - REPLACE THESE ====================

    def handle_login(self):
        """Handle user login - REPLACE WITH REAL AUTHENTICATION"""
        username = self.login_ui.usernameLineEdit.text()
        password = self.login_ui.passwordLineEdit.text()

        if not username or not password:
            QMessageBox.warning(self.login_window, "Error", "Please enter both username and password")
            return

        # Dummy authentication - REPLACE WITH REAL DATABASE CHECK
        if username == "user" and password == "password":
            self.current_user = username
            self.is_admin = False
            self.show_main_page()
        else:
            QMessageBox.warning(self.login_window, "Error", "Invalid username or password")

    def handle_admin_login(self):
        """Handle admin login - REPLACE WITH REAL AUTHENTICATION"""
        username = self.admin_login_ui.usernameLineEdit.text()
        password = self.admin_login_ui.passwordLineEdit.text()

        if not username or not password:
            QMessageBox.warning(self.admin_login_window, "Error", "Please enter both username and password")
            return

        # Dummy authentication - REPLACE WITH REAL DATABASE CHECK
        if username == "admin" and password == "admin123":
            self.current_user = username
            self.is_admin = True
            self.show_admin_main_page()
        else:
            QMessageBox.warning(self.admin_login_window, "Error", "Invalid admin credentials")

    def handle_signup(self):
        """Handle user signup - REPLACE WITH REAL REGISTRATION"""
        username = self.signup_ui.usernameLineEdit.text()
        password = self.signup_ui.passwordLineEdit.text()
        confirm_password = self.signup_ui.ConfirmPasswordLineEdit.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self.signup_window, "Error", "Please fill in all fields")
            return

        if password != confirm_password:
            QMessageBox.warning(self.signup_window, "Error", "Passwords do not match")
            return

        # Dummy registration - REPLACE WITH REAL DATABASE INSERT
        QMessageBox.information(self.signup_window, "Success", "Account created successfully!")
        self.show_login_window()

    def logout(self):
        """Handle logout"""
        self.current_user = None
        self.is_admin = False
        self.show_login_window()

    def handle_reservation(self):
        """Handle making a reservation - REPLACE WITH REAL RESERVATION LOGIC"""
        hall = self.make_reservation_ui.hallComboBox.currentText()
        date = self.make_reservation_ui.dateEdit.date().toString("yyyy-MM-dd")
        duration = self.make_reservation_ui.durationSpinBox.value()

        # Dummy reservation - REPLACE WITH REAL DATABASE INSERT
        QMessageBox.information(self.make_reservation_page, "Success",
                                f"Reservation made for {hall} on {date} for {duration} hours")

        # Show payment page - REPLACE WITH REAL PAYMENT PROCESSING
        self.show_payment_page()

    def delete_reservation(self):
        """Handle deleting a reservation - REPLACE WITH REAL DELETION LOGIC"""
        selected = self.view_reservations_ui.reservationsTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.view_reservations_page, "Error", "Please select a reservation to delete")
            return

        # Dummy deletion - REPLACE WITH REAL DATABASE DELETE
        QMessageBox.information(self.view_reservations_page, "Success", "Reservation deleted")
        self.populate_reservations_table()

    def edit_reservation(self):
        """Handle editing a reservation - REPLACE WITH REAL EDIT LOGIC"""
        selected = self.view_reservations_ui.reservationsTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.view_reservations_page, "Error", "Please select a reservation to edit")
            return

        # Dummy edit - REPLACE WITH REAL DATABASE UPDATE
        QMessageBox.information(self.view_reservations_page, "Info", "Edit functionality to be implemented")

    def add_hall(self):
        """Handle adding a hall - REPLACE WITH REAL ADD LOGIC"""
        QMessageBox.information(self.manage_halls_page, "Info", "Add hall functionality to be implemented")

    def edit_hall(self):
        """Handle editing a hall - REPLACE WITH REAL EDIT LOGIC"""
        selected = self.manage_halls_ui.hallTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.manage_halls_page, "Error", "Please select a hall to edit")
            return

        # Dummy edit - REPLACE WITH REAL DATABASE UPDATE
        QMessageBox.information(self.manage_halls_page, "Info", "Edit hall functionality to be implemented")

    def delete_hall(self):
        """Handle deleting a hall - REPLACE WITH REAL DELETE LOGIC"""
        selected = self.manage_halls_ui.hallTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.manage_halls_page, "Error", "Please select a hall to delete")
            return

        # Dummy deletion - REPLACE WITH REAL DATABASE DELETE
        QMessageBox.information(self.manage_halls_page, "Success", "Hall deleted")
        self.populate_halls_table()

    def admin_cancel_reservation(self):
        """Handle admin canceling a reservation - REPLACE WITH REAL LOGIC"""
        selected = self.manage_reservations_ui.reservationsTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.manage_reservations_page, "Error", "Please select a reservation to cancel")
            return

        # Dummy cancellation - REPLACE WITH REAL DATABASE UPDATE
        QMessageBox.information(self.manage_reservations_page, "Success", "Reservation canceled")
        self.populate_all_reservations_table()

    def admin_reschedule_reservation(self):
        """Handle admin rescheduling a reservation - REPLACE WITH REAL LOGIC"""
        selected = self.manage_reservations_ui.reservationsTable.currentRow()
        if selected == -1:
            QMessageBox.warning(self.manage_reservations_page, "Error", "Please select a reservation to reschedule")
            return

        # Dummy reschedule - REPLACE WITH REAL DATABASE UPDATE
        QMessageBox.information(self.manage_reservations_page, "Info", "Reschedule functionality to be implemented")

    def process_payment(self):
        """Handle payment processing - REPLACE WITH REAL PAYMENT GATEWAY"""
        # Dummy payment processing
        QTimer.singleShot(2000, self.show_payment_confirmation)

    def show_payment_confirmation(self):
        """Show payment confirmation - REPLACE WITH REAL CONFIRMATION"""
        self.payment_ui.confirmationFrame.show()

    # ==================== TABLE POPULATION FUNCTIONS ====================

    def populate_reservations_table(self):
        """Populate reservations table with dummy data - REPLACE WITH REAL DATA"""
        self.view_reservations_ui.reservationsTable.setRowCount(2)

        # Dummy data
        reservations = [
            ["Hall A", "2023-01-15", "2 hours", "$200"],
            ["Hall B", "2023-01-20", "3 hours", "$300"]
        ]

        for row, reservation in enumerate(reservations):
            for col, data in enumerate(reservation):
                self.view_reservations_ui.reservationsTable.setItem(row, col, QTableWidgetItem(data))

    def populate_halls_table(self):
        """Populate halls table with dummy data - REPLACE WITH REAL DATA"""
        self.manage_halls_ui.hallTable.setRowCount(3)

        # Dummy data
        halls = [
            ["Hall A", "Building 1", "100", "$100/hour"],
            ["Hall B", "Building 2", "150", "$150/hour"],
            ["Hall C", "Building 3", "200", "$200/hour"]
        ]

        for row, hall in enumerate(halls):
            for col, data in enumerate(hall):
                self.manage_halls_ui.hallTable.setItem(row, col, QTableWidgetItem(data))

    def populate_all_reservations_table(self):
        """Populate all reservations table with dummy data - REPLACE WITH REAL DATA"""
        self.manage_reservations_ui.reservationsTable.setRowCount(3)

        # Dummy data
        reservations = [
            ["Hall A", "2023-01-10", "2 hours", "Confirmed"],
            ["Hall B", "2023-01-12", "3 hours", "Pending"],
            ["Hall C", "2023-01-15", "4 hours", "Confirmed"]
        ]

        for row, reservation in enumerate(reservations):
            for col, data in enumerate(reservation):
                self.manage_reservations_ui.reservationsTable.setItem(row, col, QTableWidgetItem(data))

    def populate_transactions_table(self):
        """Populate transactions table with dummy data - REPLACE WITH REAL DATA"""
        self.payment_transactions_ui.transactionsTable.setRowCount(3)

        # Dummy data
        transactions = [
            ["TXN-001", "user1", "Hall A - 2023-01-10", "$200", "2023-01-10"],
            ["TXN-002", "user2", "Hall B - 2023-01-12", "$300", "2023-01-12"],
            ["TXN-003", "user3", "Hall C - 2023-01-15", "$400", "2023-01-15"]
        ]

        for row, transaction in enumerate(transactions):
            for col, data in enumerate(transaction):
                self.payment_transactions_ui.transactionsTable.setItem(row, col, QTableWidgetItem(data))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set application style (optional)
    app.setStyle("Fusion")

    window = MainWindow()
    sys.exit(app.exec())