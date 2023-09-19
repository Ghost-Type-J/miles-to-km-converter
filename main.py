from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)

def miles_to_km():
    kilometres = round(float(miles_input.get()) * 1.609344, 2)
    result_label.config(text=kilometres)


miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)


miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)
# miles_label.config(pady=10)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)
# is_equal_to_label.config(padx=20)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

window.mainloop()
