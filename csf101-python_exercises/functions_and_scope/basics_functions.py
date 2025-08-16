def greet():
    print(f"hello< world!")

greet()

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(7))

def print_number(n):
    for i in range(1, n + 1):
        print(i)

print_number(5)