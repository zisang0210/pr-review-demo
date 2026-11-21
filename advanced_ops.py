"""高级运算模块。"""
import math


class AdvancedOps:
    """高级运算：幂、开方、对数。"""

    def power(self, base, exponent):
        result = base ** exponent
        print(f"power result: {result}")  # 调试 print
        return result

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot sqrt negative number")
        return math.sqrt(x)

    def log(self, x, base=math.e):
        if x <= 0:
            raise ValueError("log undefined for non-positive values")
        return math.log(x, base)

    def safe_password_check(self, input_password, stored_password):
        # 直接比较密码，不安全
        if input_password == stored_password:
            return True
        return False

    def factorial(self, n):
        # 递归实现，无溢出检查
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)
