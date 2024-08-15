import tkinter as tk
from tkinter import messagebox
import requests

def submit():
    project_name = project_name_entry.get()
    dut_name = dut_name_entry.get()
    cycle_name = cycle_name_entry.get()
    speed = speed_entry.get()
    torque = torque_entry.get()
    status = status_entry.get()

    data = {'Project_Name': project_name, 'DUT_Name': dut_name, 'Cycle_Name': cycle_name,'speed': speed, 'torque': torque, 'status': status}
    response = requests.post('http://localhost:4000/set_data', json=data)
    return response.json()

    if project_name and dut_name and cycle_name and speed and torque and status:
        messagebox.showinfo("Success", "Data submitted successfully!\nProject Name: {}\nDUT Name: {}\nCycle Name: {}\nSpeed: {}\nTorque: {}\nStatus: {}".format(project_name, dut_name, cycle_name, speed, torque, status))
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def cancel():
    root.destroy()

root = tk.Tk()
root.title("Data Input Form")

# Styling
root.configure(bg="#f0f0f0")
root.option_add("*Font", "Arial 12")

# Frame
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=10)

# Project Name
tk.Label(frame, text="Project Name:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
project_name_entry = tk.Entry(frame, width=30)
project_name_entry.grid(row=0, column=1, padx=10, pady=5)

# DUT Name
tk.Label(frame, text="DUT Name:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
dut_name_entry = tk.Entry(frame, width=30)
dut_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Cycle Name
tk.Label(frame, text="Cycle Name:", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5)
cycle_name_entry = tk.Entry(frame, width=30)
cycle_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Speed
tk.Label(frame, text="Speed:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5)
speed_entry = tk.Entry(frame, width=30)
speed_entry.grid(row=3, column=1, padx=10, pady=5)

# Torque
tk.Label(frame, text="Torque:", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5)
torque_entry = tk.Entry(frame, width=30)
torque_entry.grid(row=4, column=1, padx=10, pady=5)

# Status
tk.Label(frame, text="Status:", bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=5)
status_entry = tk.Entry(frame, width=30)
status_entry.grid(row=5, column=1, padx=10, pady=5)

# Buttons
submit_button = tk.Button(frame, text="OK", width=10, bg="#4CAF50", fg="white", command=submit)
submit_button.grid(row=6, column=0, padx=10, pady=10)
cancel_button = tk.Button(frame, text="Cancel", width=10, bg="#f44336", fg="white", command=cancel)
cancel_button.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()
