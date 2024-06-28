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
