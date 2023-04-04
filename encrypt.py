def encrypt(mensaje):
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
