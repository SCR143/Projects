import requests
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import urllib.parse
import io

f1="http://api.openweathermap.org/data/2.5/weather?q="
f2="&appid=18c7f3fb7bb3507ce3fe752b68aa349f"

main=tk.Tk()
main.title("Weather Forecasting")
main.geometry("800x500")
main.resizable(0,0)

l1=tk.Label(main,text="Enter City Name: ",bg="#fca103",)
c=tk.StringVar()
l2=tk.Entry(main,textvariable=c)


def details():
    val = c.get()
    v=val.capitalize()
    API=f1+v+f2
    data = requests.get(API).json()
    rs = ""
    e=True
    if data['cod']=="404":
        messagebox.showerror("City Not Found","City entered by you is not in aur database")
        e=False
    if e==True:
        a=data.get('sys')
        rs+="Name: {}\n".format(data['name'])
        rs+="Country: {}\n".format(a.get('country'))
        b=data.get('main')
        bb=b.get('temp')
        ce=bb-273.15
        rs+="Temprature: {}°C\n".format(format(ce,".2f"))
        n=data['weather'][0]
        m=n['main']
        o=n['description']
        rs+="{} ({})".format(m,o)
        p=n['icon']
        q="https://openweathermap.org/img/wn/"
        r="@2x.png"
        ic=q+p+r
        raw_data = urllib.request.urlopen(ic).read()
        im = Image.open(io.BytesIO(raw_data))
        im = im. resize((100, 100))
        image = ImageTk.PhotoImage(im)
        lbl = tk.Label(main, image=image)
        lbl.image = image
        lbl.place(x=360,y=260)
        result.config(text=rs)
 
l3=tk.Button(main,text="Click",relief="flat",bg="#44c902",width=10,command=details)

l1.place(x=300,y=40)
l2.place(x=400,y=40)
l3.place(x=380,y=70)

main.config(bg="#fca103")

result = tk.Label(main, text="",bg="#fca103",font=("cursive",15))
result.place(x=310,y=150)

main.mainloop()