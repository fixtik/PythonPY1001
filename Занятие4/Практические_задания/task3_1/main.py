if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    # TODO посчитать через ключи
    total_price_key = 0
    for fruit in cart:
        total_price_key += cart[fruit]

    print(total_price_key)  # получаем значение по ключу

    total_price = 0
    for price in cart.values():
        total_price += price


    print(total_price)

    print(sum(cart.values()))