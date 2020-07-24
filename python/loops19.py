# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    print(f"number={number}; number%2={number % 2}")
    if number%2 == 0:
        evens.append(number)

print(f"Even Numbers = {evens}")


# -- Part 2, must be completed before submitting! --
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")