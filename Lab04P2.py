##
# Student Name - George Veney
# Date - Sep 11 2026
# Trish's Swap Shop Calculator
#
# Global Constants
BOOK_PRICE = 3.25
DVD_PRICE = 4.50
GAME_PRICE = 6.25
TAX_RATE = 0.07  # Tax Rate of 7%


def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_books = int(input('Enter the number of books: '))
    num_dvds = int(input('Enter the number of DVDs: '))
    num_games = int(input('Enter the number of games: '))

    calc_and_display_total(num_books, num_dvds, num_games)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    books  - Number of books
#    dvds  - Number of dvds
#    games  - Number of games
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.


def calc_and_display_total(books, dvds, games):
    books_total = books * BOOK_PRICE
    dvds_total = dvds * DVD_PRICE
    games_total = games * GAME_PRICE
    tax = (books_total + dvds_total + games_total) * TAX_RATE
    sub_total = books_total + dvds_total + games_total
    total_cost = books_total + dvds_total + games_total + tax

    print(f'Books: ${books_total:.2f}')
    print(f'DVDs: ${dvds_total:.2f}')
    print(f'Games: ${games_total:.2f}')
    print(f'Subtotal: ${sub_total:.2f}')
    print(f'Tax: ${tax:.2f}')
    print(f'Total: ${total_cost:.2f}')


main()
