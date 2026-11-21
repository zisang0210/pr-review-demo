"""简单计算器模块。"""


class Calculator:
    """支持加减乘除的计算器，并记录计算历史。"""

    def __init__(self):
        self._history = []

    def _record(self, op, a, b, result):
        self._history.append({"op": op, "a": a, "b": b, "result": result})
        return result

    def add(self, a, b):
        return self._record("add", a, b, a + b)

    def subtract(self, a, b):
        return self._record("subtract", a, b, a - b)

    def multiply(self, a, b):
        return self._record("multiply", a, b, a * b)

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return self._record("divide", a, b, a / b)

    def history(self):
        """返回计算历史的副本。"""
        return list(self._history)

    def clear_history(self):
        """清空计算历史。"""
        self._history.clear()
