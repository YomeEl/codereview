def count_numbers(K, N):
   def is_valid(number):
       return '0000' not in number

   count = 0
   for num in range(K**N):
       number = format(num, f'0{N}b')
       if is_valid(number):
           count += 1
   return count

# Example usage
K = 3  # base
N = 5  # number of digits
result = count_numbers(K, N)
print(result)
