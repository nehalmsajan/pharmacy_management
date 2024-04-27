from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dbms321",
            database="pharmacy_management"
        )
        return conn

    except Error as e:
        print(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drugs')
def view_drugs():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Drugs")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('drugs.html', rows=rows)

@app.route('/add_drug', methods=['GET', 'POST'])
def add_drug():
    if request.method == 'POST':
        # Retrieve form data including DrugID
        drug_id = request.form.get('drug_id')
        drug_name = request.form.get('drug_name')
        dosage = request.form.get('dosage')
        expiration_date = request.form.get('expiration_date')
        quantity_in_stock = request.form.get('quantity_in_stock')
        supplier_id = request.form.get('supplier_id')

        if not (drug_id and drug_name and dosage and expiration_date and quantity_in_stock and supplier_id):
            return "Drug ID, drug name, dosage, expiration date, quantity in stock, and supplier ID are required."

        conn = connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Drugs (DrugID, DrugName, Dosage, ExpirationDate, QuantityInStock, SupplierID) VALUES (%s, %s, %s, %s, %s, %s)",
                       (drug_id, drug_name, dosage, expiration_date, quantity_in_stock, supplier_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/drugs')
    return render_template('add_drug.html')

@app.route('/delete_drug/<int:id>', methods=['POST'])
def delete_drug(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Drugs WHERE DrugID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/drugs')


@app.route('/patients')
def view_patients():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patients")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('patients.html', rows=rows)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # Retrieve form data including PatientID
        patient_id = request.form.get('patient_id')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        contact_number = request.form.get('contact_number')
        medical_history = request.form.get('medical_history')
        allergies = request.form.get('allergies')

        # Check if any field is empty
        if not (patient_id and first_name and last_name):
            return "Patient ID, first name, and last name are required."

        conn = connect()
        cursor = conn.cursor()
        # Insert new patient into database with provided PatientID
        cursor.execute("INSERT INTO Patients (PatientID, FirstName, LastName, ContactNumber, MedicalHistory, Allergies) VALUES (%s, %s, %s, %s, %s, %s)",
                       (patient_id, first_name, last_name, contact_number, medical_history, allergies))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/patients')
    return render_template('add_patient.html')


@app.route('/delete_patient/<int:id>', methods=['POST'])
def delete_patient(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Patients WHERE PatientID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/patients')
@app.route('/prescriptions')
def view_prescriptions():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Prescriptions")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('prescriptions.html', rows=rows)

@app.route('/suppliers')
def view_suppliers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Suppliers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('suppliers.html', rows=rows)

@app.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        # Retrieve form data including SupplierID
        supplier_id = request.form.get('supplier_id')
        supplier_name = request.form.get('supplier_name')
        contact_number = request.form.get('contact_number')
        address = request.form.get('address')

        # Check if any field is empty
        if not (supplier_id and supplier_name):
            return "Supplier ID and supplier name are required."

        conn = connect()
        cursor = conn.cursor()
        # Insert new supplier into database with provided SupplierID
        cursor.execute("INSERT INTO Suppliers (SupplierID, SupplierName, ContactNumber, Address) VALUES (%s, %s, %s, %s)",
                       (supplier_id, supplier_name, contact_number, address))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/suppliers')
    return render_template('add_supplier.html')

@app.route('/delete_supplier/<int:id>', methods=['POST'])
def delete_supplier(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Suppliers WHERE SupplierID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/suppliers')


@app.route('/staff')
def view_pharmacy_staff():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PharmacyStaff")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('staff.html', rows=rows)

@app.route('/dispensed')
def view_dispensed_medications():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DispensedMedications")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('dispensed.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
