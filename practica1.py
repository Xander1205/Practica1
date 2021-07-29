from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Registro")
window.geometry("600x600")

lbl1 = Label(window, text="Nombre")
lbl2 = Label(window, text="Apellido")
lbl3 = Label(window, text="Edad")
lbl4 = Label(window, text="Correo")
lbl5 = Label(window, text="Contraseña")
lbl6 = Label(window, text="Crear Usuario")

texto1 = Entry()
texto2 = Entry()
texto3 = Entry()
texto4 = Entry()
texto5 = Entry()
texto6 = Entry()

def Registrar():
    if texto1.get() and texto2.get() and texto3.get() and texto4.get() and texto5.get() and texto6.get():
        messagebox.showinfo("Nombre de Registro", texto1.get() + " " + texto2.get() + "\n" +  "\n" + texto3.get() +  " " + "años" + "\n" + "\n" +  "Correo:" + " " + texto4.get()+ "\n" + "\n" + "Contraseña:" + " " + texto5.get()+ "\n" + "\n" +  "Usuario:" +  " " + texto6.get() )
    else:
        messagebox.showerror("Error", "Es obligatorio llenar todos los campos")

btn = Button(window, text="Registar", command=Registrar)
lbl1.pack()
texto1.pack()
lbl2.pack()
texto2.pack()
lbl3.pack()
texto3.pack()
lbl4.pack()
texto4.pack()
lbl5.pack()
texto5.pack()
lbl6.pack()
texto6.pack()
btn.pack()

window.mainloop()
