import pyautogui
import time
with open("style.css", "r") as f:
   css = f.read()
   markdown(f"<style>{css}</style>",unsafe.allow_html = True)

comando = input("Assistente: Ola Igor, o que gostaria de fazer?").lower()
pyautogui.PAUSE = 0.5

if comando == "abrir o youtube":
   print("abrindo youtube...")
   #abrir o navegador
   pyautogui.press('win')
   pyautogui.write("chrome")
   pyautogui.press('enter')

   time.sleep(3)

   pyautogui.hotkey("ctrl","l")
   pyautogui.write("https://www.youtube.com")
   pyautogui.press('enter')


elif comando == "abrir google":
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    pyautogui.write("chrome")
    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.hotkey("ctrl","l")
    pyautogui.write("https://www.google.com")
    pyautogui.press('enter')


elif comando == "abra o vscode":
   pyautogui.PAUSE = 0.5
   pyautogui.press('win')
   pyautogui.write("vscode")
   pyautogui.press('enter')

elif comando == "abra o spotify":
   pyautogui.PAUSE = 0.5
   pyautogui.press("win")
   pyautogui.write("spotify")
   pyautogui.press('enter')   