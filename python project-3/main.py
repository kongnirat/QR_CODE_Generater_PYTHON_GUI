from tkinter import *
from PIL import Image, ImageTk
import qrcode

root = Tk()
root.title("QR CODE Generator")
root.geometry("700x500")

say = Label(text="Give me your link", fg="blue", font="20").pack()

def gennerate():
    # ดึงค่าจาก Entry มาใช้
    user_link = link.get()
    name_file = name.get()
    img = qrcode.make(user_link)  # สร้าง QR code จากลิ้งค์ที่ใส่
    
    # โหลดภาพและแสดงบน Label
    img_open = Image.open(name_file)
    img_tk = ImageTk.PhotoImage(img_open)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

def save():
    img.save(name_file)  # บันทึกเป็นไฟล์ PNG

link = StringVar()
name = StringVar()
Entry(root, textvariable=link).pack()
Entry(root, textvariable=name).pack()

genneratebtn = Button(root, text="Generate", fg="white", bg="green", command=gennerate)
savebtn = Button(root, text="Save", fg="white", bg="black", command=save)
savebtn.pack()
genneratebtn.pack()

# สร้าง Label สำหรับแสดง QR code
qr_label = Label(root)
qr_label.pack()

root.mainloop()
