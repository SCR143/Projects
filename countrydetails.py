import requests

API= "https://restcountries.eu/rest/v2/all"
data = requests.get(API).json()
co=1
cou=1
c=input("\nEnter Country Name = ")
d=c.capitalize()
for i in data:
    if d==i['name']:
        print("\nName: ",i['name'])
        print("Capital :",i['capital'])
        print("Population :",i['population'])
        print("Area :",i['area'])
        print("Border :")
        for j in range(len(i.get('borders'))):
            print("   ",co,". ",i['borders'][j])
            co+=1
        print("Languages :")
        for j in range(len(i.get('languages'))):
            n=i['languages'][j]
            m=n['name']
            print("   ",cou,". ",m)
            cou+=1
        break
else:
    print("Sorry, Country not found")