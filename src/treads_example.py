import time
from sync_files import get_methods_from_url as gmfu
from multiprocessing.dummy import Pool as ThreadPool

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

# Make the Pool of workers
pool = ThreadPool(8)

# Open the URLs in their own threads
# and return the results
start_time = time.time()

results = pool.map(gmfu, urls)

# Close the pool and wait for the work to finish
pool.close()
pool.join()

end_time = time.time() - start_time
print(f"\nTreads: {end_time} seconds")