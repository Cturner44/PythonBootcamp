print("How many ounces of water did you drink today?")
ounces = input()
gallons = float(ounces)/128
roundedgallons = round(gallons, 2)
print(f"Great! Your {ounces} ounces is actually {roundedgallons} gallons. Stay hydrated!")