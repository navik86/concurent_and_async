import time

from async_files.async_get_methods import get_methods_from_url
from sync_files.get_methods_from_url import get_methods

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

# Many urls async
start_time = time.time()

get_methods_from_url(urls)

end_time = time.time() - start_time
print(f"\nMany urls async: {end_time} seconds")