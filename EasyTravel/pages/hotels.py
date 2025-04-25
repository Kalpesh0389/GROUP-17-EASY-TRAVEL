import tkinter as tk
from tkinter import ttk

class HotelsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#FFFFFF")  # Ensure clean background

        # Title for the Hotels Page
        title_label = tk.Label(self, text="Available Hotels", font=("Helvetica", 24, "bold"), bg="#FFFFFF", fg="#1A73E8")
        title_label.pack(pady=20)

        # Sample hotel data
        hotels = [
            {"name": "Hotel Sunshine", "description": "A beautiful hotel with a sea view.", "image": "hotel1.jpg"},
            {"name": "Mountain Retreat", "description": "A cozy retreat in the mountains.", "image": "hotel2.jpg"},
            {"name": "City Center Inn", "description": "Conveniently located in the city center.", "image": "hotel3.jpg"},
        ]

        # Create a frame to hold hotel listings
        hotel_frame = tk.Frame(self, bg="#FFFFFF")
        hotel_frame.pack(pady=10)

        for hotel in hotels:
            # Create a frame for each hotel
            hotel_card = tk.Frame(hotel_frame, bg="#F8F9FA", padx=10, pady=10)
            hotel_card.pack(fill="x", pady=5)

            # Hotel name
            name_label = tk.Label(hotel_card, text=hotel["name"], font=("Helvetica", 18, "bold"), bg="#F8F9FA")
            name_label.pack(anchor="w")

            # Hotel description
            description_label = tk.Label(hotel_card, text=hotel["description"], bg="#F8F9FA")
            description_label.pack(anchor="w")

            # Placeholder for hotel image
            # In a real application, you would load the image using PIL or similar
            image_label = tk.Label(hotel_card, text="[Image: {}]".format(hotel["image"]), bg="#F8F9FA")
            image_label.pack(anchor="w")

        # Back button to return to the main menu
        back_button = tk.Button(self, text="Back to Menu", command=lambda: controller.show_frame("DashboardPage"))
        back_button.pack(pady=20)
