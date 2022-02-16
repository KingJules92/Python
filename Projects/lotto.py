import random

# Westlotto

# Generate List
all_westlotto = []
all_westlotto.extend(range(1,50))

my_westlotto = random.sample(all_westlotto, 6)
my_westlotto.sort()
print(my_westlotto)

# Eurolotto

# Generate List
all_eurolotto = []
all_eurolotto.extend(range(1,51))

bonus_eurolotto = []
bonus_eurolotto.extend(range(1,11))

my_eurolotto = random.sample(all_eurolotto, 5)
my_eurolotto.sort()
print(my_eurolotto)

my_bonus = random.sample(bonus_eurolotto, 2)
my_bonus.sort
print(my_bonus)