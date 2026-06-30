import tkinter as tk
from tkinter import messagebox
import os

USERS_FILE = "users.txt"

def read_file():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if "," in line:
                    username, password = line.split(",", 1)
                    users[username] = password
    return users

def write_file(username, password):
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def login():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()
    users = read_file()
    if username in users and users[username] == password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def signup():
    username = entry_user.get().strip()
    password = entry_pass.get().strip()
    if not username or not password:
        messagebox.showwarning("Input Error", "Username and password cannot be empty.")
        return
    users = read_file()
    if username in users:
        messagebox.showwarning("Signup", "Username already exists. Choose another.")
        return
    write_file(username, password)
    messagebox.showinfo("Signup", f"Account created for {username}!")

def main():
    global entry_user, entry_pass, root
    root = tk.Tk()
    root.title("Login System")
    root.geometry("300x200")

    tk.Label(root, text="Username:").pack(pady=5)
    entry_user = tk.Entry(root, width=25)
    entry_user.pack()

    tk.Label(root, text="Password:").pack(pady=5)
    entry_pass = tk.Entry(root, show="*", width=25)
    entry_pass.pack()

    tk.Button(root, text="Login", command=login, width=10).pack(pady=5)
    tk.Button(root, text="Sign Up", command=signup, width=10).pack(pady=2)

    root.mainloop()

if __name__ == "__main__":
    print("Starting Login System...")
    main()
