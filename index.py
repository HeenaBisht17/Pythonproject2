import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    """
    Calculate the BMI based on user inputs and display the result and category.
    """
    try:
        # Get input values
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display results
        result_label.config(
            text=f"Your BMI: {bmi:.2f}\nCategory: {category}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers for weight and height.")

def show_guidance():
    """
    Display guidance on BMI and its categories.
    """
    guidance_text = (
        "Body Mass Index (BMI) Categories:\n"
        "  - Underweight: BMI < 18.5\n"
        "  - Normal weight: BMI 18.5 - 24.9\n"
        "  - Overweight: BMI 25 - 29.9\n"
        "  - Obesity: BMI >= 30\n\n"
        "To calculate your BMI:\n"
        "1. Enter your weight in kilograms.\n"
        "2. Enter your height in meters.\n"
        "3. Click 'Calculate BMI' to see your result."
    )
    messagebox.showinfo("BMI Guidance", guidance_text)

# Create main application window
app = tk.Tk()
app.title("BMI Calculator")
app.geometry("400x300")
app.resizable(False, False)

# Heading
heading_label = tk.Label(app, text="BMI Calculator", font=("Helvetica", 16))
heading_label.pack(pady=10)

# Weight input
weight_frame = tk.Frame(app)
weight_frame.pack(pady=5)
weight_label = tk.Label(weight_frame, text="Weight (kg): ", font=("Helvetica", 12))
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame, font=("Helvetica", 12), width=10)
weight_entry.pack(side=tk.LEFT)

# Height input
height_frame = tk.Frame(app)
height_frame.pack(pady=5)
height_label = tk.Label(height_frame, text="Height (m): ", font=("Helvetica", 12))
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame, font=("Helvetica", 12), width=10)
height_entry.pack(side=tk.LEFT)

# Calculate button
calculate_button = tk.Button(app, text="Calculate BMI", font=("Helvetica", 12), command=calculate_bmi)
calculate_button.pack(pady=10)

# Guidance button
guidance_button = tk.Button(app, text="BMI Guidance", font=("Helvetica", 12), command=show_guidance)
guidance_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=("Helvetica", 12), fg="blue")
result_label.pack(pady=10)

# Start the application
app.mainloop()
