'''
Goal: Convert ARS to USD at a given rate (ARS per USD).
'''
def convert_to_usd(pesos: float, rate: float = 1000.0) -> float:
    """Converts Argentine pesos to USD at a given rate."""
    if rate <= 0:
        raise ValueError('Rate must be positive.')
    return pesos / rate
if __name__ == "__main__":
    value = convert_to_usd(10_000, 980)
    print(f"{value:.2f}")