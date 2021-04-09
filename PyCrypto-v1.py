import urllib.request, time
import json
from datetime import datetime
from colorama import Fore, Back, Style
import colorama
colorama.init(autoreset=True)

# OBTENDO A HORA DO SISTEMA
def obter_hora():
	data_e_hora_atuais = datetime.now()
	data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M:%S")
	print(data_e_hora_em_texto)
	return data_e_hora_em_texto

# OBTENDO VALORES DO BITCOIN
def bitcoin_real():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Cripple&vs_currencies=brl%2Cusd%2Ceur&include_24hr_change=true"
        with urllib.request.urlopen(url) as url:
            response = url.read()
            data = json.loads(response.decode('utf-8'))
            real = float(data['bitcoin']['brl'])
            return real
    except urllib.error.HTTPError:
        print("URL Inexistente!")  

def bitcoin_dolar():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Cripple&vs_currencies=brl%2Cusd%2Ceur&include_24hr_change=true"
        with urllib.request.urlopen(url) as url:
            response = url.read()
            data = json.loads(response.decode('utf-8'))
            real = float(data['bitcoin']['usd'])
            return real
    except urllib.error.HTTPError:
        print("URL Inexistente!")      

# OBTENDO VALORES DO ETHEREUM
def ethereum_real():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Cripple&vs_currencies=brl%2Cusd%2Ceur&include_24hr_change=true"
        with urllib.request.urlopen(url) as url:
            response = url.read()
            data = json.loads(response.decode('utf-8'))
            real = float(data['ethereum']['brl'])
            return real
    except urllib.error.HTTPError:
        print("URL Inexistente!") 

def ethereum_dolar():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Cripple&vs_currencies=brl%2Cusd%2Ceur&include_24hr_change=true"
        with urllib.request.urlopen(url) as url:
            response = url.read()
            data = json.loads(response.decode('utf-8'))
            real = float(data['ethereum']['usd'])
            return real
    except urllib.error.HTTPError:
        print("URL Inexistente!") 

# OBTENDO VALORES DO XRP
def xrp_real():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Cripple&vs_currencies=brl%2Cusd%2Ceur&include_24hr_change=true"
        with urllib.request.urlopen(url) as url:
            response = url.read()
            data = json.loads(response.decode('utf-8'))
            real = float(data['ripple']['brl'])
            return real
    except urllib.error.HTTPError:
        print("URL Inexistente!")

def xrp_dolar():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin%2Cripple&vs_currencies=brl%2Cusd%2Ceur&include_24hr_change=true"
        with urllib.request.urlopen(url) as url:
            response = url.read()
            data = json.loads(response.decode('utf-8'))
            real = float(data['ripple']['usd'])
            return real
    except urllib.error.HTTPError:
        print("URL Inexistente!")

# REGRA DE NEGOCIO
def exibir_valores():
    # INICIALIZAÇÃO DAS VARIAVEIS
    bitcoin_inicio_real = bitcoin_real()
    bitcoin_inicio_dolar = bitcoin_dolar()
    ethereum_inicio_real = ethereum_real()
    ethereum_inicio_dolar = ethereum_dolar()
    xrp_inicio_real = xrp_real()
    xrp_inicio_dolar = xrp_dolar()
    nova_cotacao = True

    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +"\nInicializando o sistema..."+Style.RESET_ALL)
    print(45*"=")
    obter_hora()
    print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_inicio_real:.2f} \t$ {bitcoin_inicio_dolar:.2f}")
    print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_inicio_real:.2f} \t$ {ethereum_inicio_dolar:.2f}")
    print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_inicio_real:.2f} \t$ {xrp_inicio_dolar:.2f}")
    print(45*"=")

    print("\n"+Style.BRIGHT+"Aguardando uma nova cotação..."+Style.RESET_ALL)
    time.sleep(60)

    while True:
        bitcoin_atual_real = bitcoin_real()
        bitcoin_atual_dolar = bitcoin_dolar()
        ethereum_atual_real = ethereum_real()
        ethereum_atual_dolar = ethereum_dolar()
        xrp_atual_real = xrp_real()
        xrp_atual_dolar = xrp_dolar()

        if bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True            
            
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True 
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True 
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True 
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True 

        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True 
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real == xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real == xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real == xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real == xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True

        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True

        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real == xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real > ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.GREEN+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real == xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real == bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.LIGHTYELLOW_EX+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real < xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.RED+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real > bitcoin_inicio_real and ethereum_atual_real == ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.GREEN+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.LIGHTYELLOW_EX+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True
        
        elif bitcoin_atual_real < bitcoin_inicio_real and ethereum_atual_real < ethereum_inicio_real and xrp_atual_real > xrp_inicio_real:
            print(45*"=")
            obter_hora()
            print(Fore.RED+"BITCOIN "+Style.RESET_ALL + f"\tR$ {bitcoin_atual_real:.2f} \t$ {bitcoin_atual_dolar:.2f}")
            print(Fore.RED+"ETHEREUM "+Style.RESET_ALL + f"\tR$ {ethereum_atual_real:.2f} \t$ {ethereum_atual_dolar:.2f}")
            print(Fore.GREEN+"XRP "+Style.RESET_ALL + f"\t\tR$ {xrp_atual_real:.2f} \t$ {xrp_atual_dolar:.2f}")
            print(45*"=")
            nova_cotacao = True

        else:
            if nova_cotacao == True:
                print("\n"+Style.BRIGHT+"Aguardando uma nova cotação..."+Style.RESET_ALL)
                nova_cotacao = False
        
        print("\n"+Style.BRIGHT+"Aguardando uma nova cotação..."+Style.RESET_ALL)
        nova_cotacao = False
        bitcoin_inicio_real = bitcoin_atual_real
        bitcoin_inicio_dolar = bitcoin_atual_dolar
        ethereum_inicio_real = ethereum_atual_real
        ethereum_inicio_dolar = ethereum_atual_dolar
        xrp_inicio_real = xrp_atual_real
        xrp_inicio_dolar = xrp_atual_dolar

        time.sleep(60)

exibir_valores()
