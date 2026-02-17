n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

max_count = 0
eng_kop = numbers[0]

for i in numbers:
    count = 0
    for j in numbers:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        eng_kop = i

print(eng_kop)
