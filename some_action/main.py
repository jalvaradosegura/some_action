def apply_discount(price: int, discount: int) -> float:
    return price * (1 - discount / 100)


print(apply_discount(1000, 40))
print(apply_discount(1000, 20))
print(apply_discount(1000, 75))
