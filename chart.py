# print("\033[31mttt tgerg ewt")
# print("\033[101mttt tgerg ewt")
colors = """CEND= '\33[0mTest String\033[0m'
CBOLD     = '\33[1mTest String\033[0m'
CITALIC   = '\33[3mTest String\033[0m'
CURL      = '\33[4mTest String\033[0m'
CBLINK    = '\33[5mTest String\033[0m'
CBLINK2   = '\33[6mTest String\033[0m'
CSELECTED = '\33[7mTest String\033[0m'
CBLACK  = '\33[30mTest String\033[0m'
CRED    = '\33[31mTest String\033[0m'
CGREEN  = '\33[32mTest String\033[0m'
CYELLOW = '\33[33mTest String\033[0m'
CBLUE   = '\33[34mTest String\033[0m'
CVIOLET = '\33[35mTest String\033[0m'
CBEIGE  = '\33[36mTest String\033[0m'
CWHITE  = '\33[37mTest String\033[0m'
CBLACKBG  = '\33[40mTest String\033[0m'
CREDBG    = '\33[41mTest String\033[0m'
CGREENBG  = '\33[42mTest String\033[0m'
CYELLOWBG = '\33[43mTest String\033[0m'
CBLUEBG   = '\33[44mTest String\033[0m'
CVIOLETBG = '\33[45mTest String\033[0m'
CBEIGEBG  = '\33[46mTest String\033[0m'
CWHITEBG  = '\33[47mTest String\033[0m'
CGREY    = '\33[90mTest String\033[0m'
CRED2    = '\33[91mTest String\033[0m'
CGREEN2  = '\33[92mTest String\033[0m'
CYELLOW2 = '\33[93mTest String\033[0m'
CBLUE2   = '\33[94mTest String\033[0m'
CVIOLET2 = '\33[95mTest String\033[0m'
CBEIGE2  = '\33[96mTest String\033[0m'
CWHITE2  = '\33[97mTest String\033[0m'
CGREYBG    = '\33[100mTest String\033[0m'
CREDBG2    = '\33[101mTest String\033[0m'
CGREENBG2  = '\33[102mTest String\033[0m'
CYELLOWBG2 = '\33[103mTest String\033[0m'
CBLUEBG2   = '\33[104mTest String\033[0m'
CVIOLETBG2 = '\33[105mTest String\033[0m'
CBEIGEBG2  = '\33[106mTest String\033[0m'
CWHITEBG2  = '\33[107mTest String\033[0m'
"""
red='\33[101m'
end='\033[0m'
print(f'{red}This is being printed using ASCII color coding.{end}')


from typing import List
from typing import Tuple

# code for linear regression
def linear_regression(x: List[float], y: List[float]) -> Tuple[float, float]:
    """
    Calculates the linear regression coefficients for the given data points.

    Args:
        x: List[float]: The x-coordinates of the data points.
        y: List[float]: The y-coordinates of the data points.

    Returns:
        Tuple[float, float]: A tuple containing the slope (a) and intercept (b) of the best fit line.

    Raises:
        ValueError: If the length of x and y are not equal.
    """
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")

    n = len(x)
    sum_x, sum_y, sum_xy, sum_xx = 0, 0, 0, 0
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i] * y[i]
        sum_xx += x[i] * x[i]

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x * y)
    sum_xx = sum(x * x)
    denominator = n * sum_xx - sum_x * sum_x
    if denominator == 0:
        raise ValueError("Division by zero")

    a = (n * sum_xy - sum_x * sum_y) / denominator
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)
    b = (sum_y - a * sum_x) / n
    return a, b

    return a, b      

print(linear_regression([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
