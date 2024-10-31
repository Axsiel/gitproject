#!/bin/bash

# Проверка, что директория существует
if [ -z "$dir" ]; then
    dir="."
else
    dir="$dir"
fi

# Переход в указанную директорию
cd "$dir"

# Вывод файлов и их размеров, сортировка по размеру
du -sh .[!.]* * | sort -hr
