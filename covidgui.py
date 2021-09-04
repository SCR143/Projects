import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

API= "https://api.covid19india.org/state_district_wise.json"
data = requests.get(API).json()
state= [i for i in data]
state.pop(0)

main=tk.Tk()
main.title("New Toplevel")
main.geometry("600x400")
main.config(bg="#434543")

l1=tk.Label(main,text="State",bg="white",pady=4,padx=11.5)
l2=tk.Label(main,text="District",bg="white",pady=4,padx=6)

def display():
    v1=s1.get()
    r=""
    for i in data:
        if v1==i:
            a=data[i]
            b=a['districtData']
            dist=[j for j in b] 
            l5['values']=dist
            v2=s2.get()
            for j in b:
                if v2==j:
                    c=b[j]
                    r+="Confirmed: {}".format(c['confirmed'])
                    r+="\nRecovered: {}".format(c['recovered'])
                    r+="\nDeaths: {}".format(c['deceased'])
                    r+="\nActive: {}".format(c['active'])
                    r+="\nNotes: {}".format(c['notes'])  
    result.config(text=r)

l3=tk.Button(main,text="Search",bg="white",pady=4,padx=9,relief="flat",command=display)

l1.place(x=80,y=50)
l2.place(x=80,y=85)
l3.place(x=450,y=60)

s1=tk.StringVar()
l4=ttk.Combobox(main, textvariable=s1)
l4.place(x=170,y=53)
l4["values"]=state

s2=tk.StringVar()
l5=ttk.Combobox(main, textvariable=s2)
l5.place(x=170,y=88)

result = tk.Label(main, text="",fg="yellow",bg="grey",font=("cursive",15))
result.place(x=100,y=150)

main.mainloop()