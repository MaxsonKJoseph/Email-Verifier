from tkinter import *
from PIL import ImageTk, Image
import math
import random
import smtplib

root = Tk()
root.title("Email verifier")
root.geometry("960x540+30+30")

# Background image defining
bg = ImageTk.PhotoImage(file="Wolf Silhouette Hills Mountains Loneliness [1920x1080].png")
Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text="WELCOME TO EMAIL VERIFIER!", font=("Arabic Transparent", 20, "bold"), fg="#FC46AA", padx=10,
      pady=10).place(x=270, y=110)

# input area
email_label = Label(root, text="Enter your Email ID: ", font=("Arabic Transparent", 9, "bold"))
email_label.place(x=270, y=240)
email = Entry(root, width=50, borderwidth=7)
email.place(x=390, y=235)

OTP = 0


# verify the otp
def verify(a):
    otp_in.delete(0, END)
    if a == OTP:
        global bg3, ver_lab, btn2
        rt2 = Toplevel()
        rt2.title("OTP Verifier")
        rt2.geometry("1400x540+30+30")
        bg3 = ImageTk.PhotoImage(file="CORRECT OTP!.jpg")
        Label(rt2, image=bg3).place(x=0, y=0, relwidth=1, relheight=1)
        btn2 = Button(rt2, text="EXIT",font=("Arabic Transparent", 20, "bold"), command=rt2.destroy)
        btn2.place(x=590, y=390)
        rt2.mainloop()
    else:
        global bg4, nv_lab, btn3
        rt3 = Toplevel()
        rt3.title("OTP Verifier")
        rt3.geometry("1200x540+30+30")
        bg4 = ImageTk.PhotoImage(file="WRONG OTP!.jpg")
        Label(rt3, image=bg4).place(x=0, y=0, relwidth=1, relheight=1)
        btn3 = Button(rt3, text="TRY AGAIN",font=("Arabic Transparent", 20, "bold"), command=rt3.destroy)
        btn3.place(x=480, y=390)
        rt3.mainloop()


# code for generating otp
def gen_otp(rec_email):
    try:
        email.delete(0, END)
        global otp_label, otp_in, bg2

        # Generate otp
        global OTP
        digits = "0123456789"
        OTP = ""
        for i in range(6):
            OTP += digits[math.floor(random.random() * 10)]
        otp = OTP + " is your OTP"
        msg = otp

        # send OTP to email using SMTP
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("1hk20is044@hkbk.edu.in", "trmqqrujeyfledmf")
        s.sendmail('1hk20is044@hkbk.edu.in', rec_email, msg)

        # verification page
        rt1 = Toplevel()
        rt1.title("OTP Verifier")
        rt1.geometry("960x540+30+30")
        bg2 = ImageTk.PhotoImage(file="Wolf Silhouette Hills Mountains Loneliness [1920x1080].png")
        Label(rt1, image=bg2).place(x=0, y=0, relwidth=1, relheight=1)

        # verifying otp
        otp_label = Label(rt1, text="Enter the OTP!: ", font=("Arabic Transparent", 9, "bold"))
        otp_label.place(x=270, y=240)
        otp_in = Entry(rt1, width=50, borderwidth=7)
        otp_in.place(x=390, y=235)
        verify_btn = Button(rt1, text="VERIFY OTP!", font=("Arabic Transparent", 20, "bold"), fg="#FC46AA", borderwidth=6, command=lambda: verify(otp_in.get()))
        verify_btn.place(x=390, y=320)
        rt1.mainloop()

    except:
        email.delete(0, END)
        global bg5
        rt4 = Toplevel()
        rt4.title("OTP Verifier")
        rt4.geometry("1320x900+30+30")
        bg5 = ImageTk.PhotoImage(file="eroor has occured.jpg")
        Label(rt4, image=bg5).place(x=0, y=0, relwidth=1, relheight=1)
        rt4.mainloop()


# button to generate OTP
gen = Button(root, text="Generate OTP!", font=("Arabic Transparent", 20, "bold"), fg="#FC46AA", borderwidth=6,
             command=lambda: gen_otp(email.get()))
gen.place(x=390, y=320)

root.mainloop()
