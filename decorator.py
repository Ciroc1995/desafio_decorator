from datetime import datetime

def meu_decorator(funcao):
    def wrapper():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return wrapper

@meu_decorator
def bater_ponto():
    print('Bateu ponto')


bater_ponto()
