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
    img = qrcode.make(user_link)  # สร้าง QR code จากลิ้งค์ที่ใส่
    img.save("some_file.png")  # บันทึกเป็นไฟล์ PNG
    
    # โหลดภาพและแสดงบน Label
    img_open = Image.open("some_file.png")
    img_tk = ImageTk.PhotoImage(img_open)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

link = StringVar()
Entry(root, textvariable=link).pack()

savebtn = Button(root, text="Generate", fg="white", bg="green", command=gennerate)
savebtn.pack()

# สร้าง Label สำหรับแสดง QR code
qr_label = Label(root)
qr_label.pack()

root.mainloop()

