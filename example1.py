import time
import asyncio


async def cozinhar_macarrao():
    start = time.time()
    print('cozinhando macarrão...')
    await asyncio.sleep(10)
    end = time.time()
    print(f'macarrao demorou {end-start} minutos para cozinhar!')


async def descascar_tomate():
    start = time.time()
    print('descascando tomate...')
    time.sleep(3)
    end = time.time()
    print(f'tomate demorou {end-start} minutos para descascar!')


async def cozinhar_ovo():
    start = time.time()
    print('cozinhando ovo...')
    await asyncio.sleep(5)
    end = time.time()
    print(f'ovo demorou {end-start} minutos para cozinhar!')


async def preparar_almoco():
    print('preparando almoço...')
    start = time.time()
    await asyncio.gather(
        cozinhar_macarrao(),
        cozinhar_ovo(),
        descascar_tomate(),
    )
    end = time.time()
    print(f'almoço demorou {end-start} minutos para finalizar!')


asyncio.run(preparar_almoco())
