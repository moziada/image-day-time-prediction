import cv2
import numpy as np
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import filedialog

def HL():
    HighLight = cv2.imread("Morning.png")
    phmean ="%.3f" % np.mean(HighLight)
    phmedian = np.median(HighLight)
    phsd = "%.3f" % np.std(HighLight)
    wind = Tk()
    wind.geometry('300x150+900+600')
    wind.title('HighLight Photo')
    mean = Label(wind, text='photo mean is : '+str(phmean)).grid(row=1, sticky=W)
    median = Label(wind, text='photo median is : ' + str(phmedian)).grid(row=2, sticky=W)
    sd = Label(wind, text='photo standard deviation is : ' + str(phsd)).grid(row=3, sticky=W)
    cv2.imshow("HighLight Example", HighLight)
    plt.hist(HighLight.ravel(), 256, [0, 256])
    plt.show()
    wind.mainloop()

def MT():
    Midtones = cv2.imread("MidLight.png")
    phmean = "%.3f" % np.mean(Midtones)
    phmedian = np.median(Midtones)
    phsd = "%.3f" % np.std(Midtones)
    wind = Tk()
    wind.geometry('300x150+900+600')
    wind.title('Midtones Photo')
    mean = Label(wind, text='photo mean is : ' + str(phmean)).grid(row=1, sticky=W)
    median = Label(wind, text='photo median is : ' + str(phmedian)).grid(row=2, sticky=W)
    sd = Label(wind, text='photo standard deviation is : ' + str(phsd)).grid(row=3, sticky=W)
    cv2.imshow("Midtones Example", Midtones)
    plt.hist(Midtones.ravel(), 256, [0, 256])
    plt.show()

def SH():
    Shadows = cv2.imread("Night.png")
    phmean = "%.3f" % np.mean(Shadows)
    phmedian = np.median(Shadows)
    phsd = "%.3f" % np.std(Shadows)
    wind = Tk()
    wind.geometry('300x150+900+600')
    wind.title('Shadows Photo')
    mean = Label(wind, text='photo mean is : ' + str(phmean)).grid(row=1, sticky=W)
    median = Label(wind, text='photo median is : ' + str(phmedian)).grid(row=2, sticky=W)
    sd = Label(wind, text='photo standard deviation is : ' + str(phsd)).grid(row=3, sticky=W)
    cv2.imshow("Shadows Example", Shadows)
    plt.hist(Shadows.ravel(), 256, [0, 256])
    plt.show()

def open():
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    Origphoto = cv2.imread(root.filename)

    width = 500
    height = int(Origphoto.shape[0] * 500 / Origphoto.shape[1])
    dim = (width, height)
    # resize image
    resized = cv2.resize(Origphoto, dim, interpolation=cv2.INTER_AREA)

    phmean = "%.3f" % np.mean(resized)
    phmedian = np.median(resized)
    phsd = "%.3f" % np.std(resized)
    wind = Tk()
    wind.geometry('300x150+900+600')
    wind.title('Custom Photo')
    mean = Label(wind, text='photo mean is : ' + str(phmean)).grid(row=1, sticky=W)
    median = Label(wind, text='photo median is : ' + str(phmedian)).grid(row=2, sticky=W)
    sd = Label(wind, text='photo standard deviation is : ' + str(phsd)).grid(row=3, sticky=W)

    if phmedian>85:
        morning = Label(wind, text='photo type might be Morning').grid(row=4, sticky=W)
    else:
        night = Label(wind, text='photo type might be Night').grid(row=4, sticky=W)

    cv2.imshow("Custom Photo Example", resized)
    plt.hist(Origphoto.ravel(), 256, [0, 256])
    plt.show()

win = Tk()
win.geometry('300x150+900+400')
win.title('Photo statistics applicarion')
lbl = Label(text='Please choose the kind of the photo', fg='black').pack()
btn1 = Button(text='Morning', command=HL).pack()
btn2 = Button(text='MidLight', command=MT).pack()
btn3 = Button(text='Night', command=SH).pack()
btn4 = Button(text='choose photo', command=open).pack()
win.mainloop()