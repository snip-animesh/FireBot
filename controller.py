import main_w_xml as main
# import main
# import dataGenerator
from pyfirmata import Arduino, pyfirmata
import  keyboard
import time
import requests

port = 'COM4'

board = Arduino(port)

servo_pin = 6
board.digital[servo_pin].mode = pyfirmata.SERVO

rgbR = board.get_pin('d:11:o')
rgbG = board.get_pin('d:12:o')
rgbB = board.get_pin('d:13:o')

buzzer = board.get_pin('d:4:o')

def servo(angle):
    board.digital[servo_pin].write(angle)


def rgb(RGB):
    rgbR.write(RGB[0])
    rgbG.write(RGB[1])
    rgbB.write(RGB[2])


def buzzers(val):
    buzzer.write(val)


def telegram():
    TOKEN = "6429131512:AAH71M4_60JeTxmzbyFJwgxU-WTb_pA1c94"
    chat_id = '-4130674737'

    message = "Fire Detected. Take necessary actions."
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    requests.get(url)


def  fire():
    telegram()  # message sent to Telegram
    # time.sleep(1)
    buzzers(1)  # Buzzer on
    rgbR.write(1)  # Red light on
    rgbG.write(0)  # Green light off


def noFire():
    buzzers(0)  # Buzzer off
    rgbR.write(0)  # Red light off
    rgbG.write(1)  # Green light on


servo(0)
time.sleep(1)

ang=0
id=1

while True:
    pred= main.run()
    if pred==1:
        fire()
        time.sleep(2)
    elif pred ==0:
        noFire()
        servo(ang)
        time.sleep(0.5)

        #Change angle
        ang=ang+id
        if ang==90:
            id=-1
        elif ang==0:
            id=1

    print("Iteration Done")

    if keyboard.is_pressed("space"):
        break

servo(0)
rgbR.write(0)
rgbG.write(0)
buzzers(0)




