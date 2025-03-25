# sales.py

import tkinter as tk
from tkinter import ttk, messagebox
from utils import SAMPLE_MEDICINES, SAMPLE_SALES

class SalesManager(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.sales = SAMPLE_SALES.copy()

        tk.Label(self, text="Sales Processing", font=("Arial", 16)).pack(pady=10)

        # Sales Table
        self.tree = ttk.Treeview(self, columns=("Sale ID", "Medicine", "Qty", "Total"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")
        self.load_table()

        # Form
        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Medicine").grid(row=0, column=0)
        tk.Label(form, text="Quantity").grid(row=0, column=2)

        self.med_var = tk.StringVar()
        self.med_dropdown = ttk.Combobox(form, textvariable=self.med_var, values=[m["name"] for m in SAMPLE_MEDICINES])
        self.qty_entry = tk.Entry(form)

        self.med_dropdown.grid(row=0, column=1)
        self.qty_entry.grid(row=0, column=3)

        tk.Button(self, text="Record Sale", command=self.record_sale).pack(pady=10)

        # Back button
        role = getattr(self.app, "current_user", {}).get("role", "")
        if role == "pharmacist":
            from pharmacist import PharmacistDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(PharmacistDashboard, self.app, self.app.current_user)).pack(pady=10)

    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for sale in self.sales:
            self.tree.insert("", "end", values=(sale["id"], sale["medicine"], sale["quantity"], sale["total"]))

    def record_sale(self):
        medicine = self.med_var.get()
        qty_str = self.qty_entry.get()

        if not medicine or not qty_str:
            messagebox.showwarning("Missing Fields", "All fields required.")
            return

        try:
            quantity = int(qty_str)
        except ValueError:
            messagebox.showerror("Invalid Quantity", "Quantity must be a number.")
            return

        med = next((m for m in SAMPLE_MEDICINES if m["name"] == medicine), None)
        if not med:
            messagebox.showerror("Not Found", "Medicine not found.")
            return

        price = float(med["price"])
        total = price * quantity

        self.sales.append({
            "id": len(self.sales) + 1,
            "medicine": medicine,
            "quantity": quantity,
            "total": total
        })

        self.load_table()
        messagebox.showinfo("Success", "Sale recorded.")
