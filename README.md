
# Задание №1

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС. Эмулятор должен запускаться из реальной командной строки, а файл с виртуальной файловой системой не нужно распаковывать у пользователя.

Эмулятор принимает образ виртуальной файловой системы в виде файла формата `tar`. Эмулятор должен работать в режиме CLI.

Конфигурационный файл имеет формат `json` и содержит:
- Имя пользователя для показа в приглашении к вводу.
- Путь к архиву виртуальной файловой системы.
- Путь к стартовому скрипту.

Стартовый скрипт служит для начального выполнения заданного списка команд из файла.

Необходимо поддержать в эмуляторе команды `ls`, `cd` и `exit`, а также следующие команды:
1. `clear`
2. `cp`

Все функции эмулятора должны быть покрыты тестами, а для каждой из поддерживаемых команд необходимо написать 2 теста.

Результат работы программы

![image](https://github.com/user-attachments/assets/6638ddd9-2c1e-47b7-be1d-716bb7774744)


# Задание №2

Разработать инструмент командной строки для визуализации графа зависимостей, включая транзитивные зависимости. Сторонние средства для получения зависимостей использовать нельзя.

Зависимости определяются по имени пакета ОС Ubuntu (apt). Для описания графа зависимостей используется представление `Mermaid`. Визуализатор должен выводить результат в виде сообщения об успешном выполнении и сохранять граф в файле формата `png`.

Конфигурационный файл имеет формат `yaml` и содержит:
- Путь к программе для визуализации графов.
- Имя анализируемого пакета.
- Путь к файлу с изображением графа зависимостей.
- Максимальная глубина анализа зависимостей.

Все функции визуализатора зависимостей должны быть покрыты тестами.

Сгенерированный граф зависимостей глубины = 2

![dependencies_graph](https://github.com/user-attachments/assets/8fc48a8a-b271-47bb-98a9-8ac550c64df3)


# Задание №3

Разработать инструмент командной строки для учебного конфигурационного языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из входного формата в выходной. Синтаксические ошибки выявляются с выдачей сообщений.

Входной текст на учебном конфигурационном языке принимается из файла, путь к которому задан ключом командной строки. Выходной текст на языке `toml` попадает в файл, путь к которому задан ключом командной строки.

Многострочные комментарии:


Это многострочный 
комментарий 


Словари:

имя = значение; 
имя = значение; 
имя = значение; 
...


Имена:

[a-z]+


Значения:
- Числа.
- Строки.
- Словари.

Строки:

"Это строка"


Объявление константы на этапе трансляции:

имя = значение


Вычисление константы на этапе трансляции:

.[имя].


Результатом вычисления константного выражения является значение.

Все конструкции учебного конфигурационного языка (с учетом их возможной вложенности) должны быть покрыты тестами. Необходимо показать 3 примера описания конфигураций из разных предметных областей.

Входные файлы:
1)conf1.txt

![image](https://github.com/user-attachments/assets/108f77e1-3443-48f8-a4fb-5e740737e8ae)

2)conf2.txt

![image](https://github.com/user-attachments/assets/3012eff5-8a20-4aa4-a4ad-1b41dba254aa)

3)conf3.txt

![image](https://github.com/user-attachments/assets/2c8844a3-49fa-4017-aef1-f811bd7c1007)

Результаты запуска программы

1)./main.py --input conf1.txt --output conf1.toml

![image](https://github.com/user-attachments/assets/41983a72-7aac-4580-bfd1-b0ba2ef653d5)

2)./main.py --input conf2.txt --output conf2.toml

![image](https://github.com/user-attachments/assets/401ac336-c0ec-43dc-b031-0ac0b4e0dcf1)

3)./main.py --input conf3.txt --output conf3.toml

![image](https://github.com/user-attachments/assets/f2811421-ea2c-4863-ac52-596b0962e56d)

# Задание №4

Разработать ассемблер и интерпретатор для учебной виртуальной машины (УВМ). Система команд УВМ представлена далее.

Для ассемблера необходимо разработать читаемое представление команд УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к которой задается из командной строки. Результатом работы ассемблера является бинарный файл в виде последовательности байт, путь к которому задается из командной строки. Дополнительный ключ командной строки задает путь к файлу логу, в котором хранятся ассемблированные инструкции в духе списков `ключ=значение`, как в приведенных далее тестах.

Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон также указывается из командной строки.

Форматом для файла-лога и файла-результата является `json`.

Необходимо реализовать приведенные тесты для всех команд, а также написать и отладить тестовую программу.

## Загрузка константы
- **A** - Биты 0—3
- **B** - Биты 4—32
- Размер команды: 5 байт. Операнд: поле B. Результат: регистр-аккумулятор.

**Тест (A=5, B=148):**

0x45, 0x09, 0x00, 0x00, 0x00


## Чтение значения из памяти
- **A** - Биты 0—3
- **B** - Биты 4—9
- Размер команды: 5 байт. Операнд: значение в памяти по адресу, которым является сумма адреса (регистр-аккумулятор) и смещения (поле B). Результат: регистр-аккумулятор.

**Тест (A=15, B=20):**

0x4F, 0x01, 0x00, 0x00, 0x00


## Запись значения в память
- **A** - Биты 0—3
- **B** - Биты 4—16
- Размер команды: 5 байт. Операнд: регистр-аккумулятор. Результат: значение в памяти по адресу, которым является поле B.

**Тест (A=12, B=547):**

0x3C, 0x22, 0x00, 0x00, 0x00


## Бинарная операция: умножение
- **A** - Биты 0—3
- **B** - Биты 4—16
- Размер команды: 5 байт. Первый операнд: регистр-аккумулятор. Второй операнд: значение в памяти по адресу, которым является поле B. Результат: регистр-аккумулятор.

**Тест (A=11, B=762):**

0xAB, 0x2F, 0x00, 0x00, 0x00


## Тестовая программа

Выполнить поэлементно операцию умножение над двумя векторами длины 5. Результат записать во второй вектор.

Входной файл program.txt:
```
LOAD_CONST 5 1
WRITE_MEM 12 10
LOAD_CONST 5 2
WRITE_MEM 12 11
LOAD_CONST 5 3
WRITE_MEM 12 12
LOAD_CONST 5 4
WRITE_MEM 12 13
LOAD_CONST 5 5
WRITE_MEM 12 14
LOAD_CONST 5 100
WRITE_MEM 12 20
LOAD_CONST 5 200
WRITE_MEM 12 21
LOAD_CONST 5 300
WRITE_MEM 12 22
LOAD_CONST 5 400
WRITE_MEM 12 23
LOAD_CONST 5 500
WRITE_MEM 12 24
LOAD_CONST 5 0
LOAD_MEM 15 10
MUL 11 20
WRITE_MEM 12 20
LOAD_CONST 5 0
LOAD_MEM 15 11
MUL 11 21
WRITE_MEM 12 21
LOAD_CONST 5 0
LOAD_MEM 15 12
MUL 11 22
WRITE_MEM 12 22
LOAD_CONST 5 0
LOAD_MEM 15 13
MUL 11 23
WRITE_MEM 12 23
LOAD_CONST 5 0
LOAD_MEM 15 14
MUL 11 24
WRITE_MEM 12 24
LOAD_CONST 5 0
```
Запуск команд 

1)./assembler.py --input program.txt --output program.bin --log log.json

2)./interpreter.py --binary program.bin --result result.json --range 0-100

Выходной файл result.txt:
```
{
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 1,
    "11": 2,
    "12": 3,
    "13": 4,
    "14": 5,
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 100,
    "21": 400,
    "22": 900,
    "23": 1600,
    "24": 2500,
    "25": 0,
    "26": 0,
    "27": 0,
    "28": 0,
    "29": 0,
    "30": 0,
    "31": 0,
    "32": 0,
    "33": 0,
    "34": 0,
    "35": 0,
    "36": 0,
    "37": 0,
    "38": 0,
    "39": 0,
    "40": 0,
    "41": 0,
    "42": 0,
    "43": 0,
    "44": 0,
    "45": 0,
    "46": 0,
    "47": 0,
    "48": 0,
    "49": 0,
    "50": 0,
    "51": 0,
    "52": 0,
    "53": 0,
    "54": 0,
    "55": 0,
    "56": 0,
    "57": 0,
    "58": 0,
    "59": 0,
    "60": 0,
    "61": 0,
    "62": 0,
    "63": 0,
    "64": 0,
    "65": 0,
    "66": 0,
    "67": 0,
    "68": 0,
    "69": 0,
    "70": 0,
    "71": 0,
    "72": 0,
    "73": 0,
    "74": 0,
    "75": 0,
    "76": 0,
    "77": 0,
    "78": 0,
    "79": 0,
    "80": 0,
    "81": 0,
    "82": 0,
    "83": 0,
    "84": 0,
    "85": 0,
    "86": 0,
    "87": 0,
    "88": 0,
    "89": 0,
    "90": 0,
    "91": 0,
    "92": 0,
    "93": 0,
    "94": 0,
    "95": 0,
    "96": 0,
    "97": 0,
    "98": 0,
    "99": 0,
    "100": 0
}
```


