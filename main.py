import qrcode
from tkinter import *
from tkinter import messagebox


def reset():
    webEntry.delete(0, END)
    webEntry.config(bg='white')
    QR.config(image='', text='', width=20, height=20)


def QRCode():
    website = webEntry.get()
    try:
        web = website.split('.')
        if website.startswith('www.') or website.endswith('.com'):
            fileName = web[1] + '.jpg'
        else:
            fileName = web[0] + '.jpg'
    except:
        fileName = website

    # ============Now generate and save qr code================
    if len(website) < 1:
        messagebox.showwarning('Warning!', 'Enter name of your website first.\n\t in entry box')
        webEntry.config(bg='red2')
        QR.config(text='There is an error occured in Generating QR Code', image='',
                  width=40, height=40, fg='red')
    else:
        img = qrcode.make(website)
        img.save(fileName)
        root.photo = PhotoImage(file=fileName)
        QR.config(image=root.photo, text='QR Code Generated Successfully!',
                  fg='green', compound=TOP, width=300, height=300)
        messagebox.showinfo('Saved', 'QR code saved as " ' + fileName + ' " successfully!\n\tin current location')

# ===============  GUI Design ================================
root = Tk()
root.title('GUI App')
root.config(bg='black')
root.geometry('620x550')
root.resizable(0, 0)
try:
    root.wm_iconbitmap('cid.ico')
except:
    pass
appName = Label(root, text='QR CODE GENERATOR', bg='black', fg='dark red',
                font=('forte', 25, 'underline', 'bold', 'italic'))
appName.pack(side=TOP, fill=BOTH)
website = Label(root, text="Enter your Website :-", font=('Arial', 10))
website.place(x=10, y=72)
webEntry = Entry(root, fg='black', bd=3, width=40)
webEntry.place(x=170, y=70)
getQRCode = Button(root, text='Generate QR Code', bg='green', fg='white', activebackground='purple',
                   width=30, activeforeground='yellow', command=QRCode)
getQRCode.place(x=180, y=100)

resetApp = Button(root, text='Reset', bg='black', fg='white',
                  width=15, bd=3, command=reset)
resetApp.place(x=435, y=500)
QR = Label(root, image='', bg='black')
QR.place(x=100, y=170)

copyri8 = Label(root, text='Developed By: Rizwan.AR',
                bg='black', fg='cyan', font=('times new roman', 12, 'bold'))
copyri8.pack(side=BOTTOM)
root.mainloop()