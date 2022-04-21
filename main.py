from moneyed import Money, EUR


def get_number_of_options(price: EUR, err_rate: int, budget: EUR) -> [int]:
    if err_rate <= 0 or err_rate == 100:
        raise ValueError("Error rate must be between 0 and 100")
    max_num = int(budget / ((1 - err_rate / 100) * price))
    min_num = int(budget / ((1 + err_rate / 100) * price))
    variants = []
    for i in range(min_num, max_num + 1):
        variants.append(i)
    variants.sort()
    return list(set(variants))

if __name__ == "__main__":
    foo = get_number_of_options(Money(1, EUR), 10, Money(10, EUR))
    print(foo)
