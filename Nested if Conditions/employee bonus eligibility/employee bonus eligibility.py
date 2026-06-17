experience = int(input("Enter Years of Experience: "))
rating = float(input("Enter Performance Rating: "))

if experience >= 5:
    if rating >= 8:
        print("Eligible for Bonus")
    else:
        print("Not Eligible: Performance Rating Too Low")
else:
    print("Not Eligible: Insufficient Experience")
