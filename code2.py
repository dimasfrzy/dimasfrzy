# Membuat class ListManipulator
class ListManipulator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    # Method untuk membuat list baru yang berisi nilai yang dikuadratkan dari list asal
    def square_numbers(self):
        return [num ** 2 for num in self.numbers]
    
    # Method untuk mengambil jumlah total dari list
    def get_total(self):
        return sum(self.numbers)

# Membuat instance dari class ListManipulator
list_manipulator = ListManipulator([1, 2, 3, 4, 5])

print(list_manipulator.square_numbers()) # Output: [1, 4, 9, 16, 25]
print(list_manipulator.get_total()) # Output: 15
