# OverTheWire Bandit Progress

## Passwords (свежие)
- bandit0 → bandit0
- bandit11 → dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

## Solved Levels

### Level 0 → 1
**Команда:** `cat readme`
**Тема:** Базовое чтение файла

### Level 1 → 2
**Команда:** `cat ./-`
**Тема:** Файл с именем `-` нельзя читать напрямую — нужен `./`

### Level 3 → 4
**Команда:** `ls -a` для скрытых файлов, `cat ...Hiding-From-You`
**Тема:** Скрытые файлы (начинаются с точки)

### Level 4 → 5
**Команды:** `file ./*` затем `cat ./-file07`
**Тема:** Поиск ASCII текста среди бинарных файлов

### Level 5 → 6
**Команда:** `find . -size 1033c ! -executable -readable`
**Тема:** find с флагами размера

### Level 6 → 7
**Команда:** `find / -user bandit7 -group bandit6 -size 33c 2>/dev/null`
**Тема:** Поиск по владельцу/группе

### Level 7 → 8
**Команда:** `grep "millionth" data.txt`
**Тема:** Поиск строки в файле

### Level 8 → 9
**Команда:** `sort data.txt | uniq -u`
**Тема:** Уникальная строка через пайпы

### Level 9 → 10
**Команда:** `strings data.txt | grep "==="`
**Тема:** Извлечение читаемых строк из бинарника

### Level 10 → 11
**Команда:** `cat data.txt | base64 -d`
**Тема:** Декодирование Base64