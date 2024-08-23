def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


try:
    inner_function()
except NameError as e:
    print(f"Я вне области видимости функции test_function\nОшибка: {e}\n")


test_function()
