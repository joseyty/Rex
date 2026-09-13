import pyautogui
import timeabrir youtube

with open("style.css", "r") as f:
   css = f.read()
   markdown(f"<style>{css}</style>",unsafe.allow_html = True)



comando = input("Assistente: Ola Igor, o que gostaria de fazer?").lower()

print("Você digitou:", comando)

if comando == "abrir o youtube":
    print("Comando do YouTube reconhecido!")

elif comando == "abrir google":
    print("Comando do Google reconhecido!")