import sys
import json

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QListWidget,
                             QMainWindow, QMessageBox, QPushButton, QScrollArea, 
                             QSizePolicy, QStackedWidget, QTabWidget, QVBoxLayout, 
                             QWidget)

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        input_stylesheet = """
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """

        title_label = QLabel("<h1>WELCOME TO AMBAG CAR RENTALS</h1>")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        logo_label = QLabel()
        pixmap = QPixmap("Car Rental Logo.png") 
        logo_label.setPixmap(pixmap.scaled(200, 200))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

        message_label = QLabel("<h2>Please Login</h2>")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(message_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet(input_stylesheet) 
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(input_stylesheet)
        layout.addWidget(self.password_input)

        admin_login = QPushButton("Admin Login")
        admin_login.clicked.connect(self.admin_login)
        layout.addWidget(admin_login)

        login_button = QPushButton("Staff Login")
        login_button.clicked.connect(self.staff_login)
        layout.addWidget(login_button)

        forgot_button = QPushButton("Forgot User/Password")
        forgot_button.clicked.connect(self.forgot)
        layout.addWidget(forgot_button)

    def admin_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "Team6" and password == "CSC470":
            main_window.stacked_widget.setCurrentWidget(main_window.main_widget)

        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")

    def staff_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username == "Staff" and password == "Password":
            main_window.stacked_widget.setCurrentWidget(main_window.main_widget)

        else:
            QMessageBox.warning(self, "Error", "Invalid username or password.")


  #Displays the error message when hitting "forgot username/password"
    def forgot(self):
        QMessageBox.warning(self,"Error","Please contact admin for username or password")

class StaffSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        staff_layout = QHBoxLayout()

        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("Enter staff first name")
        self.first_name_input.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        staff_layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Enter staff last name")
        self.last_name_input.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        staff_layout.addWidget(self.last_name_input)

        add_staff_btn = QPushButton("Add Staff")
        add_staff_btn.setStyleSheet("background-color: gray; color: white; border-radius: 5px;")
        add_staff_btn.clicked.connect(self.add_staff)
        staff_layout.addWidget(add_staff_btn)

        remove_staff_btn = QPushButton("Remove Staff")
        remove_staff_btn.setStyleSheet("background-color: darkred; color: white; border-radius: 5px;")
        remove_staff_btn.clicked.connect(self.remove_staff)
        staff_layout.addWidget(remove_staff_btn)

        layout.addLayout(staff_layout)

        self.staff_list = QListWidget()
        self.staff_list.setStyleSheet("""
        background-color: #222; 
        color: white;
        border: 1px solid lightgray; 
        """)
        layout.addWidget(self.staff_list)

    def add_staff(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        if first_name and last_name:
            name = f"{first_name} {last_name}"
            main_window.staff.append(name)
            main_window.update_staff_list()
            QMessageBox.information(self, "Success", f"Staff '{name}' added!")
            self.first_name_input.clear()
            self.last_name_input.clear()
            main_window.save_data() 
        else:
            QMessageBox.warning(self, "Error", "Please enter a first and last name.")

    def remove_staff(self):
        selected_item = self.staff_list.currentItem()
        if selected_item:
            name = selected_item.text()
            main_window.staff.remove(name)
            main_window.update_staff_list()
            QMessageBox.information(self, "Success", f"Staff '{name}' removed!")
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please select a staff member to remove.")

class VehicleSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        vehicle_layout = QHBoxLayout()

        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Enter year")
        self.year_input.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        vehicle_layout.addWidget(self.year_input)

        self.make_input = QLineEdit()
        self.make_input.setPlaceholderText("Enter make")
        self.make_input.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        vehicle_layout.addWidget(self.make_input)

        self.model_input = QLineEdit()
        self.model_input.setPlaceholderText("Enter model")
        self.model_input.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        vehicle_layout.addWidget(self.model_input)

        add_vehicle_btn = QPushButton("Add Vehicle")
        add_vehicle_btn.setStyleSheet("background-color: gray; color: white; border-radius: 5px;")
        add_vehicle_btn.clicked.connect(self.add_vehicle)
        vehicle_layout.addWidget(add_vehicle_btn)

        remove_vehicle_btn = QPushButton("Remove Vehicle")
        remove_vehicle_btn.setStyleSheet("background-color: darkred; color: white; border-radius: 5px;")
        remove_vehicle_btn.clicked.connect(self.remove_vehicle)
        vehicle_layout.addWidget(remove_vehicle_btn)

        layout.addLayout(vehicle_layout)

        self.vehicle_list = QListWidget()
        self.vehicle_list.setStyleSheet("""
        background-color: #222; 
        color: white;
        border: 1px solid lightgray; 
        """)
        layout.addWidget(self.vehicle_list)

        # Modify Vehicle Section
        modify_layout = QHBoxLayout()

        self.vehicle_dropdown_modify = QComboBox()
        self.vehicle_dropdown_modify.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        modify_layout.addWidget(self.vehicle_dropdown_modify)

        self.vehicle_year_input_modify = QLineEdit()
        self.vehicle_year_input_modify.setPlaceholderText("Enter new year")
        self.vehicle_year_input_modify.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        modify_layout.addWidget(self.vehicle_year_input_modify)

        self.vehicle_make_input_modify = QLineEdit()
        self.vehicle_make_input_modify.setPlaceholderText("Enter new make")
        self.vehicle_make_input_modify.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        modify_layout.addWidget(self.vehicle_make_input_modify)

        self.vehicle_model_input_modify = QLineEdit()
        self.vehicle_model_input_modify.setPlaceholderText("Enter new model")
        self.vehicle_model_input_modify.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        modify_layout.addWidget(self.vehicle_model_input_modify)

        modify_vehicle_btn = QPushButton("Modify Vehicle")
        modify_vehicle_btn.setStyleSheet("background-color: gray; color: white; border-radius: 5px;")
        modify_vehicle_btn.clicked.connect(self.modify_vehicle)
        modify_layout.addWidget(modify_vehicle_btn)

        layout.addLayout(modify_layout) 

        # Check Availability Section
        availability_layout = QHBoxLayout()

        self.vehicle_dropdown_availability = QComboBox()
        self.vehicle_dropdown_availability.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        availability_layout.addWidget(self.vehicle_dropdown_availability)

        self.date_picker_availability = QDateEdit()
        self.date_picker_availability.setCalendarPopup(True)
        self.date_picker_availability.setStyleSheet("""
        background-color: #333;
        color: white;
        border: 1px solid lightgray;
        padding: 5px;
        border-radius: 4px;
        """)
        self.date_picker_availability.setDisplayFormat("MM-dd-yyyy")
        availability_layout.addWidget(self.date_picker_availability)

        check_availability_btn = QPushButton("Check Availability")
        check_availability_btn.setStyleSheet("background-color: gray; color: white; border-radius: 5px;")
        check_availability_btn.clicked.connect(self.check_availability)
        availability_layout.addWidget(check_availability_btn)

        layout.addLayout(availability_layout) 
       
        logout_button = QPushButton("Logout")
        logout_button.setStyleSheet("background-color: darkblue; color: white; border-radius: 5px;")
        logout_button.clicked.connect(self.logout)
        layout.addWidget(logout_button)

    def logout(self):
        main_window.stacked_widget.setCurrentWidget(main_window.login_widget)

    def add_vehicle(self):
        year = self.year_input.text()
        make = self.make_input.text()
        model = self.model_input.text()
        if year and make and model:
            name = f"{year} {make} {model}"
            main_window.vehicles.append(name)
            main_window.update_vehicle_list()
            QMessageBox.information(self, "Success", f"Vehicle '{name}' added!")
            self.year_input.clear()
            self.make_input.clear()
            self.model_input.clear()
            main_window.update_dropdowns()
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please enter year, make, and model.")

    def remove_vehicle(self):
        selected_item = self.vehicle_list.currentItem()
        if selected_item:
            name = selected_item.text()
            main_window.vehicles.remove(name)
            main_window.update_vehicle_list() 
            QMessageBox.information(self, "Success", f"Vehicle '{name}' removed!")
            main_window.update_dropdowns()
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please select a vehicle to remove.")

    def modify_vehicle(self):
        selected_vehicle = self.vehicle_dropdown_modify.currentText()
        new_year = self.vehicle_year_input_modify.text()
        new_make = self.vehicle_make_input_modify.text()
        new_model = self.vehicle_model_input_modify.text()

        if selected_vehicle and new_year and new_make and new_model:
            try:
                index = main_window.vehicles.index(selected_vehicle)
                main_window.vehicles[index] = f"{new_year} {new_make} {new_model}"
                main_window.update_vehicle_list()
                main_window.update_dropdowns() 
                main_window.save_data()
                QMessageBox.information(self, "Success", f"Vehicle modified to '{main_window.vehicles[index]}'")
            except ValueError:
                QMessageBox.warning(self, "Error", "Vehicle not found in the list.")
        else:
            QMessageBox.warning(self, "Error", "Please select a vehicle and enter all new details.")

    def check_availability(self):
        vehicle = self.vehicle_dropdown_availability.currentText()
        date = self.date_picker_availability.date().toString("yyyy-MM-dd")

        if vehicle and date:
            is_available = True 

            for reservation in main_window.reservations:
                if reservation["vehicle"] == vehicle and reservation["date"] == date:
                    is_available = False
                    break

            if is_available:
                QMessageBox.information(self, "Availability", f"{vehicle} is available on {date}.")
            else:
                QMessageBox.information(self, "Availability", f"{vehicle} is NOT available on {date}.")
        else:
            QMessageBox.warning(self, "Error", "Please select a vehicle and date.")

class CustomerSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        input_stylesheet = """
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """
        policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(5)

        grid_layout.addWidget(QLabel("First Name:"), 0, 0)
        self.first_name_input = QLineEdit()
        self.first_name_input.setStyleSheet(input_stylesheet)
        self.first_name_input.setSizePolicy(policy)
        self.first_name_input.setMaximumWidth(200)
        grid_layout.addWidget(self.first_name_input, 0, 1)

        grid_layout.addWidget(QLabel("Last Name:"), 0, 2)
        self.last_name_input = QLineEdit()
        self.last_name_input.setStyleSheet(input_stylesheet)
        self.last_name_input.setSizePolicy(policy)
        self.last_name_input.setMaximumWidth(200)
        grid_layout.addWidget(self.last_name_input, 0, 3)

        grid_layout.addWidget(QLabel("Street Address:"), 1, 0)
        self.street_input = QLineEdit()
        self.street_input.setStyleSheet(input_stylesheet)
        self.street_input.setSizePolicy(policy)
        self.street_input.setMaximumWidth(300)
        grid_layout.addWidget(self.street_input, 1, 1, 1, 3)

        grid_layout.addWidget(QLabel("City:"), 2, 0)
        self.city_input = QLineEdit()
        self.city_input.setStyleSheet(input_stylesheet)
        self.city_input.setSizePolicy(policy)
        self.city_input.setMaximumWidth(150)
        grid_layout.addWidget(self.city_input, 2, 1)

        grid_layout.addWidget(QLabel("State:"), 2, 2)
        self.state_input = QLineEdit()
        self.state_input.setStyleSheet(input_stylesheet)
        self.state_input.setSizePolicy(policy)
        self.state_input.setMaximumWidth(50)
        grid_layout.addWidget(self.state_input, 2, 3)

        grid_layout.addWidget(QLabel("Zip Code:"), 2, 4)
        self.zip_input = QLineEdit()
        self.zip_input.setStyleSheet(input_stylesheet)
        self.zip_input.setSizePolicy(policy)
        self.zip_input.setMaximumWidth(100)
        grid_layout.addWidget(self.zip_input, 2, 5)

        layout.addLayout(grid_layout)

        button_layout = QHBoxLayout()
        add_customer_btn = QPushButton("Add Customer")
        add_customer_btn.clicked.connect(self.add_customer)
        add_customer_btn.setStyleSheet("background-color: gray; color: white; border-radius: 5px;")
        button_layout.addWidget(add_customer_btn)

        remove_customer_btn = QPushButton("Remove Customer")
        remove_customer_btn.clicked.connect(self.remove_customer)
        remove_customer_btn.setStyleSheet("background-color: darkred; color: white; border-radius: 5px;")
        button_layout.addWidget(remove_customer_btn)
        layout.addLayout(button_layout)

        self.customer_list = QListWidget()
        self.customer_list.setStyleSheet("""
        background-color: #222;
        color: white;
        border: 1px solid lightgray;
        """)
        layout.addWidget(self.customer_list)

        logout_button = QPushButton("Logout")
        logout_button.setStyleSheet("background-color: darkblue; color: white; border-radius: 5px;")
        logout_button.clicked.connect(self.logout)
        layout.addWidget(logout_button)

    def logout(self):
        main_window.stacked_widget.setCurrentWidget(main_window.login_widget)

    def add_customer(self):
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        street = self.street_input.text()
        city = self.city_input.text()
        state = self.state_input.text()
        zip_code = self.zip_input.text()

        if first_name and last_name and street and city and state and zip_code:
            name = f"{first_name} {last_name}"
            main_window.customers[name] = {
                "vehicles_rented": [], 
                "address": f"{street}, {city}, {state}, {zip_code}"
            }
            main_window.update_customer_list()
            QMessageBox.information(self, "Success", f"Customer '{name}' added!")
            self.first_name_input.clear()
            self.last_name_input.clear()
            self.street_input.clear()
            self.city_input.clear()
            self.state_input.clear()
            self.zip_input.clear()
            main_window.update_dropdowns()
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please fill in all customer details.")

    def remove_customer(self):
        selected_item = self.customer_list.currentItem()
        if selected_item:
            name = selected_item.text()
            del main_window.customers[name]
            main_window.customer_list.takeItem(main_window.customer_list.row(selected_item))
            QMessageBox.information(self, "Success", f"Customer '{name}' removed!")
            main_window.update_dropdowns()
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please select a customer to remove.")


class ReservationSection(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        reservation_layout = QHBoxLayout()

        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setStyleSheet("""
        background-color: #333;
        color: white;
        border: 1px solid lightgray;
        padding: 5px;
        border-radius: 4px;
        """)
        self.date_picker.setDisplayFormat("MM-dd-yyyy")
        reservation_layout.addWidget(self.date_picker)

        self.customer_dropdown = QComboBox()
        self.customer_dropdown.setStyleSheet("""
        background-color: #333; 
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        reservation_layout.addWidget(self.customer_dropdown)

        self.vehicle_dropdown = QComboBox()
        self.vehicle_dropdown.setStyleSheet("""
        background-color: #333;
        color: white;
        border: 1px solid lightgray; 
        padding: 5px;
        border-radius: 4px;
        """)
        reservation_layout.addWidget(self.vehicle_dropdown)

        create_reservation_btn = QPushButton("Create Reservation")
        create_reservation_btn.clicked.connect(self.create_reservation)
        create_reservation_btn.setStyleSheet("background-color: gray; color: white; border-radius: 5px;")
        reservation_layout.addWidget(create_reservation_btn)

        cancel_reservation_btn = QPushButton("Cancel Reservation")
        cancel_reservation_btn.clicked.connect(self.cancel_reservation)
        cancel_reservation_btn.setStyleSheet("background-color: darkred; color: white; border-radius: 5px;")
        reservation_layout.addWidget(cancel_reservation_btn)

        layout.addLayout(reservation_layout)

        self.reservation_list = QListWidget()
        self.reservation_list.setStyleSheet("""
        background-color: #222;
        color: white;
        border: 1px solid lightgray; 
        """)
        layout.addWidget(self.reservation_list)

        logout_button = QPushButton("Logout")
        logout_button.setStyleSheet("background-color: darkblue; color: white; border-radius: 5px;")
        logout_button.clicked.connect(self.logout)
        layout.addWidget(logout_button)

    def logout(self):
        main_window.stacked_widget.setCurrentWidget(main_window.login_widget)

    def create_reservation(self):
        date = self.date_picker.date().toString("yyyy-MM-dd")
        customer = self.customer_dropdown.currentText()
        vehicle = self.vehicle_dropdown.currentText()
        if customer and vehicle:
            reservation = {
                "customer": customer,
                "vehicle": vehicle,
                "date": date
            }
            main_window.reservations.append(reservation)

            main_window.update_reservation_list()

            QMessageBox.information(self, "Success",
                                         f"Reservation created for '{customer}' for vehicle '{vehicle}' on '{date}'.")
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please select a customer and a vehicle.")

    def cancel_reservation(self):
        selected_item = self.reservation_list.currentItem()
        if selected_item:
            reservation_text = selected_item.text()
            for reservation in main_window.reservations:
                if reservation_text == f"{reservation['customer']} reserved {reservation['vehicle']} on {reservation['date']}":
                    main_window.reservations.remove(reservation)
                    break

            main_window.update_reservation_list()

            QMessageBox.information(self, "Success", f"Reservation cancelled.")
            main_window.save_data()
        else:
            QMessageBox.warning(self, "Error", "Please select a reservation to cancel.")

class CarManagementSystemUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Management System")
        self.setGeometry(100, 100, 800, 600)

        self.setStyleSheet("background-color: black; color: white;")

        self.staff = []
        self.vehicles = []
        self.customers = {}
        self.reservations = [] 

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_widget = LoginScreen() 
        self.stacked_widget.addWidget(self.login_widget)

        self.main_widget = QWidget()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.main_widget)

        self.tab_widget = QTabWidget(self.main_widget)
        main_layout = QVBoxLayout(self.main_widget)

        self.add_logo(main_layout)
        main_layout.addWidget(QLabel("<h1>AMBAG Rentals Car Management System</h1>"))

        main_layout.addWidget(self.tab_widget)

        self.staff_tab = StaffSection() 
        self.tab_widget.addTab(self.staff_tab, "Staff")

        self.vehicle_tab = VehicleSection() 
        self.tab_widget.addTab(self.vehicle_tab, "Vehicle")

        self.customer_tab = CustomerSection() 
        self.tab_widget.addTab(self.customer_tab, "Customer")

        self.reservation_tab = ReservationSection() 
        self.tab_widget.addTab(self.reservation_tab, "Reservation")

        self.stacked_widget.addWidget(self.main_widget)

        self.load_data()

        self.stacked_widget.setCurrentWidget(self.login_widget)
        
        self.logout_button = QPushButton("Logout")
        self.logout_button.setStyleSheet("background-color: darkblue; color: white; border-radius: 5px;")
        self.logout_button.clicked.connect(self.logout)
        main_layout.addWidget(self.logout_button)

    def logout(self):
        main_window.stacked_widget.setCurrentWidget(main_window.login_widget)

    def add_logo(self, layout):
        logo_label = QLabel()
        pixmap = QPixmap("Car Rental Logo.png") 
        logo_label.setPixmap(pixmap.scaled(200, 200))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(logo_label)

    def load_data(self):
        try:
            with open("car_management_data.json", "r") as f:
                data = json.load(f)
                self.staff = data.get("staff", [])
                self.vehicles = data.get("vehicles", [])
                self.customers = data.get("customers", {})
                self.reservations = data.get("reservations", []) 

                self.update_staff_list()
                self.update_vehicle_list()
                self.update_customer_list()
                self.update_dropdowns()
                self.update_reservation_list() 

        except FileNotFoundError:
            pass

    def save_data(self):
        data = {
            "staff": self.staff,
            "vehicles": self.vehicles,
            "customers": self.customers,
            "reservations": self.reservations 
        }
        with open("car_management_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def update_staff_list(self):
        self.staff_tab.staff_list.clear()
        self.staff_tab.staff_list.addItems(self.staff)

    def update_vehicle_list(self):
        self.vehicle_tab.vehicle_list.clear()
        self.vehicle_tab.vehicle_list.addItems(self.vehicles)

    def update_customer_list(self):
        self.customer_tab.customer_list.clear()
        self.customer_tab.customer_list.addItems(self.customers.keys())

    def update_reservation_list(self):
        self.reservation_tab.reservation_list.clear()
        for reservation in self.reservations:
            customer = reservation["customer"]
            vehicle = reservation["vehicle"]
            date = reservation["date"]
            self.reservation_tab.reservation_list.addItem(f"{customer} reserved {vehicle} on {date}")

    def update_dropdowns(self):
        self.reservation_tab.customer_dropdown.clear()
        self.reservation_tab.customer_dropdown.addItems(self.customers.keys())
        self.reservation_tab.vehicle_dropdown.clear()
        self.reservation_tab.vehicle_dropdown.addItems(self.vehicles)
        self.vehicle_tab.vehicle_dropdown_modify.clear()
        self.vehicle_tab.vehicle_dropdown_modify.addItems(self.vehicles)
        self.vehicle_tab.vehicle_dropdown_availability.clear()
        self.vehicle_tab.vehicle_dropdown_availability.addItems(self.vehicles)

    def closeEvent(self, event):
        """Save data when the window is closed."""
        self.save_data()
        event.accept()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CarManagementSystemUI() 
    main_window.show()
    sys.exit(app.exec())
