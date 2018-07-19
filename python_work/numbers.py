numbers=list(range(1,10))
for number in numbers:
    print(number)

numbers2=list(range(1,1000001))
print(min(numbers2))
print(max(numbers2))
print(sum(numbers2))

odd_number=list(range(1,21,2))
for number in odd_number:
    print(number)

numbers3=list(range(3,31,3))
for number in numbers3:
    print(number)

big_number=list(three**3 for three in range(1,11))
print(big_number)