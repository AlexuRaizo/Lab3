import price_info

def test_total_cost_shopping():
    result = 0
    test_arr = 46.75

    result = price_info.total_cost_shopping()

    assert (result == test_arr)

def test_cost_of_fruits():
    result = 0
    input_key = 'apple'
    input_quantity = 10
    test_arr = 12.0

    result = price_info.cost_of_fruits(input_key, input_quantity)

    assert (result == test_arr)