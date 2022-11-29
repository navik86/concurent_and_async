import time

from async_files.async_get_methods import get_methods_from_url
from sync_files.get_methods_from_url import get_methods

# One url sync
start_time = time.time()

get_methods('https://www.google.ru/')

end_time = time.time() - start_time

print(f"\nOne url sync: {end_time} seconds")

# One url async
start_time = time.time()

get_methods_from_url(['https://www.google.ru/'])

end_time = time.time() - start_time
print(f"\nOne url async: {end_time} seconds")

