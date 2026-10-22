def count_items(values: list) -> dict:
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts

def unique_sorted(values: list) -> list:
    return sorted(set(values))

def common(first: list, second: list) -> list:
    return sorted(set(first) & set(second))

def only_in_first(first: list, second: list) -> list:
    return sorted(set(first) - set(second))


if __name__ == "__main__":
    values = ["ошибка", "запуск", "ошибка", "проверка"]
    
    print(count_items(values))
    
    print(unique_sorted(values))
    
    print(common(["иванов", "петрова"], ["петрова", "котов"]))
    
    print(only_in_first(["иванов", "петрова"], ["петрова", "котов"]))