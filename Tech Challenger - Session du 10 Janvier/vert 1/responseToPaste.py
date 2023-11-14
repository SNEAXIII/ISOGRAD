
result = int(input())

for _ in range(4):
    if result % 3 == 0:
        result //= 3
    elif result % 2 == 0:
        result //= 2
    else: result -= 1

print(result)
