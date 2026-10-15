from tablestats import read_rows, count_types, total_minutes, to_csv

def main():
    # Считываем путь к файлу из консоли
    path = input().strip()
    
    # Открываем файл и читаем все строки в список
    with open(path, encoding="utf-8") as table:
        lines = table.readlines()  # Читаем все строки в список
        rows = read_rows(lines)    # Передаем список строк в функцию

    # Считаем статистику
    counts = count_types(rows)
    
    # Выводим результаты
    print(len(rows))                       # Количество строк данных
    print(len(counts))                     # Количество уникальных типов
    print(total_minutes(rows, "ошибка"))   # Суммарное время для типа "ошибка"

    # Сохраняем результат в CSV файл
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(to_csv(counts))

if __name__ == "__main__":
    main()