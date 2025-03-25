# utils.py

USERS = [
    {'username': 'admin1', 'password': 'admin123', 'role': 'admin'},
    {'username': 'pharma1', 'password': 'pharma123', 'role': 'pharmacist'},
    {'username': 'staff1', 'password': 'staff123', 'role': 'staff'},
]

SAMPLE_MEDICINES = [
    {'name': 'Paracetamol 650mg', 'price': '30', 'stock': '1000', 'category': 'Pain Relief'},
    {'name': 'Azithromycin 500mg', 'price': '120', 'stock': '500', 'category': 'Antibiotic'},
    {'name': 'Vitamin C 1000mg', 'price': '50', 'stock': '800', 'category': 'Supplements'},
]

SAMPLE_INVENTORY = [
    {'medicine': 'Paracetamol 650mg', 'stock': '1000', 'updated': '2025-03-01'},
    {'medicine': 'Azithromycin 500mg', 'stock': '500', 'updated': '2025-03-01'},
    {'medicine': 'Vitamin C 1000mg', 'stock': '800', 'updated': '2025-03-01'},
]

SAMPLE_ORDERS = [
    {'id': 1, 'medicine': 'Paracetamol 650mg', 'quantity': 100, 'status': 'delivered'},
    {'id': 2, 'medicine': 'Vitamin C 1000mg', 'quantity': 50, 'status': 'pending'},
]

SAMPLE_SALES = [
    {'id': 1, 'medicine': 'Paracetamol 650mg', 'quantity': 5, 'total': 150.0},
    {'id': 2, 'medicine': 'Azithromycin 500mg', 'quantity': 3, 'total': 360.0},
]

SAMPLE_PAYMENTS = [
    {'id': 1, 'order_id': 1, 'amount': 250.00, 'method': 'Credit Card', 'status': 'Completed'},
    {'id': 2, 'order_id': 2, 'amount': 500.00, 'method': 'UPI', 'status': 'Pending'},
    {'id': 3, 'order_id': 3, 'amount': 1250.00, 'method': 'Debit Card', 'status': 'Completed'},
]

SAMPLE_SUPPLIERS = [
    {'id': 1, 'name': 'MediCare Pvt Ltd', 'contact': 'Ramesh Kumar', 'email': 'ramesh.kumar@medicare.com', 'phone': '9876543210'},
    {'id': 2, 'name': 'Health Plus', 'contact': 'Sanjay Patel', 'email': 'sanjay.patel@healthplus.com', 'phone': '9988776655'},
    {'id': 3, 'name': 'Apollo Pharma', 'contact': 'Vikash Joshi', 'email': 'vikash.joshi@apollo.com', 'phone': '9900990099'},
]
