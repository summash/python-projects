import time
timestamp=time.strftime('%H:%M:%S')
timestamp_h=int(time.strftime('%H'))
print(timestamp_h)
if(timestamp_h<12):
    print("good morning sir")
elif(12<timestamp_h<16):
    print("good eveing sir")
elif(16<timestamp_h<24):
    print("good night")