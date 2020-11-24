import RPi.GPIO as GPIO                     # 라즈베리파이의 핀들을 사용하기 위함입니다.(# 뒤에 있는 문장들은 주석이라고 해요. 코드를 돌려도 이 부분은 수행하지 않아서 설명하는 데 주로 쓰여요.)
import paho.mqtt.client as mqtt             # 거리 센서 값들을 웹으로 보내기 위한 모듈입니다.(이건 스킵해도 돼요)
import time

GPIO.setmode(GPIO.BCM)
trig = 13                                   # 핀 번호를 의미합니다.(라즈베리파이에서 핀을 바꾼다면 13이라는 숫자도 바꿔야겠죠? )
echo = 26                                   # 핀 번호를 의미합니다.(라즈베리파이에서 핀을 바꾼다면 26이라는 숫자도 바꿔야겠죠? )

GPIO.setup(trig, GPIO.OUT)                  # trig를 출력모드로 설정합니다.
GPIO.setup(echo, GPIO.IN)                   # echo를 입력모드로 설정합니다.


# 14번째 줄에서 31번째 줄까지는 거리 센서 값들을 웹으로 보내는 코드에요. 스킵하고 34번째 줄로 갈까요?!
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

client = mqtt.Client("P1")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

broker_address = "52.79.220.60"             # 바꾸기!

client.connect(broker_address)

 
while True:                                         # 코드를 돌려서 학생들의 거리 값들을 알아볼까요?!

    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        pass

    fpulseStart = time.time()

    while GPIO.input(echo) == 1:
        pass

    fpulseEnd = time.time()

    fpulseDuration = fpulseEnd - fpulseStart

    fDistance = round((fpulseDuration * 171.50), 2)
    
    print("Distance: ", fDistance, "m")                                 # 거리 값들을 출력하는 코드랍니다.
    client.publish("/home/jeongin/kkk/distance", fDistance)             # 바꾸기!   # 나만의 거리 값들을 웹으로 보내는 코드에요


    time.sleep(3)

client.disconnect()
