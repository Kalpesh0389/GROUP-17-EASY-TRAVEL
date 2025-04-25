import tkinter as tk
from tkinter import messagebox
from db import connect_db
import hashlib

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#E8F0FE")

        tk.Label(self, text="Login", font=("Helvetica", 24, "bold"), bg="#E8F0FE", fg="#1A73E8").pack(pady=20)
        tk.Label(self, text="Email:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.email_entry = tk.Entry(self, font=("Helvetica", 12))
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Password:", font=("Helvetica", 12), bg="#E8F0FE", fg="#1A73E8").pack()
        self.password_entry = tk.Entry(self, show="*", font=("Helvetica", 12))
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Login", font=("Helvetica", 12), bg="#1A73E8", fg="white",
                  command=self.login).pack(pady=10)

        tk.Button(self, text="Sign Up", font=("Helvetica", 12), bg="#34A853", fg="white",
                  command=lambda: controller.show_frame("SignupPage")).pack(pady=5)

    def login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = connect_db()
        cursor = conn.cursor()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        cursor.execute("SELECT * FROM users WHERE email=%s AND password_hash=%s", (email, hashed_password))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()

        if user:
            messagebox.showinfo("Success", "Login Successful!")
            self.controller.show_frame("DashboardPage")
        else:
            messagebox.showerror("Error", "Invalid email or password!")
