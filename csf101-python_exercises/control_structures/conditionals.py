number = 10
if number > 0:
    print("the number is positive.")
else:
    print("the number is non-positive.")

number = 0
if number > 0:
    print("the number is positive.")
elif number < 0:
    print("the number is negative.")
else:
    print("the number is zero.")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"your grade is: {grade}")

number = 7
result = "even" if number % 2 == 0 else "odd"
print(f"The number is {result}.")

num1 = 10
num2 = 20
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Erroe: Invalid operator"

print(f"Result: {result}")   
