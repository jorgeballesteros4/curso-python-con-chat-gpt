import streamlit as st
import google.generativeai as google_ia
from PIL import Image
import os
import config

# --- 1. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Cristian AI (C.A.I)", 
    page_icon="✝️", 
    layout="wide"
)

# Conectamos la llave mágica de Gemini
google_ia.configure(api_key=config.LLAVE_SECRETA)

# Buscamos la carpeta exacta donde está guardado este archivo
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Usamos el nombre exacto de tu archivo de imagen
ruta_logo = os.path.join(directorio_actual, "logo.png.png")

# --- 2. BARRA LATERAL (MENÚ Y CONFIGURACIONES) 🎛️ ---
with st.sidebar:
    # Mostramos tu logo si existe el archivo 'logo.png.png'
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    
    st.header("⚙️ Configuración")
    
    # Selector de personalidad
    personalidad = st.selectbox(
        "¿Cómo quieres que te hable Cristian AI?",
        [
            "Para niños (Fácil y con historias)",
            "Sabio y Maestro (Explicaciones profundas)",
            "Amigo y Consejero (Amable y con cariño)"
        ]
    )
    
    # Nivel de creatividad
    creatividad = st.slider(
        "Nivel de imaginación / creatividad:",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )
    
    st.divider()
    
    # 📸 Subir imagen para que Cristian AI la vea
    st.subheader("📸 Ojos de Cristian AI")
    foto_subida = st.file_uploader(
        "Sube una foto o versículo (opcional):",
        type=["jpg", "jpeg", "png"]
    )
    
    if foto_subida:
        imagen = Image.open(foto_subida)
        st.image(imagen, caption="Foto lista para analizar", use_container_width=True)
    else:
        imagen = None

    st.divider()

    # Botón para borrar el chat y empezar de nuevo
    if st.button("🗑️ Borrar conversación"):
        st.session_state.messages = []
        st.rerun()

# --- 3. REGLAS Y PERSONALIDAD DEL ROBOT ---
instrucciones_base = {
    "Para niños (Fácil y con historias)": (
        "Eres Cristian AI, un maestro cristiano muy cariñoso. "
        "Explicas historias bíblicas de forma divertida, sencilla y con ejemplos para niños de 10 años."
    ),
    "Sabio y Maestro (Explicaciones profundas)": (
        "Eres Cristian AI, un teólogo y experto en historia bíblica. "
        "Das explicaciones detalladas con contexto histórico, teológico y referencias de versículos exactos."
    ),
    "Amigo y Consejero (Amable y con cariño)": (
        "Eres Cristian AI, un guía espiritual cálido, paciente y comprensivo. "
        "Das ánimo, paz y consejos de vida basados en las enseñanzas de la Biblia."
    )
}

instruccion_actual = instrucciones_base[personalidad]

# Cerebro de Gemini con el modelo actualizado
cerebro = google_ia.GenerativeModel(
    model_name="gemini-3.6-flash",
    system_instruction=instruccion_actual,
    generation_config={"temperature": creatividad}
)

# --- 4. ÁREA PRINCIPAL DEL CHAT ---

# Mostramos el logo principal si existe
if os.path.exists(ruta_logo):
    # Usamos width para controlar el tamaño. Puedes subir o bajar este número a tu gusto.
    st.image(ruta_logo, width=100) 
else:
    # Título de respaldo por si la imagen no se encuentra
    st.title("✝️ Cristian AI (C.A.I)")

st.caption("📖 *Respuestas basadas en la Biblia*")

# Memoria del chat (para recordar toda la plática)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "¡Hola! Soy Cristian AI. ¿Qué historia, duda o versículo bíblico te gustaría consultar hoy?"
        }
    ]

# Mostramos todos los mensajes anteriores
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 5. CUANDO EL USUARIO ESCRIBE UNA PREGUNTA ---
if prompt := st.chat_input("Escribe tu pregunta para Cristian AI..."):
    
    # 1. Mostramos tu mensaje en el chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Cristian AI procesa y responde
    with st.chat_message("assistant"):
        with st.spinner("Consultando la Biblia y pensando..."):
            try:
                # Si subiste una foto, enviamos el texto + la imagen a Gemini
                if imagen:
                    contenido = [prompt, imagen]
                else:
                    contenido = prompt
                
                respuesta = cerebro.generate_content(contenido)
                st.markdown(respuesta.text)
                
                # Guardamos la respuesta en la memoria
                st.session_state.messages.append({"role": "assistant", "content": respuesta.text})
            except Exception as error:
                st.error(f"Ocurrió un error: {error}")