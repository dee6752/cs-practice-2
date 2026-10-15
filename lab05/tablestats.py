def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Разбиваем строку по запятой
        f = [value.strip() for value in line.split(",")]

        # Если заголовок еще не задан, берем текущую строку как заголовок
        if not header:
            header = f
            continue
            
        # Пропускаем строки, где количество элементов не совпадает с заголовком
        if len(f) != len(header):
            continue
            
        # Создаем словарь и добавляем в список. Используем 'f', а не 'parts'
        rows.append(dict(zip(header, f)))
        
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get('тип') != kind:
            continue
            
        # Безопасно получаем значение и заменяем запятую на точку для float
        minutes_str = row.get('минуты', '0').replace(',', '.')
        try:
            total += float(minutes_str)
        except ValueError:
            # Если не удалось преобразовать в число (например, пустая строка), пропускаем
            continue
            
    return round(total, 1)


def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]

    # Убираем двойной цикл, оставляем один проход по отсортированным ключам
    for kind in sorted(counts.keys()):
        lines.append(f"{kind},{counts[kind]}")
        
    return "\n".join(lines) + "\n"