class Solution:
    def finalPrices(self, prices):
        stack = []
        res = prices[:]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                res[idx] = prices[idx] - prices[i]
            stack.append(i)

        return res

        