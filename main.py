import tkinter

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Km to Miles Converter")
window.minsize(width=100, height=50)
miles_label = tkinter.Label(text="Miles")
km_label = tkinter.Label(text="Km")
result = tkinter.Label(text="0")
inp_space = tkinter.Entry(width=10)

def convert():
    num = inp_space.get()
    try:
        num = int(num)
        miles = round((num * 1.609), 2)
        result.config(text=f"{miles}")
    except:
        pass

button_convert = tkinter.Button(text='Convert', command=convert)

miles_label.grid(row=0, column=0)
km_label.grid(row=1, column=0)
inp_space.grid(row=0, column=1)
result.grid(row=1, column=1)
button_convert.grid(row=2, column=1)

window.mainloop()