def twoSum(nums, target):
    num_to_index = {}  # 用于存储数字到索引的映射
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
twoSum([2, 7, 11, 15],26)
print(twoSum([2, 7, 11, 15],26))


squares = [x**2 for x in range(1, 11)]
print(squares)

squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)

class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person = Person("gss",25)

print(person.hello())

def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1,2,3,4]))

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

print(two_sum([2, 7, 11, 15],26))



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # 外层循环控制排序的轮数
        swapped = False  # 用于优化算法，如果某一轮没有发生交换，说明已经排序完成
        for j in range(0, n - i - 1):  # 内层循环控制每轮的比较和交换
            if arr[j] > arr[j + 1]:  # 比较相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换元素
                swapped = True  # 标记发生了交换
        if not swapped:  # 如果某一轮没有发生交换，提前结束排序
            break
    return arr

print(bubble_sort([11, 22, 3, 41, 52, 6, 71, 800, 9, 12]))



