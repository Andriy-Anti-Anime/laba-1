from functools import wraps
class HistoryTracker:
    def __init__(self, func):
        self.func = func
        self.history = []
        wraps(func)(self)
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        self.history.append(result)
        return result

@HistoryTracker
def calculate_area(width, height):
    """Обчислює площу прямокутника."""
    print(f"Обчислення площі: {width} x {height}")
    return width * height

area_1 = calculate_area(5, 4)
area_2 = calculate_area(10, 2)
area_3 = calculate_area(3, 3)

print("\n--- Результати обчислень ---")
print(f"Площа 1: {area_1}")
print(f"Площа 2: {area_2}")
print(f"Площа 3: {area_3}")

print("\n--- Історія результатів (calculate_area.history) ---")
print(calculate_area.history)