import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from login_signup import LoginPage, SignupPage
from pages.dashboard import DashboardPage
from pages.destination import DestinationFrame
from pages.itinerary import ItineraryPage
from pages.suggestions import SuggestionsPage
from pages.necessities import NecessitiesPage
from pages.checklist import ChecklistPage
from pages.budget import BudgetPage
from pages.reviews import ReviewsPage

# Get the absolute path of the image inside the EasyTravel folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "main.jpg")

class EasyTravelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Easy Travel Management System")
        self.geometry("1000x700")
        self.current_destination = None  # To store selected destination

        # Load and set background image
        self.bg_image = Image.open(image_path)
        self.bg_image = self.bg_image.resize((1000, 700), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a Canvas to hold the background image
        self.canvas = tk.Canvas(self, width=1000, height=700)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
        self.canvas.place(relwidth=1, relheight=1)

        # Create a main frame with rounded corners effect
        main_frame = tk.Frame(self, bg="#F8F9FA", padx=20, pady=20)
        main_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        # Create a container for page frames
        container = tk.Frame(main_frame, bg="#F8F9FA")
        container.pack(fill="both", expand=True)

        # Initialize frames
        self.frames = {}

        # Add all pages
        pages = [
            LoginPage, SignupPage, DashboardPage, DestinationFrame,
            ItineraryPage, BudgetPage, SuggestionsPage,
            NecessitiesPage, ChecklistPage, ReviewsPage
        ]

        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.configure(bg="#FFFFFF")
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Configure content area grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Show initial frame (Login Page)
        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        """Show the specified frame."""
        frame = self.frames[page_name]
        frame.tkraise()
        
        # Update dashboard header if showing dashboard
        if page_name == "DashboardPage" and hasattr(frame, 'update_destination_label'):
            frame.update_destination_label()

# Run Application
if __name__ == "__main__":
    app = EasyTravelApp()
    app.mainloop()