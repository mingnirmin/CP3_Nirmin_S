from tkinter import *
import math

def leftClickButton(event):
    labelResult.configure(text=format(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2),'.2f'))
    bmishow = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if float(bmishow) > 30:
        bmiResult.configure(text="อ้วนมาก")
    elif float(bmishow) >= 25:
        bmiResult.configure(text="อ้วน")
    elif int(bmishow) >= 23:
        bmiResult.configure(text="น้ำหนักเกิน")
    elif int(bmishow) >= 18.6:
        bmiResult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        bmiResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)

textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)

labelWeight = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

calculateButton = Button(MainWindow,text = "คำนวณ",bg='cyan')
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)

labelResult = Label(MainWindow,text="ผลลัพธ์", bg='cyan')
labelResult.grid(row=2,column=1)

bmiShow = Label(MainWindow,text = "ระดับ", bg='green')
bmiShow.grid(row=3,column=0)

bmiResult = Label(MainWindow,text="ผลลัพธ์", bg='green')
bmiResult.grid(row=3,column=1)

MainWindow.mainloop()