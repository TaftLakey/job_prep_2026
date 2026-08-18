def smallestNumber(n, t):
    """
    :type n: int
    :type t: int
    :rtype: int
    """
    def determineProduct(n, t):
        string_n = str(n)

        product = 1
        for i in range(len(string_n)):

            product = int(string_n[i]) * product

        if product % t == 0:
            return True

    while(not determineProduct(n,t)):
        n += 1

    return n






print(smallestNumber(15, 3))