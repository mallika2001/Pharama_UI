# login.py

import tkinter as tk
from tkinter import messagebox
from utils import USERS

class LoginPage(tk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.configure(bg="#d0f4f7")  # Light teal background

        # Login Box Frame
        box = tk.Frame(self, bg="white", bd=0, highlightbackground="#ccc", highlightthickness=1)
        box.place(relx=0.5, rely=0.5, anchor="center", width=350, height=350)

        # Title
        tk.Label(box, text="Pharmacy Login", font=("Helvetica", 18, "bold"), bg="white", fg="#333").pack(pady=20)

        # Username Field
        tk.Label(box, text="Username", font=("Helvetica", 12), bg="white", anchor="w").pack(fill="x", padx=30)
        self.username_entry = tk.Entry(box, font=("Helvetica", 12), bd=1, relief="flat", highlightthickness=1, highlightcolor="#00acc1")
        self.username_entry.pack(padx=30, pady=(0, 15), fill="x")

        # Password Field
        tk.Label(box, text="Password", font=("Helvetica", 12), bg="white", anchor="w").pack(fill="x", padx=30)
        self.password_entry = tk.Entry(box, font=("Helvetica", 12), show="*", bd=1, relief="flat", highlightthickness=1, highlightcolor="#00acc1")
        self.password_entry.pack(padx=30, pady=(0, 25), fill="x")

        # Login Button
        tk.Button(
            box, text="Login", command=self.login_user,
            font=("Helvetica", 12, "bold"), bg="#00acc1", fg="white",
            activebackground="#0097a7", activeforeground="white",
            relief="flat", padx=10, pady=5
        ).pack(pady=10)

        # Extra Links
        tk.Label(box, text="Forgot Password?", bg="white", fg="#00acc1", font=("Helvetica", 10)).pack()
        tk.Button(
            box, text="New User? Register", command=self.register_user,
            bg="white", fg="#00acc1", font=("Helvetica", 10, "underline"),
            relief="flat", cursor="hand2"
        ).pack(pady=(5, 10))

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = next((u for u in USERS if u['username'] == username and u['password'] == password), None)

        if user:
            self.app.current_user = user
            role = user['role']
            if role == 'admin':
                from admin import AdminDashboard
                self.app.switch_frame(AdminDashboard, self.app, user)
            elif role == 'pharmacist':
                from pharmacist import PharmacistDashboard
                self.app.switch_frame(PharmacistDashboard, self.app, user)
            elif role == 'staff':
                from staff import StaffDashboard
                self.app.switch_frame(StaffDashboard, self.app, user)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def register_user(self):
        reg_win = tk.Toplevel(self)
        reg_win.title("New User Registration")
        reg_win.geometry("300x250")
        reg_win.configure(bg="#f0f0f0")
        reg_win.grab_set()

        tk.Label(reg_win, text="Create New Account", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(reg_win, text="Username", bg="#f0f0f0").pack()
        username = tk.Entry(reg_win)
        username.pack(pady=5)

        tk.Label(reg_win, text="Password", bg="#f0f0f0").pack()
        password = tk.Entry(reg_win, show="*")
        password.pack(pady=5)

        tk.Label(reg_win, text="Role", bg="#f0f0f0").pack()
        role_var = tk.StringVar()
        role_menu = tk.OptionMenu(reg_win, role_var, "admin", "pharmacist", "staff")
        role_menu.pack(pady=5)

    def register_user(self):
        reg_win = tk.Toplevel(self)
        reg_win.title("New User Registration")
        reg_win.geometry("300x250")
        reg_win.configure(bg="#f0f0f0")
        reg_win.grab_set()

        tk.Label(reg_win, text="Create New Account", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(reg_win, text="Username", bg="#f0f0f0").pack()
        username = tk.Entry(reg_win)
        username.pack(pady=5)

        tk.Label(reg_win, text="Password", bg="#f0f0f0").pack()
        password = tk.Entry(reg_win, show="*")
        password.pack(pady=5)

        tk.Label(reg_win, text="Role", bg="#f0f0f0").pack()
        role_var = tk.StringVar()
        role_menu = tk.OptionMenu(reg_win, role_var, "admin", "pharmacist", "staff")
        role_menu.pack(pady=5)

    def register_user(self):
        reg_win = tk.Toplevel(self)
        reg_win.title("New User Registration")
        reg_win.geometry("300x250")
        reg_win.configure(bg="#f0f0f0")
        reg_win.grab_set()

        tk.Label(reg_win, text="Create New Account", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(reg_win, text="Username", bg="#f0f0f0").pack()
        username = tk.Entry(reg_win)
        username.pack(pady=5)

        tk.Label(reg_win, text="Password", bg="#f0f0f0").pack()
        password = tk.Entry(reg_win, show="*")
        password.pack(pady=5)

        tk.Label(reg_win, text="Role", bg="#f0f0f0").pack()
        role_var = tk.StringVar()
        role_menu = tk.OptionMenu(reg_win, role_var, "admin", "pharmacist", "staff")
        role_menu.pack(pady=5)

        def save_user():
            uname = username.get()
            pwd = password.get()
            role = role_var.get()

            if not uname or not pwd or not role:
                messagebox.showwarning("Input Error", "All fields are required.")
                return

            if any(u['username'] == uname for u in USERS):
                messagebox.showerror("Exists", "Username already exists.")
                return

            USERS.append({'username': uname, 'password': pwd, 'role': role})
            messagebox.showinfo("Success", "User registered!")
            reg_win.destroy()

        tk.Button(reg_win, text="Register", command=save_user,
                  bg="#00acc1", fg="white", relief="flat", font=("Helvetica", 11, "bold")).pack(pady=10)