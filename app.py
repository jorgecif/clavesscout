import streamlit as st
from streamlit_option_menu import option_menu
import PIL.Image
import unicodedata
import string



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
    normalized_text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
    return normalized_text

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

def murcielago_to_text2(murcielago_text):
    text = ''
    murcielago_list = murcielago_text.split(' ')
    for murcielago_char in murcielago_list:
        for key, value in murcielago_dict.items():
            if value == murcielago_char:
                text += key
                break
        else:
            text += murcielago_char
    return text

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

image =  PIL.Image.open('logoscoutscol.png')
st.sidebar.image(image,width=None, use_column_width=None )

with st.sidebar:
    selected = option_menu(
            menu_title="Claves  Scout",  # required
            options=["Home", "Morse", "Murciélago", "Cenit Polar","Contacto"],  # required
            icons=["house", "caret-right-fill",  "caret-right-fill", "caret-right-fill","envelope"],  # optional
            menu_icon="upc-scan",  # optional
            default_index=0,  # optional
        )


if selected == "Home":
    st.title("Traductor de claves scout")
    st.write("Esta aplicación te permitirá codificar o traducir texto normal a diferentes claves scout y/o viceversa.")
    image =  PIL.Image.open('cifrado.jpg')
    st.image(image,width=None, use_column_width=True )
    st.write("Selecciona una clave en el menú de la izquierda para iniciar")



if selected == "Morse":
    st.title(f"Clave {selected}")


    # Get user input
    choice = st.selectbox("Select Translation Direction", ["Text to Morse", "Morse to Text"])
    if choice == "Text to Morse":
        text_input = st.text_input("Enter the text you want to translate")
        if st.button("Translate"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            morse_output = text_to_morse(text_without_marks)
            st.write("Morse code translation:")
            st.write(morse_output)
    elif choice == "Morse to Text":
        morse_input = st.text_input("Enter the Morse code you want to translate")
        if st.button("Translate"):
            text_output = morse_to_text(morse_input)

            
            st.write("Text translation:")
            st.write(text_output)

if selected == "Murciélago":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Murciélago", "Murciélago to Text"])

    if choice == "Text to Murciélago":
        text_input = st.text_input("Enter the text you want to code")
        if st.button("Translate"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_murcielago(text_without_marks)
            st.write("Murciélago code translation:")
            st.write(text_output)
    elif choice == "Murciélago to Text":
        text_input = st.text_input("Enter the Murciélago code you want to decode")
        if st.button("Translate"):
            text_output = murcielago_to_text(text_input)
            st.write("Text translation:")
            st.write(text_output)

if selected == "Cenit Polar":
    st.title(f"Clave {selected}")
    choice = st.selectbox("Select Translation Direction", ["Text to Cenit Polar", "Cenit Polar to Text"])

    if choice == "Text to Cenit Polar":
        text_input = st.text_input("Enter the text you want to translate")
        if st.button("Translate"):
            text_without_accents=remove_spanish_accents(text_input)
            text_without_marks=remove_punctuation(text_without_accents)
            text_output = text_to_cenitpolar(text_without_marks)
            st.write("Morse code translation:")
            st.write(text_output)
    elif choice == "Cenit Polar to Text":
        text_input = st.text_input("Enter the Morse code you want to translate")
        if st.button("Translate"):
            text_output = cenitpolar_to_text(text_input)
            st.write("Text translation:")
            st.write(text_output)

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