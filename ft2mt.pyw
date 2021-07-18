from tkinter import Tk, Button, Label, DoubleVar, Entry

#Main Window
window = Tk()
window.title("Feet To Meter Converter")
window.geometry("320x220")
window.configure(background="light blue")
window.resizable(width=False, height=False)

#Create Functions
def convert():
    value = float(ft_entry.get())
    meter = value * .3048
    mt_value.set("%.4f" % meter)
    

def clear():
    ft_value.set('')
    mt_value.set('')

#Adding Buttons And Labels

lbl = Label(window, text='Feet', bg='green', fg='white', width=14)
lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

lbl2 = Label(window, text='Meter', bg='green', fg='white', width=14)
lbl2.grid(column=0, row=1)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, 'end')

btn1 = Button(window, text='Convert', bg='red', fg='white', width=14, command=convert)
btn1.grid(column=0, row=3, padx=15)

btn2= Button(window, text='Clear', bg='black', fg='white', width=14, command=clear)
btn2.grid(column=1, row=3, padx=15)

window.mainloop()