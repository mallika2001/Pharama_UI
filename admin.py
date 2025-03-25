# admin.py

import tkinter as tk
from login import LoginPage

class AdminDashboard(tk.Frame):
    def __init__(self, master, app, user):
        super().__init__(master)
        self.app = app
        self.user = user
        self.configure(bg="#d0f4f7")  # Match login screen background

        # Welcome label
        tk.Label(self, text=f"Welcome, Admin!", font=("Helvetica", 22, "bold"), bg="#d0f4f7", fg="#00838f").pack(pady=30)

        # Dashboard card
        card = tk.Frame(self, bg="white", bd=0, highlightbackground="#ccc", highlightthickness=1)
        card.pack(pady=10)

        # Button styling helper
        def styled_button(text, command):
            return tk.Button(
                card, text=text, command=command,
                font=("Helvetica", 12, "bold"), bg="#00acc1", fg="white",
                activebackground="#0097a7", activeforeground="white",
                relief="flat", width=25, pady=10
            )

        # Buttons
        styled_button("Manage Medicines", self.go_to_medicines).pack(pady=10)
        styled_button("Manage Inventory", self.go_to_inventory).pack(pady=10)
        styled_button("Manage Payments", self.go_to_payments).pack(pady=10)
        styled_button("Manage Suppliers", self.go_to_suppliers).pack(pady=10)

        # Logout button
        tk.Button(
            self, text="Logout",
            command=lambda: self.app.switch_frame(LoginPage, self.app),
            font=("Helvetica", 11), bg="#f44336", fg="white",
            activebackground="#d32f2f", relief="flat", width=12, pady=5
        ).pack(pady=30)

    def go_to_medicines(self):
        from medicines import MedicineManager
        self.app.switch_frame(MedicineManager, self.app)

    def go_to_inventory(self):
        from inventory import InventoryManager
        self.app.switch_frame(InventoryManager, self.app)

    def go_to_payments(self):
        from payments import PaymentsManager
        self.app.switch_frame(PaymentsManager, self.app)

    def go_to_suppliers(self):
        from suppliers import SuppliersManager
        self.app.switch_frame(SuppliersManager, self.app)
