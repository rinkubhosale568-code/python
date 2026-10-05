age = int(input("Enter your age: "))

if age < 0 or age > 100:
    print("Invalid Age")

elif age >= 18:
    print("Valid Age")
    print("Eligible for Voting")

else:
    print("Valid Age")
    print("Not Eligible for Voting")