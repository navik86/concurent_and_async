import time
from get_methods_from_url import get_methods

urls2 = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]


start_time = time.time()
results2 = map(get_methods, urls2)
print(list(results2))

end_time = time.time() - start_time
print(f"\nExecution time: {end_time} seconds")