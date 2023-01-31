from enum import Enum


class QuoteType(Enum):
    STOCK = "stock"
    FII = "fii"
    OPTION = "option"
    FUTURE = "future"
    BOND = "bond"
    ETF = "etf"
    OTHERS = "others"
