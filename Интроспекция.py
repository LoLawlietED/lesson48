def introspection_info(obj):
    """
    Функция для интроспекции объекта, возвращает информацию о его типе, атрибутах, методах и других свойствах.

    :param obj: Объект для интроспекции
    :return: Словарь с информацией об объекте
    """
    info = {
        'type': str(type(obj)),  # Тип объекта
        'attributes': [],         # Атрибуты объекта
        'methods': [],            # Методы объекта
        'module': None,           # Модуль, к которому принадлежит объект (по умолчанию None)
        'doc': obj.__doc__,      # Докстрока объекта (если есть)
        'is_callable': callable(obj)  # Проверка, является ли объект вызываемым
    }

    # Устанавливаем модуль, если объект не встроенный тип
    if not isinstance(obj, (int, float, str, list, dict, set, tuple)):
        info['module'] = obj.__module__

    # Получаем атрибуты и методы объекта
    for attr in dir(obj):
        if not attr.startswith('__'):  # Игнорируем специальные атрибуты
            value = getattr(obj, attr)
            if callable(value):  # Если атрибут - метод
                info['methods'].append(attr)
            else:  # Если атрибут - обычный
                info['attributes'].append(attr)

    return info

# Пример использования функции
if __name__ == "__main__":
    # Пример с числом
    number_info = introspection_info(42)
    print("Информация о числе 42:")
    print(number_info)

    # Пример со строкой
    string_info = introspection_info("Hello, World!")
    print("\nИнформация о строке 'Hello, World!':")
    print(string_info)

    # Пример со списком
    list_info = introspection_info([1, 2, 3])
    print("\nИнформация о списке [1, 2, 3]:")
    print(list_info)

    # Пример с пользовательским классом
    class Example:
        """Это пример класса для демонстрации интроспекции."""
        def __init__(self):
            self.attribute1 = "value1"
            self.attribute2 = "value2"

        def method1(self):
            return "method1 called"

        def method2(self):
            return "method2 called"

    example_obj = Example()
    example_info = introspection_info(example_obj)
    print("\nИнформация о объекте Example:")
    print(example_info)