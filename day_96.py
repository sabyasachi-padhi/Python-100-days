#in day 96 we are going to learn about ASYNCIO in python.....
#async io is used in python for doing powerfull io opretion.... 
import asyncio
import requests


async def function_1():
  URL = "https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram1.ico", "wb").write(response.content)
  print("function 1")


async def function_2():
  URL = "https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram2.ico", "wb").write(response.content)
  print("function 2")


async def function_3():
  URL = "https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)
  print("function 3")


async def main():

  #but it is not an organisized way..
  # task = asyncio.create_task(function_1())

  # await function_2()
  # await function_3()

  L = await asyncio.gather(function_1(), function_2(), function_3())

  print(L)


asyncio.run(main())
