numbers = int(input("Enter up to 6 numbers. USE SPACES!: "))
numbers = list(numbers)
print(numbers)


def largest(numbers, length):
  max = numbers[0]
  for i in range(1, length):
    if numbers[i] > max:
      max = numbers[i]
  return max

def smallest(numbers, length):
  min = numbers[0]
  for i in range(1, length):
    if numbers[i] < min:
      min = numbers[i]
  return min

length = len(numbers)
max_num = largest(numbers, length)
min_num = smallest(numbers, length)
print("The largest number in the list of numbers: ", numbers, "is ", max_num, ", and the smallest number is ", min_num)

