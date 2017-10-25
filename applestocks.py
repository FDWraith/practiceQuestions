import sys

stock_prices_yesterday = [10,7,5,8,11,9]

# StockPrice is a Number
# Represents the price value of a stock

# [ListOf StockPrice] -> Number
# Returns the max profit that could've been earned
def get_max_profits( stockprices ):

    # O(n^2) algorithm
    
    #for i in range(len(stockprices)-1):
    #    for j in range(i+1,len(stockprices)):
    #        max_so_far = max( stockprices[j] - stockprices[i], max_so_far )

    # Use min possible value as starting max
    max_so_far = -sys.maxint -1
    # Keep track of a minimum price we could buy at (so far)
    min_num = stockprices[0]

    #Start at index 1, because index 0 is the min_num so far.
    for i in range(1,len(stockprices)):

        # Calculate potential profit (if we chose to sell right now)
        potential_profit = stockprices[i] - min_num

        # Is potential profit greater than the max profit so far?
        # If it is, replace it,
        # If not, keep current max
        max_so_far = max( potential, max_so_far)

        # Can I buy at a lower price for a greater profit later
        # down the line?
        min_num = min( min_num, stockprices[i] )
    

    return max_so_far



print get_max_profits( stock_prices_yesterday )
print get_max_profits( [10, 2, 3, 9, 11, 3, 28] )
