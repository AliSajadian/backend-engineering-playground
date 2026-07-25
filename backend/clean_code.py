'''
Clean code
'''
def dirty_process_order(order):
    '''bad code'''
    if order["status"] == "pending":
        if order["total"] > 100:
            discount = order["total"] * 0.1
        else:
            discount = 0

        final_price = order["total"] - discount

        if order["country"] == "US":
            tax = final_price * 0.07
        elif order["country"] == "CA":
            tax = final_price * 0.05
        else:
            tax = 0

        return final_price + tax

    return None


TAX_RATES = {
    "US": 0.07,
    "CA": 0.05,
}

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.10


def calculate_discount(total: float) -> float:
    '''discount'''
    if total > DISCOUNT_THRESHOLD:
        return total * DISCOUNT_RATE

    return 0


def calculate_tax(amount: float, country: str) -> float:
    '''tax'''
    tax_rate = TAX_RATES.get(country, 0)
    return amount * tax_rate


def process_order(order: dict) -> float | None:
    '''order'''
    if order["status"] != "pending":
        return None

    total = order["total"]

    discount = calculate_discount(total)
    price_after_discount = total - discount

    tax = calculate_tax(
        price_after_discount,
        order["country"]
    )

    return price_after_discount + tax
