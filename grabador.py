import subprocess
from datetime import datetime

# URL del stream de radio
url_emision = "https://samuel.i-radio.co:9000/lacheverisima"

def grabar_emision(url, duracion):
    archivo_salida = f"grabacion_{datetime.now().strftime('%Y%m%d_%H%M')}.mp3"

    comando = [
        "ffmpeg",         # Usamos el comando de Linux, no ruta específica
        "-i", url,
        "-t", str(duracion),
        "-c", "copy",
        archivo_salida
    ]

    resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    print("Salida de FFmpeg:")
    print(resultado.stdout)
    print("Errores de FFmpeg:")
    print(resultado.stderr)

if __name__ == "__main__":
    grabar_emision(url_emision, 5700)  # 95 minutos = 5700 segundos
