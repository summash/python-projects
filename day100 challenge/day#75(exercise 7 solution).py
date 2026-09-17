import os
i=1

files = os.listdir('clutter')
for file in files:
    if file.endswith('.txt'):
        print(file)
        os.rename(f'clutter/{file}',f'clutter/{i}.txt')
        i=i+1
        
    

