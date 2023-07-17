# # # Среднее значение, медиана и мода
# # a = [5, 5, 5, 5, 1, 5, 5, 5, 5]
# #
# # # Определение средне арифметического значения массива
# # def mean(a):
# #     return sum(a) / len(a) # 45 / 9 = 5
# #
# # # Определение центра в отсортированном массиве
# # def median(a):
# #     a = sorted(a)
# #
# #     if not len(a):
# #         return None
# #
# #     if len(a) == 1:
# #         return a[0]
# #
# #     if len(a) % 2 == 0:
# #         return (a[len(a) // 2 + 1] + a[len(a) // 2]) / 2
# #     else:
# #         return a[len(a) // 2]
# #
# # # Определение самого часто встречаемого элемента в массиве (Выборке)
# # def moda(a): # (NLog(N))
# #     counter = {} # key = numbers, value = frequency
# #
# #     for i in range(len(a)): # O(N)
# #         if a[i] in counter: # O(logN)
# #             counter[a[i]] += 1
# #         else:
# #             counter[a[i]] = 1
# #
# #     return (max(counter.values())) # O(N)
# #
# # # print(moda(a))
# #
# # b = [0, 0, 0, 0, 0]
# # c = [-2, -1, 0, 1, 2]
# #
# # # print("Mean: ", mean(b), " Median: ", median(b))
# # # print("Mean: ", mean(c), " Median: ", median(c))
# #
# # def deviation(arr):
# #     arrMean = mean(arr)
# #
# #     sumOfDifferences = 0
# #     for i in arr:
# #         sumOfDifferences += (i - arrMean) ** 2
# #
# #     sumOfDifferences /= (len(arr) - 1)
# #
# #     return (sumOfDifferences) ** 0.5
# #
# # # print("Deviation: ", deviation(b))
# # # print("Deviation: ", deviation(c))
# #
# #
# # a = [0, 1, 2, 3]
# #
# # b = [100000, 200000, 300000, 400000]
# # c = [10, 11, 12, 13]
# # d = [3, 0, 2, 1]
# #
# # cntOfCigarretesPerDay = [0, 1, 5, 100]
# # lifetime = [80, 78, 60, 0]
# #
# # def coefCorr(a, b):
# #     sum = 0
# #     n = len(a)
# #     for i, j in zip(a, b):
# #         sum += i * j
# #
# #     sum -= n * mean(a) * mean(b)
# #
# #     sum /= (n - 1) * deviation(a) * deviation(b)
# #
# #
# # # coefCorre e [-1: 1]
# #
# # # coefCorr(cntOfCigarretesPerDay, lifetime) # -0.9802915968005523
# # # coefCorr(a, b) # 0.9999999999999998
# # # coefCorr(a, d) # -0.4
# #
# # # sort
# #
# # # bubble sort O(N^2)
# #
# # # merge sort O(NLog(N))
# #
# # # counting sort time complexity O(N) space complexity O(max(A[i]))
# # arr = [4, 63, 7, 38, 24, 79, 50, 74, 45, 56, 5, 100, 58, 71, 29, 20, 52, 42, 67, 47]
# #
# # # [10000000000000000]
# # # 0: 0
# # # 1: 1
# # # 2: 0
# # # 3: 2
# # # 4: 1
# # # ...
# # # 10: 1
# # # 1 3 3 4 10
# #
# # def countingSort(arr):
# #     counter = [0] * 1000
# #
# #     for i in range(len(arr)):
# #         counter[arr[i]] += 1
# #
# #     resArray = []
# #     for i in range(len(counter)):
# #         if counter[i] != 0:
# #             resArray += [i] * counter[i]
# #
# #     return resArray
# # # print("Array: ", arr)
# # # print("Sorted by counting array: ", countingSort(arr))
# #
# # arr = [4, 63, 7, 38, 24, 79, 50, 74, 45, 56, 5, 100, 58, 71, 29, 20, 52, 42, 67, 47]
# #
# # # 42, 67, 47
# #
# # # 20, 52,
# # # 5, 100, 58, 71, 29,
# # # 4, 63, 7, 38, 24, 79, 50, 74, 45, 56,
# #
# #
# # a = [1, 3]
# # b = [2, 4]
# #
# # c = [1, 2, 3, 4]
#
#
# # 1 3 5 7 9 10 12
# # 2
# a = [1, 3, 5, 7, 9, 10, 12]
# b = [2]
# #
#
#
# def merge(a, b):
#     i, j = 0, 0
#
#     resArray = []
#
#     while i != len(a) and j != len(b):
#         # print(resArray)
#         if a[i] > b[j]:
#             resArray.append(b[j])
#             j+=1
#         else:
#             resArray.append(a[i])
#             i+=1
#
#     if i != len(a):
#         resArray += (a[i:])
#     if j != len(b):
#         resArray += (b[j:])
#     return resArray
#
# print(merge(a, b)) # 1, 2, 3

# number = 2023
# rom_numbers = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
# num = [1000, 900, 500, 400, 100, 90,50, 40, 10, 9, 5, 4, 1]
#
# rom = ""
# while number > 0:
#     for i in range(len(rom_numbers)):
#         if number >= num[i]:
#             number -= num[i]
#             rom += rom_numbers[i]
#             break
# print(rom)


# def number_roman(number):
#
#     rom_num = {"M": 1000,
#                "CM": 900,
#                "D": 500,
#                "CD": 400,
#                "C": 100,
#                "XC": 90,
#                "L": 50,
#                "XL": 40,
#                "X": 10,
#                "IX": 9,
#                "V": 5,
#                "IV": 4,
#                "I": 1
#                }
#     rom = ""
#     while number > 0:
#         for i in rom_num.items():
#             if number >= i[1]:
#                 number -= i[1]
#                 rom += i[0]
#                 break
#     return(rom)


# def number_roman(number):
#
#     rom_num = {"M": 1000,
#                "D": 500,
#                "C": 100,
#                "L": 50,
#                "X": 10,
#                "V": 5,
#                "I": 1
#                }
#     rom = ""
#     while number > 0:
#         for i in rom_num.items():
#             if number >= i[1]:
#                 number -= i[1]
#                 rom += i[0]
#                 break
#     return(rom)


#
# var_name = "False"
# # son -> int ex: 5
# # matn -> str ex: "abc"
# # mantiqiy -> bool ex: True | False
# # kaslik -> float ex: 5.5
#
# print(type(var_name))


# Sikl for | while for - ma'lumotlar to'plami bo'yicha ishliydi | while - nomalum malutla bo'yicha

# for i in range(5): #(0,1,2,3,4)
#     print(i)

# my_tuple = (1,2,3,4,5,6,7,8,9)
# iter = 0
# while iter < len(my_tuple):
#     print(my_tuple[iter])
#     iter += 1

# def Behruz(nbr1, nbr2, nbr3 = 5):
#     return nbr1 + nbr2 + nbr3
#
#
# print(Behruz(5,7))
#
# print(Behruz(10,7, 3))
# print(Behruz(5,8))
# print(Behruz(9,7))

# my_list = ["Behruz", "Damir", "Abdulaziz"]
# my_list.append("Firdavs")
# my_list[0] = "Soatov"
# # my_list.remove("Abdulaziz")
# print(my_list)

# my_tuple = ("142", 53, 373, 3476, 347, ("strh",464))
# print(my_tuple)


# my_dict = {
#     # key : value
#     "Behruz": 18,
#     "Damir": 15,
#     "Abdulaziz": 19
# }
#
# print(my_dict)



# my_set = {1,"wgwq","GERg",1}
# print(my_set)


# Exx 1


#a = 20
#b = 30
#print(a*b)

#a = 30
#b = 40
#print(a+b)
# a = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# b = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# for i in range(0, 10):
#     print(f (a + b) {i})


# def merge_sorted_arrays(arr1, arr2):
#
#     merged_arr = []
#
#     i = 0
#     j = 0
#
#     while i < len(arr1) and j < len(arr2):
#
#         if arr1[i] <= arr2[j]:
#
#             merged_arr.append(arr1[i])
#             i += 1
#         else:
#
#             merged_arr.append(arr2[j])
#             j += 1
#
#     while i < len(arr1):
#         merged_arr.append(arr1[i])
#         i += 1
#     while j < len(arr2):
#         merged_arr.append(arr2[j])
#         j += 1
#     return merged_arr
#
#
# arr1 = [1, 3, 5, 7, 9, 120, 120, 120]
# arr2 = [2, 4, 6, 8, 10, 25, 120, 120]
# merged_arr = merge_sorted_arrays(arr1, arr2)
# print(merged_arr)




# lst=[]
# while True:
#     user_number = int(input("enter the number: "))
#     lst.append(user_number)
#     user_input =input("do you wnt to add another number. If you don't write no: ")
#     if user_input.lower()== "no":
#         break
#
# new_list = sorted(lst)
# # print(new_list[-3])
# for i in range(1, len(new_list)+1):
#     print(new_list[-i])
#




# user_input = input("Sonlar to'plamini kriting: ")
# sonlar_toplami = user_input.split(" ")
# my_uniq_lst = set(sonlar_toplami)
# print(my_uniq_lst)



def my_adder(*args, **kwargs):
    sum_all = 0
    if len(args) != 0:
        for i in args:
            sum_all += i

    if len(kwargs) != 0:
        for j in kwargs.values():
            sum_all += j
    return sum_all

print(my_adder(1,2, fstn = 1, stn = 2))



















