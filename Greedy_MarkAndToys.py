def maximumToys(prices, k):
    prices.sort()
    rp = prices[::-1]
    total = 0
    count = 0
    while total < k and count <= len(prices):
        total += rp.pop()
        count += 1
    return count-1