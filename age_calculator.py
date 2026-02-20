import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, datetime
import math

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("520x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#0f0f1a")

        # ── Fonts ──────────────────────────────────────────────
        self.font_title  = ("Georgia", 26, "bold")
        self.font_label  = ("Georgia", 11)
        self.font_entry  = ("Courier New", 13)
        self.font_result = ("Georgia", 13)
        self.font_big    = ("Georgia", 42, "bold")
        self.font_small  = ("Georgia", 11, "italic")
        self.font_btn    = ("Georgia", 13, "bold")

        # ── Colors ─────────────────────────────────────────────
        self.bg       = "#0f0f1a"
        self.card     = "#1a1a2e"
        self.accent   = "#e8b86d"
        self.accent2  = "#c084fc"
        self.text     = "#f0ece2"
        self.muted    = "#8b8fa8"
        self.entry_bg = "#252540"
        self.success  = "#6ee7b7"

        self._build_ui()

    # ─────────────────────────────────────────────────────────
    def _build_ui(self):
        # Title strip
        title_frame = tk.Frame(self.root, bg=self.bg, pady=20)
        title_frame.pack(fill="x")

        tk.Label(title_frame, text="✦ AGE CALCULATOR ✦",
                 font=self.font_title, bg=self.bg, fg=self.accent).pack()
        tk.Label(title_frame, text="Discover how far you've journeyed through time",
                 font=self.font_small, bg=self.bg, fg=self.muted).pack(pady=(4,0))

        # ── Input card ────────────────────────────────────────
        card = tk.Frame(self.root, bg=self.card, bd=0, relief="flat",
                        padx=30, pady=24)
        card.pack(fill="x", padx=30)

        tk.Label(card, text="Enter Your Date of Birth",
                 font=("Georgia", 12, "bold"), bg=self.card, fg=self.accent2).pack(anchor="w")
        tk.Label(card, text="Day / Month / Year",
                 font=("Georgia", 9), bg=self.card, fg=self.muted).pack(anchor="w", pady=(2,12))

        row = tk.Frame(card, bg=self.card)
        row.pack(fill="x")

        self.day_var   = tk.StringVar()
        self.month_var = tk.StringVar()
        self.year_var  = tk.StringVar()

        for var, lbl, width in [
            (self.day_var,   "DD",   5),
            (self.month_var, "MM",   5),
            (self.year_var,  "YYYY", 7),
        ]:
            col = tk.Frame(row, bg=self.card)
            col.pack(side="left", padx=(0,10))
            tk.Label(col, text=lbl, font=("Courier New", 9), bg=self.card, fg=self.muted).pack()
            e = tk.Entry(col, textvariable=var, width=width,
                         font=self.font_entry, bg=self.entry_bg, fg=self.text,
                         insertbackground=self.accent, relief="flat",
                         highlightthickness=2, highlightcolor=self.accent,
                         highlightbackground=self.entry_bg, justify="center")
            e.pack(ipady=6)

        # separator
        sep = tk.Frame(card, bg=self.muted, height=1)
        sep.pack(fill="x", pady=(18,14))

        # Reference date (optional)
        tk.Label(card, text="Reference Date  (leave blank = today)",
                 font=("Georgia", 9), bg=self.card, fg=self.muted).pack(anchor="w", pady=(0,6))

        row2 = tk.Frame(card, bg=self.card)
        row2.pack(fill="x")

        self.ref_day_var   = tk.StringVar()
        self.ref_month_var = tk.StringVar()
        self.ref_year_var  = tk.StringVar()

        for var, lbl, width in [
            (self.ref_day_var,   "DD",   5),
            (self.ref_month_var, "MM",   5),
            (self.ref_year_var,  "YYYY", 7),
        ]:
            col = tk.Frame(row2, bg=self.card)
            col.pack(side="left", padx=(0,10))
            tk.Label(col, text=lbl, font=("Courier New", 9), bg=self.card, fg=self.muted).pack()
            e = tk.Entry(col, textvariable=var, width=width,
                         font=self.font_entry, bg=self.entry_bg, fg=self.muted,
                         insertbackground=self.accent, relief="flat",
                         highlightthickness=2, highlightcolor=self.accent2,
                         highlightbackground=self.entry_bg, justify="center")
            e.pack(ipady=6)

        # ── Buttons ───────────────────────────────────────────
        btn_frame = tk.Frame(self.root, bg=self.bg, pady=18)
        btn_frame.pack()

        calc_btn = tk.Button(btn_frame, text="Calculate Age →",
                             font=self.font_btn, bg=self.accent, fg=self.bg,
                             relief="flat", padx=24, pady=10, cursor="hand2",
                             activebackground="#d4a45a", activeforeground=self.bg,
                             command=self.calculate)
        calc_btn.pack(side="left", padx=(0,12))

        clear_btn = tk.Button(btn_frame, text="Clear",
                              font=("Georgia", 11), bg=self.entry_bg, fg=self.muted,
                              relief="flat", padx=16, pady=10, cursor="hand2",
                              activebackground="#333355",
                              command=self.clear)
        clear_btn.pack(side="left")

        # ── Results card ──────────────────────────────────────
        self.result_frame = tk.Frame(self.root, bg=self.card, padx=30, pady=22)
        self.result_frame.pack(fill="x", padx=30)

        tk.Label(self.result_frame, text="Your Age",
                 font=("Georgia", 10, "bold"), bg=self.card, fg=self.muted).pack()

        self.age_label = tk.Label(self.result_frame, text="—",
                                  font=self.font_big, bg=self.card, fg=self.accent)
        self.age_label.pack()

        self.age_sub = tk.Label(self.result_frame, text="years old",
                                font=self.font_small, bg=self.card, fg=self.muted)
        self.age_sub.pack()

        sep2 = tk.Frame(self.result_frame, bg=self.muted, height=1)
        sep2.pack(fill="x", pady=14)

        self.detail_label = tk.Label(self.result_frame, text="",
                                     font=self.font_result, bg=self.card,
                                     fg=self.text, justify="left", wraplength=420)
        self.detail_label.pack(anchor="w")

        self.extra_label = tk.Label(self.result_frame, text="",
                                    font=("Georgia", 9, "italic"), bg=self.card,
                                    fg=self.success, justify="left")
        self.extra_label.pack(anchor="w", pady=(6,0))

        # Footer
        tk.Label(self.root, text="Made with Python & Tkinter  ·  ✦",
                 font=("Georgia", 8), bg=self.bg, fg=self.muted).pack(pady=14)

    # ─────────────────────────────────────────────────────────
    def calculate(self):
        try:
            day   = int(self.day_var.get())
            month = int(self.month_var.get())
            year  = int(self.year_var.get())
            dob   = date(year, month, day)
        except (ValueError, TypeError):
            messagebox.showerror("Invalid Input", "Please enter a valid Date of Birth.\nDay (1-31), Month (1-12), Year (e.g. 1998)")
            return

        # Reference date
        try:
            rd = self.ref_day_var.get().strip()
            rm = self.ref_month_var.get().strip()
            ry = self.ref_year_var.get().strip()
            if rd and rm and ry:
                ref = date(int(ry), int(rm), int(rd))
            else:
                ref = date.today()
        except ValueError:
            messagebox.showerror("Invalid Input", "Reference date is invalid.")
            return

        if dob > ref:
            messagebox.showerror("Error", "Date of birth cannot be in the future!")
            return

        # ── Calculations ──────────────────────────────────────
        years  = ref.year - dob.year
        months = ref.month - dob.month
        days   = ref.day   - dob.day

        if days < 0:
            months -= 1
            prev_month = (ref.month - 1) or 12
            prev_year  = ref.year if ref.month > 1 else ref.year - 1
            import calendar
            days += calendar.monthrange(prev_year, prev_month)[1]

        if months < 0:
            years  -= 1
            months += 12

        total_days   = (ref - dob).days
        total_weeks  = total_days // 7
        total_months = years * 12 + months
        total_hours  = total_days * 24
        next_bday    = date(ref.year, dob.month, dob.day)
        if next_bday < ref:
            try:
                next_bday = date(ref.year + 1, dob.month, dob.day)
            except ValueError:
                next_bday = date(ref.year + 1, dob.month, dob.day - 1)
        days_to_bday = (next_bday - ref).days

        # ── Update UI ──────────────────────────────────────────
        self.age_label.config(text=str(years), fg=self.accent)

        detail = (
            f"  {years} years   {months} months   {days} days\n\n"
            f"  Total days    :  {total_days:,}\n"
            f"  Total weeks   :  {total_weeks:,}\n"
            f"  Total months  :  {total_months:,}\n"
            f"  Total hours   :  {total_hours:,}"
        )
        self.detail_label.config(text=detail)

        if days_to_bday == 0:
            extra = "🎂  Happy Birthday today!"
        elif days_to_bday == 1:
            extra = "🎉  Your birthday is tomorrow!"
        else:
            extra = f"🗓  Next birthday in {days_to_bday} days  ({next_bday.strftime('%d %b %Y')})"

        self.extra_label.config(text=extra)

    # ─────────────────────────────────────────────────────────
    def clear(self):
        for v in [self.day_var, self.month_var, self.year_var,
                  self.ref_day_var, self.ref_month_var, self.ref_year_var]:
            v.set("")
        self.age_label.config(text="—")
        self.detail_label.config(text="")
        self.extra_label.config(text="")


# ─── Entry point ───────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app  = AgeCalculatorApp(root)
    root.mainloop()