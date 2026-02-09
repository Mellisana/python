import pytest


def all_division(*arg1):
    """Функция для тестирования - делит все переданные числа последовательно"""
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures("class_fixture")
class TestAllDivision:
    """Класс с тестами для функции all_division"""

    def test_simple_division(self, test_timer, setup_data):
        """Простой тест деления с использованием фикстур"""
        result = all_division(*setup_data["numbers"])
        expected = setup_data["expected"]
        assert result == expected, f"Ожидалось {expected}, получено {result}"
        print(f"Тест: {setup_data['description']} - УСПЕХ")

    def test_division_by_zero(self, test_timer):
        """Тест деления на ноль"""
        with pytest.raises(ZeroDivisionError):
            all_division(10, 0)
        print("Тест деления на ноль - УСПЕХ (исключение перехвачено)")

    def test_parametrized_division(self, division_test_cases):
        """Тест с параметрами из фикстуры"""
        for test_case in division_test_cases:
            result = all_division(*test_case["args"])
            expected = test_case["expected"]
            assert result == expected, (
                f"Тест '{test_case['name']}': "
                f"Ожидалось {expected}, получено {result} "
                f"для аргументов {test_case['args']}"
            )
        print(f"Все {len(division_test_cases)} параметризованных тестов - УСПЕХ")

    def test_large_numbers_division(self):
        """Тест без фикстуры таймера (для демонстрации)"""
        result = all_division(1000000, 10, 100)
        assert result == 1000.0
        print("Тест с большими числами - УСПЕХ")

    @pytest.mark.slow
    def test_slow_operation(self, test_timer):
        """Медленный тест для демонстрации работы таймера"""
        import time
        # Имитация долгой операции
        time.sleep(0.5)
        result = all_division(100, 4, 5)
        assert result == 5.0
        print("Медленный тест - УСПЕХ")


class TestAdditionalOperations:
    """Другой класс тестов для демонстрации работы class_fixture"""

    @pytest.mark.usefixtures("class_fixture")
    def test_additional_operation(self):
        """Дополнительный тест в другом классе"""
        result = all_division(20, 2, 2)
        assert result == 5.0
        print("Дополнительный тест - УСПЕХ")