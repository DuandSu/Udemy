user_age = int(input("Enter you age: "))
months = user_age * 12
days = user_age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Your are {user_age} years old which is approximately {months} months, which is also:")
print(f"----- Days: {days}")
print(f"----- Hours: {hours}")
print(f"----- Minutes: {minutes}")
print(f"----- Seconds: {seconds}")