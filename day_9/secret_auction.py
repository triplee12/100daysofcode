#!/usr/bin/python3
"""Secret auction program"""

logo = '''
 #####                                          #
#     # ######  ####  #####  ###### #####      # #   #    #  ####  ##### #  ####  #    #
#       #      #    # #    # #        #       #   #  #    # #    #   #   # #    # ##   #
 #####  #####  #      #    # #####    #      #     # #    # #        #   # #    # # #  #
      # #      #      #####  #        #      ####### #    # #        #   # #    # #  # #
#     # #      #    # #   #  #        #      #     # #    # #    #   #   # #    # #   ##
 #####  ######  ####  #    # ######   #      #     #  ####   ####    #   #  ####  #    #
'''

print(logo)
print("Welcome to secret auction program.")
other_user = "yes"
bid_record = {}
highest_bid = 0

while(other_user == "yes"):
    name = input("What's your name?\n")
    price = int(input("What's your bid in usd?\n"))
    bid_record["name"] = name
    bid_record["price"] = price

    # check who has the highest bid
    for value in bid_record:
        if bid_record["price"] > highest_bid:
            highest_bid = bid_record["price"]
            winner = bid_record[value]
    
    other_user = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    print(f"The winner is {winner} with a bid of ${highest_bid}")
