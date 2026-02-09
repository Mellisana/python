import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestAllDivision:
    """Тесты для функции all_division"""

    @pytest.mark.parametrize("numbers, expected, test_id", [
        # smoke-тест - простой случай деления
        pytest.param((10, 2), 5.0, "smoke_simple_division", marks=pytest.mark.smoke),

        # Деление нескольких чисел
        ((100, 2, 5, 2), 5.0, "multiple_division"),

        # Деление с дробным результатом
        ((5, 2), 2.5, "float_division"),

        # Деление отрицательных чисел
        ((-10, 2, -1), 5.0, "negative_numbers"),

        # Деление на ноль - должно вызывать исключение
        pytest.param((10, 0), None, "division_by_zero",
                     marks=pytest.mark.xfail(raises=ZeroDivisionError)),

        # Один аргумент
        ((7,), 7.0, "single_argument"),

        # Пропускаемый тест - деление нуля на число
        pytest.param((0, 5), 0.0, "zero_divided", marks=pytest.mark.skip("Не актуально")),

        # Большие числа
        ((1000000, 10, 100), 1000.0, "large_numbers"),
    ])
    def test_parametrized_all_division(self, numbers, expected, test_id):
        """Параметризованный тест для функции all_division"""

        # Обработка случая с делением на ноль
        if test_id == "division_by_zero":
            with pytest.raises(ZeroDivisionError):
                all_division(*numbers)
        else:
            result = all_division(*numbers)
            assert result == expected, (
                f"Тест {test_id}: "
                f"Ожидалось {expected}, получено {result} "
                f"для входных данных {numbers}"
            )