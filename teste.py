import pyautogui
import time
import os

while True:
    
   comando = input("Assistente: Ola Igor, o que gostaria de fazer?").lower()
   pyautogui.PAUSE = 0.5

   if "youtube" in comando:
      video = input("qual video você quer assistir?").lower()
      print("abrindo youtube...")
      #abrir o navegador
      pyautogui.press('win')
      pyautogui.write("chrome")
      pyautogui.press('enter')

      time.sleep(2)
      pyautogui.hotkey("ctrl","l")
      time.sleep(0.5)
      pyautogui.write("https://www.youtube.com")
      pyautogui.press('enter')

      time.sleep(4)
      
      pyautogui.press('tab')
      time.sleep(1)
      pyautogui.press('tab')
      time.sleep(1)
      pyautogui.press('tab')
      time.sleep(1)
      pyautogui.press('tab')
      time.sleep(1)
      pyautogui.press('tab')
      time.sleep(3)
      
      pyautogui.press("enter")
      time.sleep(1)
     
      pyautogui.write(video)
      time.sleep(1)
      pyautogui.press('enter')

      time.sleep(3)
      pyautogui.press('tab')
      time.sleep(1)
      pyautogui.press('enter')

      print("Video iniciado com sucesso!,bom video!")

      





   elif "google" in comando:
      pesquisa = input("qual pesquisa você quer fazer?").lower()
      print("abrindo google...")
      pyautogui.PAUSE = 0.5
      pyautogui.press('win')
      pyautogui.write("chrome")
      pyautogui.press('enter')

      time.sleep(3)

      pyautogui.hotkey("ctrl","l")
      pyautogui.write("https://www.google.com")
      pyautogui.press('enter')


   elif "vscode" in comando:
      pyautogui.PAUSE = 0.5
      pyautogui.press('win')
      pyautogui.write("vscode")
      pyautogui.press('enter')

   elif "spotify" in comando:
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

   elif "sair" in comando:
      print("Saindo do assistente...")
      break


   elif "fortnite" in comando:
      try:
         pyautogui.PAUSE = 5
         pyautogui.press("win")
         pyautogui.write("epic games")
         time.sleep(2)
         pyautogui.press("enter")
         time.sleep(5)

         # Pressiona Tab 40 vezes com um pequeno intervalo
         for _ in range(40):
             pyautogui.press('tab')
             time.sleep(0.1)

         # Pressiona Enter no final da navegação
         pyautogui.press("enter")
      except Exception as e:
         print("Erro ao abrir a Epic Games:", e)
      else:
         print("ate mais tarde.")

   else:
      print("Comando não reconhecido. Por favor, tente novamente.")