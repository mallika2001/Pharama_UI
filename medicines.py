# medicines.py

import tkinter as tk
from tkinter import messagebox, ttk
from utils import SAMPLE_MEDICINES

class MedicineManager(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.medicines = SAMPLE_MEDICINES.copy()

        tk.Label(self, text="Medicine Management", font=("Arial", 16)).pack(pady=10)

        # Form
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name").grid(row=0, column=0)
        tk.Label(form_frame, text="Price").grid(row=0, column=2)

        self.name_entry = tk.Entry(form_frame)
        self.price_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1)
        self.price_entry.grid(row=0, column=3)

        tk.Label(form_frame, text="Stock").grid(row=1, column=0)
        tk.Label(form_frame, text="Category").grid(row=1, column=2)

        self.stock_entry = tk.Entry(form_frame)
        self.category_entry = tk.Entry(form_frame)
        self.stock_entry.grid(row=1, column=1)
        self.category_entry.grid(row=1, column=3)

        tk.Button(self, text="Add Medicine", command=self.add_medicine).pack(pady=5)

        # Table
        self.tree = ttk.Treeview(self, columns=("Name", "Price", "Stock", "Category"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")
        self.load_table()

        # Back button based on role
        role = getattr(self.app, "current_user", {}).get("role", "")
        if role == "admin":
            from admin import AdminDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(AdminDashboard, self.app, self.app.current_user)).pack(pady=10)
        elif role == "pharmacist":
            from pharmacist import PharmacistDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(PharmacistDashboard, self.app, self.app.current_user)).pack(pady=10)

    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for med in self.medicines:
            self.tree.insert("", "end", values=(med["name"], med["price"], med["stock"], med["category"]))

    def add_medicine(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        stock = self.stock_entry.get()
        category = self.category_entry.get()

        if not name or not price or not stock or not category:
            messagebox.showwarning("Missing Info", "All fields are required.")
            return

        self.medicines.append({
            "name": name,
            "price": price,
            "stock": stock,
            "category": category
        })
        self.load_table()
        messagebox.showinfo("Success", "Medicine added!")
