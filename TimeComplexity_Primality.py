def primality(n):
    rn = n**(1/2)
    i = 2
    found = False
    while i <= rn and not found:
        if n % i == 0:
            found = True
        else:
            i += 1
    if found or n == 1:
        return 'Not prime'
    else:
        return 'Prime'