import tkinter

def on_click():
    print("I got clicked")
    km = round((float(mile_input.get()) * 1.60934), 2)
    km_label.config(text=km)

my_screen = tkinter.Tk()
my_screen.title("Mile to KM Converter")
my_screen.config(padx=20, pady=20)

mile_input = tkinter.Entry(width=7, font=("Arial", 10))
mile_input.insert(string="0", index=0)
mile_input.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0,row=1)

km_label = tkinter.Label(text="0")
km_label.grid(column=1,row=1)

kilo_label = tkinter.Label(text="KM")
kilo_label.grid(column=2,row=1)

calculate = tkinter.Button(fg="red", bg="blue", text="calculate", command=on_click)
calculate.grid(column=1, row=2)




my_screen.mainloop()