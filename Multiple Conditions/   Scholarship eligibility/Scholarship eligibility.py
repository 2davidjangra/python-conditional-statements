marks = float(input("Enter Marks: "))
sports = input("Do you have a Sports Certificate (yes/no)? ")

if marks >= 85 or sports == "yes":
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")
