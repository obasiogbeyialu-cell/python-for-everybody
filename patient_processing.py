patients = int(input("How many patients today? "))
count = 1

while count <= patients:
    name = input("Enter patient name: ")
    print("Processing patient", count, ":", name)
    count = count + 1

print("All", patients, "patients processed for today")
