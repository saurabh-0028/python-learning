import tkinter as tk

class BubbleCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✦ Bubble Calculator")
        self.root.geometry("380x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4ff")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")
        self.sub_display_var = tk.StringVar(value="")

        self.setup_ui()

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg="#f0f4ff", padx=15, pady=15)
        main_frame.pack(fill="both", expand=True)

        # Title
        title_label = tk.Label(
            main_frame,
            text="◈Calculator◈",
            font=("Courier New", 20, "bold"),
            bg="#f0f4ff",
            fg="#3355cc"
        )
        title_label.pack(pady=(5, 0))

        # Sub display (expression)
        sub_frame = tk.Frame(main_frame, bg="#dde4f5", bd=0,
                             highlightthickness=1, highlightbackground="#aabbee")
        sub_frame.pack(fill="x", pady=(10, 2))
        self.sub_label = tk.Label(
            sub_frame,
            textvariable=self.sub_display_var,
            font=("Courier New", 12),
            bg="#dde4f5",
            fg="#7788bb",
            anchor="e",
            padx=15,
            pady=4
        )
        self.sub_label.pack(fill="x")

        # Main display
        display_frame = tk.Frame(main_frame, bg="#ffffff",
                                  highlightthickness=2, highlightbackground="#99aadd")
        display_frame.pack(fill="x", pady=(0, 15))
        self.display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("Courier New", 38, "bold"),
            bg="#ffffff",
            fg="#223399",
            anchor="e",
            padx=20,
            pady=15
        )
        self.display_label.pack(fill="x")

        # Buttons
        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
        ]

        btn_frame = tk.Frame(main_frame, bg="#f0f4ff")
        btn_frame.pack(fill="both", expand=True)

        for r, row in enumerate(buttons):
            btn_frame.grid_rowconfigure(r, weight=1)
            for c, label in enumerate(row):
                btn_frame.grid_columnconfigure(c, weight=1)
                self.create_bubble_button(btn_frame, label, r, c)

    def get_button_style(self, label):
        # Returns: (normal_bg, hover_bg, text_color, outline_color)
        if label == "=":
            return "#3355ff", "#5577ff", "#ffffff", "#1133cc"
        elif label in ["C", "⌫"]:
            return "#ff4477", "#ff6699", "#ffffff", "#cc1144"
        elif label in ["÷", "×", "−", "+", "%"]:
            return "#4488ee", "#66aaff", "#ffffff", "#2266cc"
        else:
            return "#ffffff", "#e8eeff", "#223399", "#aabbdd"

    def create_bubble_button(self, parent, label, row, col):
        bg, hover_bg, fg, outline = self.get_button_style(label)

        outer = tk.Frame(parent, bg="#f0f4ff", padx=4, pady=4)
        outer.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

        canvas = tk.Canvas(outer, bg="#f0f4ff", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        def draw_button(fill_color=bg):
            canvas.delete("all")
            w = canvas.winfo_width()
            h = canvas.winfo_height()
            if w < 10 or h < 10:
                return

            # Shadow
            canvas.create_oval(6, 6, w-2, h-2, fill="#ccccdd", outline="")

            # Main bubble
            canvas.create_oval(3, 3, w-5, h-5, fill=fill_color, outline=outline, width=2)

            # Shine (stipple for semi-transparent effect)
            shine_x1 = w // 2 - 14
            shine_y1 = 9
            shine_x2 = w // 2 + 2
            shine_y2 = 19
            canvas.create_oval(shine_x1, shine_y1, shine_x2, shine_y2,
                               fill="#ffffff", outline="", stipple="gray25")

            # Label text
            canvas.create_text(
                w // 2, h // 2,
                text=label,
                font=("Courier New", 17, "bold"),
                fill=fg
            )

        def on_hover(e):
            draw_button(hover_bg)

        def on_leave(e):
            draw_button(bg)

        def on_click(e):
            self.button_action(label)
            canvas.delete("all")
            w = canvas.winfo_width()
            h = canvas.winfo_height()
            canvas.create_oval(3, 3, w-5, h-5, fill="#ffffff", outline=outline, width=2)
            canvas.create_text(w // 2, h // 2, text=label,
                               font=("Courier New", 17, "bold"), fill="#223399")
            canvas.after(100, lambda: draw_button(bg))

        canvas.bind("<Configure>", lambda e: draw_button(bg))
        canvas.bind("<Enter>", on_hover)
        canvas.bind("<Leave>", on_leave)
        canvas.bind("<Button-1>", on_click)

        canvas.after(150, lambda: draw_button(bg))

    def button_action(self, label):
        if label == "C":
            self.expression = ""
            self.display_var.set("0")
            self.sub_display_var.set("")

        elif label == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")

        elif label == "=":
            try:
                self.sub_display_var.set(self.expression + " =")
                expr = self.expression.replace("÷", "/").replace("×", "*").replace("−", "-")
                result = eval(expr)
                if result == int(result):
                    result = int(result)
                self.display_var.set(str(result))
                self.expression = str(result)
            except:
                self.display_var.set("Error")
                self.expression = ""

        elif label == "±":
            if self.expression.startswith("-"):
                self.expression = self.expression[1:]
            elif self.expression:
                self.expression = "-" + self.expression
            self.display_var.set(self.expression or "0")

        elif label == "%":
            try:
                result = float(self.expression) / 100
                if result == int(result):
                    result = int(result)
                self.expression = str(result)
                self.display_var.set(self.expression)
            except:
                pass

        else:
            if self.display_var.get() == "Error":
                self.expression = ""
            self.expression += label
            self.display_var.set(self.expression)

    def run(self):
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"+{x}+{y}")
        self.root.mainloop()


if __name__ == "__main__":
    app = BubbleCalculator()
    app.run()