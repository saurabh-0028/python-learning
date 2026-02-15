import tkinter as tk
from tkinter import messagebox, ttk


class AttendanceSystemGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Attendance System")
        self.root.geometry("520x420")
        self.root.resizable(False, False)

        self.attendance: dict[str, str] = {}

        self._build_header()
        self._build_form()
        self._build_actions()
        self._build_table()

    def _build_header(self) -> None:
        title = tk.Label(
            self.root,
            text="Attendance System",
            font=("Arial", 18, "bold"),
            pady=10,
        )
        title.pack()

    def _build_form(self) -> None:
        form_frame = tk.Frame(self.root, padx=12, pady=8)
        form_frame.pack(fill="x")

        tk.Label(form_frame, text="Employee ID:", font=("Arial", 11)).grid(
            row=0, column=0, sticky="w", pady=6
        )
        self.employee_entry = tk.Entry(form_frame, width=30, font=("Arial", 11))
        self.employee_entry.grid(row=0, column=1, padx=8, pady=6)

        tk.Label(form_frame, text="Status:", font=("Arial", 11)).grid(
            row=1, column=0, sticky="w", pady=6
        )
        self.status_var = tk.StringVar(value="Present")
        self.status_combo = ttk.Combobox(
            form_frame,
            textvariable=self.status_var,
            values=["Present", "Absent"],
            width=27,
            state="readonly",
            font=("Arial", 11),
        )
        self.status_combo.grid(row=1, column=1, padx=8, pady=6)

    def _build_actions(self) -> None:
        action_frame = tk.Frame(self.root, padx=12, pady=8)
        action_frame.pack(fill="x")

        mark_btn = tk.Button(
            action_frame,
            text="Mark Attendance",
            command=self.mark_attendance,
            bg="#1f6aa5",
            fg="white",
            width=18,
            font=("Arial", 10, "bold"),
        )
        mark_btn.grid(row=0, column=0, padx=6)

        clear_btn = tk.Button(
            action_frame,
            text="Clear Fields",
            command=self.clear_fields,
            width=14,
            font=("Arial", 10),
        )
        clear_btn.grid(row=0, column=1, padx=6)

        delete_btn = tk.Button(
            action_frame,
            text="Delete Selected",
            command=self.delete_selected,
            width=14,
            font=("Arial", 10),
        )
        delete_btn.grid(row=0, column=2, padx=6)

    def _build_table(self) -> None:
        table_frame = tk.Frame(self.root, padx=12, pady=10)
        table_frame.pack(fill="both", expand=True)

        columns = ("employee_id", "status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        self.tree.heading("employee_id", text="Employee ID")
        self.tree.heading("status", text="Status")
        self.tree.column("employee_id", width=220, anchor="center")
        self.tree.column("status", width=220, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def mark_attendance(self) -> None:
        employee_id = self.employee_entry.get().strip()
        status = self.status_var.get().strip()

        if not employee_id:
            messagebox.showwarning("Missing Employee ID", "Please enter an Employee ID.")
            return

        self.attendance[employee_id] = status
        self.refresh_table()
        self.clear_fields(set_focus=True)
        messagebox.showinfo("Success", f"Attendance marked for {employee_id}: {status}")

    def clear_fields(self, set_focus: bool = False) -> None:
        self.employee_entry.delete(0, tk.END)
        self.status_var.set("Present")
        if set_focus:
            self.employee_entry.focus_set()

    def delete_selected(self) -> None:
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a record to delete.")
            return

        employee_id = self.tree.item(selected_item[0], "values")[0]
        if employee_id in self.attendance:
            del self.attendance[employee_id]
        self.refresh_table()
        messagebox.showinfo("Deleted", f"Attendance record removed for {employee_id}.")

    def refresh_table(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)

        for employee_id, status in sorted(self.attendance.items()):
            self.tree.insert("", tk.END, values=(employee_id, status))


if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceSystemGUI(root)
    root.mainloop()