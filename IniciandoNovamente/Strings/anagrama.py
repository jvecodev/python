def verificar_anagrama(frase1, frase2):
    
    minuscula1 = frase1.lower()
    minuscula2 = frase2.lower()
    if minuscula1.isalpha() and minuscula2.isalpha():
        return sorted(minuscula2) == sorted(minuscula1)
    else:
        print('Apenas valores do alfabeto')

opcao1 = str(input('Digite a primeira palavra → '))
opcao2 = str(input('Digite a segunda palavra → ' ))

if verificar_anagrama(opcao1, opcao2):
    print( f'\033[0;33;41mAs palavras {opcao1} e {opcao2} são anagramas\033[m')
else:
    print( f'\033[0;33;44m As palavras {opcao1} e {opcao2} não são anagramas \033[m')




    