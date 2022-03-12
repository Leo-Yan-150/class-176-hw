import speedtest
import matplotlib .pyplot as plt
import time

dsl = []
usl = []

for i in range(5):
    st = speedtest.Speedtest()
    ds = round(st.download()/1000000,2)
    dsl.append(ds)
    us = round(st.upload()/1000000,2)
    usl.append(us)
    time.sleep(60)
    print(dsl)
    print(usl)

x = [1,2,3,4,5]
plt.plot(x,dsl,label = "Download Speed")
plt.plot(x,usl,label = "Upload Speed")
plt.title("Speed")
plt.lengend()
plt.show()

#to be honest I have no idea if this works or not, spyder always crashes when I run the program. Yea sorry. -Leo
