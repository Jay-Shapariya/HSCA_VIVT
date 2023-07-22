# Virtually Indexed Virtually Tagged Memory Project

This is a Python project that implements a Virtually Indexed Virtually Tagged (VIVT) cache. The VIVT cache is a type of cache memory where the virtual address is used as an index to access cache lines, and the virtual address is also used as a tag to identify the data stored in the cache.

## Description

The project consists of a Python script that simulates a VIVT cache and main memory interaction. The cache lookup function is implemented to handle cache hits and misses, as well as eviction and replacement of cache lines when the cache is full. The LRU (Least Recently Used) algorithm is used to track the cache line usage and decide which cache line to replace on a cache miss.

## How to use

1. Input the cache size and block size in bytes when prompted. The cache size and block size will determine the number of cache blocks in the cache.

2. Test the cache lookup function with sample virtual addresses and operations (read or write). The program will output the data retrieved from the cache, the number of cache hits, and the number of cache misses.

3. You can continue testing the cache by entering new virtual addresses and operations. The program will display the cache contents after each access.

4. To exit the program, type "no" when prompted if you want to continue testing.

## Cache Contents

After each cache access, the program will display the contents of the cache. For each block in the cache, the following information will be shown:

Block index: The index of the cache block.
Tag: The tag associated with the data in the cache block.
Data: The data stored in the cache block.
Dirty bit: Indicates if the cache block has been modified (True) or not (False).
LRU counter: The LRU counter value for the cache block, used in the replacement algorithm.

## Note

This project is a simulation of a VIVT cache and is intended for educational purposes. The implementation may not be optimized for real-world use and may not handle all corner cases. It assumes the main memory data is represented as a string in hexadecimal format ('0x' + hex_data). For optimize use run code on Google Colab.
