# Stock Transactions

from decimal import *

# calculate purchase price
def purchase():
	global purchase_price

	shares_purchased = Decimal(input("How many shares were bought? "))
	share_initial_price = Decimal(input("What was the price per share? $"))
	purchase_price = Decimal(shares_purchased * share_initial_price)

	broker_purchase_commission = Decimal(input("What percentage commission is due to the stockbroker? ") / Decimal(100.00))
	broker_purchase_commission = Decimal(broker_purchase_commission * purchase_price)

	purchase_price = Decimal(purchase_price + broker_purchase_commission)

	print ""
	print "You purchased stock worth $", purchase_price
	print "Two weeks later you decide to sell the stock."
	print ""

	return purchase_price

# calculate proceeds
def proceeds():
	global proceeds

	shares_sold = Decimal(input("How many shares are sold? "))
	share_present_price = Decimal(input("What is the price per share? $"))
	sale_price = Decimal(shares_sold * share_present_price)

	broker_sale_commission = Decimal(input("What percentage commission is due to the stockbroker? ") / Decimal(100.00))
	broker_sale_commission = Decimal(broker_sale_commission * sale_price)

	proceeds = Decimal(sale_price - broker_sale_commission)

	print "Your proceeds are $", proceeds
	print ""

	return proceeds

# determin profit or loss
def investment():
	if (proceeds - purchase_price) > 0:
		print "You made a profit of $", proceeds - purchase_price
	else:
		print "You took a loss of $", (purchase_price - proceeds)


purchase()
proceeds()
investment()