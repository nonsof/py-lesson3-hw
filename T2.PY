# Требуется найти в массиве list_1 самый близкий по величине 
# элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5,] 
k = -1
# for i in list_1: 
#     if i < k: 
#         nearest_num = -k 
#     else: 
#         nearest_num = nearest_num + 0 
#     if i >= k and i - k <= nearest_num - k: 
#         nearest_num = i 
#     elif i <= k and nearest_num - k <= i - k: 
#         nearest_num = i 
# print(nearest_num)

b = [abs(list_1[i]-k) 
   for i in range(len(list_1))]
print(list_1[b.index(min(b))])

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)