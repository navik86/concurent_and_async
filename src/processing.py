import time
from get_methods_from_url import get_methods
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

# Make the Pool of workers
pool = Pool(8)

# Open the URLs in their own threads
# and return the results
start_time = time.time()
results = pool.map(get_methods, urls)
print(results)
# Close the pool and wait for the work to finish
pool.close()
pool.join()

end_time = time.time() - start_time
print(f"\nExecution time: {end_time} seconds")