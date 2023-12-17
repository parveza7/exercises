


# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

#step 1
# prompt user for credit card number
# remove any dashes if present
# remove any spaces if present

#step 2
# reverse credit_card_digits
# for every digit in the odd place double its value
# sum all the digits....create a variable called sum_odd_digits
# before adding to sum make sure you convert to int


#step 3
# for every digit in the odd place double its value
# Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# sum all the digits....create a variable called sum_even_digits


#step 4
# sum the totals of steps 2 & 3


#step 5
# If sum is divisible by 10, the credit card # is valid

#is_valid = (sum_of_digits % 10 == 0)
#print is valid or not


#Example Credit Card Numbers (for testing):
#Valid Credit Card Number: 4532015112830366
#Invalid Credit Card Number: 6011123456789012


# Enter the credit card number: 4532015112830366
# Valid credit card number!

# Enter the credit card number: 6011123456789012
# Invalid credit card number.
