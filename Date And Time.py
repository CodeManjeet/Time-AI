import time
timestamp = time.strftime('%H:%M:%S')

print(timestamp)
if '04:59:59' > timestamp <= '05:00:00':
    print("Good Morning Sir, Have Nice Day Gretting From Python AI Which Is Made By Manjeet Singh")

elif '11:59:59' > timestamp <= '12:00:00':
    print("Good Afternoon Sir, Have Nice Day Gretting From Python AI Which Is Made By Manjeet Singh")

elif '17:59:59' > timestamp <= '06:00:00':
    print("Good Evening Sir, Have Nice Day Gretting From Python AI Which Is Made By Manjeet Singh")

elif '21:59:59' > timestamp <= '22:00:00':
    print("Good Night Sir, Have Nice Day Gretting From Python AI Which Is Made By Manjeet Singh")

else:
    print("Kya ??")