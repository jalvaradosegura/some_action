def apply_discount(price: int, discount: int) -> float:
    new_price = price * (1 - discount / 100)
    assert 0 <= new_price <= price, 'The discount does not make sense'
    return new_price


print(apply_discount(price=1000, discount=140))
print(apply_discount(price=1000, discount=20))
print(apply_discount(price=1000, discount=75))
