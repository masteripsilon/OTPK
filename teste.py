import pyautogui
import time
from discord_webhook import DiscordWebhook
import win32api , win32con




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

    chat()