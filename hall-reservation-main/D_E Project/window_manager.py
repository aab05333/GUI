from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
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


class WindowManager:
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

    #WINDOW NAVIGATION

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
