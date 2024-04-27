# Pharmacy Management System
This project is a Pharmacy Management System developed using Flask and MySQL. It allows users to manage drugs, patients, suppliers, prescriptions, and pharmacy staff efficiently.

## Features
- **Manage Drugs:** Add, delete, and view details of drugs in the inventory.
- **Manage Patients:** Add, delete, and view details of patients.
- **Manage Suppliers:** Add, delete, and view details of suppliers.
- **Prescriptions:** View prescriptions issued to patients.
- **Pharmacy Staff:** View details of pharmacy staff.

## Technologies Used
- **Flask:** Flask is a lightweight WSGI web application framework in Python. It provides tools, libraries, and technologies for building web applications.
- **MySQL:** MySQL is an open-source relational database management system. It is widely used for managing structured data.
- **HTML/CSS:** HTML is used for creating the structure of web pages, while CSS is used for styling the appearance of web pages.

## Getting Started
To run this project locally, follow these steps:
1. Clone this repository to your local machine.
2. Install Python and MySQL if you haven't already.
3. Set up a virtual environment for the project and install the required dependencies from the `requirements.txt` file.
4. Set up a MySQL database and configure the connection details in the Flask application.
5. Run the Flask application using the command `python app.py`.
6. Access the application in your web browser at `http://localhost:5000`.

  ## SQL Tables

This project utilizes several SQL tables to manage data related to patients, drugs, prescriptions, suppliers, pharmacy staff, and dispensed medications. Below is an overview of these tables:

- **Patients:** Stores information about patients, including their ID, first name, last name, contact number, medical history, and allergies.
- **Drugs:** Contains details about drugs available in the pharmacy, such as drug ID, name, dosage, expiration date, quantity in stock, and supplier ID.
- **Prescriptions:** Tracks prescriptions issued to patients, including prescription ID, patient ID, drug ID, prescription date, and quantity prescribed.
- **Suppliers:** Stores information about suppliers who provide drugs to the pharmacy, including supplier ID, name, contact information, and address.
- **PharmacyStaff:** Manages details about pharmacy staff members, including staff ID, name, role, and contact information.
- **DispensedMedications:** Records medications dispensed to patients, including dispensation ID, prescription ID, patient ID, quantity dispensed, and dispensation date.

Please note that the SQL database containing these tables is not included with the code repository. Due to privacy and security concerns, the database may contain sensitive information that should not be shared publicly. Therefore, you will need to set up your own database and populate it with relevant data before running the application.

If you need assistance setting up the database schema or have any questions about the tables used in this project, feel free to reach out for support.
