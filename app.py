import streamlit as st
from streamlit_option_menu import option_menu
import PIL.Image
import unicodedata
import string
import matplotlib.pyplot as plt
import numpy as np



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


# Logo sidebar
image =  PIL.Image.open('logoscoutscol.png')
st.sidebar.image(image,width=None, use_container_width=None )

with st.sidebar:
    selected = option_menu(
            menu_title="Claves  Scout",  # required
            options=["Home", "Morse", "Murciélago", "Cenit Polar", "Cajón", "Palitos", "Electrocardiograma", "7 cruces", "Baden Powell", "Contacto"],  # required
            icons=["house", "caret-right-fill",  "caret-right-fill",  "caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill", "caret-right-fill","envelope"],  # optional
            menu_icon="upc-scan",  # optional
            default_index=0,  # optional
        )


if selected == "Home":
    st.title("Traductor de claves scout")
    st.write("Esta aplicación te permitirá codificar o traducir texto normal a diferentes claves scout y/o viceversa.")
    image =  PIL.Image.open('cifrado.jpg')
    st.image(image,width=None, use_container_width=True )
    st.write("Selecciona una clave en el menú de la izquierda para iniciar")



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


if selected == "opcion2":
    st.title(f"You have selected {selected}")


if selected == "opcion3":
    st.title(f"You have selected {selected}")

if selected == "Contacto":
    st.title(f"Créditos y {selected}")
    st.subheader("Esta aplicación ha sido desarrollada por Jorge O. Cifuentes (Águila Vigilante)")
    st.subheader("Grupo 10 Meraki - Girón, Santander")
    st.write('Email: *jorgecif@gmail.com* :heart: :fleur_de_lis:')
    st.write("Traductor de claves scout")
    st.write("Version 1.0")
    st.text("")
