import tkinter as tk
from login import LoginPage

class StaffDashboard(tk.Frame):
    def __init__(self, master, app, user):
        super().__init__(master)
        self.app = app
        self.configure(bg="#d0f4f7")

        tk.Label(self, text=f"Welcome, Staff!", font=("Helvetica", 22, "bold"), bg="#d0f4f7", fg="#00838f").pack(pady=30)

        tk.Button(self, text="View Inventory", command=self.view_inventory,
                  font=("Helvetica", 12, "bold"), bg="#00acc1", fg="white", relief="flat", width=25, pady=10).pack(pady=10)

        tk.Button(self, text="Logout", command=lambda: self.app.switch_frame(LoginPage, self.app),
                  font=("Helvetica", 11), bg="#f44336", fg="white", relief="flat", width=12, pady=5).pack(pady=30)

    def view_inventory(self):
        from inventory import InventoryManager
        self.app.switch_frame(InventoryManager, self.app)
