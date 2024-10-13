# Leetcode 787
import logging

logger = logging.basicConfig(level=logging.DEBUG)

class Solution:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def findCheapestPrice1(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        logger_name = f"{self.__class__.__name__}.{self.findCheapestPrice.__name__}"
        method_logger = logging.getLogger(logger_name)
        method_logger.setLevel(logging.INFO)

        method_logger.debug(f"From source city: {src} to destination city: {dst} with at most {k} stop(s)")
        prices = [float("inf")] * n # create inf cost for flying to each city

        prices[src] = 0
        method_logger.info(f"Initial prices: {prices}")

        try:
            for i in range(k + 1):
                method_logger.info(f"Currently looking at {i} stop(s)")
                temp_prices = prices.copy()
                for start, end, price in flights:
                    if prices[start] != float("inf") and prices[start] + price < prices[end]:
                        temp_prices[end] = prices[start] + price

                prices = temp_prices
                method_logger.info(f"Prices mapping at {i} stop(s)")

            return prices[dst] if prices[dst] != float("inf") else -1
        except Exception as e:
            method_logger.exception(f"Error occurred: {str(e)}")
            raise


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