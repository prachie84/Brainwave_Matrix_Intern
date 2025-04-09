import tkinter as tk
from tkinter import messagebox

users = {'1234': {'pin': '1111', 'balance': 1000}}
current_user = None

def atm_screen():
    def balance():
        messagebox.showinfo("Balance", f"₹ {users[current_user]['balance']}")

    def deposit():
        amt = entry.get()
        if amt.isdigit():
            users[current_user]['balance'] += int(amt)
            messagebox.showinfo("Success", f"₹{amt} deposited.")
            entry.delete(0, tk.END)

    def withdraw():
        amt = entry.get()
        if amt.isdigit():
            amt = int(amt)
            if amt <= users[current_user]['balance']:
                users[current_user]['balance'] -= amt
                messagebox.showinfo("Success", f"₹{amt} withdrawn.")
            else:
                messagebox.showerror("Error", "Insufficient funds")
            entry.delete(0, tk.END)

    win = tk.Tk()
    win.title("ATM")
    tk.Label(win, text="ATM Dashboard", font=("Arial", 14)).pack(pady=10)
    tk.Button(win, text="Check Balance", command=balance).pack(pady=5)
    entry = tk.Entry(win)
    entry.pack(pady=5)
    tk.Button(win, text="Deposit", command=deposit).pack(pady=2)
    tk.Button(win, text="Withdraw", command=withdraw).pack(pady=2)
    tk.Button(win, text="Logout", command=win.destroy).pack(pady=10)
    win.mainloop()

def login():
    def verify():
        card = card_entry.get()
        pin = pin_entry.get()
        if card in users and users[card]['pin'] == pin:
            global current_user
            current_user = card
            login_win.destroy()
            atm_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid Card or PIN")

    login_win = tk.Tk()
    login_win.title("Login")
    tk.Label(login_win, text="ATM Login", font=("Arial", 14)).pack(pady=10)
    tk.Label(login_win, text="Card:").pack()
    card_entry = tk.Entry(login_win)
    card_entry.pack()
    tk.Label(login_win, text="PIN:").pack()
    pin_entry = tk.Entry(login_win, show="*")
    pin_entry.pack()
    tk.Button(login_win, text="Login", command=verify).pack(pady=10)
    login_win.mainloop()

login()
