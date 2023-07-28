'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
'''

from typing import Any, Dict, Iterable, List, Tuple


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)


# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return list(i for i in args if type(i) == int)


# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return list(i for i in args if type(i) == argument_type)


# Сконструировать и вернуть список из переданных аргументов, тип которых входит заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    return [i for i in args if type(i) in set(argument_types)]


# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second


# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    lst = []
    for i in lists:
        lst.extend(i)
    return lst


# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length


# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    values.remove(value_to_remove)
    return values


# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [i for i in values if i != value_to_remove]


# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda i: i != value_to_remove, values))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    return [i for i in values if i not in set(values_to_remove)]


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [i for i in values if i not in set(value_to_remove)]


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda i: i not in set(value_to_remove), values))


# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))


# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {k: v for k, v in kwargs.items() if type(v) == int}


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return dict.fromkeys(values, default)


# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {k: v for k, v in enumerate(values)}


# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)


# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))


# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    first.update(second)
    return first


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    dictionary.update(kwargs)
    return dictionary


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    for key, value in kwargs.items():
        dictionary[key] = [dictionary[key], value] if key in dictionary else value
    return dictionary


# Объединить два словарь и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    third = {**first, **second}
    for key, value in third.items():
        third[key] = [first[key], value] if key in first else value
    return third


# Объединить два словарь и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    for k, v in second.items():
        if k in first:
            if isinstance(first[k], dict) and isinstance(v, dict):
                deep_merge_two_dicts(first[k], v)
            elif isinstance(first[k], list) and isinstance(v, list):
                first[k].extend(v)
            elif isinstance(first[k], set) and isinstance(v, set):
                first[k].update(v)
            else:
                first[k] = [first[k], v]
        else:
            first[k] = v
    return first


# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary)


# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    return list(dictionary.values())


# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    return list(dictionary.items())


# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    return dict(reversed(dictionary.items()))


# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    return {k: v for k, v in dictionary.items() if v not in (None, '', [], {})}


# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    newdict = {}
    for k, v in dictionary.items():
        if v not in (None, '', [], {}) and v not in newdict.values():
            newdict[k] = v
    return newdict


# Обменять в словаре клчи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    return {v: k for k, v in dictionary.items()}


# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items()))


# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    return dict(reversed(sorted(dictionary.items())))


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    order = {int: 1, float: 2, str: 3}
    return {k: dictionary[k] for k in sorted(dictionary, key=lambda key: order[type(key)])}


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    order = {int: 1, float: 2, str: 3}
    return {k: dictionary[k] for k in sorted(dictionary, key=lambda key: (order[type(key)], -dictionary[key]))}


# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> Dict:
    return sum(1 for v in dictionary.values() if isinstance(v, (int, float)) and -10 <= v <= 25)


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    newdict = dict.fromkeys(keys)
    newdict.update(zip(keys, values))
    return newdict


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    newdict = dict.fromkeys(keys, default)
    newdict.update(zip(keys, values))
    return newdict


# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    newdict = dict.fromkeys(keys)
    newdict.update(zip(keys, values))
    return newdict
