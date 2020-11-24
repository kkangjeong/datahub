import Adafruit_DHT                     # 온습도 센서 코드를 돌리기 위한 모듈을 사용하기 위함입니다.(# 뒤에 있는 문장들은 주석이라고 해요. 코드를 돌려도 이 부분은 수행하지 않아서 설명하는 데 주로 쓰여요.)
import paho.mqtt.client as mqtt         # 온습도 센서 값들을 웹으로 보내기 위한 모듈입니다.(이건 스킵해도 돼요)
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 2                             # 핀 번호를 의미합니다.(라즈베리파이에서 핀을 바꾼다면 2라는 숫자도 바꿔야겠죠? )


# 10번째 줄에서 27번째 줄까지는 온습도 센서 값들을 웹으로 보내는 코드에요. 스킵하고 30번째 줄로 갈까요?!
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

client = mqtt.Client("P1")

client.on_connect = on_connect
client.on_disconnect = on_disconnect

broker_address = "52.79.220.60"         # 바꾸기!

client.connect(broker_address)
 

while True:                                                                     # 여기 코드가 가장 중요해요

    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)              # 코드를 돌려서 학생들의 온도, 습도 값들을 알아볼까요?!

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))    # 온도, 습도 값들을 출력하는 코드랍니다.
        client.publish("/home/jeongin/kkk/temperature", temperature)                # 바꾸기!   # 나만의 온도 값들을 웹으로 보내는 코드에요
        client.publish("/home/jeongin/kkk/humidity", humidity)                      # 바꾸기!   # 나만의 습도 값들을 웹으로 보내는 코드에요
    
    else:
        print("아직 센서 값이 안읽히네요. 기다려주세요..")

    time.sleep(3)

client.disconnect()
