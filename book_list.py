"""
Authors: Arlo Virta, Erik Granse
Date: 2025-11-17
Description: Gets book price information from the user and displays it in a nice format, now with PyInputPlus!
"""

import pyinputplus as pyip

print('This program summarizes a book list.')  # print intro


def main():  											# call functions and save results under key variable names.
    try:  												# generic exception handling - turn off during development
        num_books, book_prices = inputs()
        total, average = processing(book_prices.values()) # no list-specific methods used; iterator work here
        outputs(num_books, book_prices, total, average)
        restart = pyip.inputYesNo('Need more books? Enter y or n: ') == "yes"  # restart feature
        if restart:
            print('OK, let\'s create a new list.')
            main()
        else:
            print('Thanks for using the program.')
    except Exception as err:
        print(err)


def inputs():  											# collect info needed from the user.
    num_books = pyip.inputInt('Enter the number of books that you need: ') # user sets the list length/ repetitions of the for loop
    book_prices = {}  									# create list to save prices
    for index in range(num_books):  					# for loop runs user-specified number of times & collects info on each book
        book_title = pyip.inputStr(f'Enter the title of book #{index +1}: ').lower()
        book_cost = pyip.inputInt(f'Enter the cost, to the nearest dollar: ', min=0)  						# call validation function to collect int > 0
        book_prices[book_title] = book_cost # build price map
    return num_books, book_prices


def processing(price_list):  							# use the list to calculate summary data
    total = sum(price_list) 							# add up all of the prices
    price_list_len = len(price_list) 					# this is how many prices we have
    average = total / price_list_len 					# calculate the total
    average_rounded = round(average, 2) 				# round the total

    return total, average_rounded


def outputs(num_books, book_prices, total, average):  	# display information about each book, and summary info
    print(f'Info on {num_books} Books Needed')
    print(f'{"Book Title":<20}{"Price":>10}')

    t = {}

    DETAIL_LINE = '{:<12}\t\t${:>8.2f}'
    for title in book_prices.keys():
        print(DETAIL_LINE.format(title.title(), book_prices[title]))

    print(f'{"Total":<10} ${total:>8.2f}')
    print(f'{"Average":<10} ${average:>8.2f}')


main()  												# call main to start or restart program.