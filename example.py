import time


def cozinhar_macarrao():
    start = time.time()
    print('cozinhando macarrão...')
    time.sleep(10)
    end = time.time()
    print(f'macarrao demorou {end-start} minutos para cozinhar!')


def descascar_tomate():
    start = time.time()
    print('descascando tomate...')
    time.sleep(3)
    end = time.time()
    print(f'tomate demorou {end-start} minutos para descascar!')


def cozinhar_ovo():
    start = time.time()
    print('cozinhando ovo...')
    time.sleep(5)
    end = time.time()
    print(f'ovo demorou {end-start} minutos para cozinhar!')


def preparar_almoco():
    print('preparando almoço...')
    start = time.time()
    cozinhar_macarrao()
    cozinhar_ovo()
    descascar_tomate()
    end = time.time()
    print(f'almoço demorou {end-start} minutos para fazer!')


preparar_almoco()
