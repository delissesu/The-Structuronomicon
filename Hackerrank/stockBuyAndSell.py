prices = [7, 10, 1, 3, 6, 9, 2]
# [7, 6, 4, 3, 1]
# [7, 6, 5]
"""
left = 7

max-profit = 0

prices[1] = 6 < 7


"""

def maximumProfit(prices):
    if len(prices) < 2:
        return 0
        
    left = 0  # Buy pointer
    max_profit = 0
    
    for right in range(1, len(prices)):  # Sell pointer
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right  # Found a better buying point
            
    return max_profit

print(maximumProfit(prices))

def maximumProfit2(prices):
    if len(prices) < 2:  # Need at least 2 prices to make profit
        return 0
    
    min_so_far = prices[0]  # Minimum price seen so far
    max_profit = 0  # Maximum profit possible
    
    for current_price in prices[1:]:
        # Can we get better profit with current price?
        possible_profit = current_price - min_so_far
        max_profit = max(max_profit, possible_profit)
        
        # Update minimum price seen so far
        min_so_far = min(min_so_far, current_price)
    
    return max_profit

print(maximumProfit2(prices))

def maximumProfit3(prices):
    if len(prices) <= 1:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices[1:]:
        if min_price > price:
            min_price = price
        
        temp_profit = price - min_price
        
        if temp_profit > max_profit:
            max_profit = temp_profit
    
    return max_profit

print(maximumProfit3(prices))