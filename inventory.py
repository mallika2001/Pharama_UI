# inventory.py

import tkinter as tk
from tkinter import ttk, messagebox
from utils import SAMPLE_INVENTORY

class InventoryManager(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.inventory = SAMPLE_INVENTORY.copy()

        tk.Label(self, text="Inventory Management", font=("Arial", 16)).pack(pady=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("Medicine", "Stock", "Last Updated"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")
        self.load_table()

        # Update form
        update_frame = tk.Frame(self)
        update_frame.pack(pady=10)

        tk.Label(update_frame, text="Medicine").grid(row=0, column=0)
        tk.Label(update_frame, text="New Stock").grid(row=0, column=2)

        self.medicine_entry = tk.Entry(update_frame)
        self.stock_entry = tk.Entry(update_frame)
        self.medicine_entry.grid(row=0, column=1)
        self.stock_entry.grid(row=0, column=3)

        tk.Button(self, text="Update Stock", command=self.update_stock).pack(pady=10)

        # Back Button (role-based)
        role = getattr(self.app, "current_user", {}).get("role", "")
        if role == "admin":
            from admin import AdminDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(AdminDashboard, self.app, self.app.current_user)).pack(pady=10)
        elif role == "pharmacist":
            from pharmacist import PharmacistDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(PharmacistDashboard, self.app, self.app.current_user)).pack(pady=10)
        elif role == "staff":
            from staff import StaffDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(StaffDashboard, self.app, self.app.current_user)).pack(pady=10)

    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.inventory:
            self.tree.insert("", "end", values=(item["medicine"], item["stock"], item["updated"]))

    def update_stock(self):
        med_name = self.medicine_entry.get()
        new_stock = self.stock_entry.get()

        if not med_name or not new_stock:
            messagebox.showwarning("Input Error", "Both fields required.")
            return

        found = False
        for item in self.inventory:
            if item["medicine"].lower() == med_name.lower():
                item["stock"] = new_stock
                item["updated"] = "Now"
                found = True
                break

        if not found:
            messagebox.showerror("Not Found", f"No inventory found for '{med_name}'")
        else:
            self.load_table()
            messagebox.showinfo("Updated", "Stock updated successfully.")
