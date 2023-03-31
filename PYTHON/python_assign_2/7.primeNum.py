nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

prime_nums = []

for number in nums:     #iterating each number
    if number > 1:
        is_prime = True     #initializing to true
        for i in range(2, number):
            if number % i == 0:   
                is_prime = False    # if condition is true then is_prime initilized to false
                break
        if is_prime:
            prime_nums.append(number)

print("Prime numbers:", prime_nums)
