import os

def get_size(path):
    """Возвращает размер файла или директории."""
    total_size = 0
    try:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
        else:
            total_size = os.path.getsize(path)
    except (FileNotFoundError, PermissionError):
        # Игнорируем ошибки, если файл или директория не найдены или нет доступа
        return 0
    return total_size

def format_size(size):
    """Форматирует размер в байты, килобайты, мегабайты и террабайты."""
    if size >= 1024**4:
        return f"{size / (1024**4):.2f} TB"
    elif size >= 1024**3:
        return f"{size / (1024**3):.2f} GB"
    elif size >= 1024**2:
        return f"{size / (1024**2):.2f} MB"
    elif size >= 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size} bytes"

def main():
    current_directory = '.'  # Текущий каталог
    sizes = []

    # Получаем размеры всех файлов и директорий в текущем каталоге, включая скрытые
    for entry in os.listdir(current_directory):
        path = os.path.join(current_directory, entry)
        size = get_size(path)
        sizes.append((size, entry))  # Добавляем все элементы, включая нулевые размеры

    # Сортируем по размеру в порядке убывания
    sizes.sort(key=lambda x: x[0], reverse=True)

    # Выводим результаты
    for size, entry in sizes:
        formatted_size = format_size(size)
        print(f"{formatted_size}\t{entry}")

if __name__ == "__main__":
    main()
