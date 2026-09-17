import multiprocessing
import requests

def downloadfile(url,name):
    print('started downloading {name}')
    response = requests.get(url)
    open(f'files/file{name}.jpg','wb').write(response.content)
    print(f'finished downloading {name}')
    
url= 'https://picsum.photos/200/300'
pros=[]
for i in range(5):
    # downloadfile(url,i)
    
    
    p=multiprocessing.Process(target=downloadfile, args=[url,i])

    p.start()
    pros.append(p)
    
for p in pros:
    p.join()
        