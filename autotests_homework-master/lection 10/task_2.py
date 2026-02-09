import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestAllDivision:
    """Тесты для функции all_division"""

    @pytest.mark.smoke
    def test_division_two_numbers(self):
        """Тест деления двух чисел"""
        result = all_division(10, 2)
        assert result == 5.0, f"Ожидалось 5.0, получено {result}"

    @pytest.mark.smoke
    def test_division_multiple_numbers(self):
        """Тест деления нескольких чисел последовательно"""
        result = all_division(100, 2, 5, 2)
        assert result == 5.0, f"Ожидалось 5.0, получено {result}"

    @pytest.mark.negative
    def test_division_by_zero(self):
        """Тест деления на ноль - должен вызывать ZeroDivisionError"""
        with pytest.raises(ZeroDivisionError, match="division by zero"):
            all_division(10, 0)

    @pytest.mark.negative
    def test_division_with_float_result(self):
        """Тест деления с получением дробного результата"""
        result = all_division(5, 2)
        assert result == 2.5, f"Ожидалось 2.5, получено {result}"

    @pytest.mark.boundary
    def test_division_single_argument(self):
        """Тест с одним аргументом - должен вернуть это же число"""
        result = all_division(7)
        assert result == 7.0, f"Ожидалось 7.0, получено {result}"

    @pytest.mark.boundary
    def test_division_negative_numbers(self):
        """Тест деления отрицательных чисел"""
        result = all_division(-10, 2, -1)
        assert result == 5.0, f"Ожидалось 5.0, получено {result}"

    @pytest.mark.parametrize("numbers, expected", [
        ((10, 2), 5.0),
        ((100, 2, 5, 2), 5.0),
        ((5, 2), 2.5),
        ((7,), 7.0),
        ((-10, 2, -1), 5.0),
    ])
    def test_parametrized_division(self, numbers, expected):
        """Параметризованный тест для проверки различных случаев"""
        result = all_division(*numbers)
        assert result == expected, f"Ожидалось {expected}, получено {result}"