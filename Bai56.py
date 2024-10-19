# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:20:03 2024

@author: NGUYEN THANH HUY
"""

import math

def calculate_perimeter_area(*args, shape, operation):
    """
    Calculates the perimeter or area of a given shape.

    Args:
        args: A variable number of arguments representing the dimensions of the shape.
        shape: The name of the shape (e.g., "square", "rectangle", "circle").
        operation: The operation to perform (either "perimeter" or "area").

    Returns:
        The calculated perimeter or area, or an error message if the shape or operation is invalid.
    """

    if shape == "square":
        side = args[0]
        return 4 * side if operation == "perimeter" else side**2
    elif shape == "rectangle":
        length = args[0]
        width = args[1]
        return 2 * (length + width) if operation == "perimeter" else length * width
    elif shape == "circle":
        radius = args[0]
        return 2 * math.pi * radius if operation == "perimeter" else math.pi * radius**2
    else:
        return "Invalid shape"

if __name__ == "__main__":
    print("Perimeter of square:", calculate_perimeter_area(3, shape="square", operation="perimeter"))
    print("Area of square:", calculate_perimeter_area(3, shape="square", operation="area"))
    print("Perimeter of rectangle:", calculate_perimeter_area(3, 4, shape="rectangle", operation="perimeter"))
    print("Area of rectangle:", calculate_perimeter_area(3, 4, shape="rectangle", operation="area"))
    print("Perimeter of circle:", calculate_perimeter_area(3, shape="circle", operation="perimeter"))
    print("Area of circle:", calculate_perimeter_area(3, shape="circle", operation="area"))