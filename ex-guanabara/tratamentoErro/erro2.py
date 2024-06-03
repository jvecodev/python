import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')    
except urllib .error.URLError:
    print('\033[30;41mO site Pudim não está acessível no momento, por falta de conexão no recinto.\033[m')
except urllib.error.HTTPError:
    print('\033[30;42mA Url esta incorreta ou proibida no momento.\033[m')

else:
    print('\033[30;44mO site Pudim está acessível no momento.\033[m')
    # neste caso, a funcionalidade read() é usada para ler o conteúdo do site, por exemplo HTML e CSS
    print(site.read())
    print('='*182)

finally:
    print('\033[35mAgradecemos pela confinça em nossos serviços.\033[m')