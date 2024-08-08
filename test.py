"""Sqrt Feature"""

import math
import os

import pandas as pd
from sklearn.preprocessing import (
    LabelBinarizer,
    MaxAbsScaler,
    PolynomialFeatures,
    RobustScaler,
    SplineTransformer,
)


def sqrt(x: float) -> float:
    """_summary_

    Args:
        x (float): _description_

    Returns:
        float: _description_
    """

    return math.sqrt(x)
