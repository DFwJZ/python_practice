#Leetcode 227

import logging 

logging.basicConfig(level=logging.DEBUG)

class Solution:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def calculate(self, s: str) -> int:
        method_logger = logging.getLogger(f"{self.__class__.__name__}.{self.calculate.__name__}")

        stack = []
        sign = '+'
        num = 0
        s = s.strip()

        # if s[0] == '-':
        #     s = '0' + s

        for i, char in enumerate(s):
            if char.isdigit():
                method_logger.info(f"triggered .isdigit at {i}, current char is {char}")
                num = num * 10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                method_logger.info(f"triggered non-digit check at {i}, current char is {char}")
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)    
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                sign = char
                num = 0

            method_logger.info(f"at iteration {i}, current stack: {stack}\n")

        return sum(stack)

    def calculate_no_stack(self, s: str) -> int:
        res = 0
        cur_num = 0
        last_num = 0
        sign = '+'
        s = s.strip()

        for i, char in enumerate(s):
            if char.isdigit():
                cur_num = cur_num * 10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                print(f"last_num: {last_num}, cur_num: {cur_num}")
                if sign == '+':
                    res += last_num
                    last_num = cur_num
                elif sign == '-':
                    res += last_num
                    last_num = -cur_num
                elif sign == '*':
                    last_num *= cur_num
                elif sign == '/':
                    last_num = int(last_num/cur_num)

                cur_num = 0
                sign = char

            print(f"res: {res}")
        
        res += last_num
        return res
 
def main():
    solution = Solution()
    # print(solution.calculate("-1+2*2*2*2*2"))  # Output: 33
    print(solution.calculate_no_stack(" -1 + -3/2 + 3 "))  # Output: 1
    # print(solution.calculate(" 3+5 / 2 "))  # Output: 5



if __name__ == '__main__':
    main()