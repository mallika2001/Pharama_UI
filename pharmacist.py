import tkinter as tk
from login import LoginPage

class PharmacistDashboard(tk.Frame):
    def __init__(self, master, app, user):
        super().__init__(master)
        self.app = app
        self.user = user
        self.configure(bg="#d0f4f7")

        tk.Label(self, text=f"Welcome, Pharmacist!", font=("Helvetica", 22, "bold"), bg="#d0f4f7", fg="#00838f").pack(pady=30)

        card = tk.Frame(self, bg="white", highlightbackground="#ccc", highlightthickness=1)
        card.pack(pady=10)

        def styled_button(text, command):
            return tk.Button(card, text=text, command=command,
                             font=("Helvetica", 12, "bold"), bg="#00acc1", fg="white",
                             activebackground="#0097a7", relief="flat", width=25, pady=10)

        styled_button("Manage Medicines", self.go_to_medicines).pack(pady=10)
        styled_button("Inventory", self.go_to_inventory).pack(pady=10)
        styled_button("Process Sales", self.go_to_sales).pack(pady=10)
        styled_button("Orders", self.go_to_orders).pack(pady=10)

        tk.Button(self, text="Logout", command=lambda: self.app.switch_frame(LoginPage, self.app),
                  font=("Helvetica", 11), bg="#f44336", fg="white", relief="flat", width=12, pady=5).pack(pady=30)

    def go_to_medicines(self):
        from medicines import MedicineManager
        self.app.switch_frame(MedicineManager, self.app)

    def go_to_inventory(self):
        from inventory import InventoryManager
        self.app.switch_frame(InventoryManager, self.app)

    def go_to_sales(self):
        from sales import SalesManager
        self.app.switch_frame(SalesManager, self.app)

    def go_to_orders(self):
        from orders import OrdersManager
        self.app.switch_frame(OrdersManager, self.app)
