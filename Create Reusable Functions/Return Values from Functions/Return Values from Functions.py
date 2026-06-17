def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

interest = simple_interest(10000, 5, 2)

print("Simple Interest =", interest)
