import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = None
        operators = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                secondNumber = stack.pop()
                firstNumber = stack.pop()
                match token:
                    case "+":
                        stack.append(firstNumber + secondNumber)
                    case "-":
                        stack.append(firstNumber - secondNumber)
                    case "*":
                        stack.append(firstNumber * secondNumber)
                    case "/":
                        stack.append(int(firstNumber / secondNumber))
                    case _:
                        pass

        return int(stack.pop())