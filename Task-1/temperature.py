import tkinter as tk
from tkinter import ttk
def convert_temperature():
    try:
        temp = float(entry_temp.get())
    except ValueError:
        label_result.config(text="Please enter a valid number", foreground="red")
        return 
    from_unit = combo_from.get()
    to_unit = combo_to.get()  
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            result = (temp * 9/5) + 32
        elif to_unit == "Kelvin":
            result = temp + 273.15
        else:
            result = temp
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            result = (temp - 32) * 5/9
        elif to_unit == "Kelvin":
            result = (temp - 32) * 5/9 + 273.15
        else:
            result = temp
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            result = temp - 273.15
        elif to_unit == "Fahrenheit":
            result = (temp - 273.15) * 9/5 + 32
        else:
            result = temp
    label_result.config(text=f"Result: {result:.2f} {to_unit}", foreground="#333333")
root = tk.Tk()
root.title("Futuristic Temperature Converter")
root.geometry("400x300")
root.configure(bg="#e0f7fa") 
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 12)
font_entry = ("Arial", 12)
font_button = ("Arial", 12, "bold")
style = ttk.Style()
style.theme_use("clam")  
style.configure("TLabel", background="#e0f7fa", foreground="#333333", font=font_label)
style.configure("TButton", background="#4dd0e1", foreground="#ffffff", font=font_button)
style.configure("TCombobox", background="#ffffff", foreground="#333333", fieldbackground="#ffffff", font=font_entry)
label_title = ttk.Label(root, text="Temperature Converter", font=font_title, anchor="center")
label_title.grid(column=0, row=0, columnspan=2, padx=10, pady=15)
label_temp = ttk.Label(root, text="Enter Temperature:")
label_temp.grid(column=0, row=1, padx=10, pady=10, sticky="E")
entry_temp = ttk.Entry(root, font=font_entry)
entry_temp.grid(column=1, row=1, padx=10, pady=10)
label_from = ttk.Label(root, text="From:")
label_from.grid(column=0, row=2, padx=10, pady=10, sticky="E")
combo_from = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=font_entry, state="readonly")
combo_from.grid(column=1, row=2, padx=10, pady=10)
combo_from.current(0)
label_to = ttk.Label(root, text="To:")
label_to.grid(column=0, row=3, padx=10, pady=10, sticky="E")
combo_to = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=font_entry, state="readonly")
combo_to.grid(column=1, row=3, padx=10, pady=10)
combo_to.current(1)
button_convert = ttk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(column=0, row=4, columnspan=2, padx=10, pady=20)
label_result = ttk.Label(root, text="Result:", font=font_label)
label_result.grid(column=0, row=5, columnspan=2, padx=10, pady=10)
root.mainloop()
