import asyncio
from jikan4snek import Jikan4SNEK, dump

async def main():
    jikan = Jikan4SNEK()
    anime = await jikan.get(36896).anime()
    user = await jikan.search()
    #user = await jikan.get(123123).users()
    #print(anime) ## this is <class 'dict'>
    print(dump(user)) ## this is <class 'str'>

asyncio.run(main())