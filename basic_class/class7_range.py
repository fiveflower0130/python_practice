import random

# data = []
# for i in range(10):
#     # data2 = []
#     # for j in range(5):
#     #     r = random.randint(0, 1)
#     #     data2.append(r)
#     data.append([random.randint(0, 1) for j in range(5)])
# print(data)
# data = [d for d in data if 0 not in d]
# print(len(data))
call_list = []
for i in range(5):
    call_level = random.randint(1, 3)
    call_list.append(call_level)
print(call_list)