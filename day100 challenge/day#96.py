 
import asyncio
import requests

async def function1():
   
    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


    response = requests.get(url)
    file_Path = 'research_Paper_1.pdf'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')
    else:
        print('Failed to download file')

    print('funct 1')
    
async def function2():
   
    url = 'https://sl.bing.net/iE4SmRXyr9g.jpg'


    response = requests.get(url)
    file_Path = 'research_Paper_1.pdf'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')
    else:
        print('Failed to download file')

    print('funct 2')
    
async def function3():

    url = 'https://media.geeksforgeeks.org/wp-content/uploads/20240226121023/GFG.pdf'


    response = requests.get(url)
    file_Path = 'research_Paper_1.pdf'

    if response.status_code == 200:
        with open(file_Path, 'wb') as file:
            file.write(response.content)
        print('File downloaded successfully')
    else:
        print('Failed to download file')

    print('funct 3')
    
async def main():
    l= await asyncio.gather(function1(),function2(),function3())
    #task = asyncio.create_task(function1())
    #await function1()
    #await function2()
   # await function3()
    print(l)
#asyncio.run(main())