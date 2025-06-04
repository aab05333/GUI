import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox

# Import all your UI files
from AdminLogin import Ui_Dialog as AdminLoginUI
from Login import Ui_Dialog as LoginUI
from Signup import Ui_Dialog as SignupUI
from MainPage import Ui_Dialog as MainPageUI
from AdminMainPage import Ui_Dialog as AdminMainPageUI
from MakeReservation import Ui_ReservationView as MakeReservationUI
from ViewReservations import Ui_MyReservationsView as ViewReservationsUI
from PaymentPage import Ui_PaymentPage as PaymentPageUI
from ManageHall import Ui_HallView as ManageHallUI
from ManageReservations import Ui_MyReservationsView as ManageReservationsUI
from PaymentTransactions import Ui_PaymentTransactions as PaymentTransactionsUI


class MainController:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        # Initialize all windows but don't show them yet
        self.login_window = QtWidgets.QDialog()
        self.login_ui = LoginUI()
        self.login_ui.setupUi(self.login_window)

        self.signup_window = QtWidgets.QDialog()
        self.signup_ui = SignupUI()
        self.signup_ui.setupUi(self.signup_window)

        self.admin_login_window = QtWidgets.QDialog()
        self.admin_login_ui = AdminLoginUI()
        self.admin_login_ui.setupUi(self.admin_login_window)

        self.main_page_window = QtWidgets.QDialog()
        self.main_page_ui = MainPageUI()
        self.main_page_ui.setupUi(self.main_page_window)

        self.admin_main_page_window = QtWidgets.QDialog()
        self.admin_main_page_ui = AdminMainPageUI()
        self.admin_main_page_ui.setupUi(self.admin_main_page_window)

        self.make_reservation_window = QtWidgets.QWidget()
        self.make_reservation_ui = MakeReservationUI()
        self.make_reservation_ui.setupUi(self.make_reservation_window)

        self.view_reservations_window = QtWidgets.QWidget()
        self.view_reservations_ui = ViewReservationsUI()
        self.view_reservations_ui.setupUi(self.view_reservations_window)

        self.payment_page_window = QtWidgets.QWidget()
        self.payment_page_ui = PaymentPageUI()
        self.payment_page_ui.setupUi(self.payment_page_window)

        self.manage_hall_window = QtWidgets.QWidget()
        self.manage_hall_ui = ManageHallUI()
        self.manage_hall_ui.setupUi(self.manage_hall_window)

        self.manage_reservations_window = QtWidgets.QWidget()
        self.manage_reservations_ui = ManageReservationsUI()
        self.manage_reservations_ui.setupUi(self.manage_reservations_window)

        self.payment_transactions_window = QtWidgets.QWidget()
        self.payment_transactions_ui = PaymentTransactionsUI()
        self.payment_transactions_ui.setupUi(self.payment_transactions_window)

        # Connect signals
        self.connect_signals()

        # Start with login window
        self.login_window.show()

    def connect_signals(self):
        # Login page connections
        self.login_ui.pushButton.clicked.connect(self.show_admin_login)
        self.login_ui.pushButton_2.clicked.connect(self.show_signup)
        self.login_ui.loginButton.clicked.connect(self.user_login)

        # Signup page connections
        self.signup_ui.loginButton.clicked.connect(self.user_signup)

        # Admin login connections
        self.admin_login_ui.pushButton.clicked.connect(self.show_login)
        self.admin_login_ui.loginButton.clicked.connect(self.admin_login)

        # Main page connections
        self.main_page_ui.cancelReservationButton.clicked.connect(self.show_make_reservation)
        self.main_page_ui.cancelReservationButton_3.clicked.connect(self.show_view_reservations)
        self.main_page_ui.cancelReservationButton_2.clicked.connect(self.logout)

        # Admin main page connections
        self.admin_main_page_ui.cancelReservationButton.clicked.connect(self.show_manage_hall)
        self.admin_main_page_ui.cancelReservationButton_3.clicked.connect(self.show_manage_reservations)
        self.admin_main_page_ui.cancelReservationButton_4.clicked.connect(self.show_payment_transactions)
        self.admin_main_page_ui.cancelReservationButton_2.clicked.connect(self.admin_logout)

        # Make reservation connections
        self.make_reservation_ui.reserveButton.clicked.connect(self.show_payment_page)

        # View reservations connections
        self.view_reservations_ui.cancelReservationButton.clicked.connect(self.cancel_reservation)
        self.view_reservations_ui.rescheduleReservationButton.clicked.connect(self.reschedule_reservation)

        # Payment page connections
        self.payment_page_ui.payButton.clicked.connect(self.process_payment)
        self.payment_page_ui.doneButton.clicked.connect(self.return_to_main_page)

        # Manage hall connections
        self.manage_hall_ui.addHallButton.clicked.connect(self.add_hall)
        self.manage_hall_ui.editHallButton.clicked.connect(self.edit_hall)
        self.manage_hall_ui.deleteHallButton.clicked.connect(self.delete_hall)

        # Manage reservations connections
        self.manage_reservations_ui.cancelReservationButton.clicked.connect(self.admin_cancel_reservation)
        self.manage_reservations_ui.rescheduleReservationButton.clicked.connect(self.admin_reschedule_reservation)

        # Payment transactions connections
        self.payment_transactions_ui.exportButton.clicked.connect(self.export_transactions)

    # Navigation methods
    def show_login(self):
        self.admin_login_window.hide()
        self.login_window.show()

    def show_admin_login(self):
        self.login_window.hide()
        self.admin_login_window.show()

    def show_signup(self):
        self.login_window.hide()
        self.signup_window.show()

    def user_login(self):
        # Basic validation - in a real app, you'd check credentials against a database
        username = self.login_ui.usernameLineEdit.text()
        password = self.login_ui.passwordLineEdit.text()

        if username and password:  # Simple check for non-empty fields
            print("Login successful!")
            self.login_window.hide()
            self.main_page_window.show()
        else:
            QMessageBox.warning(self.login_window, "Login Failed", "Please enter both username and password")

    def user_signup(self):
        # Basic validation
        username = self.signup_ui.usernameLineEdit.text()
        password = self.signup_ui.passwordLineEdit.text()
        confirm_password = self.signup_ui.passwordLineEdit_2.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self.signup_window, "Signup Failed", "All fields are required")
            return

        if password != confirm_password:
            QMessageBox.warning(self.signup_window, "Signup Failed", "Passwords do not match")
            return

        print("Signup successful!")  # In a real app, you'd save to database
        self.signup_window.hide()
        self.login_window.show()

    def admin_login(self):
        # Basic validation for admin login
        username = self.admin_login_ui.usernameLineEdit.text()
        password = self.admin_login_ui.passwordLineEdit.text()

        if username == "admin" and password == "admin":  # Hardcoded for demo
            print("Admin login successful!")
            self.admin_login_window.hide()
            self.admin_main_page_window.show()
        else:
            QMessageBox.warning(self.admin_login_window, "Login Failed", "Invalid admin credentials")

    def show_make_reservation(self):
        self.main_page_window.hide()
        self.make_reservation_window.show()

    def show_view_reservations(self):
        self.main_page_window.hide()
        self.view_reservations_window.show()

    def logout(self):
        self.main_page_window.hide()
        self.login_window.show()

    def admin_logout(self):
        self.admin_main_page_window.hide()
        self.admin_login_window.show()

    def show_payment_page(self):
        self.make_reservation_window.hide()
        self.payment_page_window.show()

    def show_manage_hall(self):
        self.admin_main_page_window.hide()
        self.manage_hall_window.show()

    def show_manage_reservations(self):
        self.admin_main_page_window.hide()
        self.manage_reservations_window.show()

    def show_payment_transactions(self):
        self.admin_main_page_window.hide()
        self.payment_transactions_window.show()

    def return_to_main_page(self):
        self.payment_page_window.hide()
        self.main_page_window.show()

    # Placeholder methods for actions that would have more logic in a real app
    def cancel_reservation(self):
        QMessageBox.information(self.view_reservations_window, "Info", "Reservation cancelled (placeholder)")

    def reschedule_reservation(self):
        QMessageBox.information(self.view_reservations_window, "Info", "Reservation rescheduled (placeholder)")

    def process_payment(self):
        # Show the confirmation frame (hidden by default in the UI)
        self.payment_page_ui.confirmationFrame.show()
        QMessageBox.information(self.payment_page_window, "Info", "Payment processed (placeholder)")

    def add_hall(self):
        QMessageBox.information(self.manage_hall_window, "Info", "Add hall functionality (placeholder)")

    def edit_hall(self):
        QMessageBox.information(self.manage_hall_window, "Info", "Edit hall functionality (placeholder)")

    def delete_hall(self):
        QMessageBox.information(self.manage_hall_window, "Info", "Delete hall functionality (placeholder)")

    def admin_cancel_reservation(self):
        QMessageBox.information(self.manage_reservations_window, "Info", "Admin cancel reservation (placeholder)")

    def admin_reschedule_reservation(self):
        QMessageBox.information(self.manage_reservations_window, "Info", "Admin reschedule reservation (placeholder)")

    def export_transactions(self):
        QMessageBox.information(self.payment_transactions_window, "Info", "Export transactions (placeholder)")


if __name__ == "__main__":
    controller = MainController()
    sys.exit(controller.app.exec())
