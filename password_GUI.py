import tkinter as tk
from tkinter import messagebox


class PasswordCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f6f8")

        self.build_ui()

    def build_ui(self):
        # Header
        header = tk.Label(
            self.root,
            text="Password Strength Checker",
            font=("Arial", 16, "bold"),
            bg="#1f6aa5",
            fg="white",
            pady=10
        )
        header.pack(fill="x")

        # Frame
        frame = tk.Frame(self.root, bg="#f4f6f8", pady=30)
        frame.pack(fill="both", expand=True)

        tk.Label(
            frame,
            text="Enter Password:",
            bg="#f4f6f8",
            font=("Arial", 11)
        ).pack(pady=5)

        self.password_entry = tk.Entry(
            frame,
            width=30,
            show="*",
            font=("Arial", 11)
        )
        self.password_entry.pack(pady=5)

        tk.Button(
            frame,
            text="Check Strength",
            command=self.check_password,
            bg="#1f6aa5",
            fg="white",
            width=18,
            font=("Arial", 10, "bold")
        ).pack(pady=15)

        self.result_label = tk.Label(
            frame,
            text="",
            font=("Arial", 12, "bold"),
            bg="#f4f6f8"
        )
        self.result_label.pack(pady=10)

    def check_password(self):
        password = self.password_entry.get()

        if not password:
            messagebox.showwarning("Input Error", "Please enter a password")
            return

        score = 0

        if len(password) >= 8:
            score += 1
        if any(ch.isupper() for ch in password):
            score += 1
        if any(ch.isdigit() for ch in password):
            score += 1
        if any(not ch.isalnum() for ch in password):
            score += 1

        if score <= 1:
            self.result_label.config(
                text="❌ Weak Password",
                fg="red"
            )
        elif score == 2 or score == 3:
            self.result_label.config(
                text="⚠ Medium Password",
                fg="orange"
            )
        else:
            self.result_label.config(
                text="✅ Strong Password",
                fg="green"
            )


# ---------- RUN ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCheckerGUI(root)
    root.mainloop()
