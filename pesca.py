import pyautogui
import time
import multiprocessing
import win32api , win32con
from discord_webhook import DiscordWebhook

battle=str(input("posicione seu mouse e digite b para marcar posicao do target: "))
if battle == "b":
    bt=pyautogui.position()

agua=str(input("posicione seu mouse e digite l para marcar posicao na agua: "))
if agua == "l":
    ag  = pyautogui.position() 

loot=str(input("posicione seu mouse e digite u para marcar corpo: "))
if loot == "u":
    lt  = pyautogui.position()

pegar=str(input("posicione seu mouse e digite p para marcar loot: "))
if pegar == "p":
    pb  = pyautogui.position()


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



def pescar():

        barra = pyautogui.locateOnScreen('barra.PNG')
        if barra != None:
                vara = pyautogui.locateOnScreen('vara.PNG', confidence=0.7)
                x_vara, y_vara = pyautogui.center(vara)
                pyautogui.moveTo(x_vara, y_vara)
                click()
                pyautogui.moveTo(ag)
                click()
                time.sleep(1)


def localizarpeixe():
        if pyautogui.locateOnScreen('peixe.png', confidence=0.7):
            peixe = pyautogui.locateOnScreen('peixe.png', confidence=0.7)
            x_peixe, y_peixe = pyautogui.center(peixe)
            pyautogui.moveTo(x_peixe, y_peixe, 0.1)
            click()
            time.sleep(0.1)
            click()
            click()
            
            pyautogui.moveTo(bt)
            click()
            time.sleep(0.8)
            pyautogui.press("f1")
            pyautogui.press("f2")
            pyautogui.press("f3")
            pyautogui.press("f4")
            pyautogui.press("f5")
            pyautogui.press("f6")
            pyautogui.press("f7")
            pyautogui.press("f8")
            pyautogui.press("f9")
            pyautogui.press("f10")
            time.sleep(0.3)
            pyautogui.moveTo(lt)
            pyautogui.rightClick()
            time.sleep(0.3)
            pyautogui.moveTo(pb)
            time.sleep(0.2)
            click()
            click()
            click()
            time.sleep(0.2)
            pyautogui.moveTo(lt)
            pyautogui.press("f12")
            click()


def chat():

     if pyautogui.locateOnScreen('chat.PNG'):

                pyautogui.press("tab")

                chat = pyautogui.screenshot()
                chat.save(r'C:\BOT\print.jpg')

                pyautogui.press("tab")

                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1055968269451935754/cIkPguNXCtzX1r8h5mohAzDOVYYxWHvhx_ZVtCJZzeQttlflvsxBrskm6AtPP-8twdT2', username="undermortis")

                with open(r'C:\BOT\print.jpg', 'rb') as f:
                    webhook.add_file(file=f.read(), filename='print.jpg')

                response = webhook.execute()

                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1055968269451935754/cIkPguNXCtzX1r8h5mohAzDOVYYxWHvhx_ZVtCJZzeQttlflvsxBrskm6AtPP-8twdT2', content='@everyone')
                response = webhook.execute()

            

while True:

    pescar()
    localizarpeixe()
    chat()


