import os
import json
import pyautogui
import time
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer



# =========================
# VOSK
# =========================

modelo = Model(
    r"C:\Users\lmelo\Downloads\vosk-model-small-pt-0.3\vosk-model-small-pt-0.3"
)

fila = queue.Queue()


def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    fila.put(bytes(indata))


reconhecedor = KaldiRecognizer(modelo, 16000)


# =========================
# FUNÇÃO PARA OUVIR RESPOSTAS SECUNDÁRIAS (Criada aqui!)
# =========================
def ouvir_resposta(pergunta_prompt):
    print(f"\n🎤 Assistente: {pergunta_prompt}")
    
    # Esvazia a fila para garantir que não sobrou lixo de áudio antigo
    while not fila.empty():
        fila.get()

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=audio_callback
    ):
        while True:
            dados = fila.get()
            if reconhecedor.AcceptWaveform(dados):
                resultado = json.loads(reconhecedor.Result())
                texto = resultado.get("text", "").strip().lower()
                if texto:
                    print("Você disse:", texto)
                    return texto


# =========================
# ASSISTENTE (LOOP PRINCIPAL)
# =========================

while True:
    comando = ouvir_resposta("Olá Igor, o que gostaria de fazer?")

    pyautogui.PAUSE = 0.5


    # =========================
    # YOUTUBE
    # =========================

    if "youtube" in comando:

        video = ouvir_resposta("Qual vídeo gostaria de assistir?")

        print("abrindo youtube...")

        pyautogui.press('win')
        pyautogui.write("chrome")
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.hotkey("ctrl", "l")

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

        print("Video iniciado com sucesso!, bom video!")


    # =========================
    # GOOGLE
    # =========================

    elif "google" in comando:

        pesquisa = ouvir_resposta("Qual pesquisa você quer fazer?")

        print("abrindo google...")

        pyautogui.PAUSE = 0.5

        pyautogui.press('win')
        pyautogui.write("chrome")
        pyautogui.press('enter')

        time.sleep(3)

        pyautogui.hotkey("ctrl", "l")

        pyautogui.write("https://www.google.com")

        pyautogui.press('enter')


    # =========================
    # VSCODE
    # =========================

    elif "vscode" in comando:

        pyautogui.PAUSE = 0.5

        pyautogui.press('win')
        pyautogui.write("vscode")
        pyautogui.press('enter')


    # =========================
    # SPOTIFY
    # =========================

    elif "spotify" in comando:

        musica = ouvir_resposta("Qual música você quer ouvir?")

        print("abrindo spotify...")

        pyautogui.PAUSE = 0.5

        pyautogui.press("win")
        pyautogui.write("spotify")
        pyautogui.press('enter')

        time.sleep(10)

        pyautogui.hotkey("ctrl", "l")

        time.sleep(1)

        pyautogui.write(musica)

        time.sleep(3)

        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.press('tab')

        time.sleep(0.5)

        pyautogui.press('down')

        time.sleep(0.5)

        pyautogui.press('enter')

        print("Música iniciada com sucesso!")


    # =========================
    # SAIR
    # =========================

    elif "sair" in comando:

        print("Saindo do assistente...")

        break


    # =========================
    # COMANDO NÃO RECONHECIDO
    # =========================

    else:

        print(
            "Comando não reconhecido. "
            "Por favor, tente novamente."
        )