#list itterable[2, 3, 4, 5]

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total    
        
#tuple are itterable
print(multiply(2, 3, 4, 5))