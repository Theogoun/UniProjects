import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
#"https://api.openweathermap.org/data/2.5/weather?q=larissa,gr&appid=e953f11d852d5833e92ea4ccc393a59d"

lat=39.6372
lon=22.4203
city="larissa,gr"
apikey="e953f11d852d5833e92ea4ccc393a59d"
endpoint=f"https://api.openweathermap.org/data/2.5/forecast?q={city},gr&appid={apikey}"

text=requests.get(endpoint).text
response=json.loads(text)

#values
Temp=[]
TempFL=[]
Wind=[]
Hum=[]
time=[]

#filling values
for i in range(40):
    Temp.append(response["list"][i]["main"]["temp"])
    TempFL.append(response["list"][i]["main"]["feels_like"])
    Wind.append(response["list"][i]["wind"]["speed"])
    Hum.append(response["list"][i]["main"]["humidity"])
    time.append(i*3)


#temp
fig,ax=plt.subplots()
ax.plot(time,Temp,"r")
ax.plot(time,TempFL,"g")
ax.set_xlabel("Time (h)")
ax.set_ylabel("Temperature (K)")

#minmax Temp
flag=1
flag1=1
for i in range(len(time)):
    if Temp[i]==max(Temp)  and flag==1:
        ax.annotate('Max Temp:{}'.format(max(Temp)), xy=(time[i], max(Temp)), xytext=(time[i], max(Temp)+.2), arrowprops=dict(arrowstyle="->", color="r"))
        flag=0
    elif Temp[i]==min(Temp) and flag1==1:
        ax.annotate('Min Temp:{}'.format(min(Temp)), xy=(time[i], min(Temp)), xytext=(time[i], min(Temp)+.2), arrowprops=dict(arrowstyle="->", color="r"))
        flag1==1

#minmax TempFL
flag=1
flag1=1
for i in range(len(time)):
    if TempFL[i]==max(TempFL)  and flag==1:
        ax.annotate('Max Temp Feel:{}'.format(max(TempFL)), xy=(time[i], max(TempFL)), xytext=(time[i], max(TempFL)-.3), arrowprops=dict(arrowstyle="->", color="g"))
        flag=0
    elif TempFL[i]==min(TempFL) and flag1==1:
        ax.annotate('Min Temp Feel:{}'.format(min(TempFL)), xy=(time[i], min(TempFL)), xytext=(time[i], min(TempFL)-.3), arrowprops=dict(arrowstyle="->", color="g"))
        flag1==1

plt.show()

#wind
fig1,ax1=plt.subplots()
ax1.plot(time,Wind,"b")
ax1.set_xlabel("Time(h)")
ax1.set_ylabel("Wind Speed (m/s)")

#minmax Wind
flag=1
flag1=1
for i in range(len(time)):
    if Wind[i]==max(Wind)  and flag==1:
        ax1.annotate('Max:{}'.format(max(Wind)), xy=(time[i], max(Wind)), xytext=(time[i], max(Wind)), arrowprops=dict(arrowstyle="->", color="b"))
        flag=0
    elif Wind[i]==min(Wind) and flag1==1:
        ax1.annotate('Min:{}'.format(min(Wind)), xy=(time[i], min(Wind)), xytext=(time[i], min(Wind)), arrowprops=dict(arrowstyle="->", color="b"))
        flag1==1

plt.show()

#humidity
fig2,ax2=plt.subplots()
ax2.plot(time,Hum,"orange")
ax2.set_xlabel("Time(h)")
ax2.set_ylabel("Humidity (%)")

#minmax Humidity
flag=1
flag1=1
for i in range(len(time)):
    if Hum[i]==max(Hum)  and flag==1:
        ax2.annotate('Max:{}'.format(max(Hum)), xy=(time[i], max(Hum)), xytext=(time[i], max(Hum)), arrowprops=dict(arrowstyle="->", color="orange"))
        flag=0
    elif Hum[i]==min(Hum) and flag1==1:
        ax2.annotate('Min:{}'.format(min(Hum)), xy=(time[i], min(Hum)), xytext=(time[i], min(Hum)), arrowprops=dict(arrowstyle="->", color="orange"))
        flag1==1

plt.show()