# -*- coding: utf-8 -*-
"""VIVT_Group 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16bMPYi8UPEUeq2_Dt_6ZP9j5vg6g95wE
"""

# Initialize the cache as a dictionary of cache lines
cache = {}
cache_size = int(input("Enter cache size in bytes: "))
block_size = int(input("Enter block size in bytes: "))
num_blocks = cache_size // block_size

# Initialize the LRU counter and the cache hit/miss counters
lru_counter = 0
cache_hits = 0
cache_misses = 0

# Define the cache lookup function
def cache_lookup(virtual_address, operation):
    global lru_counter, cache_hits, cache_misses, cache

    # Extract the tag and index from the virtual address
    tag = virtual_address // cache_size
    index = (virtual_address % cache_size) // block_size

    # Check if the cache line is present in the cache
    if index in cache and cache[index]['tag'] == tag:
        # Increment the LRU counter for all cache lines with a lower counter value
        for i in cache:
            if cache[i]['lru'] < cache[index]['lru']:
                cache[i]['lru'] += 1
        # Reset the LRU counter for the hit cache line
        cache[index]['lru'] = 0
        # Update the dirty bit if the operation is a write
        if operation == 'write':
            cache[index]['dirty'] = True
        # Increment the cache hit counter and return the data
        cache_hits += 1
        return cache[index]['data']
    else:
        # Increment the LRU counter for all cache lines
        for i in cache:
            cache[i]['lru'] += 1
        # Check if the cache is full
        if len(cache) < num_blocks:
            # Insert the new cache line
            cache[index] = {'tag': tag, 'data': '0x' + hex(virtual_address)[2:].zfill(8), 'dirty': False, 'lru': 0}
        else:
            # Find the LRU cache line and replace it
            max_lru = max([cache[i]['lru'] for i in cache])
            for i in cache:
                if cache[i]['lru'] == max_lru:
                    # Update the main memory if the cache line is dirty
                    if cache[i]['dirty']:
                        main_memory_address = cache[i]['tag'] * cache_size + i * block_size
                        main_memory_data = cache[i]['data']
                        print(f"Updating main memory at 0x{hex(main_memory_address)[2:].zfill(8)} with data {main_memory_data}")
                    # Replace the cache line
                    cache[i] = {'tag': tag, 'data': '0x' + hex(virtual_address)[2:].zfill(8), 'dirty': False, 'lru': 0}
                    break
        # Update the dirty bit if the operation is a write
        if operation == 'write':
            cache[index]['dirty'] = True
        # Increment the cache miss counter and return the data
        cache_misses += 1
        return '0x' + hex(virtual_address)[2:].zfill(8)

# Test the cache lookup function with sample virtual addresses
virtual_address = int(input("Enter virtual address: "), 16)
operation = input("Enter operation (read or write): ")
data = cache_lookup(virtual_address, operation)
print(f"Data: {data}")
print(f"Cache hits: {cache_hits}")
print(f"Cache misses: {cache_misses}")

while True:
  virtual_address = int(input("Enter virtual address (in hex): "), 16)
  operation = input("Enter operation (read/write): ")
  # Perform the cache lookup
  data = cache_lookup(virtual_address, operation)

  # Print the results
  print(f"Virtual address: 0x{hex(virtual_address)[2:].zfill(8)}")
  print(f"Operation: {operation}")
  print(f"Data: {data}")
  print(f"Cache hits: {cache_hits}")
  print(f"Cache misses: {cache_misses}")
  print("Cache contents:")
  for i in range(num_blocks):
      if i in cache:
          print(f"Block {i}: tag={cache[i]['tag']}, data={cache[i]['data']}, dirty={cache[i]['dirty']}, LRU={cache[i]['lru']}")
      else:
          print(f"Block {i}: empty")
  print()

  # Ask the user if they want to continue
  choice = input("Do you want to continue (yes/no)? ")
  if choice.lower() != "yes":
      break
  print("Exiting the program...")