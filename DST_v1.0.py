print(" ____________________________________________")
print("|                                            |")
print("|  Application: DST (Distance, Speed, Time)  |")
print("|  Version: 1.0                              |")
print("|____________________________________________|")

print()

print("1. Distance = Speed * Time\n2. Speed = Distance / Time\n3. Time = Distance / Speed")

print()

Option = int(input("Option >>> "))

print()

if Option == 1:
    Speed = float(input("Speed (KM/Hour): ")) # Input
    Time = float(input("Time (Hour): ")) # Input
    Distance = Speed * Time # Formula
    Unit = ["KM", "M"] # Unit
    print(f"\nDistance: {Distance} {Unit[0]}") # Output
elif Option == 2:
    Distance = float(input("Distance (KM): ")) # Input
    Time = float(input("Time (Hour): ")) # Input
    Speed = Distance / Time # Formula
    Unit = ["KM/Hour", "M/Second"] # Unit
    print(f"\nSpeed: {Speed} {Unit[0]}") # Output
elif Option == 3:
    Distance = float(input("Distance (KM): ")) # Input
    Speed = float(input("Speed (KM/Hour): ")) # Input
    Time = Distance / Speed # Formula
    Unit = ["Hour", "Minute"] # Unit
    print(f"\nTime: {Time} {Unit[0]}") # Output
else:
    print("Invalid Option!")

print()