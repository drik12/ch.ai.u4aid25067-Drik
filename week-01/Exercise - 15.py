numbers = [12, 45, 3, 98, 7, 34, 21]

print("All numbers:")
for num in numbers:
    print(num)

print("\nNumbers greater than 30:")
count = 0
for num in numbers:
    if num > 30:
        print(num)
        count += 1

print("\nCount of numbers greater than 30:", count)