import functools
import time 

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print('done for 20')
print(fx(5))
print('done fo 5')

print(fx(20))
print('done for 20')
print(fx(5))
print('done fo 5')