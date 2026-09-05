#
# George Veney
# Sep 5 2026
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Display the inventory stock table.
for month in range(3):
    books = books + 45
    dvds = dvds + 32
    games = games + 15
    print(f'Month {month + 1}')
    print(f'\tBooks: {books}')
    print(f'\t DVDs: {dvds}')
    print(f'\tGames: {games}')

