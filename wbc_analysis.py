wbc_counts = [4.5, 6.2, 3.8, 7.1, 5.5]
total = 0

for count in wbc_counts:
    if count >= 5:
        total = total + count

print("Total of high WBC counts:", total)
