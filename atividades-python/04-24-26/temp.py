import pyautogui
import time

tempincial = 20
tempfinal = 38
tempatual = tempincial

while tempatual<tempfinal:
    print("Temperatura atual: {}°C".format(tempatual))
    time.sleep(0.3)
    tempatual +=1

pyautogui.alert("Temperatura estabilizada a 38 C°")
print("Fim de Operação")

