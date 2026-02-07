# TypeError
# len(12345)

# No TypeError
len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Casting
print(int("123") + int("345"))

str()
int()
float()
bool()

# My answer
# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

name_of_user = input("Enter your name: ")
length_of_name = len(name_of_user)

print("Number of letters in your name: " + str(length_of_name))