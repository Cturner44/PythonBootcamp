print("How many kilometers did you cycle today?")

kms = input()
miles = float(kms)/1.60934
roundedmiles = round(miles, 2)
print(f"Wow! That is equal to {roundedmiles} miles!")