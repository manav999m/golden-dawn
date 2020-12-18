from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("feet to meter")
window.configure(background="red")
window.geometry("320x220")
window.resizable(height=False, width=False)


def convert():
    if mt_entry.get() == "":
        value1 = float(ft_entry.get())
        meter = value1*0.3048
        mt_value.set("%.4f" % meter)
    else :
        #pass
    #if ft_entry == None:
        value2 = float(mt_entry.get())
        feet = value2/0.3048
        ft_value.set("%.4f" % feet)


def clear():
    ft_value.set("")
    mt_value.set("")


ft_lbl = Label(window, text="feet", bg="purple", fg="white", width=14)
ft_lbl.grid(row=0, column=0, padx=30, pady=30)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(row=0, column=1)
ft_entry.delete(0, 'end')

mt_lbl = Label(window, text="meter", bg="green", fg="white", width=14)
mt_lbl.grid(row=1, column=0, pady=30)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(row=1, column=1, pady=0)
mt_entry.delete(0, 'end')

convert_btn = Button(window, text="convert", bg="blue", fg="black", width=14, command=convert)
convert_btn.grid(row=3, column=0, padx=30)

clear_btn = Button(window, text="clear", bg="blue", fg="black", width=14, command=clear)
clear_btn.grid(row=3, column=1, padx=30)


window.mainloop()
