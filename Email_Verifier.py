from tkinter import *
from PIL import ImageTk, Image
import math
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

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
def verify(a, rec_mail):
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

        # Send the pdf of Python notes
        body = '''Hello,
        This email contain the Application development using Pyhton's  Module 5 notes
        sicerely yours
        Email Verifier
        '''
        # put your email here
        sender = '1hk20is044@hkbk.edu.in'
        password = 'trmqqrujeyfledmf'
        # put the email of the receiver here
        receiver = rec_mail

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'This email has an attacment, a pdf file'

        message.attach(MIMEText(body, 'plain'))

        pdfname = 'PY Mod5@AzDOCUMENTS.in.pdf'

        # open the file in bynary
        binary_pdf = open(pdfname, 'rb')

        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        # payload = MIMEBase('application', 'pdf', Name=pdfname)
        payload.set_payload((binary_pdf).read())

        # enconding the binary into base64
        encoders.encode_base64(payload)

        # add header with pdf name
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)

        #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

        #enable security
        session.starttls()

        #login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()

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
        verify_btn = Button(rt1, text="VERIFY OTP!", font=("Arabic Transparent", 20, "bold"), fg="#FC46AA", borderwidth=6, command=lambda: verify(otp_in.get(), rec_email))
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
