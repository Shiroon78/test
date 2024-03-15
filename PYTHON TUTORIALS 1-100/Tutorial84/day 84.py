import time

# def uuw():
#     i = 0
#     while i<100:
#         i = i +1
#         print(i)

# def usingfor():
#     for i in range(100):
#         print(i)

# init = time.time()
# usingfor()
# t1 = time.time() - init
# init = time.time()
# uuw()
# print(time.time() - init)
# print(t1)

# print(4)       
# time.sleep(3)

# print("This is printed after 3 second")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M", t)

print(formatted_time)
