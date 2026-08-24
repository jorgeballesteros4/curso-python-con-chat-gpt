import google.generativeai as google_ia
import config

# 1. Le ponemos la llave mágica al robot
google_ia.configure(api_key=config.LLAVE_SECRETA)

# 2. Elegimos el modelo de inteligencia de Google
cerebro = google_ia.GenerativeModel('gemini-3.6-flash')

# 3. Le damos su personalidad y sus reglas
instruccion = "Eres un experto en la Biblia. Eres amable, paciente y explicas las cosas de forma muy sencilla."

print("¡Hola! Soy tu IA Bíblica. ¿Qué historia o versículo quieres explorar hoy?")

# 4. Creamos un ciclo (como un juego infinito) para poder chatear
while True:
    pregunta = input("Tú: ")
    
    # Una palabra mágica para apagar el robot
    if pregunta.lower() == "salir":
        print("¡Que Dios te bendiga! Hasta pronto.")
        break
        
    # El robot piensa la respuesta combinando su personalidad y tu pregunta
    respuesta = cerebro.generate_content(instruccion + " El usuario pregunta: " + pregunta)
    
    print("\nRobot Bíblico:", respuesta.text)
    print("-" * 30) # Solo una línea para separar los mensajes