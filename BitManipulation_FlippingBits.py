def flippingBits(n):
    stack = []
    while n > 0:
        stack.append(n%2)
        n = n//2
    while len(stack) < 32:
        stack.append(0)
    ans = 0
    i = 31
    while stack != []:
        sp = stack.pop()
        if sp == 0:
            ans += 2**i
        i -= 1
    return ans