# payments.py

import tkinter as tk
from tkinter import ttk, messagebox
from utils import SAMPLE_PAYMENTS

class PaymentsManager(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.payments = SAMPLE_PAYMENTS.copy()

        tk.Label(self, text="Payment Records", font=("Arial", 16)).pack(pady=10)

        # Payment Table
        self.tree = ttk.Treeview(self, columns=("Payment ID", "Order ID", "Amount", "Method", "Status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="x", pady=10)
        self.load_table()

        # Update Section
        form = tk.Frame(self)
        form.pack(pady=10)

        tk.Label(form, text="Payment ID").grid(row=0, column=0)
        tk.Label(form, text="New Status").grid(row=0, column=2)

        self.id_entry = tk.Entry(form)
        self.status_var = tk.StringVar()
        self.status_menu = ttk.Combobox(form, textvariable=self.status_var, values=["Pending", "Completed", "Failed"])

        self.id_entry.grid(row=0, column=1)
        self.status_menu.grid(row=0, column=3)

        tk.Button(self, text="Update Status", command=self.update_status).pack(pady=5)

        # Back button for admin only
        role = getattr(self.app, "current_user", {}).get("role", "")
        if role == "admin":
            from admin import AdminDashboard
            tk.Button(self, text="Back", command=lambda: self.app.switch_frame(AdminDashboard, self.app, self.app.current_user)).pack(pady=10)

    def load_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for p in self.payments:
            self.tree.insert("", "end", values=(p["id"], p["order_id"], p["amount"], p["method"], p["status"]))

    def update_status(self):
        try:
            pay_id = int(self.id_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Payment ID must be a number.")
            return

        new_status = self.status_var.get()
        if not new_status:
            messagebox.showwarning("Select Status", "Please select a new status.")
            return

        for p in self.payments:
            if p["id"] == pay_id:
                p["status"] = new_status
                self.load_table()
                messagebox.showinfo("Updated", "Payment status updated.")
                return

        messagebox.showerror("Not Found", f"No payment found with ID {pay_id}")
