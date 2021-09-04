import requests

f1="https://api.openweathermap.org/data/2.5/forecast?q="
f2="&appid=18c7f3fb7bb3507ce3fe752b68aa349f"
c=input("\nEnter City Name = ")
d=c.capitalize()
path = "{}.html".format(d)

try:
    API=f1+d+f2
    data = requests.get(API).json()
    e=True
    if data['cod']=="404":
        print("'{}' is not a valid City name".format(d))
        e=False
    if e==True:
        file=open(path, 'x')
        s=""
        a=data.get('city')
        s+="<h1>\t{} ({})<h1>".format(a.get('name'),a.get('country'))
        for i in range(len(data.get('list'))):
            s+="<div style='text-align:center;margin:0 auto;float:left;width:25%;box-shadow:0px 0px 10px black;padding:40px;'>"
            we=data.get('list')
            wea=we[i]
            n=wea['weather'][0]
            p=n['icon']
            q="https://openweathermap.org/img/wn/"
            r="@2x.png"
            ic=q+p+r
            s+="<img src='{}'style='height:125px;width:50%'>".format(ic)
            s+="<h3>\t{}</h3>".format(wea['dt_txt'])
            b=wea.get('main')
            bb=b.get('temp')
            ce=bb-273.15
            s+="\t Temp: {}°C".format(format(ce,".2f"))
            m=n['main']
            o=n['description']
            s+="<p>\t{} ({})</p>".format(m,o)
            s+="</div>"
        file.write(s)
        file.close()
        print("File {} created Successfully".format(d))

except FileExistsError:
    print("File with same name already exists")
