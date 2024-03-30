from functools import *
@lru_cache()
def f(n):
    if n >= 2024:
        return 1
    if n < 2024:
        return f(n+2) + f(n+4)

print(f(1300))