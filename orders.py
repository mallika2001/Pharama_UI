# orders.py

import tkinter as tk
from tkinter import ttk, messagebox
from utils import SAMPLE_ORDERS, SAMPLE_MEDICINES

class OrdersManager(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.orders = SAMPLE_ORDERS.copy()

        tk.Label(self, text="Order Management", font=("Arial", 16)).pack(pady=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("Order ID", "Medicine", "Quantity", "Status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")
        self.load_table()

        # Add Order Form
        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Medicine").grid(row=0, column=0)
        tk.Label(form, text="Quantity").grid(row=0, column=2)

        self.medicine_var = tk.StringVar()
        self.medicine_menu = ttk.Combobox(form, textvariable=self.medicine_var, values=[m["name"] for m in SAMPLE_MEDICINES])
        self.quantity_entry = tk.Entry(form)

        self.medicine_menu.grid(row=0, column=1)
        self.quantity_entry.grid(row=0, column=3)

        tk.Button(self, text="Place Order", command=self.place_order).pack(pady=5)

        # Back Button (pharmacist only)
        role = getattr(self.app, "current_user", {}).get("role", "")
        if role == "pharmacist":
            from pharmacist import PharmacistDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(PharmacistDashboard, self.app, self.app.current_user)).pack(pady=10)

    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for order in self.orders:
            self.tree.insert("", "end", values=(order["id"], order["medicine"], order["quantity"], order["status"]))

    def place_order(self):
        medicine = self.medicine_var.get()
        quantity = self.quantity_entry.get()

        if not medicine or not quantity:
            messagebox.showwarning("Missing Fields", "Please fill all fields.")
            return

        try:
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Invalid Input", "Quantity must be a number.")
            return

        new_order = {
            "id": len(self.orders) + 1,
            "medicine": medicine,
            "quantity": quantity,
            "status": "pending"
        }

        self.orders.append(new_order)
        self.load_table()
        messagebox.showinfo("Success", "Order placed.")
