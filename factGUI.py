from tkinter import *

#
#
# This is comment

# Deuxieme commentaire

def calculer():
    text1 = entry1.get()
    if text1.isnumeric():
        fact = factorial(int(text1))
        entry2.insert(END, str(fact))

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def effacer():
    entry1.delete(0, END)
    entry2.delete(0, END)

window = Tk()
window.title("tk")
window.geometry("320x160")
window.minsize(0,0)
canvasImg = Canvas(window, width=120, height=120, bg="ivory")

label1 = Label(window, text="Entrez la valeur de n :")
label2 = Label(window, text="La factorielle de N est :")

entry1 = Entry(window, width=20)
entry2 = Entry(window, width=20)

button1 = Button(window, text="Effacer le contenu", command=effacer)
button2 = Button(window, text="Calculer la factorielle", command=calculer)

label1.grid(row = 0, column = 0, sticky = E, padx = 15, pady = 15)
label2.grid(row = 1, column = 0, sticky = E, padx = 15, pady = 15)
button1.grid(row = 4, column = 0, sticky = E, pady = 15)

entry1.grid(row = 0, column = 1, sticky = E, padx = 15, pady = 15)
entry2.grid(row = 1, column = 1, sticky = E, padx = 15)
button2.grid(row = 4, column = 1, sticky = E, pady = 15)

window.mainloop()