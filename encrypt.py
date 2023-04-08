def transpositionencrypt(mensaje):
    mensaje = mensaje.replace(" ", "$")
    len_text = len(mensaje)
    key = 5
    col = int(len_text / key) + (0 if (len_text % key == 0) else 1)
    mensaje += " " * (col * key - len_text)

    ciphertext = ''
    for i in range(key):
        for j in range(col):
            index = j * key + i
            if index < len_text:
                ciphertext += mensaje[index]
            else:
                ciphertext += ' '

    return ciphertext


def transpositiondecrypt(mensaje):
    key = 5
    col = int(len(mensaje) / key)
    texto = ''
    for i in range(col):
        for j in range(key):
            index = i + j*col
            texto += mensaje[index]
    texto = texto.rstrip()
    texto = texto.replace("$", " ")
    return texto


def rot13(mensaje):
    texto = ""
    for char in mensaje:
        if char.isalpha():
            if char == 'ñ' or char == 'Ñ':
                texto += char
            elif char.isupper():
                texto += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                texto += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            texto += char
    return texto


def encrypt(mensaje):
    mensaje = rot13(mensaje)
    mensaje = transpositionencrypt(mensaje)
    return mensaje


def decrypt(mensaje):
    mensaje = transpositiondecrypt(mensaje)
    mensaje = rot13(mensaje)
    return mensaje
