import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import json

# This is the Student Budget Tracker application
# Purpose: Help students track income and expenses easily

# Initialize main window
root = tk.Tk()
root.title("Student Budget Tracker")
root.geometry("600x400")

# Global variables to store income and expenses
income_list = []
expense_list = []

# Function to add income
def add_income():
    try:
        amount = float(income_entry.get())
        source = income_source_entry.get()
        if source == "":
            messagebox.showerror("Input Error", "Please enter the income source.")
            return
        income_list.append({"amount": amount, "source": source})
        messagebox.showinfo("Success", "Income added successfully!")
        income_entry.delete(0, tk.END)
        income_source_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for income.")

# Function to add expense
def add_expense():
    try:
        amount = float(expense_entry.get())
        category = expense_category.get()
        if category == "Select Category":
            messagebox.showerror("Input Error", "Please select a category.")
            return
        expense_list.append({"amount": amount, "category": category})
        messagebox.showinfo("Success", "Expense added successfully!")
        expense_entry.delete(0, tk.END)
        expense_category.set("Select Category")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for expense.")

# Function to view summary
def view_summary():
    total_income = sum(item['amount'] for item in income_list)
    total_expense = sum(item['amount'] for item in expense_list)
    balance = total_income - total_expense

    summary_message = f"Total Income: ${total_income:.2f}\nTotal Expenses: ${total_expense:.2f}\nRemaining Balance: ${balance:.2f}"
    messagebox.showinfo("Budget Summary", summary_message)

# Function to exit the app
def exit_app():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# Function to save data to file
def save_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        data = {"income": income_list, "expenses": expense_list}
        with open(file_path, 'w') as f:
            json.dump(data, f)
        messagebox.showinfo("Saved", "Data saved successfully!")

# Function to create second window for adding income and expenses
def open_add_window():
    add_window = tk.Toplevel(root)
    add_window.title("Add Income / Expense")
    add_window.geometry("400x400")

    # Labels
    tk.Label(add_window, text="Income Amount:").pack(pady=5)
    global income_entry
    income_entry = tk.Entry(add_window)
    income_entry.pack(pady=5)

    tk.Label(add_window, text="Income Source:").pack(pady=5)
    global income_source_entry
    income_source_entry = tk.Entry(add_window)
    income_source_entry.pack(pady=5)

    tk.Button(add_window, text="Add Income", command=add_income).pack(pady=10)

    tk.Label(add_window, text="Expense Amount:").pack(pady=5)
    global expense_entry
    expense_entry = tk.Entry(add_window)
    expense_entry.pack(pady=5)

    tk.Label(add_window, text="Expense Category:").pack(pady=5)
    global expense_category
    expense_category = ttk.Combobox(add_window, values=["Rent", "Groceries", "Transportation", "Entertainment", "Other"])
    expense_category.set("Select Category")
    expense_category.pack(pady=5)

    tk.Button(add_window, text="Add Expense", command=add_expense).pack(pady=10)

# Adding simple images (replace 'logo.png' with your real image)
try:
    logo_img = Image.open("logo.png")
    logo_img = logo_img.resize((100, 100))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_photo)
    logo_label.pack(pady=10)
except Exception as e:
    print("Logo image not found.")

# Labels in the main window
tk.Label(root, text="Welcome to Student Budget Tracker", font=("Arial", 16)).pack(pady=10)

# Buttons in the main window
tk.Button(root, text="Add Income / Expense", command=open_add_window).pack(pady=5)
tk.Button(root, text="View Summary", command=view_summary).pack(pady=5)
tk.Button(root, text="Save Data", command=save_data).pack(pady=5)
tk.Button(root, text="Exit", command=exit_app).pack(pady=5)

# Start the GUI event loop
root.mainloop()
