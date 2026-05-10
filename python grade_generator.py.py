import tkinter as tk
from tkinter import messagebox, ttk

class GradeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("AcaGrade: Automated GPA Generator")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f2f5")

        # Data Storage
        self.subjects = []

        # UI Styling
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10, "bold"))
        
        # Header
        tk.Label(root, text="AcaGrade Generator", font=("Arial", 20, "bold"), bg="#f0f2f5", fg="#1a73e8").pack(pady=20)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f2f5")
        input_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(input_frame, text="Subject Name:", bg="#f0f2f5").grid(row=0, column=0, sticky="w")
        self.sub_entry = tk.Entry(input_frame)
        self.sub_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(input_frame, text="Credit Hours:", bg="#f0f2f5").grid(row=1, column=0, sticky="w")
        self.credit_entry = tk.Entry(input_frame)
        self.credit_entry.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(input_frame, text="Grade (0.0 - 4.0):", bg="#f0f2f5").grid(row=2, column=0, sticky="w")
        self.grade_entry = tk.Entry(input_frame)
        self.grade_entry.grid(row=2, column=1, pady=5, padx=5)

        # Buttons
        btn_frame = tk.Frame(root, bg="#f0f2f5")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add Subject", command=self.add_subject, bg="#34a853", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Calculate GPA", command=self.calculate_gpa, bg="#1a73e8", fg="white", width=15).grid(row=0, column=1, padx=5)

        # Listbox to show added items
        self.listbox = tk.Listbox(root, height=10, width=50)
        self.listbox.pack(pady=10, padx=20)

        # Result Label
        self.result_label = tk.Label(root, text="Final GPA: 0.00", font=("Arial", 14, "bold"), bg="#f0f2f5", fg="#d93025")
        self.result_label.pack(pady=20)

    def add_subject(self):
        name = self.sub_entry.get()
        try:
            credits = float(self.credit_entry.get())
            grade = float(self.grade_entry.get())
            if not (0 <= grade <= 4.0): raise ValueError
            
            self.subjects.append({'credits': credits, 'grade': grade})
            self.listbox.insert(tk.END, f"{name} | Credits: {credits} | Grade: {grade}")
            
            # Clear entries
            self.sub_entry.delete(0, tk.END)
            self.credit_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers (Grade: 0-4).")

    def calculate_gpa(self):
        if not self.subjects:
            messagebox.showwarning("No Data", "Please add subjects first.")
            return

        total_points = sum(s['grade'] * s['credits'] for s in self.subjects)
        total_credits = sum(s['credits'] for s in self.subjects)
        gpa = total_points / total_credits
        self.result_label.config(text=f"Final GPA: {gpa:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeGenerator(root)
    root.mainloop()