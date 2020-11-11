"""
Обратный порядок введённых чисел
"""
nums = []
for i in range(int(input("Введите количество чисел:"))):
    nums.append(int(input("Введите числа:")))
print(list(reversed(sorted(nums))))