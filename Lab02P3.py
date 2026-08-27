#
# George Veney
# Aug 26 2026
# Gift card program
# This is a gift card program for loyal customers
# and for customers that buy a lot.
#
# Get a $20 gift card if in loyalty program and buy $50 - $100
# Get a $30 gift card if in loyalty program and buy over $100
# Get a $10 gift card if in not in loyalty program and buy over $100
# The gift card is NOT included in the total
# The gift card is not considered when calculating the tax.
#
SALES_TAX = 0.07
#
# Input
purchase = float(input("Enter the total purchase amount: "))  # Obtain purchase amount
loyalty_member = input("Is the customer a loyalty program member (y/n)")  # Verify if loyalty program member

# Processing
tax = purchase * SALES_TAX  # Calculate the amount of tax for the purchase
total_purchase = purchase + tax  # Total of purchase plus tax

# Determine gift card amount for non loyalty members
if loyalty_member == "n" and purchase >= 100: # non loyalty member with purchase under $100
    gift_card_reward = 10
else:
    gift_card_reward = 0

# Determine gift card amount for loyalty members
if loyalty_member == "y" and purchase < 50.0: # loyalty member with less than $50 purchase
    gift_card_reward = 0
elif loyalty_member == "y" and purchase >= 50.0 and purchase < 100.0: # loyalty member with purchases $50 - $100
    gift_card_reward = 20
elif loyalty_member == "y" and purchase >= 100.0: # loyalty member with purchase over $R00
    gift_card_reward = 30

# Output
print(f'Sales Tax: ${tax:.2f}') # Total sales tax
print(f'Total after tax: ${total_purchase:.2f}') # Purchase amount plus tax
print(f'Gift Card Awarded: ${gift_card_reward}') # Amount of gift card awarded
