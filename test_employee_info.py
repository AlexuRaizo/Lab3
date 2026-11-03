import employee_info

def test_get_employees_by_age_range():
    result = []
    input_min_age = 20
    input_max_age = 32
    test_arr = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]

    result = employee_info.get_employees_by_age_range(input_min_age, input_max_age)

    assert (result == test_arr)

def test_calculate_average_salary():
    result = 0
    test_arr = 60166.666666666664

    result = employee_info.calculate_average_salary()

    assert (result == test_arr)

def test_get_employees_by_dept():
    result = []
    input_dept = 'Engineering'
    test_arr = [
        {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]

    result = employee_info.get_employees_by_dept(input_dept)

    assert (result == test_arr)