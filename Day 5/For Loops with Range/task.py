# Range function with For loop

# Prints with a gap of 3 numbers, eg: 1,4,7,10
# for number in range(1, 11, 3):
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)


# Answer for the quiz
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)