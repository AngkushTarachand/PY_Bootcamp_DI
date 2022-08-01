import time

before = time.time()
print("before,", before)
long_number = 1000**1000
after = time.time()

print(f"It took {after - before} seconds to execute 1000**1000")

print("before sleep 3 seconds")

time.sleep(3)

print("after sleep 3 second")


