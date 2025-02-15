from tkinter import *
window = Tk()
window.title("Distance Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)
entry = Entry(width=10)
entry.grid(column=1, row=0)
label1 = Label(text="Miles")
label1.grid(column=2, row=0)
label2 = Label(text="Km")
label2.grid(column=2, row=1)
label3 = Label(text="is equal to")
label3.grid(column=0, row=1)
output_label = Label(text=0)
output_label.grid(column=1, row=1)
def calculate():
    miles = float(entry.get())  # Get miles from entry
    kilometers = miles * 1.60934  # Convert to kilometers
    output_label.config(text=f"{kilometers:.2f}")
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)
window.mainloop()


