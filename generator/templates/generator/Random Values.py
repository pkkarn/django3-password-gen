import random
import string
print(random.random())

print(random.randint(1, 1000))

print(random.choices([9, 8, 2, 1, 5, 3, 6, 7, 4]))

print("".join(random.choices(string.ascii_letters, k=6)))

numbers = [1,2,3,4]
random.shuffle(numbers)

print(numbers)
