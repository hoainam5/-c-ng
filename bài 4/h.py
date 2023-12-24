def is_perfect_number(number):
    if number <= 0:
        return False
    divisors = [i for i in range(1, int(number/2)+1) if number % i == 0]
    sum_of_divisors = sum(divisors)

    return sum_of_divisors == number

print(is_perfect_number(100))
n=100
m=n+100
while True:
    m+=1
    if is_perfect_number(m) and (m-n)>100:
        print(m)
        break 