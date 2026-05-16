class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._log(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._log(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._log(f"{a} × {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self._log(f"{a} ÷ {b} = {result}")
        return result

    def power(self, a: float, b: float) -> float:
        result = a ** b
        self._log(f"{a} ^ {b} = {result}")
        return result

    def modulo(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")
        result = a % b
        self._log(f"{a} % {b} = {result}")
        return result

    def _log(self, entry: str):
        self.history.append(entry)

    def get_history(self) -> list:
        return self.history.copy()

    def clear_history(self):
        self.history.clear()
