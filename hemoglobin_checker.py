hemoglobin = float(input("Enter hemoglobin level (g/dL): "))

if hemoglobin < 12:
    print("Low hemoglobin - Anemia suspected")
elif hemoglobin >= 12 and hemoglobin <= 17:
    print("Hemoglobin within normal range")
else:
    print("High hemoglobin - Review patient")
