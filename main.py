"""Basic Caculator Application """

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


class Calculator:
    """_summary_"""

    def __init__(self):
        """init for class"""

        pass

    def sum(self, a: int, b: int) -> int:
        """_summary_

        Args:
            a (int): _description_
            b (int): _description_

        Returns:
            int: _description_
        """
        logger.info("Summing {a} and {b}")
        return a + b

    def substract(self, a: int, b: int) -> int:
        """_summary_

        Args:
            a (int): _description_
            b (int): _description_

        Returns:
            int: _description_
        """
        logger.info("Substracing {a} and {b}")
        return a - b


if __name__ == "__main__":
    app = Calculator()

    while True:
        x = int(input("Enter a:"))
        y = int(input("Enter b:"))

        op = str(input("Enter operation: "))

        if op == "+":
            result = app.sum(x, y)
        elif op == "-":
            result = app.substract(x, y)
        else:
            raise ValueError

        print(f"Result {result}")
