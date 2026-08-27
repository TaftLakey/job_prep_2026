def combinationSum(candidates, target):
    result = []

    def backtrack(start, remainder, curr_comb):
        if remainder == 0:
            result.append(curr_comb[:])
            return
        for i in range(start, len(candidates)):
            num = candidates[i]

            if num > remainder:
                return

            curr_comb.append(num)

            backtrack(i, remainder-num, curr_comb)

            curr_comb.pop()


    backtrack(0, target, [])
    return result

print(combinationSum([2,3,6,7], 7))

gorilla = [6,7,2,3]
gorilla.sort()
print(gorilla)