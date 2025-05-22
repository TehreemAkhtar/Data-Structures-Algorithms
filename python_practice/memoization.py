
cache = {}
def memoize(a, b):
    if (a, b) in cache:
        print('Cached result')
        return cache[(a, b)]
    sum = a + b
    cache[(a, b)] = sum
    return sum



print(memoize(1, 2))
print(memoize(1, 2))
print(memoize(1, 2))
print(memoize(1, 2))
print(memoize(1, 2))



import time
import threading
from functools import wraps

def memoize_with_ttl(ttl=300, cleanup_interval=60):
    cache = {}

    def cleanup():
        while True:
            now = time.time()
            keys_to_delete = [k for k, (_, ts) in cache.items() if now - ts > ttl]
            for k in keys_to_delete:
                del cache[k]
            time.sleep(cleanup_interval)

    # Start a background thread to clean the cache
    threading.Thread(target=cleanup, daemon=True).start()

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            now = time.time()
            key = args
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl:
                    print("Returning cached result")
                    return result
            result = func(*args)
            cache[key] = (result, now)
            return result
        return wrapper

    return decorator
