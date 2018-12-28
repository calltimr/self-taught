user_number=input("Enter a number: ")
try:
    int_user_number=int(float(user_number))
    print(int_user_number)
except ValueError:
    print("Must enter a number.")
