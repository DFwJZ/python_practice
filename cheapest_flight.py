# Leetcode 787
import logging

logger = logging.basicConfig(level=logging.DEBUG)

class Solution:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        self.logger.info(f"Starting findCheapestPrice function from {src} to {dst}, with at most {k} stops")
        prices = [float("inf")] * n # create inf cost for flying to each city

        prices[src] = 0 # at the start, the cost is 0
        self.logger.debug(f"Initial prices: {prices}")

        try:
            for i in range(k + 1): 
                self.logger.debug(f"Iteration {i}")
                temp_prices = prices.copy()

                for start, end, price in flights:
                    if prices[start] != float("inf") and prices[start] + price < prices[end]:
                        temp_prices[end] = prices[start] + price
                        self.logger.debug(f"Updated price for city {end}: {temp_prices[end]}")

                prices = temp_prices
                self.logger.info(f"Cheapest price found: {prices}")

            result = prices[dst] if prices[dst] != float("inf") else -1
            return result 
        
        except Exception as e:
            self.logger.exception(f"An error occured: {str(e)}")
            return -1            

def main():
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    solution = Solution()
    print(solution.findCheapestPrice(n, flights, src, dst, k))

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0

    solution = Solution()
    print(solution.findCheapestPrice(n, flights, src, dst, k))

    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1

    solution = Solution()
    print(solution.findCheapestPrice(n, flights, src, dst, k))

if __name__ == '__main__':
    main()