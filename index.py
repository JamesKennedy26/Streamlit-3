import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.configure(bg='Black') 
frame = tkinter.Frame(window)
frame = tkinter.Frame(window, bg='Black')
window.title("Hello")
frame.pack()

# Getting User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information", bg='black', fg='white', font=("Helvetica", 18))
user_info_frame.grid(row=0, column=0, padx=20, pady=30)

first_name_label = tkinter.Label(user_info_frame, text="First Name", bg='black', fg='white')
first_name_label.grid(row=0, column=0, padx=15, pady=3)
last_name_label = tkinter.Label(user_info_frame, text="Last Name", bg='black', fg='white')
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title", bg='black', fg='white')
title_combobox = ttk.Combobox(user_info_frame,
                              values=["Mr.", "Mrs.", "Ms.", "Dr."])
title_label.grid(row=0, column=2, padx=15, pady=3)
title_combobox.grid(row=1, column=2, padx=15, pady=3)

age_label = tkinter.Label(user_info_frame, text="Age", bg='black', fg='white')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0, padx=12, pady=3)
age_spinbox.grid(row=3, column=0, padx=12, pady=3)

nationality_label = tkinter.Label(user_info_frame, text="Nationality", bg='black', fg='white')
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=[
                                        "Africa", "Antartica", "Asia",
                                        "Europe", "North America", "Oceania",
                                        "South America"
                                    ])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)
window.mainloop()