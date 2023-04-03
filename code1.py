# Membuat list baru yang berisi nilai yang dikuadratkan dari list asal
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# Mengambil jumlah total dari list
total = 0
for num in numbers:
    total += num
    
print(total) # Output: 15
