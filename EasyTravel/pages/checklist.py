import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

CHECKLIST_FILE = "checklist.csv"

# Initialize CSV if not exists
def init_checklist_csv():
    if not os.path.exists(CHECKLIST_FILE):
        df = pd.DataFrame(columns=["Item", "Status"])
        df.to_csv(CHECKLIST_FILE, index=False)

class ChecklistPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0E68C")  # Light Khaki background
        self.controller = controller
        
        # Title Label
        tk.Label(self, text="📝 Travel Checklist", font=("Arial", 18, "bold"), bg="#8B4513", fg="white", padx=20, pady=10).pack(fill="x")
        
        # Entry Section
        entry_frame = tk.Frame(self, bg="#F0E68C")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="👜 Item:", font=("Arial", 12), bg="#F0E68C").grid(row=0, column=0, padx=5)
        self.item_entry = tk.Entry(entry_frame, font=("Arial", 12), width=30)
        self.item_entry.grid(row=0, column=1, padx=5)

        # Buttons Section
        button_frame = tk.Frame(self, bg="#F0E68C")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="✅ Add to Checklist", font=("Arial", 12, "bold"), bg="#008000", fg="white", command=self.add_item).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(button_frame, text="✔ Mark as Completed", font=("Arial", 12, "bold"), bg="#FF4500", fg="white", command=self.mark_completed).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(button_frame, text="🗑 Delete Item", font=("Arial", 12, "bold"), bg="#B22222", fg="white", command=self.delete_item).grid(row=0, column=2, padx=5, pady=5)

        # Listbox Section
        listbox_frame = tk.Frame(self, bg="#FFFACD", relief="ridge", bd=2)
        listbox_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.listbox = tk.Listbox(listbox_frame, font=("Arial", 12), height=10, width=50, bg="white", fg="black", relief="solid")
        self.listbox.pack(padx=10, pady=10, fill="both", expand=True)

        # ✅ Back to Dashboard Button
        tk.Button(self, text="⬅ Back to Dashboard", font=("Arial", 12, "bold"), bg="#8B0000", fg="white", command=lambda: controller.show_frame("DashboardPage")).pack(pady=10)

        self.load_checklist()
    
    def add_item(self):
        item = self.item_entry.get().strip()
        if item:
            df = pd.read_csv(CHECKLIST_FILE)
            new_entry = pd.DataFrame([[item, "Pending"]], columns=["Item", "Status"])
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(CHECKLIST_FILE, index=False)
            
            self.item_entry.delete(0, tk.END)
            self.load_checklist()
        else:
            messagebox.showwarning("⚠ Input Error", "Please enter an item.")
    
    def load_checklist(self):
        self.listbox.delete(0, tk.END)
        df = pd.read_csv(CHECKLIST_FILE)
        for _, row in df.iterrows():
            self.listbox.insert(tk.END, f"{row['Item']} - {row['Status']}")
    
    def mark_completed(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("⚠ Selection Error", "Please select an item to mark as completed.")
            return
        
        selected_text = self.listbox.get(selected_index)
        item_name = selected_text.split(" - ")[0]
        
        df = pd.read_csv(CHECKLIST_FILE)
        df.loc[df["Item"] == item_name, "Status"] = "Completed"
        df.to_csv(CHECKLIST_FILE, index=False)
        
        self.load_checklist()
    
    def delete_item(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("⚠ Selection Error", "Please select an item to delete.")
            return
        
        selected_text = self.listbox.get(selected_index)
        item_name = selected_text.split(" - ")[0]
        
        df = pd.read_csv(CHECKLIST_FILE)
        df = df[df["Item"] != item_name]  # Remove selected item
        df.to_csv(CHECKLIST_FILE, index=False)
        
        self.load_checklist()
        messagebox.showinfo("🗑 Item Deleted", f"'{item_name}' has been removed from the checklist.")

# Initialize CSV file on startup
init_checklist_csv()
