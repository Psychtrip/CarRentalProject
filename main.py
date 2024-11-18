import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QComboBox, QListWidget, QMessageBox, QWidget
)
from PyQt6.QtGui import QPixmap


class CarManagementSystemUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Car Management System")
        self.setGeometry(100, 100, 800, 600)

        # Data structures
        self.staff = []
        self.vehicles = []
        self.customers = {}

        # Main layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()

        # Add the logo at the top
        self.add_logo()

        # Section headers
        self.layout.addWidget(QLabel("<h1>Car Management System</h1>"))

        # Staff Management
        self.add_staff_section()
        self.add_vehicle_section()
        self.add_customer_section()
        self.add_reservation_section()

        self.main_widget.setLayout(self.layout)

    def add_logo(self):
        logo_label = QLabel()
        pixmap = QPixmap("Car Rental Logo.png")  # Replace with the path to the saved logo
        logo_label.setPixmap(pixmap.scaled(200, 100))  # Adjust size as needed
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(logo_label)

    # STAFF SECTION
    def add_staff_section(self):
        header = QLabel("<h2>Staff Management</h2>")
        self.layout.addWidget(header)

        staff_layout = QHBoxLayout()

        # Staff input
        self.staff_input = QLineEdit()
        self.staff_input.setPlaceholderText("Enter staff name")
        staff_layout.addWidget(self.staff_input)

        # Buttons
        add_staff_btn = QPushButton("Add Staff")
        add_staff_btn.clicked.connect(self.add_staff)
        staff_layout.addWidget(add_staff_btn)

        remove_staff_btn = QPushButton("Remove Staff")
        remove_staff_btn.clicked.connect(self.remove_staff)
        staff_layout.addWidget(remove_staff_btn)

        self.layout.addLayout(staff_layout)

        # Staff list
        self.staff_list = QListWidget()
        self.layout.addWidget(self.staff_list)

    def add_staff(self):
        name = self.staff_input.text()
        if name:
            self.staff.append(name)
            self.staff_list.addItem(name)
            QMessageBox.information(self, "Success", f"Staff '{name}' added!")
            self.staff_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter a staff name.")

    def remove_staff(self):
        selected_item = self.staff_list.currentItem()
        if selected_item:
            name = selected_item.text()
            self.staff.remove(name)
            self.staff_list.takeItem(self.staff_list.row(selected_item))
            QMessageBox.information(self, "Success", f"Staff '{name}' removed!")
        else:
            QMessageBox.warning(self, "Error", "Please select a staff member to remove.")

    # VEHICLE SECTION
    def add_vehicle_section(self):
        header = QLabel("<h2>Vehicle Management</h2>")
        self.layout.addWidget(header)

        vehicle_layout = QHBoxLayout()

        # Vehicle input
        self.vehicle_input = QLineEdit()
        self.vehicle_input.setPlaceholderText("Enter vehicle name")
        vehicle_layout.addWidget(self.vehicle_input)

        # Buttons
        add_vehicle_btn = QPushButton("Add Vehicle")
        add_vehicle_btn.clicked.connect(self.add_vehicle)
        vehicle_layout.addWidget(add_vehicle_btn)

        remove_vehicle_btn = QPushButton("Remove Vehicle")
        remove_vehicle_btn.clicked.connect(self.remove_vehicle)
        vehicle_layout.addWidget(remove_vehicle_btn)

        self.layout.addLayout(vehicle_layout)

        # Vehicle list
        self.vehicle_list = QListWidget()
        self.layout.addWidget(self.vehicle_list)

    def add_vehicle(self):
        name = self.vehicle_input.text()
        if name:
            self.vehicles.append(name)
            self.vehicle_list.addItem(name)
            QMessageBox.information(self, "Success", f"Vehicle '{name}' added!")
            self.vehicle_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter a vehicle name.")

    def remove_vehicle(self):
        selected_item = self.vehicle_list.currentItem()
        if selected_item:
            name = selected_item.text()
            self.vehicles.remove(name)
            self.vehicle_list.takeItem(self.vehicle_list.row(selected_item))
            QMessageBox.information(self, "Success", f"Vehicle '{name}' removed!")
        else:
            QMessageBox.warning(self, "Error", "Please select a vehicle to remove.")

    # CUSTOMER SECTION
    def add_customer_section(self):
        header = QLabel("<h2>Customer Management</h2>")
        self.layout.addWidget(header)

        customer_layout = QHBoxLayout()

        # Customer input
        self.customer_input = QLineEdit()
        self.customer_input.setPlaceholderText("Enter customer name")
        customer_layout.addWidget(self.customer_input)

        # Buttons
        add_customer_btn = QPushButton("Add Customer")
        add_customer_btn.clicked.connect(self.add_customer)
        customer_layout.addWidget(add_customer_btn)

        remove_customer_btn = QPushButton("Remove Customer")
        remove_customer_btn.clicked.connect(self.remove_customer)
        customer_layout.addWidget(remove_customer_btn)

        self.layout.addLayout(customer_layout)

        # Customer list
        self.customer_list = QListWidget()
        self.layout.addWidget(self.customer_list)

    def add_customer(self):
        name = self.customer_input.text()
        if name:
            self.customers[name] = {"vehicles_rented": []}
            self.customer_list.addItem(name)
            QMessageBox.information(self, "Success", f"Customer '{name}' added!")
            self.customer_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter a customer name.")

    def remove_customer(self):
        selected_item = self.customer_list.currentItem()
        if selected_item:
            name = selected_item.text()
            del self.customers[name]
            self.customer_list.takeItem(self.customer_list.row(selected_item))
            QMessageBox.information(self, "Success", f"Customer '{name}' removed!")
        else:
            QMessageBox.warning(self, "Error", "Please select a customer to remove.")

    # RESERVATION SECTION
    def add_reservation_section(self):
        header = QLabel("<h2>Reservations</h2>")
        self.layout.addWidget(header)

        reservation_layout = QHBoxLayout()

        # Dropdown for customers
        self.customer_dropdown = QComboBox()
        self.customer_dropdown.addItems(self.customers.keys())
        reservation_layout.addWidget(self.customer_dropdown)

        # Dropdown for vehicles
        self.vehicle_dropdown = QComboBox()
        self.vehicle_dropdown.addItems(self.vehicles)
        reservation_layout.addWidget(self.vehicle_dropdown)

        # Buttons
        create_reservation_btn = QPushButton("Create Reservation")
        create_reservation_btn.clicked.connect(self.create_reservation)
        reservation_layout.addWidget(create_reservation_btn)

        self.layout.addLayout(reservation_layout)

        # Reservation list
        self.reservation_list = QListWidget()
        self.layout.addWidget(self.reservation_list)

    def create_reservation(self):
        customer = self.customer_dropdown.currentText()
        vehicle = self.vehicle_dropdown.currentText()
        if customer and vehicle:
            self.customers[customer]["vehicles_rented"].append(vehicle)
            self.reservation_list.addItem(f"{customer} reserved {vehicle}")
            QMessageBox.information(self, "Success", f"Reservation created for '{customer}' for vehicle '{vehicle}'.")
        else:
            QMessageBox.warning(self, "Error", "Please select a customer and a vehicle.")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarManagementSystemUI()
    window.show()
    sys.exit(app.exec())
