from random import randint

nums = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(f'Os números sorteados foram:')
for num in nums:
    print(f'{num} ', end=' ')
print(f'\nO maior número foi: {max(nums)}')
print(f'O menor número foi: {min(nums)}')