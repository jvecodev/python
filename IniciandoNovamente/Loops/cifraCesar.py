def Decifrar(frase):
    frase_decifrada = ''
    
    while True:  # Loop para repetir até que uma frase válida seja digitada
        for letra in frase.strip():
            if letra.isnumeric():
                print('Apenas letras')
                print('-'*20)
                frase = input('Digite novamente: ')

                break  # Sai do for e reinicia o while com a nova entrada
        else:
            # Se não houver números, decifra a frase
            for letra in frase.strip():
                frase_decifrada += (chr(ord(letra) + 3) )

            print('-'*20)
            print('Aqui está a frase com o decifrador de César →', frase_decifrada)

            break  # Sai do loop while após decifrar a frase corretamente
    return frase
texto = input('Digite uma frase → ')
Decifrar(texto)

