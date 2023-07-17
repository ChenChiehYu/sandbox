MIN_LEN = 5
input_password = input("Enter your password: ")
while len(input_password)<MIN_LEN:
    print("Invalid length")
    input_password = input("Enter your password: ")
print(len(input_password)*"*")