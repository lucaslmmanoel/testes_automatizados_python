import string

def verificar_pangrama(frase):
    for letra in string.ascii_lowercase:
        if letra not in frase:
            return False
    return True