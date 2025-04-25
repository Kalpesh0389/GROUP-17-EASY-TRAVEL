import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class DashboardPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg="#f5f7fa")  # Light background
        
        # Header Frame with gradient effect
        header_frame = tk.Frame(self, bg="#4b6cb7", height=100)
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Add a subtle pattern or logo
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
            self.logo_img = ImageTk.PhotoImage(Image.open(logo_path).resize((40,40)))
            tk.Label(header_frame, image=self.logo_img, bg="#4b6cb7").pack(side="left", padx=20)
        except:
            pass  # Skip if no logo
        
        self.destination_label = tk.Label(
            header_frame, 
            text="Welcome to Easy Travel", 
            font=("Montserrat", 18, "bold"), 
            bg="#4b6cb7", 
            fg="white"
        )
        self.destination_label.pack(pady=20, expand=True)
        
        # Main Content Frame
        content_frame = tk.Frame(self, bg="#f5f7fa")
        content_frame.pack(fill="both", expand=True, padx=40, pady=10)
        
        # Button Container with shadow effect
        button_container = tk.Frame(content_frame, bg="#f5f7fa")
        button_container.pack(expand=True)
        
        # Navigation Buttons with modern colors
        buttons = [
            ("📍 Select Destination", "DestinationFrame", "#6a11cb", "#2575fc"),
            ("🗓 Itinerary Planner", "ItineraryPage", "#11998e", "#38ef7d"),
            ("💰 Budget Calculator", "BudgetPage", "#f46b45", "#eea849"),
            ("💡 Travel Suggestions", "SuggestionsPage", "#8e2de2", "#4a00e0"),
            ("🧳 Packing Checklist", "ChecklistPage", "#f12711", "#f5af19"),
            ("⭐ Destination Reviews", "ReviewsPage", "#c31432", "#240b36")
        ]
        
        for text, page, color1, color2 in buttons:
            btn = tk.Button(
                button_container, 
                text=text, 
                command=lambda p=page: controller.show_frame(p),
                width=25,
                font=("Montserrat", 12),
                bd=0,
                padx=15,
                pady=12,
                activebackground="#f5f7fa",
                activeforeground="black"
            )
            
            # Apply gradient background effect
            btn.configure(
                bg=color1,
                fg="white",
                relief="flat",
                borderwidth=0,
                highlightthickness=0
            )
            
            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn, c=color2: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=color1: b.config(bg=c))
            
            btn.pack(pady=8, fill="x")
        
        # Footer Frame
        footer_frame = tk.Frame(self, bg="#4b6cb7", height=50)
        footer_frame.pack(side="bottom", fill="x", pady=(20,0))
        
        # Logout Button with modern style
        logout_btn = tk.Button(
            footer_frame, 
            text="🚪 Logout", 
            command=lambda: controller.show_frame("LoginPage"),
            font=("Montserrat", 10),
            bg="#4b6cb7",
            fg="white",
            bd=0,
            activebackground="#3a56a5",
            activeforeground="white"
        )
        logout_btn.pack(side="right", padx=20)
        
        # Current Destination Indicator
        self.dest_indicator = tk.Label(
            footer_frame,
            text="No destination selected",
            font=("Montserrat", 9),
            bg="#4b6cb7",
            fg="white"
        )
        self.dest_indicator.pack(side="left", padx=20)
    
    def update_destination_label(self):
        """Update the header with current destination"""
        if self.controller.current_destination:
            self.destination_label.config(
                text=f"Planning trip to: {self.controller.current_destination}"
            )
            self.dest_indicator.config(
                text=f"Current destination: {self.controller.current_destination}",
                fg="#f5f7fa"
            )
        else:
            self.destination_label.config(text="Welcome to Easy Travel")
            self.dest_indicator.config(text="No destination selected", fg="#cccccc")
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