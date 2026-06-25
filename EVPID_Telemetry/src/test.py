import serial

data = serial.Serial("COM5", 9600)

while True:
    values = data.readline().decode("UTF-8").strip()
    print(values)