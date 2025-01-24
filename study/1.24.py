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