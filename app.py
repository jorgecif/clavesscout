import streamlit as st
from streamlit_option_menu import option_menu
import PIL.Image
import unicodedata
import string
import matplotlib.pyplot as plt
import numpy as np
import random
from PIL import Image




# Page config
st.set_page_config(
	page_title="Traductor Scout",
	page_icon="random",
	layout="centered",
	initial_sidebar_state="expanded",
	)

# Oculto botones de Streamlit - fondo de sidebar
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            [data-testid=stSidebar] {
                background-color: #6E20A0;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 



# Color morado #9b51e0

# Diccionarios

# Morse
morse_dict = {
    'A': '.-', 
    'B': '-...', 
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/',
}


# Murciélago
murcielago_dict = {
    'M': '0', 
    'U': '1', 
    'R': '2', 
    'C': '3', 
    'I': '4', 
    'E': '5', 
    'L': '6', 
    'A': '7', 
    'G': '8', 
    'O': '9', 
    ' ': '/',
}

inv_murcielago_dict= {}
for key in murcielago_dict.keys() :
    val = murcielago_dict[key]
    inv_murcielago_dict[val] = key

# Cenit Polar

cenitpolar_dict = {
    'C': 'P', 
    'E': 'O', 
    'N': 'L',     
    'I': 'A', 
    'T': 'R', 
    'P': 'C', 
    'O': 'E', 
    'L': 'N', 
    'A': 'I', 
    'R': 'T',    
    ' ': '/',
}
inv_cenitpolar_dict= {}
for key in cenitpolar_dict.keys() :
    val = cenitpolar_dict[key]
    inv_cenitpolar_dict[val] = key

# Cajón

cajon_dict = {
    'A': 'clave_cajon/_a.png', 
    'B': 'clave_cajon/_b.png', 
    'C': 'clave_cajon/_c.png',     
    'D': 'clave_cajon/_d.png', 
    'E': 'clave_cajon/_e.png', 
    'F': 'clave_cajon/_f.png', 
    'G': 'clave_cajon/_g.png', 
    'H': 'clave_cajon/_h.png', 
    'I': 'clave_cajon/_i.png', 
    'J': 'clave_cajon/_j.png',    
    'K': 'clave_cajon/_k.png',
    'L': 'clave_cajon/_l.png', 
    'M': 'clave_cajon/_m.png', 
    'N': 'clave_cajon/_n.png', 
    'Ñ': 'clave_cajon/_nn.png',    
    'O': 'clave_cajon/_o.png',
    'P': 'clave_cajon/_p.png', 
    'Q': 'clave_cajon/_q.png', 
    'R': 'clave_cajon/_r.png', 
    'S': 'clave_cajon/_s.png',    
    'T': 'clave_cajon/_t.png',
    'U': 'clave_cajon/_u.png', 
    'V': 'clave_cajon/_v.png', 
    'W': 'clave_cajon/_w.png', 
    'X': 'clave_cajon/_x.png',    
    'Y': 'clave_cajon/_y.png',
    'Z': 'clave_cajon/_z.png',
    ' ': 'clave_cajon/_espacio.png',
}

# Palitos

palitos_dict = {
    'A': 'clave_palitos/_a.png', 
    'B': 'clave_palitos/_b.png', 
    'C': 'clave_palitos/_c.png',     
    'D': 'clave_palitos/_d.png', 
    'E': 'clave_palitos/_e.png', 
    'F': 'clave_palitos/_f.png', 
    'G': 'clave_palitos/_g.png', 
    'H': 'clave_palitos/_h.png', 
    'I': 'clave_palitos/_i.png', 
    'J': 'clave_palitos/_j.png',    
    'K': 'clave_palitos/_k.png',
    'L': 'clave_palitos/_l.png', 
    'M': 'clave_palitos/_m.png', 
    'N': 'clave_palitos/_n.png', 
    'Ñ': 'clave_palitos/_nn.png',    
    'O': 'clave_palitos/_o.png',
    'P': 'clave_palitos/_p.png', 
    'Q': 'clave_palitos/_q.png', 
    'R': 'clave_palitos/_r.png', 
    'S': 'clave_palitos/_s.png',    
    'T': 'clave_palitos/_t.png',
    'U': 'clave_palitos/_u.png', 
    'V': 'clave_palitos/_v.png', 
    'W': 'clave_palitos/_w.png', 
    'X': 'clave_palitos/_x.png',    
    'Y': 'clave_palitos/_y.png',
    'Z': 'clave_palitos/_z.png',
    ' ': 'clave_palitos/_espacio.png',
}

# 7 cruces

cruces_dict = {
    'A': '7cruces/a.png', 
    'B': '7cruces/b.png', 
    'C': '7cruces/c.png',     
    'D': '7cruces/d.png', 
    'E': '7cruces/e.png', 
    'F': '7cruces/f.png', 
    'G': '7cruces/g.png', 
    'H': '7cruces/h.png', 
    'I': '7cruces/i.png', 
    'J': '7cruces/j.png',    
    'K': '7cruces/k.png',
    'L': '7cruces/l.png', 
    'M': '7cruces/m.png', 
    'N': '7cruces/n.png', 
    'Ñ': '7cruces/nn.png',    
    'O': '7cruces/o.png',
    'P': '7cruces/p.png', 
    'Q': '7cruces/q.png', 
    'R': '7cruces/r.png', 
    'S': '7cruces/s.png',    
    'T': '7cruces/t.png',
    'U': '7cruces/u.png', 
    'V': '7cruces/v.png', 
    'W': '7cruces/w.png', 
    'X': '7cruces/x.png',    
    'Y': '7cruces/y.png',
    'Z': '7cruces/z.png',
    ' ': '7cruces/espacio.png',
}

sombra_dict = {
    'A': 'clave_sombra/_a.png', 
    'B': 'clave_sombra/_b.png', 
    'C': 'clave_sombra/_c.png',     
    'D': 'clave_sombra/_d.png', 
    'E': 'clave_sombra/_e.png', 
    'F': 'clave_sombra/_f.png', 
    'G': 'clave_sombra/_g.png', 
    'H': 'clave_sombra/_h.png', 
    'I': 'clave_sombra/_i.png', 
    'J': 'clave_sombra/_j.png',    
    'K': 'clave_sombra/_k.png',
    'L': 'clave_sombra/_l.png', 
    'M': 'clave_sombra/_m.png', 
    'N': 'clave_sombra/_n.png', 
    'Ñ': 'clave_sombra/_nn.png',    
    'O': 'clave_sombra/_o.png',
    'P': 'clave_sombra/_p.png', 
    'Q': 'clave_sombra/_q.png', 
    'R': 'clave_sombra/_r.png', 
    'S': 'clave_sombra/_s.png',    
    'T': 'clave_sombra/_t.png',
    'U': 'clave_sombra/_u.png', 
    'V': 'clave_sombra/_v.png', 
    'W': 'clave_sombra/_w.png', 
    'X': 'clave_sombra/_x.png',    
    'Y': 'clave_sombra/_y.png',
    'Z': 'clave_sombra/_z.png',
    ' ': 'clave_sombra/_espacio.png',
}

giros_dict = {
    90: "clave_sombra/_90.png",
    180: "clave_sombra/_180.png",
    270: "clave_sombra/_270.png",
    0: "clave_sombra/_0.png"  
}


# Eletro

electro_dict = {
    'A': 27, 
    'B': 26, 
    'C': 25,     
    'D': 24, 
    'E': 23, 
    'F': 22, 
    'G': 21, 
    'H': 20, 
    'I': 19, 
    'J': 18,    
    'K': 17,
    'L': 16, 
    'M': 15, 
    'N': 14, 
    'Ñ': 13,    
    'O': 12,
    'P': 11, 
    'Q': 10, 
    'R': 9, 
    'S': 8,    
    'T': 7,
    'U': 6, 
    'V': 5, 
    'W': 4, 
    'X': 3,    
    'Y': 2,
    'Z': 1,
    ' ': 0,
}

# Baden Powell


badenpowell_dict = {
    'B': 'P', 
    'A': 'O', 
    'D': 'W',     
    'E': 'E', 
    'N': 'L', 
    'P': 'B', 
    'O': 'A', 
    'W': 'D', 
    'E': 'E', 
    'L': 'N',    
    ' ': '/',

}

inv_badenpowell_dict= {}
for key in badenpowell_dict.keys() :
    val = badenpowell_dict[key]
    inv_badenpowell_dict[val] = key


# Eucalipto
eucalipto_dict = {
    'E': '1', 
    'U': '2', 
    'C': '3', 
    'A': '4', 
    'L': '5', 
    'I': '6', 
    'P': '7', 
    'T': '8', 
    'O': '9', 
    ' ': '/',
}

inv_eucalipto_dict= {}
for key in eucalipto_dict.keys() :
    val = eucalipto_dict[key]
    inv_eucalipto_dict[val] = key



# Serrucho
serrucho_dict = {
    'A': 'ʌɅ', 
    'B': 'Ʌʌʌʌ', 
    'C': 'ɅʌɅʌ', 
    'D': 'Ʌʌʌ', 
    'E': 'ʌ', 
    'F': 'ʌʌɅʌ', 
    'G': 'ɅɅʌ', 
    'H': 'ʌʌʌʌ', 
    'I': 'ʌʌ', 
    'J': 'ʌɅɅɅ', 
    'K': 'ɅʌɅ', 
    'L': 'ʌɅʌʌ', 
    'M': 'ɅɅ', 
    'N': 'Ʌʌ', 
    'O': 'ɅɅɅ', 
    'P': 'ʌɅɅʌ', 
    'Q': 'ɅɅʌɅ', 
    'R': 'ʌɅʌ', 
    'S': 'ʌʌʌ', 
    'T': 'Ʌ', 
    'U': 'ʌʌɅ', 
    'V': 'ʌʌʌɅ', 
    'W': 'ʌɅɅ', 
    'X': 'ɅʌʌɅ', 
    'Y': 'ɅʌɅɅ', 
    'Z': 'ɅɅʌʌ',
    '0': 'ɅɅɅɅɅ',
    '1': 'ʌɅɅɅɅ',
    '2': 'ʌʌɅɅɅ',
    '3': 'ʌʌʌɅɅ',
    '4': 'ʌʌʌʌɅ',
    '5': 'ʌʌʌʌʌ',
    '6': 'Ʌʌʌʌʌ',
    '7': 'ɅɅʌʌʌ',
    '8': 'ɅɅɅʌʌ',
    '9': 'ɅɅɅɅʌ',
    ' ': '/',
}

# Mnemotécnica Morse
mnemotecnica_dict = {
    'A': 'asno', 
    'B': 'bonaparte', 
    'C': 'cocacola', 
    'D': 'docena', 
    'E': 'el', 
    'F': 'fumarola', 
    'G': 'gondola', 
    'H': 'himalaya', 
    'I': 'iris', 
    'J': 'jabonoso', 
    'K': 'kohinor', 
    'L': 'limonada', 
    'M': 'moto', 
    'N': 'noche',
    'Ñ': 'ñoñopatoso',  
    'O': 'oporto', 
    'P': 'pisotones', 
    'Q': 'qocorico', 
    'R': 'ramona', 
    'S': 'sardina', 
    'T': 'tos', 
    'U': 'unico', 
    'V': 'ventilador', 
    'W': 'wagonpost', 
    'X': 'Xochimilco', 
    'Y': 'yositomo', 
    'Z': 'zocoyula',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    ' ': '/',
}


# Funciones

# Quitar signos de puntuación 
def remove_punctuation(text):
    # Use the string module to get a list of punctuation marks
    punctuation = string.punctuation

    # Remove punctuation marks from the text
    no_punct = "".join([char for char in text if char not in punctuation])
    return no_punct

# Quitar acentos
def remove_spanish_accents(text):
    # Use unicodedata.normalize to remove accents from the text
    text=text.upper()
    texto_2 = text.replace('Ñ','-&-')
    normalized_text = unicodedata.normalize('NFKD', texto_2).encode('ASCII', 'ignore').decode('utf-8')
    normalized_text_2 = normalized_text.replace('-&-','Ñ')	

    return normalized_text_2


# Funciones por  clave

# MORSE
# Convertir texto a morse
def text_to_morse(text):
    morse_text = ''
    for char in text:
        if char.upper() in morse_dict:
            morse_text += morse_dict[char.upper()] + ' '
        else:
            morse_text += char
    return morse_text

# Convertir morse a texto
def morse_to_text(morse_text):
    text = ''
    morse_list = morse_text.split(' ')
    for morse_char in morse_list:
        for key, value in morse_dict.items():
            if value == morse_char:
                text += key
                break
        else:
            text += morse_char
    return text

# MURCIELAGO
# Convertir texto a murciélago
def text_to_murcielago(text_to_encode):
    text_encoded = ''
    for char in text_to_encode:
        if char.upper() in murcielago_dict:
            text_encoded += murcielago_dict[char.upper()]
        else:
            text_encoded += char.upper() 
    return text_encoded

# Convertir murciélago a texto
def murcielago_to_text(text_to_decode):
    text_decoded = ''
    for char in text_to_decode:
        if char.upper() in inv_murcielago_dict:
            text_decoded += inv_murcielago_dict[char.upper()]
        else:
            text_decoded += char.upper() 
    return text_decoded


# CENIT POLAR
# Convertir texto a Cenit
def text_to_cenitpolar(text_to_encode):
    text_encoded = ''
    for char in text_to_encode:
        if char.upper() in cenitpolar_dict:
            text_encoded += cenitpolar_dict[char.upper()]
        else:
            text_encoded += char.upper() 
    return text_encoded

# Convertir Cenit a texto
def cenitpolar_to_text(text_to_decode):
    text_decoded = ''
    for char in text_to_decode:
        if char.upper() in inv_cenitpolar_dict:
            text_decoded += inv_cenitpolar_dict[char.upper()]
        else:
            text_decoded += char.upper() 
    return text_decoded

# BADEN POWELL
# Convertir texto a Baden Powell
def text_to_badenpowell(text_to_encode):
    text_encoded = ''
    for char in text_to_encode:
        if char.upper() in badenpowell_dict:
            text_encoded += badenpowell_dict[char.upper()]
        else:
            text_encoded += char.upper() 
    return text_encoded

# Convertir Baden Powell a texto
def badenpowell_to_text(text_to_decode):
    text_decoded = ''
    for char in text_to_decode:
        if char.upper() in inv_badenpowell_dict:
            text_decoded += inv_badenpowell_dict[char.upper()]
        else:
            text_decoded += char.upper() 
    return text_decoded

# CAJON
# Convertir texto a cajon
def text_to_cajon(text_to_encode):
    URL_images_encoded = []
    for char in text_to_encode:
        if char.upper() in cajon_dict:
            imagen_char =cajon_dict[char.upper()]
            URL_images_encoded.append(imagen_char)
           
        else:
            URL_images_encoded += char

    return URL_images_encoded

# PALITOS
# Convertir texto a palitos
def text_to_palitos(text_to_encode):
    URL_images_encoded = []
    for char in text_to_encode:
        if char.upper() in palitos_dict:
            imagen_char =palitos_dict[char.upper()]
            URL_images_encoded.append(imagen_char)
           
        else:
            URL_images_encoded += char

    return URL_images_encoded


# 7 CRUCES
# Convertir texto a 7 ccruces
def text_to_cruces(text_to_encode):
    URL_images_encoded = []
    for char in text_to_encode:
        if char.upper() in cruces_dict:
            imagen_char =cruces_dict[char.upper()]
            URL_images_encoded.append(imagen_char)
           
        else:
            URL_images_encoded += char

    return URL_images_encoded

# SOMBRA
# Convertir texto a sombra
def text_to_sombra(text_to_encode, posiciones, giros): 
    """
    Convierte el texto a código sombra e inserta imágenes de giros en posiciones específicas.

    Args:
        text_to_encode (str): Texto limpio a codificar.
        posiciones (list): Lista de posiciones (enteros) donde insertar los giros.
        giros (list): Lista de valores de giros (ej: [90, 180, 270]).
        sombra_dict (dict): Diccionario de letras a imágenes.
        giros_dict (dict): Diccionario de grados de giro a imágenes.

    Returns:
        list: Secuencia de imágenes (URL o paths) codificadas con giros insertados.
    """
    resultado = []
    idx_giro = 0
    letra_idx = 0
    giro_actual = 0  # empieza en 0

    total_len = len(text_to_encode) + len(posiciones)

    for i in range(total_len):
        if idx_giro < len(posiciones) and i == posiciones[idx_giro]:
            giro_actual = giros[idx_giro]
            ruta_giro = giros_dict.get(giro_actual)
            if ruta_giro:
                img_giro = Image.open(ruta_giro)
                resultado.append(img_giro)
            idx_giro += 1
        else:
            char = text_to_encode[letra_idx].upper()
            ruta_letra = sombra_dict.get(char)
            if ruta_letra:
                img_letra = Image.open(ruta_letra)
                img_rotada = img_letra.rotate(giro_actual, expand=True)
                resultado.append(img_rotada)
            else:
                resultado.append(char)  # si no hay imagen, lo deja como texto
            letra_idx += 1

    return resultado


# ELECTROCARDIOGRAMA
# Convertir texto a electrocardiograma
def text_to_electro(text_to_encode):
    URL_images_encoded = []
    for char in text_to_encode:
        if char.upper() in electro_dict:
            imagen_char =electro_dict[char.upper()]
            URL_images_encoded.append(imagen_char)
           
        else:
            URL_images_encoded += char

    return URL_images_encoded


def text_to_electro(text_to_encode):
    text_encoded = []
    for char in text_to_encode:
        if char.upper() in electro_dict:
            text_encoded.append(electro_dict[char.upper()])
        else:
            text_encoded.append(char.upper())
    return text_encoded

# EUCALIPTO
# Convertir texto a eucalipto
def text_to_eucalipto(text_to_encode):
    text_encoded = ''
    for char in text_to_encode:
        if char.upper() in eucalipto_dict:
            text_encoded += eucalipto_dict[char.upper()]
        else:
            text_encoded += char.upper() 
    return text_encoded

# Convertir eucalipto a texto
def eucalipto_to_text(text_to_decode):
    text_decoded = ''
    for char in text_to_decode:
        if char.upper() in inv_eucalipto_dict:
            text_decoded += inv_eucalipto_dict[char.upper()]
        else:
            text_decoded += char.upper() 
    return text_decoded


# SERRUCHO
# Convertir texto a serrucho
def text_to_serrucho(text):
    text_encoded = ''
    for char in text:
        if char.upper() in serrucho_dict:
            text_encoded += serrucho_dict[char.upper()] + ' '
        else:
            text_encoded += char
    return text_encoded

# Convertir serrucho a texto
def serrucho_to_text(serrucho_text):
    text = ''
    serrucho_list = serrucho_text.split(' ')
    for serrucho_char in serrucho_list:
        for key, value in serrucho_dict.items():
            if value == serrucho_char:
                text += key
                break
        else:
            text += serrucho_char
    return text

# MNEMOTECNICA MORSE
# Convertir texto a MNEMOTECNICA MORSE
def text_to_mnemotecnica(text):
    text_encoded = ''
    for char in text:
        if char.upper() in mnemotecnica_dict:
            text_encoded += mnemotecnica_dict[char.upper()] + ' '
        else:
            text_encoded += char
    return text_encoded

# Convertir mnemotecnica morse a texto
def mnemotecnica_to_text(mnemotecnica_text):
    text = ''
    mnemotecnica_list = mnemotecnica_text.split(' ')
    for mnemotecnica_char in mnemotecnica_list:
        for key, value in mnemotecnica_dict.items():
            if value == mnemotecnica_char:
                text += key
                break
        else:
            text += mnemotecnica_char
    return text


# Logo sidebar
image =  PIL.Image.open('logoscoutscol.png')
st.sidebar.image(image,width="stretch", use_container_width=None )

with st.sidebar:
    selected = option_menu(
            menu_title="Claves  Scout",  # required
            options=["Home", "Morse", "Murciélago", "Cenit Polar", "Cajón", "Palitos", "Electrocardiograma", "7 cruces", "Baden Powell","Eucalipto",  "Serrucho", "Mnenotecnica Morse", "Código Sombra","Contacto"],  # required
            icons=["house", "caret-right-fill",  "caret-right-fill",  "caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill","caret-right-fill", "caret-right-fill", "caret-right-fill","caret-right-fill", "caret-right-fill", "caret-right-fill","envelope"],  # optional
            menu_icon="upc-scan",  # optional
            default_index=0,  # optional
        )


if selected == "Home":
    # Anuncio destacado

    st.write("Esta aplicación te permitirá codificar o traducir texto normal a diferentes claves scout y/o viceversa.")

    image = Image.open('cifrado.jpg')
    st.image(image, use_container_width=True)

    st.write("Selecciona una clave en el menú de la izquierda para iniciar")
    st.markdown(
        """
        <div style='background-color:#fff8b3; padding: 12px; border-radius: 8px; text-align: center; border: 1px solid #f0d000;'>
            <span style="font-size:18px; color:#333333;">
                🔐 ¡Nueva clave disponible! Ya puedes utilizar el <strong style="color:#d10000;">Código Sombra</strong> en el menú de la izquierda.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

if selected == "Morse":
    st.title(f"Clave {selected}")
    # Get user input
    choice = st.selectbox("Select Translation Direction", ["Text to Morse", "Morse to Text"])
    if choice == "Text to Morse":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            morse_output = text_to_morse(text_without_marks)
            st.write("Texto codificado:")
            st.write(morse_output)
    elif choice == "Morse to Text":
        morse_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = morse_to_text(morse_input)
            st.write("Texto decodificado:")
            st.write(text_output)

if selected == "Murciélago":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Murciélago", "Murciélago to Text"])

    if choice == "Text to Murciélago":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_murcielago(text_without_marks)
            st.write("Texto codificado:")
            st.write(text_output)
    elif choice == "Murciélago to Text":
        text_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = murcielago_to_text(text_input)
            st.write("Texto decodificado:")
            st.write(text_output)

if selected == "Cenit Polar":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Cenit Polar", "Cenit Polar to Text"])

    if choice == "Text to Cenit Polar":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_cenitpolar(text_without_marks)
            st.write("Texto codificado:")
            st.write(text_output)
    elif choice == "Cenit Polar to Text":
        text_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = cenitpolar_to_text(text_input)
            st.write("Texto decodificado:")
            st.write(text_output)



if selected == "Cajón":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Cajón"])

    if choice == "Text to Cajón":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_cajon(text_without_marks)
            st.write("Texto codificado:")
            #st.write(text_output)
            #st.image(image,width=None, use_container_width=True )
            st.image(text_output, width=40, use_container_width=False)

if selected == "Palitos":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Palitos"])

    if choice == "Text to Palitos":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_palitos(text_without_marks)
            st.write("Texto codificado:")
            #st.write(text_output)
            #st.image(image,width=None, use_container_width=True )
            st.image(text_output, width=40, use_container_width=False)

if selected == "Electrocardiograma":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Electrocardiograma"])

    if choice == "Text to Electrocardiograma":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_electro(text_without_marks)
            st.write("Texto codificado:")
            st.write(text_output)

            st.line_chart(text_output)


if selected == "7 cruces":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to 7 cruces"])

    if choice == "Text to 7 cruces":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_cruces(text_without_marks)
            st.write("Texto codificado:")
            #st.write(text_output)
            #st.image(image,width=None, use_container_width=True )
            st.image(text_output, width=40, use_container_width=False)


if selected == "Baden Powell":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Baden Powell", "Baden Powell to Text"])

    if choice == "Text to Baden Powell":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_badenpowell(text_without_marks)
            st.write("Texto codificado:")
            st.write(text_output)
    elif choice == "Baden Powell to Text":
        text_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = badenpowell_to_text(text_input)
            st.write("Texto decodificado:")
            st.write(text_output)

if selected == "Eucalipto":
    st.title(f"Clave {selected}")
    # Get user input
    choice = st.selectbox("Select Translation Direction", ["Text to Eucalipto", "Eucalipto to Text"])
    if choice == "Text to Eucalipto":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            eucalipto_output = text_to_eucalipto(text_without_marks)
            st.write("Texto codificado:")
            st.write(eucalipto_output)
    elif choice == "Eucalipto to Text":
        eucalipto_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = eucalipto_to_text(eucalipto_input)
            st.write("Texto decodificado:")
            st.write(text_output)

if selected == "Serrucho":
    st.title(f"Clave {selected}")
    # Get user input
    choice = st.selectbox("Select Translation Direction", ["Text to Serrucho","Serrucho to Text"])
    if choice == "Text to Serrucho":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            serrucho_output = text_to_serrucho(text_without_marks)
            st.write("Texto codificado:")
            st.write(serrucho_output)
    elif choice == "Serrucho to Text":
        serrucho_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = serrucho_to_text(serrucho_input)
            st.write("Texto decodificado:")
            st.write(text_output)

if selected == "Mnenotecnica Morse":
    st.title(f"Clave {selected}")
    # Get user input
    choice = st.selectbox("Select Translation Direction", ["Text to Mnemotecnica Morse", "Mnemotecnica Morse to Text"])
    if choice == "Text to Mnemotecnica Morse":
        text_input = st.text_input("Ingrese el texto a codificar")
        if st.button("Codificar"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            mnemotecnica_output = text_to_mnemotecnica(text_without_marks)
            st.write("Texto codificado:")
            st.write(mnemotecnica_output)
    elif choice == "Mnemotecnica Morse to Text":
        mnemotecnica_input = st.text_input("Ingrese el texto a decodificar")
        if st.button("Decodificar"):
            text_output = mnemotecnica_to_text(mnemotecnica_input)
            st.write("Texto decodificado:")
            st.write(text_output)            

if selected == "Código Sombra":
    st.title(f"Clave {selected}")
    with st.expander("¿Qué es el Código Sombra?"):
        st.markdown("""
El **Código Sombra** es un sistema de codificación en el que cada letra del alfabeto se representa mediante un símbolo. 
Adicionalmente, se pueden insertar "giros" en posiciones específicas del mensaje, 
los cuales alteran la orientación del "papel" y dificultan la lectura para quienes no conocen el código.

- Cada símbolo representa una letra.
- Existen 4 símbolos especiales de giro que pueden insertarse en cualquier parte del mensaje y lo que indicarán es que a partir de ese símbolo el papel debe girarse 90, 180 o 270 grados.
- Para decodificar el mensaje, cada vez que aparezca un símbolo de giro el receptor deberá girar la hoja a la posición indicada.

**🔐 Ejemplo:** Si aparece el símbolo de giro 1, deberás girar el papel a 90° para decodificar los siguientes símbolos, los cuales ahora aparecerán rotados.

Tomado del Libro **El Idioma de los Espías** de Martin Gardner


                    
                    """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.image("clave_sombra/alfabeto.png", caption="Alfabeto", use_container_width=True)
            st.image("clave_sombra/modificadores.png", caption="Símbolos de giro")
        with col2:
            st.markdown("""
            Cada línea del interior de un símbolo extra es un indicador que señala si 
            la parte superior del papel debe estar para arriba, para abajo, 
            para la izquierda o para la derecha. Por ejemplo, si aparece el símbolo extra 3, 
            el papel debe ponerse cabeza abajo. El símbolo 2 significa que la página 
            debe girarse de modo que su borde superior quede hacia la derecha. 
            El símbolo 4 te dice que debes girar la hoja para que su borde superior quede a la izquierda. El primer símbolo extra señala que el papel debe quedar en posición normal, es decir con el borde superior hacia arriba.
             """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.image("clave_sombra/ejemplo.png", caption="Ejemplo: ESTOY EN PELIGRO SOCORRO", use_container_width=True)
        with col2:
            st.markdown("""
            El primer símbolo señala que debes dar a la página un cuarto de 
            giro antes de decodificar los cuatro símbolos que siguen. 
            Después llegas a otro símbolo extra que te indica que debes restituir 
            la página a la posición normal hasta que llegues al siguiente símbolo extra. 
            Este constante giro de la página, en tanto la clave alfabética 
            permanece siempre en la misma posición, es una “vuelta” 
            novedosa que hace más confuso el código para cualquier enemigo que pueda interceptarlo.


             """, unsafe_allow_html=True)

    # Get user input
    choice = st.selectbox("Select Translation Direction", ["Text to Sombra"])
    if choice == "Text to Sombra":
        text_input = st.text_input("Ingrese el texto a codificar")
        Ngiros_input = st.slider("Ingrese el número de giros del papel", 0, 10, 1)

        if text_input:
            text_without_accents = remove_spanish_accents(text_input)
            text_without_marks = remove_punctuation(text_without_accents)
            texto_limpio = text_without_marks.replace(" ", "")
            num_letras = len(texto_limpio)

            if Ngiros_input >= num_letras:
                st.error("El número de giros debe ser menor que la cantidad de letras del texto ingresado.")
            else:
                st.subheader("Selecciona la posición y el valor de cada giro")
                col_pos, col_giro = st.columns(2)
                posiciones = []
                lista_giros = []
                inicio = 1

                for i in range(Ngiros_input):
                    with col_pos:
                        opciones = list(range(inicio, num_letras))
                        pos = st.selectbox(f"Posición #{i + 1}", opciones, key=f"pos_{i}")
                        posiciones.append(pos)
                        inicio = pos + 1

                    with col_giro:
                        giro = st.selectbox(f"Giro #{i + 1}", [0, 90, 180, 270], key=f"giro_{i}")
                        lista_giros.append(giro)

                if st.button("Codificar"):
                    #st.write("Giros seleccionados:", lista_giros)
                    #st.write("Posiciones seleccionadas:", posiciones)

                    text_output = text_to_sombra(text_without_marks, posiciones, lista_giros)
                    st.write("Texto codificado:")
                    st.image(text_output, width=40, use_container_width=False)

if selected == "Contacto":
    st.title(f"Créditos y {selected}")
    st.subheader("Esta aplicación ha sido desarrollada por Jorge O. Cifuentes (Águila Vigilante)")
    st.subheader("Grupo 10 Meraki - Girón, Santander")
    st.write('Email: *jorgecif@gmail.com* :heart: :fleur_de_lis:')
    st.write("Traductor de claves scout")
    st.write("Version 1.0")
    st.text("")
