
def myAtoi(s):
        """
        :type s: str
        :rtype: int
        """
        isNegative = False
        iterationCount = 0
        result = 0
        for i in s:
            if not i.isdigit():
                if i == " ":
                    if iterationCount > 0:
                        return checkRound(result, isNegative)
                    else:
                        continue
                if i == "-":
                    if iterationCount > 0:
                        return checkRound(result, isNegative)
                    isNegative = True
                    iterationCount += 1
                    continue
                if i == "+":
                    if iterationCount > 0:
                        return checkRound(result, isNegative)
                    else:
                        iterationCount += 1
                        continue
                return checkRound(result, isNegative)
            result *= 10
            result += int(i)
            iterationCount += 1
        return checkRound(result, isNegative)

def checkRound(result, isNegative):
    if isNegative:
        result *= -1
    if result < -2**31:
        return -2**31
    elif result > 2**31-1:
        return 2**31-1
    else:
        return result

print(myAtoi("  -0012a42"))