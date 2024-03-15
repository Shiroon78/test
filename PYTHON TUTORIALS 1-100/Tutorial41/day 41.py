marks = [12,45,67,87,45,567,11,34,98]

# index = 0
# for mark in marks:
#     print(mark)
#     if index == 3:
#         print("Shiro Lica")
#     index +=1

for index, mark in enumerate(marks, start=1):
    print(mark)
    if index ==  3:
        print("lica")