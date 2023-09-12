# Документация к тестовому заданию для компании "Статус"
Выполнил: `Цыденов Саян Баирович`

- vk: https://vk.com/say1ts
- github: https://github.com/Say1ts
- telegram: https://t.me/say1ts
- linkedin: https://www.linkedin.com/in/sayan-tsydenov-9a7315222/

## Описание задачи
Задача заключается в реализации структуры данных для хранения иерархической структуры в виде дерева. Для этого предоставлены два решения: одно с использованием классов и другое без использования классов.

### Методы
- `getAll()`: Возвращает все элементы в их исходной форме.
- `getItem(id: int)`: Возвращает элемент по его ID.

- `getChildren(id: int)`: Возвращает дочерние элементы элемента с заданным ID.
- `getAllParents(id: Union[int, str])`: Возвращает всех родителей элемента с заданным ID, вплоть до корневого элемента.

## Решения
### `Решение без использования классов`
Этот подход минимизирует количество операций и использует меньше памяти. Он основан на использовании словарей и списков для индексации и хранения данных.


### `Решение с использованием классов`
Этот подход использует объектно-ориентированное программирование для представления каждого узла как объекта. Это делает код более читаемым и легко расширяемым, но может быть менее эффективным по памяти и скорости выполнения.


# Почему реализовано два решения
Два решения реализованы для демонстрации различных подходов к решению задачи. 

Решение без классов может быть более быстрым и эффективным по памяти, но оно может быть менее читаемым и труднее для расширения. 

Решение с классами, наоборот, легче читать и расширять, но может быть менее эффективным.

# Тестовые кейсы
- Тестирование метода `getAll()`: Проверяет, возвращает ли метод все элементы в их исходной форме.

- Тестирование метода `getItem(id: int)`: Проверяет, возвращает ли метод элемент по его ID или None, если элемент не найден.

- Тестирование метода `getChildren(id: int)`: Проверяет, возвращает ли метод все дочерние элементы элемента с заданным ID.

- Тестирование метода `getAllParents(id: int)`: Проверяет, возвращает ли метод всех родителей элемента с заданным ID, вплоть до корневого элемента.

Каждый из этих тестовых кейсов применяется к обоим решениям для обеспечения их функциональной эквивалентности.