marks = float(input("Enter Marks: "))
age = int(input("Enter Age: "))

if marks >= 60:
    if age >= 17:
        print("Eligible for College Admission")
    else:
        print("Not Eligible: Age Requirement Not Met")
else:
    print("Not Eligible: Marks Requirement Not Met")
