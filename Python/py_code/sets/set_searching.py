import time

list_1million=list(range(1000000))
set_1million=set(list_1million)
target=199_199

time_start=time.time()

if target in list_1million:
    print("yes")

time_end=time.time()
print(time_end-time_start)

time_start=time.time()

if target in set_1million:
    print("yes")

time_end=time.time()
print(time_end-time_start)