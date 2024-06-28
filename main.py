"""Basic Caculator Application """

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


class Calculator:
    """Calculator in CLI which perform basic math operation.
    Future: Scientific Calculation will be added."""

    def __init__(self):
        pass

    # Addition
    def sum(self, a: int, b: int) -> int:
        """Perform addition between two given number

        Parameters
        ----------
        a : int
            real integer number
        b : int
            real integer number

        Returns
        -------
        int
            real integer number
        """
        logger.info("Summing {a} and {b}")
        return a + b

    def substract(self, a: int, b: int) -> int:
        """Perform subtraction from first given number with second given number.

        Parameters
        ----------
        a : int
            real integer number
        b : int
            real integer number

        Returns
        -------
        int
            real integer number
        """
        logger.info("Substracing {a} and {b}")
        return a - b


if __name__ == "__main__":
    app = Calculator()

    while True:
        x = int(input("Enter a:"))
        y = int(input("Enter b:"))

        op = str(input("Enter operation: "))  # pylint: disable=C0103

        if op == "+":
            result = app.sum(x, y)
        elif op == "-":
            result = app.substract(x, y)
        else:
            raise ValueError

        print(f"Result {result}")
