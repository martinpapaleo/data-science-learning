"""
Goal: Return area of a circle given radius.
"""
import math

def area_circle(r: float) -> float:
    """Returns area of a circle. Rejects negative radius."""
    if r < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (r ** 2)
if __name__ == "__main__":
    area = area_circle(3)
    print(f"{area:.2f}")
