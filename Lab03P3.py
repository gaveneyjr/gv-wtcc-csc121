#
# George Veney
# Sep 5 2026
# Bargain Shop Calculator
# This program will capture data entry errors and give the user a chance
# to reenter the data.
#
# Constants
BOOKS_PRICE = 3.25
DVD_PRICE = 4.5
GAMES_PRICE = 6.25
TAX = .07
#
# Inputs / Processing
# Books
books = int(input('Enter the number of books: '))
while books > 35 or books < 0:  # Verify number is between 0 and 35
    print(f'Number of books nust be between 0 and 35.')
    books = int(input('Enter the number of books: '))
else:
    book_total = books * BOOKS_PRICE

# DVDs
dvd = int(input('Enter the number of DVDs: '))
while dvd > 20 or dvd < 0:  # Verify the number is between 0 and 20
    print(f'Number of DVDs must be between 0 an 20.')
    dvd = int(input('Enter the number of DVDs: '))
else:
    dvd_total = dvd * DVD_PRICE

# Games
games = int(input('Enter the number of games: '))
while games > 15 or games < 0:  # Verify the number is between 0 and 15
    print(f'Number of games must be between 0 and 15.')
    games = int(input('Enter the number of games: '))
else:
    game_total = games * GAMES_PRICE

# Calculate totals
subtotal = book_total + dvd_total + game_total  # Calculate the total of books, dvds, and games
total_tax = subtotal * TAX  # Calculate the tax from the totals of the books, dvds, and games
cost_after_tax = subtotal + total_tax  # Calculate the total plus tax of the books, dvds, and games
# Outputs
# Print totals
print(f'Cost before tax: ${subtotal:.2f}')
print(f'Sales tax: ${total_tax:.2f}')
print(f'Cost after tax: ${cost_after_tax:.2f}')
