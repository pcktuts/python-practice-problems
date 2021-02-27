#Sum of Integers Up To n 
'''
num_sum(3) = 1 + 2 + 3 = 6
num_sum(5) = 1 + 2 + 3 + 4 + 5 = 15
'''
def num_sum(n):
    sum = 0
    current_number = 1
    while current_number < n + 1:
        sum = sum + current_number
        current_number = current_number + 1
    return sum 

print(num_sum(3))
print(num_sum(5))
