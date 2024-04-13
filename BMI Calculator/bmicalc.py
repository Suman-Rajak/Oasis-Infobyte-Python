import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi_label.config(text=f"BMI: {bmi:.2f}")

        if bmi < 18.5:
            category_label.config(text="Category: Underweight")
        elif 18.5 <= bmi < 25:
            category_label.config(text="Category: Normal weight")
        elif 25 <= bmi < 30:
            category_label.config(text="Category: Overweight")
        else:
            category_label.config(text="Category: Obese")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

bmi_label = tk.Label(root, text="")
bmi_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

category_label = tk.Label(root, text="")
category_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
