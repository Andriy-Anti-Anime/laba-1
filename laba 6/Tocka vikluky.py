from functools import wraps


class HistoryTracker:
    """
    Декоратор на основі класу для збереження історії результатів функції.
    Історія зберігається в атрибуті 'history' екземпляра.
    """

    def __init__(self, func):
        """
        Метод ініціалізації: зберігає оригінальну функцію і створює список історії.
        """
        self.func = func
        self.history = []

        #@wraps для збереження метаданих оригінальної функції
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        """
        Точка входу для виклику декорованої функції.
        """
        result = self.func(*args, **kwargs)

        self.history.append(result)

        return result