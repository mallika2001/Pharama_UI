# suppliers.py

import tkinter as tk
from tkinter import ttk, messagebox
from utils import SAMPLE_SUPPLIERS

class SuppliersManager(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.suppliers = SAMPLE_SUPPLIERS.copy()

        tk.Label(self, text="Supplier Management", font=("Arial", 16)).pack(pady=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Contact", "Email", "Phone"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="x", pady=10)
        self.load_table()

        # Form to add supplier
        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Name").grid(row=0, column=0)
        tk.Label(form, text="Contact Person").grid(row=1, column=0)
        tk.Label(form, text="Email").grid(row=0, column=2)
        tk.Label(form, text="Phone").grid(row=1, column=2)

        self.name_entry = tk.Entry(form)
        self.contact_entry = tk.Entry(form)
        self.email_entry = tk.Entry(form)
        self.phone_entry = tk.Entry(form)

        self.name_entry.grid(row=0, column=1)
        self.contact_entry.grid(row=1, column=1)
        self.email_entry.grid(row=0, column=3)
        self.phone_entry.grid(row=1, column=3)

        tk.Button(self, text="Add Supplier", command=self.add_supplier).pack(pady=5)

        # Back button for admin
        role = getattr(self.app, "current_user", {}).get("role", "")
        if role == "admin":
            from admin import AdminDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(AdminDashboard, self.app, self.app.current_user)).pack(pady=10)

    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for sup in self.suppliers:
            self.tree.insert("", "end", values=(sup["id"], sup["name"], sup["contact"], sup["email"], sup["phone"]))

    def add_supplier(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not contact or not email or not phone:
            messagebox.showwarning("Missing Fields", "All fields are required.")
            return

        new_supplier = {
            "id": len(self.suppliers) + 1,
            "name": name,
            "contact": contact,
            "email": email,
            "phone": phone
        }

        self.suppliers.append(new_supplier)
        self.load_table()
        messagebox.showinfo("Success", "Supplier added.")
