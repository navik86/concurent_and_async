import time
from async_func import get_methods_from_url
from multiprocessing import Pool

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]

pool = Pool(8)


start_time = time.time()
results = pool.map(get_methods_from_url, urls)


pool.close()
pool.join()

end_time = time.time() - start_time
print(f"\nExecution time: {end_time} seconds")