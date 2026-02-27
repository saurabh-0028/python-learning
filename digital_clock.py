import tkinter as tk
import time
import math
import random

# ── Palette ──────────────────────────────────────────────────────────────────
BG       = "#0a0a0f"
PANEL    = "#0f0f1a"
ACCENT   = "#00ffe5"
ACCENT2  = "#ff2d78"
DIM      = "#1a2a2a"
GLOW     = "#00ffe588"
TEXT_DIM = "#2a5a55"
WHITE    = "#e8fff8"

# ── Glitch characters pool ────────────────────────────────────────────────────
GLITCH_CHARS = "▓░▒█▄▀■□◆◇●○▪▫"

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CHRONO-X")
        self.resizable(False, False)
        self.configure(bg=BG)
        self.overrideredirect(False)

        # State
        self._drag_start = None
        self._glitch_active = False
        self._tick_count = 0
        self._particles = []
        self._scanline_offset = 0

        self._build_ui()
        self._bind_drag()
        self._tick()

    # ── UI Construction ───────────────────────────────────────────────────────
    def _build_ui(self):
        W, H = 620, 320

        # Outer glow border frame
        outer = tk.Frame(self, bg=ACCENT, padx=2, pady=2)
        outer.pack(padx=18, pady=18)

        inner = tk.Frame(outer, bg=BG, padx=0, pady=0)
        inner.pack()

        # Main canvas
        self.canvas = tk.Canvas(inner, width=W, height=H,
                                bg=BG, highlightthickness=0)
        self.canvas.pack()

        self._W, self._H = W, H
        c = self.canvas

        # Background grid lines
        for x in range(0, W, 30):
            c.create_line(x, 0, x, H, fill=DIM, width=1, tags="grid")
        for y in range(0, H, 30):
            c.create_line(0, y, W, y, fill=DIM, width=1, tags="grid")

        # Corner brackets
        bkt = 28
        t = 2
        for (x1,y1,x2,y2) in [(8,8,8+bkt,8),(8,8,8,8+bkt),
                                (W-8-bkt,8,W-8,8),(W-8,8,W-8,8+bkt),
                                (8,H-8-bkt,8,H-8),(8,H-8,8+bkt,H-8),
                                (W-8-bkt,H-8,W-8,H-8),(W-8,H-8-bkt,W-8,H-8)]:
            c.create_line(x1,y1,x2,y2, fill=ACCENT, width=t, tags="corners")

        # Header label
        c.create_text(W//2, 22, text="◈  C H R O N O - X  ◈",
                      font=("Courier", 11, "bold"), fill=ACCENT, tags="header")

        # Sub-label left
        c.create_text(20, 22, text="SYS:ACTIVE", anchor="w",
                      font=("Courier", 8), fill=TEXT_DIM, tags="sys_label")

        # Sub-label right
        self._version_id = c.create_text(W-20, 22, text="v3.14.00",
                                          anchor="e", font=("Courier", 8),
                                          fill=TEXT_DIM)

        # Separator line
        c.create_line(40, 38, W-40, 38, fill=ACCENT, width=1, dash=(6,4))

        # ── Big time display ──────────────────────────────────────────────
        # Shadow / glow layer
        self._time_shadow = c.create_text(W//2+3, 135+3, text="00:00:00",
                                           font=("Courier", 72, "bold"),
                                           fill="#002222", anchor="center")
        self._time_text = c.create_text(W//2, 135, text="00:00:00",
                                         font=("Courier", 72, "bold"),
                                         fill=ACCENT, anchor="center")
        # Glitch overlay (hidden by default)
        self._glitch_text = c.create_text(W//2, 135, text="",
                                           font=("Courier", 72, "bold"),
                                           fill=ACCENT2, anchor="center")

        # ── Date display ──────────────────────────────────────────────────
        self._date_text = c.create_text(W//2, 192, text="",
                                         font=("Courier", 14),
                                         fill=WHITE, anchor="center")

        # ── Bottom separator ──────────────────────────────────────────────
        c.create_line(40, 215, W-40, 215, fill=DIM, width=1, dash=(3,6))

        # ── Status bar ────────────────────────────────────────────────────
        self._status_bar = c.create_text(20, 230, text="",
                                          anchor="w", font=("Courier", 8),
                                          fill=TEXT_DIM)

        # ── Millisecond bar ───────────────────────────────────────────────
        c.create_rectangle(40, 250, W-40, 262, outline=DIM, fill="", width=1)
        self._ms_bar = c.create_rectangle(40, 250, 40, 262,
                                           fill=ACCENT2, outline="")
        self._ms_label = c.create_text(W//2, 256, text="",
                                        font=("Courier", 7), fill=BG)

        # ── Timezone / UTC offset ──────────────────────────────────────────
        self._tz_text = c.create_text(W-20, 275, text="",
                                       anchor="e", font=("Courier", 9),
                                       fill=TEXT_DIM)

        # ── Design By credit ───────────────────────────────────────────────
        c.create_text(W-20, 300, text="⟡ Design By mr selfish",
                      anchor="e", font=("Courier", 9, "italic"),
                      fill=ACCENT2)

        # ── Scanline overlay (drawn on top) ────────────────────────────────
        self._scanlines = []
        for y in range(0, H, 4):
            ln = c.create_line(0, y, W, y, fill="#000000", width=1,
                               stipple="gray25", tags="scanlines")
            self._scanlines.append(ln)

        # ── Particle dots ─────────────────────────────────────────────────
        self._init_particles()

        # Close button
        close_btn = tk.Label(self, text="  ×  ", bg=BG, fg=ACCENT2,
                             font=("Courier", 12, "bold"), cursor="hand2")
        close_btn.place(x=W+22, y=14)
        close_btn.bind("<Button-1>", lambda e: self.destroy())

    def _init_particles(self):
        c = self.canvas
        W, H = self._W, self._H
        for _ in range(18):
            x = random.randint(0, W)
            y = random.randint(0, H)
            r = random.uniform(1, 3)
            speed = random.uniform(0.3, 1.2)
            alpha_color = random.choice([ACCENT, ACCENT2, TEXT_DIM])
            dot = c.create_oval(x-r, y-r, x+r, y+r, fill=alpha_color,
                                outline="", tags="particle")
            self._particles.append({"id": dot, "x": x, "y": y,
                                     "r": r, "speed": speed, "dy": speed})

    # ── Drag to move ──────────────────────────────────────────────────────────
    def _bind_drag(self):
        self.canvas.bind("<ButtonPress-1>", self._on_drag_start)
        self.canvas.bind("<B1-Motion>", self._on_drag_move)

    def _on_drag_start(self, e):
        self._drag_start = (e.x_root - self.winfo_x(),
                            e.y_root - self.winfo_y())

    def _on_drag_move(self, e):
        if self._drag_start:
            x = e.x_root - self._drag_start[0]
            y = e.y_root - self._drag_start[1]
            self.geometry(f"+{x}+{y}")

    # ── Tick (update every ~50ms) ─────────────────────────────────────────────
    def _tick(self):
        now = time.localtime()
        ms  = int((time.time() % 1) * 1000)

        time_str = time.strftime("%H:%M:%S", now)
        date_str = time.strftime("%A  •  %d %B %Y", now)

        # Update main clock
        self.canvas.itemconfig(self._time_text,  text=time_str)
        self.canvas.itemconfig(self._time_shadow, text=time_str)
        self.canvas.itemconfig(self._date_text,  text=date_str)

        # Millisecond progress bar
        W = self._W
        bar_x = 40 + int((ms / 1000) * (W - 80))
        self.canvas.coords(self._ms_bar, 40, 250, bar_x, 262)
        self.canvas.itemconfig(self._ms_label, text=f"{ms:03d} ms")

        # Status bar cycling messages
        msgs = [
            f"UPTIME: {self._tick_count // 20:05d}s  |  CPU: {random.randint(1,8)}%  |  MEM: {random.randint(40,60)}%",
            f"SIGNAL: {'▌'*(random.randint(3,8))}  LOCK: {'OK' if random.random()>.1 else 'ERR'}",
            f"EPOCH: {int(time.time())}  |  LAT: 52.3°N  LON: 4.8°E",
        ]
        self.canvas.itemconfig(self._status_bar,
                               text=msgs[self._tick_count % (20*3) // 20])

        # UTC offset
        utc_off = -time.timezone // 3600
        sign = "+" if utc_off >= 0 else ""
        self.canvas.itemconfig(self._tz_text,
                               text=f"UTC{sign}{utc_off}  |  TZ:{time.tzname[0]}")

        # Glitch effect every ~8 seconds for half a second
        if self._tick_count % 160 == 0:
            self._trigger_glitch(time_str)

        # Animate particles
        self._animate_particles()

        # Color pulse on the second boundary
        if ms < 60:
            self.canvas.itemconfig(self._time_text, fill=WHITE)
        else:
            self.canvas.itemconfig(self._time_text, fill=ACCENT)

        self._tick_count += 1
        self.after(50, self._tick)

    def _trigger_glitch(self, original):
        """Briefly show scrambled text."""
        def scramble():
            glitch = "".join(
                random.choice(GLITCH_CHARS) if random.random() < 0.4 else c
                for c in original
            )
            self.canvas.itemconfig(self._glitch_text, text=glitch)
            self.canvas.itemconfig(self._time_text, fill=ACCENT2)

        def restore():
            self.canvas.itemconfig(self._glitch_text, text="")
            self.canvas.itemconfig(self._time_text, fill=ACCENT)

        self.after(0,   scramble)
        self.after(80,  restore)
        self.after(140, scramble)
        self.after(200, restore)

    def _animate_particles(self):
        c = self.canvas
        W, H = self._W, self._H
        for p in self._particles:
            p["y"] -= p["speed"]
            if p["y"] < -5:
                p["y"] = H + 5
                p["x"] = random.randint(0, W)
            r = p["r"]
            c.coords(p["id"],
                     p["x"]-r, p["y"]-r,
                     p["x"]+r, p["y"]+r)


if __name__ == "__main__":
    app = DigitalClock()
    # Center on screen
    app.update_idletasks()
    sw = app.winfo_screenwidth()
    sh = app.winfo_screenheight()
    w  = app.winfo_width()
    h  = app.winfo_height()
    app.geometry(f"+{(sw-w)//2}+{(sh-h)//2}")
    app.mainloop()