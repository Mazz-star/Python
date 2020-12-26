hours = input("Enter Hours:")
rate = input("Enter Rate Per Hour:")
try:
    h = float(hours)
    r = float(rate)
except:
    print("Error, please enter numeric values")
    quit()

print("You have entered", "employee working hours = ", h, "and rate per hour =", r, "rupees")
if h>40:
    pay = (40*r) + (h-40)*(r*1.5)
    print("Amount to be paid is", pay, "rupees")

else:
    pay = h*r
    print("Amount to be paid is", pay, "rupees")