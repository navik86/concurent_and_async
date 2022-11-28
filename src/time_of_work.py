import time
from get_methods_from_url import get_methods
from async_func import get_methods_from_url


# One url
start_time = time.time()

get_methods('https://www.google.ru/')

end_time = time.time() - start_time

print(f"\nSingle url: {end_time} seconds")

# One url async
start_time = time.time()

get_methods_from_url('https://www.google.ru/')

end_time = time.time() - start_time
print(f"\nSingle url async: {end_time} seconds")

