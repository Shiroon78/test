import time 
import asyncio
import requests

async def funtion1():
    url = 'https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg'
    r = requests.get(url, allow_redirects=True)
    open('gogo.jpg', 'wb').write(r.content)
    print("Done!")
    return "Lica"
async def funtion2():
    url = 'https://t4.ftcdn.net/jpg/05/25/08/09/360_F_525080936_JEpnKXh2siYKBPpsqd98pbbcIzy4ySKz.jpg'
    r = requests.get(url, allow_redirects=True)
    open('gogo2.jpg', 'wb').write(r.content)
    print("Done!")
async def funtion3():
    url = 'https://t3.ftcdn.net/jpg/05/71/06/76/360_F_571067620_JS5T5TkDtu3gf8Wqm78KoJRF1vobPvo6.jpg'
    r = requests.get(url, allow_redirects=True)
    open('gogo3.jpg', 'wb').write(r.content)
    print("Done!")
async def main():
        await funtion2()
        await funtion3()
        await funtion1()
        return 3
    # L = await asyncio.gather(
    #     funtion2(),
    #     funtion3(),
    #     funtion1(),
    # )
    # print(L)
asyncio.run(main())            