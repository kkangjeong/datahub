from MCP3008 import MCP3008         # MCP3008 디지털-아날로그 변환기를 사용하기 위함입니다.(# 뒤에 있는 문장들은 주석이라고 해요. 코드를 돌려도 이 부분은 수행하지 않아서 설명하는 데 주로 쓰여요.)
import paho.mqtt.client as mqtt     # 사운드 센서 값들을 웹으로 보내기 위한 모듈입니다.(이건 스킵해도 돼요)
import time

# 7번째 줄에서 24번째 줄까지는 사운드 센서 값들을 웹으로 보내는 코드에요. 스킵하고 28번째 줄로 갈까요?!
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

broker_address = "52.79.220.60"          # 바꾸기!

client.connect(broker_address)
 


while True:                                 # 코드를 돌려서 학생들의 사운드 값들을 알아볼까요?!

    adc = MCP3008()
    sound = adc.read( channel = 0 )         # 핀 번호(= 채널 번호)를 의미합니다.(라즈베리파이에서 핀을 바꾼다면 0이라는 숫자도 바꿔야겠죠? )
    print("sound: %d" %(sound))             # 사운드 값들을 출력하는 코드랍니다.
    client.publish("/home/jeongin/kkk/sound", sound)            # 바꾸기!   # 나만의 사운드 값들을 웹으로 보내는 코드에요

    time.sleep(1)

client.disconnect()
