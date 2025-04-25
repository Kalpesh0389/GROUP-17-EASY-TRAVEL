import tkinter as tk
from tkinter import scrolledtext

class NecessitiesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F5F5DC")  # Beige Background
        self.controller = controller

        # Title
        tk.Label(self, text="🏥🍽️🛒 Basic Necessities", font=("Arial", 18, "bold"), bg="#8B4513", fg="white", padx=20, pady=10).pack(fill="x")

        # Buttons Section
        button_frame = tk.Frame(self, bg="#F5F5DC")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="🏥 Hospitals", width=20, font=("Arial", 12, "bold"), bg="#FF4500", fg="white", command=self.show_hospitals).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="🍽️ Restaurants", width=20, font=("Arial", 12, "bold"), bg="#008000", fg="white", command=self.show_restaurants).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="🛒 Grocery Stores", width=20, font=("Arial", 12, "bold"), bg="#4169E1", fg="white", command=self.show_groceries).grid(row=0, column=2, padx=10, pady=5)

        # Frame for Details
        self.details_frame = tk.Frame(self, bg="#FFFACD", relief="ridge", bd=2)
        self.details_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Scrolled Text Widget to Display Details
        self.details_text = scrolledtext.ScrolledText(self.details_frame, wrap="word", font=("Arial", 12), height=12, width=60, bg="white", fg="black", relief="solid")
        self.details_text.pack(padx=10, pady=10, fill="both", expand=True)
        self.details_text.config(state="disabled")

        # ✅ Back to Dashboard Button
        tk.Button(self, text="⬅ Back to Dashboard", font=("Arial", 12, "bold"), bg="#8B0000", fg="white", command=lambda: controller.show_frame("DashboardPage")).pack(pady=10)

    def clear_details(self):
        """Clear the details text widget."""
        self.details_text.config(state="normal")
        self.details_text.delete(1.0, tk.END)
        self.details_text.config(state="disabled")

    def show_hospitals(self):
        """Display hospital details in a formatted way."""
        hospitals = {
            "🏥 City General Hospital": "24/7 Emergency, Cardiology, Orthopedics",
            "🏥 Green Valley Hospital": "Maternity, Pediatrics, General Surgery",
            "🏥 Sunrise Medical Center": "Oncology, Neurology, Radiology"
        }

        self.clear_details()
        self.details_text.config(state="normal")
        self.details_text.insert(tk.END, "🏥 Hospitals:\n\n")
        for name, services in hospitals.items():
            self.details_text.insert(tk.END, f"{name}\n")
            self.details_text.insert(tk.END, f"  🔹 Services: {services}\n\n")
        self.details_text.config(state="disabled")

    def show_restaurants(self):
        """Display restaurant details in a formatted way."""
        restaurants = {
            "🍽️ The Gourmet Kitchen": "Famous for Steak & Seafood",
            "🍽️ La Pasta": "Authentic Italian Pasta & Pizza",
            "🍽️ Spice Garden": "Best Indian Curries & Biryanis"
        }

        self.clear_details()
        self.details_text.config(state="normal")
        self.details_text.insert(tk.END, "🍽️ Restaurants:\n\n")
        for name, specialty in restaurants.items():
            self.details_text.insert(tk.END, f"{name}\n")
            self.details_text.insert(tk.END, f"  🔹 Specialty: {specialty}\n\n")
        self.details_text.config(state="disabled")

    def show_groceries(self):
        """Display grocery store details in a formatted way."""
        groceries = {
            "🛒 FreshMart": "Fresh Produce, Dairy, Bakery",
            "🛒 SuperSaver": "Discount Groceries, Household Items",
            "🛒 Organic Heaven": "Organic Fruits, Vegetables, Health Foods"
        }

        self.clear_details()
        self.details_text.config(state="normal")
        self.details_text.insert(tk.END, "🛒 Grocery Stores:\n\n")
        for name, items in groceries.items():
            self.details_text.insert(tk.END, f"{name}\n")
            self.details_text.insert(tk.END, f"  🔹 Items: {items}\n\n")
        self.details_text.config(state="disabled")
