import matplotlib.pyplot as plt
import speedtest
import time

list_download=[]
list_upload=[]
for i in range(5):
    
    st=speedtest.Speedtest()
    speed_download =  round(st.download()/1000000,2)
    list_download.append(speed_download)
    
    speed_upload =  round(st.upload()/1000000,2)
    list_upload.append(speed_upload)
    
    time.sleep(60)
    print(list_download)
    print(list_upload)  
    
x=[1,2,3,4,5]
plt.plot(x,list_download,label="download speed")
plt.title("speed")

plt.plot(x,list_upload,label="upload speed")
plt.legends()

   
plt.show()