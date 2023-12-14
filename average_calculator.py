from colorama import Fore, Style
from time import sleep
import pyfiglet
import os

# Criando a saída de letra por letra
def letra_por_letra(frase):
    for x in frase:
        print (x, end='', flush=True)
        sleep(0.05)
    print ("\n")


# Criando o banner da ferramenta
def banner():
    ascii_banner = pyfiglet.figlet_format("Average Calculator")
    for x in ascii_banner:
        print (x, end='', flush=True)
        sleep(0.001)
    print ("\n")
banner()


# Incrementando cores
reset = Style.RESET_ALL
magenta = Fore.MAGENTA
red = Fore.RED
green = Fore.GREEN
black = Fore.BLACK
yellow = Fore.YELLOW


# Personalizando o shell do usuário  final
name = os.getenv("USER")
prop =  green + f"</[{name}]>" + reset


def calc_media():
    try:
        qnt_notas = int(input(f"{red}[+]{reset} - Quantas notas são?\n{prop}"))
        soma = 0

        for x in range(1, qnt_notas + 1):
            nota = float(input(f"{magenta}[+]{reset} - Nota {x}: "))
            soma += nota

        media = soma / qnt_notas
        print_media = f"{red}[+]{reset} - Sua média é: {media:.2f}"
        letra_por_letra(print_media)

    except Exception as err: # Interagindo com os erros de digitação
        os.system("clear")
        print (f"{red}[!]{reset} - Opção {yellow}{err}{reset} inválida")
        banner()
        calc_media()

    def retorno():
        try:
            r = str(input(f"{red}[*]{reset} - Deseja calcular mais alguma média? {magenta}[S/N]{reset}:\n{prop}"))
            if r.lower() == "s" or r.lower() == "sim":
                calc_media()
                retorno() 
            elif r.lower() == "n" or r.lower() == "não" or r.lower() == "nao":
                exit_program = f"{red}[*]{reset} - Ok, fechando programa..."
                letra_por_letra(exit_program)
                exit(0)
            else:
                print(f"{red}[*]{reset} - Opção {r} inválida.")
                retorno() 

        except Exception as err:
            print(f"{red}[!]{reset} - Ocorreu um erro: {yellow}{err}{reset}")
            exit(0)
    retorno()
calc_media()
