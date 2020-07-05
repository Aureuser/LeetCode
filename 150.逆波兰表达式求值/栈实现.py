class Solution:
    def evalRPN(self, tokens):
        def is_num(x):
            try:
                int(x)
                return True
            except:
                return False
        dp = [0]
        for c in tokens:
            if is_num(c):
                dp.append(int(c))
            elif c == '+':
                dp.append(dp.pop() + dp.pop())
            elif c == '-':
                dp.append(-dp.pop() + dp.pop())
            elif c == '*':
                dp.append(dp.pop() * dp.pop())
            elif c == '/':
                a = dp.pop()
                b = dp.pop()
                dp.append(int(b/a))
        return dp.pop()