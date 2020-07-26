from tkinter import *
import tkinter.font as font

def button_click(number):
    current = e.get()
    if current == 'Error':
        current = ''
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    current = e.get()
    e.delete(0, END)
    e.insert(0, current[:-1])

def button_equal():
    q = e.get()
    e.delete(0, END)
    try:
        e.insert(0, eval(q))
    except:
        e.insert(0, 'Error')

def buttons(num, i, j, myFont):
    button = Button(root, text=num, width=10, height=4, command=lambda: button_click(num))
    button['font'] = myFont
    button.grid(row=i, column=j)

if __name__ == "__main__":
    root = Tk()
    root.title("Simple Calculator")

    myFont = font.Font(family='Courier', weight='bold')

    nums = [7,8,9,'/',4,5,6,'*',1,2,3,'-']
    x = 0

    e = Entry(root, width=35, borderwidth=5, justify = RIGHT, font = ('Courier', 15, 'bold'))
    e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    for i in range(1,4):
        for j in range(0,4):
            buttons(nums[x], i, j, myFont)
            x+=1

    button_add = Button(root, text="+", width=10, height=4, command=lambda: button_click('+'))
    button_equal = Button(root, text="=", width=10, height=4,  command=button_equal)
    button_clear = Button(root, text="\u232B", width=10, height=4, command=button_clear)
    button_0 = Button(root, text="0", width=10, height=4, command=lambda: button_click(0))

    button_add['font'] = myFont
    button_equal['font'] = myFont
    button_clear['font'] = myFont
    button_0['font'] = myFont

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1)
    button_equal.grid(row=4, column=2)
    button_add.grid(row=4, column=3)

    root.mainloop()