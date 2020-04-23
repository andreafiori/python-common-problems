class BestTimeToBuyAndSellStock(object):
    def maxProfit(self, prices):
        """
        Sum of prices[i + 1] - prices[i], if prices[i + 1] > prices[i]
        :type prices: List[int]
        :rtype: int
        """
        return sum([y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y])
