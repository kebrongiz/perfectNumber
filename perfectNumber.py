ef is_perfect_number(num):
    divisors = []
    div_sum = 0
    is_perfect = False

    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            divisors.append(str(i))
            div_sum += i

    if div_sum == num:
        is_perfect = True

    print(f"{num} is {'perfect' if is_perfect else 'not perfect'} and its divisors are {', '.join(divisors)}")


num = int(input("Enter a positive integer: "))

is_perfect_number(num)