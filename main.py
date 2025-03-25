# main.py
import tkinter as tk
from login import LoginPage

class PharmacyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pharmacy Management System")
        self.geometry("1000x650")
        self.resizable(False, False)
        self.configure(bg="#f5f5f5")

        self.current_frame = None
        self.current_user = None
        self.switch_frame(LoginPage, self)

    def switch_frame(self, frame_class, *args):
        if frame_class.__name__ in ["AdminDashboard", "PharmacistDashboard", "StaffDashboard"]:
            self.current_user = args[1]  # Save user for role-based views

        new_frame = frame_class(self, *args)
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = PharmacyApp()
    app.mainloop()
