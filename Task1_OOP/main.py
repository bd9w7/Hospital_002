# GUI Main Program Entry - tkinter Framework | Hospital Calling System Task1
import tkinter as tk
from tkinter import ttk, messagebox
from appointment_system import AppointmentSystem

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Intelligent Appointment and Calling System - 2026 Spring Pre-Submission")
        self.root.geometry("800x600")
        # Initialize core appointment system object
        self.system = AppointmentSystem()
        # Build interface widgets (initial framework)
        self._create_widgets()

    def _create_widgets(self):
        # Title bar
        title_label = ttk.Label(self.root, text="Hospital Intelligent Appointment and Calling System", font=("SimHei", 20, "bold"))
        title_label.pack(pady=20)

        # Patient registration frame
        register_frame = ttk.LabelFrame(self.root, text="Patient Registration", padding=10)
        register_frame.pack(pady=10, fill=tk.X, padx=20)

        # Registration form - Name/Age/Department
        ttk.Label(register_frame, text="Name：").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(register_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(register_frame, text="Age：").grid(row=0, column=2, padx=5, pady=5)
        self.age_entry = ttk.Entry(register_frame)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(register_frame, text="Department：").grid(row=0, column=4, padx=5, pady=5)
        self.dept_entry = ttk.Entry(register_frame)
        self.dept_entry.grid(row=0, column=5, padx=5, pady=5)

        # Emergency option
        self.emergency_var = tk.BooleanVar()
        ttk.Checkbutton(register_frame, text="Emergency", variable=self.emergency_var).grid(row=0, column=6, padx=5, pady=5)

        ttk.Label(register_frame, text="Priority (1-5)：").grid(row=0, column=7, padx=5, pady=5)
        self.priority_entry = ttk.Entry(register_frame)
        self.priority_entry.insert(0, "5")
        self.priority_entry.grid(row=0, column=8, padx=5, pady=5)

        # Register button
        ttk.Button(register_frame, text="Register Patient", command=self._register_patient).grid(row=0, column=9, padx=10, pady=5)

        # Function buttons frame
        func_frame = ttk.Frame(self.root, padding=10)
        func_frame.pack(pady=20)

        # Core function buttons
        ttk.Button(func_frame, text="Call Patient", command=self._call_patient, width=15).grid(row=0, column=0, padx=10)
        ttk.Button(func_frame, text="Undo Operation", command=self._undo_operation, width=15).grid(row=0, column=1, padx=10)
        ttk.Button(func_frame, text="Search Patient", command=self._open_search_window, width=15).grid(row=0, column=2, padx=10)
        ttk.Button(func_frame, text="Sort Patients", command=self._open_sort_window, width=15).grid(row=0, column=3, padx=10)

        # Information display text box
        self.info_text = tk.Text(self.root, height=15, width=90)
        self.info_text.pack(pady=10, padx=20)
        self.info_text.insert(tk.END, "System initialized successfully, waiting for operations...\n")

    def _register_patient(self):
        
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        dept = self.dept_entry.get().strip()
        is_emergency = self.emergency_var.get()
        priority = self.priority_entry.get().strip()

        # Simple validation
        if not all([name, age, dept]):
            messagebox.showerror("Error", "Name, age, and department cannot be empty!")
            return
        try:
            age = int(age)
            priority = int(priority)
            if not (1 <= priority <= 5):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Age must be a positive integer, and priority must be an integer between 1 and 5!")
            return

        # Call system registration method
        pid = self.system.register_patient(name, age, dept, is_emergency, priority)
        self.info_text.insert(tk.END, f"【Registration Successful】Patient ID: {pid}, Name: {name}\n")

        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.dept_entry.delete(0, tk.END)
        self.emergency_var.set(False)
        self.priority_entry.delete(0, tk.END)
        self.priority_entry.insert(0, "5")

    def _call_patient(self):
        patient = self.system.call_patient()
        if patient:
            self.info_text.insert(tk.END, f"【Calling Successful】{patient.get_name()} (ID: {patient.get_pid()}) please go to the corresponding department for treatment\n")
        else:
            self.info_text.insert(tk.END, "【Calling Failed】No patients waiting for treatment currently\n")

    def _undo_operation(self):
        res = self.system.undo_operation()
        if res:
            op_type, pid = res
            self.info_text.insert(tk.END, f"【Undo Successful】Operation Type: {op_type}, Patient ID: {pid}\n")
        else:
            self.info_text.insert(tk.END, "【Undo Failed】No operations to undo or patient information does not exist\n")

    def _open_search_window(self):
        search_win = tk.Toplevel(self.root)
        search_win.title("Search Patient")
        search_win.geometry("300x150")
        search_win.resizable(False, False)

        ttk.Label(search_win, text="Patient ID：").pack(pady=10)
        pid_entry = ttk.Entry(search_win)
        pid_entry.pack(pady=5)

        def search():
            pid = pid_entry.get().strip()
            if not pid:
                messagebox.showerror("Error", "Patient ID cannot be empty!")
                return
            try:
                pid = int(pid)
            except ValueError:
                messagebox.showerror("Error", "Patient ID must be a number!")
                return
            self.system.search_patient(pid)

        ttk.Button(search_win, text="Search", command=search).pack(pady=10)

    def _open_sort_window(self):
        sort_win = tk.Toplevel(self.root)
        sort_win.title("Sort Patients")
        sort_win.geometry("300x150")
        sort_win.resizable(False, False)

        ttk.Label(sort_win, text="Select Sort Method：").pack(pady=10)
        sort_var = tk.StringVar(value="age")
        ttk.Radiobutton(sort_win, text="By Age", variable=sort_var, value="age").pack()
        ttk.Radiobutton(sort_win, text="By Patient ID", variable=sort_var, value="pid").pack()
        ttk.Radiobutton(sort_win, text="By Name", variable=sort_var, value="name").pack()

        def sort():
            self.system.sort_patients(sort_var.get())

        ttk.Button(sort_win, text="Sort", command=sort).pack(pady=10)

# Program entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()