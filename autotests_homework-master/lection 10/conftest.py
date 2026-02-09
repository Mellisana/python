import pytest
import datetime
import time


@pytest.fixture(scope="class")
def class_fixture(request):
    """Фикстура для класса - печатает время начала и окончания выполнения тестов класса"""
    start_time = datetime.datetime.now()
    print(f"\n{'=' * 50}")
    print(f"Начало выполнения класса тестов: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Класс: {request.cls.__name__ if hasattr(request, 'cls') else 'Бесклассовые тесты'}")
    print(f"{'=' * 50}")

    yield  # Здесь выполняются тесты

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print(f"\n{'=' * 50}")
    print(f"Окончание выполнения класса тестов: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Продолжительность: {duration.total_seconds():.2f} секунд")
    print(f"{'=' * 50}")


@pytest.fixture
def test_timer(request):
    """Фикстура для конкретного теста - измеряет время выполнения теста"""
    start_time = time.time()

    yield  # Здесь выполняется тест

    end_time = time.time()
    duration = end_time - start_time
    print(f"\nТест '{request.node.name}' выполнен за {duration:.3f} секунд")


@pytest.fixture
def setup_data():
    """Дополнительная фикстура с тестовыми данными"""
    test_data = {
        "numbers": (10, 2, 5),
        "expected": 1.0,
        "description": "Деление 10 на 2 на 5"
    }
    return test_data


@pytest.fixture
def division_test_cases():
    """Фикстура с различными тестовыми случаями для деления"""
    return [
        {"args": (10, 2), "expected": 5.0, "name": "simple_division"},
        {"args": (100, 2, 5, 2), "expected": 5.0, "name": "multiple_division"},
        {"args": (5, 2), "expected": 2.5, "name": "float_division"},
        {"args": (-10, 2, -1), "expected": 5.0, "name": "negative_numbers"},
        {"args": (7,), "expected": 7.0, "name": "single_argument"},
    ]