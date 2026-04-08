# Main Program Entry
# Hospital Management System - Full OOP Implementation
# Functions: Menu, Patient, Doctor, Appointment, File Save


import tkinter as tk
from tkinter import ttk, messagebox
from appointment import AppointmentSystem

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Intelligent Appointment and Calling System")
        self.root.geometry("900x650")
        self.system = AppointmentSystem()
        self._create_widgets()

    def _create_widgets(self):
        # Title
        ttk.Label(self.root, text="Hospital Intelligent Appointment and Calling System", font=("SimHei", 20, "bold")).pack(pady=10)

        # Registration area
        reg_frame = ttk.LabelFrame(self.root, text="Patient Registration", padding=10)
        reg_frame.pack(pady=10, fill=tk.X, padx=20)

        ttk.Label(reg_frame, text="Name:").grid(row=0, column=0, padx=5)
        self.name_entry = ttk.Entry(reg_frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        ttk.Label(reg_frame, text="Age:").grid(row=0, column=2, padx=5)
        self.age_entry = ttk.Entry(reg_frame)
        self.age_entry.grid(row=0, column=3, padx=5)

        ttk.Label(reg_frame, text="Department:").grid(row=0, column=4, padx=5)
        self.dept_entry = ttk.Entry(reg_frame)
        self.dept_entry.grid(row=0, column=5, padx=5)

        self.emergency_var = tk.BooleanVar()
        ttk.Checkbutton(reg_frame, text="Emergency", variable=self.emergency_var).grid(row=0, column=6, padx=5)

        ttk.Label(reg_frame, text="Priority (1-5):").grid(row=0, column=7, padx=5)
        self.priority_entry = ttk.Entry(reg_frame, width=5)
        self.priority_entry.insert(0, "5")
        self.priority_entry.grid(row=0, column=8, padx=5)

        ttk.Button(reg_frame, text="Register", command=self._register).grid(row=0, column=9, padx=10)

        # Function buttons
        func_frame = ttk.Frame(self.root)
        func_frame.pack(pady=10)
        ttk.Button(func_frame, text="Call Patient", command=self._call, width=12).grid(row=0, column=0, padx=5)
        ttk.Button(func_frame, text="Undo", command=self._undo, width=12).grid(row=0, column=1, padx=5)
        ttk.Button(func_frame, text="Search Patient", command=self._open_search, width=12).grid(row=0, column=2, padx=5)
        ttk.Button(func_frame, text="Sort", command=self._open_sort, width=12).grid(row=0, column=3, padx=5)
        ttk.Button(func_frame, text="Visit History", command=self._show_history, width=12).grid(row=0, column=4, padx=5)

        # Information display area
        self.info_text = tk.Text(self.root, height=20, width=100, wrap=tk.WORD)
        self.info_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.info_text.insert(tk.END, "System started, waiting for operation...\n")

    def _log(self, msg):
        self.info_text.insert(tk.END, msg + "\n")
        self.info_text.see(tk.END)

    def _register(self):
        name = self.name_entry.get().strip()
        age_str = self.age_entry.get().strip()
        dept = self.dept_entry.get().strip()
        is_emergency = self.emergency_var.get()
        priority_str = self.priority_entry.get().strip()

        if not (name and age_str and dept):
            messagebox.showerror("Error", "Name, age, and department cannot be empty!")
            return
        try:
            age = int(age_str)
            priority = int(priority_str)
            if not (1 <= priority <= 5):
                raise ValueError
        except:
            messagebox.showerror("Error", "Age must be an integer, priority must be between 1 and 5!")
            return

        pid = self.system.register_patient(name, age, dept, is_emergency, priority)
        self._log(f"Registration successful | Patient ID: {pid} | Name: {name}")
        # Clear input fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.dept_entry.delete(0, tk.END)
        self.emergency_var.set(False)
        self.priority_entry.delete(0, tk.END)
        self.priority_entry.insert(0, "5")

    def _call(self):
        patient = self.system.call_patient()
        if patient:
            self._log(f"📢 Calling successful | {patient.get_name()} (ID:{patient.get_pid()}) please go to {patient.get_department()} for treatment")
        else:
            self._log("Calling failed | No patients waiting for treatment currently")

    def _undo(self):
        res = self.system.undo_operation()
        if res:
            op_type, pid = res
            self._log(f" Undo successful | Operation type: {op_type}, Patient ID: {pid}")
        else:
            self._log("Undo failed | No operation to undo or patient does not exist")

    def _open_search(self):
        win = tk.Toplevel(self.root)
        win.title("Search Patient")
        win.geometry("300x150")
        ttk.Label(win, text="Patient ID:").pack(pady=10)
        pid_entry = ttk.Entry(win)
        pid_entry.pack(pady=5)
        def do_search():
            pid_str = pid_entry.get().strip()
            if not pid_str:
                messagebox.showerror("Error", "Patient ID cannot be empty!")
                return
            try:
                pid = int(pid_str)
            except:
                messagebox.showerror("Error", "Patient ID must be a number!")
                return
            patient = self.system.search_patient(pid)
            if patient:
                self._log(f"🔍 Patient found | {patient}")
            else:
                self._log(f"No patient found with ID {pid}")
            win.destroy()
        ttk.Button(win, text="Search", command=do_search).pack(pady=10)

    def _open_sort(self):
        win = tk.Toplevel(self.root)
        win.title("Sort Patients")
        win.geometry("300x200")
        sort_var = tk.StringVar(value="age")
        ttk.Label(win, text="Select sorting method:").pack(pady=10)
        ttk.Radiobutton(win, text="By Age (Bubble Sort)", variable=sort_var, value="age").pack()
        ttk.Radiobutton(win, text="By ID (Selection Sort)", variable=sort_var, value="pid").pack()
        ttk.Radiobutton(win, text="By Name (Merge Sort)", variable=sort_var, value="name").pack()
        ttk.Radiobutton(win, text="By Priority (Cocktail Sort)", variable=sort_var, value="priority_cocktail").pack()
        def do_sort():
            sort_type = sort_var.get()
            sorted_list = self.system.sort_patients(sort_type)
            if sorted_list:
                self._log(f"Sorting completed ({sort_type}):")
                for p in sorted_list:
                    self._log(f"   {p}")
            else:
                self._log("No patient data, cannot sort")
            win.destroy()
        ttk.Button(win, text="Sort", command=do_sort).pack(pady=10)

    def _show_history(self):
        history = self.system.get_visit_history()
        self._log("Patient visit history:")
        if not history:
            self._log("   No records")
        else:
            for record in history:
                self._log(f"   {record}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalGUI(root)
    root.mainloop()