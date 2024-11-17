
Prefix_Validation = ["024","025","053","054","055","059","027","057","026","056","020","050"]
while True:
    Phone_Number = input("Enter Phone Number: ")
    if len(Phone_Number) == 10 and Phone_Number.isdigit():
        prefix = Phone_Number[:3]
        if prefix in Prefix_Validation:
            print(f"{Phone_Number} is a Valid number")
            break
        else:
            print("Invalid Number")
    else:
        print("Phone Number must be 10 digits long and contain only digits")


