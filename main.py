import pyautogui
import time

while True:
    
   comando = input("Assistente: Ola Igor, o que gostaria de fazer?").lower()
   pyautogui.PAUSE = 0.5

   if comando == "abrir o youtube":
      comando = input("qual video você quer assistir?").lower()
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
      comando = input("qual pesquisa você quer fazer?").lower()
      print("abrindo google...")
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
      musica = input("qual musica você quer ouvir?").lower()
      print("abrindo spotify...")
      pyautogui.PAUSE = 0.5
      pyautogui.press("win")
      pyautogui.write("spotify")
      pyautogui.press('enter')

      time.sleep(10)

      pyautogui.hotkey("ctrl","l")

      time.sleep(1)
      pyautogui.write(musica)

      time.sleep(3)

      pyautogui.press('enter')
      time.sleep(2)

      # Dá um Tab para entrar na lista de resultados
      pyautogui.press('tab')
      time.sleep(0.5)
        
      # Desce para o primeiro resultado e dá Enter para tocar
      pyautogui.press('down')
      time.sleep(0.5)
      pyautogui.press('enter')
        
      print("Música iniciada com sucesso!")

   else:
      print("Comando não reconhecido. Por favor, tente novamente.")   