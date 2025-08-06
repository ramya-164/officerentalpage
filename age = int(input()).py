age = int(input())
name=(input())
if age >= 18:
    print("You are eligible to vote.")
else:
    print(f'(name), wait for {18-age} year')