import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://greendigital.uth.gr/data/meteo48h.csv.txt")

time=(df['Unix_time']-df.at[0,'Unix_time'])/3600
TO=df['Temp_Out']
THWS=df['THWS_Index']
WS=df['Wind_Speed']
HS=df['Hi_Speed']
OH=df['Out_Hum']
IH=df['In_Hum']

#temp
fig,ax=plt.subplots()
axa=ax.twinx()
ax.plot(time,TO,"r")
axa.plot(time,THWS,"g")
ax.set_xlabel("Time (h)")
ax.set_ylabel("Temperature (C)")
axa.set_ylabel("Temperature with HWS (C)")

#max min TO
flag=1
flag1=1
for i in range(len(time)):
    if TO[i]==max(TO)  and flag==1:
        ax.annotate('Max Temp:{}'.format(max(TO)), xy=(time[i], max(TO)), xytext=(time[i], max(TO)+.2), arrowprops=dict(arrowstyle="->", color="r"))
        flag=0
    elif TO[i]==min(TO) and flag1==1:
        ax.annotate('Min Temp:{}'.format(min(TO)), xy=(time[i], min(TO)), xytext=(time[i], min(TO)-.2), arrowprops=dict(arrowstyle="->", color="r"))
        flag1==1

#max min THWS
flag=1
flag1=1
for i in range(len(time)):
    if THWS[i]==max(THWS) and flag==1:
        axa.annotate('Max THWS:{}'.format(max(THWS)), xy=(time[i], max(THWS)), xytext=(time[i], max(THWS)-1), arrowprops=dict(arrowstyle="->", color="g"))
        flag=0
    elif THWS[i]==min(THWS) and flag1==1:
        axa.annotate('Min THWS:{}'.format(min(THWS)), xy=(time[i], min(THWS)), xytext=(time[i], min(THWS)+1), arrowprops=dict(arrowstyle="->", color="g"))
        flag1==1

plt.show()
fig.savefig("graph1.png")

#wind
fig1,ax1=plt.subplots()
ax1a=ax1.twinx()
ax1.plot(time,WS,"b")
ax1a.plot(time,HS,"y")
ax1.set_xlabel("Time(h)")
ax1.set_ylabel("Wind Speed Avg (m/s)")
ax1a.set_ylabel("Wind Speed Highest (m/s)")

#max min WS
flag=1
flag1=1
for i in range(len(time)):
    if WS[i]==max(WS) and flag==1:
        ax1.annotate('Max WS Avg.:{}'.format(max(WS)), xy=(time[i], max(WS)), xytext=(time[i], max(WS)+.2), arrowprops=dict(arrowstyle="->", color="b"))
        flag=0
    elif WS[i]==min(WS) and flag1==1:
        ax1.annotate('Min WS Avg.:{}'.format(min(WS)), xy=(time[i], min(WS)), xytext=(time[i], min(WS)-.2), arrowprops=dict(arrowstyle="->", color="b"))
        flag1=0

#max min HS
flag=1
flag1=1
for i in range(len(time)):
    if HS[i]==max(HS) and flag==1:
        ax1a.annotate('Max WS High:{}'.format(max(HS)), xy=(time[i], max(HS)), xytext=(time[i], max(HS)-1), arrowprops=dict(arrowstyle="->", color="y"))
        flag=0
    elif HS[i]==min(HS) and flag1==1:
        ax1a.annotate('Min WS High:{}'.format(min(HS)), xy=(time[i], min(HS)), xytext=(time[i], min(HS)+1), arrowprops=dict(arrowstyle="->", color="y"))
        flag1=0


plt.show()
fig1.savefig("graph2.png")

#Humidity
fig2,ax2=plt.subplots()
ax2a=ax2.twinx()
ax2.plot(time,OH,"r")
ax2a.plot(time,IH,"b")
ax2.set_xlabel("Time (h)")
ax2.set_ylabel("Outside Humidity (%)")
ax2a.set_ylabel("Inside Humidity (%)")

#max min OH
flag=1
flag1=1
for i in range(len(time)):
    if OH[i]==max(OH) and flag==1:
        ax2.annotate('Max Humidity Out:{}'.format(max(OH)), xy=(time[i], max(OH)), xytext=(time[i], max(OH)+.2), arrowprops=dict(arrowstyle="->", color="r"))
        flag=0
    elif OH[i]==min(OH) and flag1==1:
        ax2.annotate('Min Humidity Out:{}'.format(min(OH)), xy=(time[i], min(OH)), xytext=(time[i], min(OH)-.2), arrowprops=dict(arrowstyle="->", color="r"))
        flag1=0

#max min IH
flag=1
flag1=1
for i in range(len(time)):
    if IH[i]==max(IH) and flag==1:
        ax2a.annotate('Max Humidity In:{}'.format(max(IH)), xy=(time[i], max(IH)), xytext=(time[i], max(IH)-1), arrowprops=dict(arrowstyle="->", color="b"))
        flag=0
    elif IH[i]==min(IH) and flag1==1:
        ax2a.annotate('Min Humidity In:{}'.format(min(IH)), xy=(time[i], min(IH)), xytext=(time[i], min(IH)+1), arrowprops=dict(arrowstyle="->", color="b"))
        flag1=0

plt.show()
fig2.savefig("graph3.png")