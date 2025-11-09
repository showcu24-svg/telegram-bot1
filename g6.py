from aiogram import Bot, Dispatcher, F  # type: ignore
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton  # type: ignore
from aiogram.filters import CommandStart  # type: ignore
import asyncio

BOT_TOKEN = "8316008530:AAFwHgcXoUjvdHKJi56v7hYFkrgnUwfBNNI"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[  # <-- должно быть с маленькой буквы!
            [KeyboardButton(text="print()")],
            [KeyboardButton(text="input()")],
            [KeyboardButton(text="sep")],
            [KeyboardButton(text="end")],
            [KeyboardButton(text="map()")],
            [KeyboardButton(text="sum()")],
            [KeyboardButton(text="split()")],
            [KeyboardButton(text="Вложенные циклы")],
            [KeyboardButton(text="While")],
            [KeyboardButton(text="lower()")],
            [KeyboardButton(text="upper()")],
            [KeyboardButton(text="math")],
            [KeyboardButton(text="break")],
            [KeyboardButton(text="continue")]

        ],
        resize_keyboard=True  # <-- тут была опечатка: было resize_keybooard
    )
    await message.answer("Добро пожаловать! Выберите опцию, которая вас интересует:", reply_markup=keyboard)


@dp.message(F.text == "print()")
async def print_info(message: Message):
    await message.answer(
        " *print()* — это встроенная команда Python, которая выводит данные на экран.\n\n"
        "Она может показывать текст, числа, результаты вычислений и значения переменных.\n"
        "После каждого вызова *print()* курсор по умолчанию переходит на новую строку.\n\n"
        " Пример:\n"
        "```python\n"
        "print('Привет, мир!')\n"
        "print(2 + 3)\n"
        "```",
        parse_mode="Markdown"
    )


@dp.message(F.text == "input()")
async def input_info(message: Message):
    await message.answer(
        " *input()* — это встроенная команда Python, которая позволяет пользователю вводить данные с клавиатуры.\n\n"
        "Когда программа доходит до *input()*, она приостанавливается и ждёт, пока пользователь что-то введёт.\n\n"
        " Пример:\n"
        "```python\n"
        "name = input('Введите имя: ')\n"
        "print('Привет,', name)\n"
        "```\n"
        "Если пользователь введёт:\n"
        "```\n"
        "Алина\n"
        "```\n"
        "То программа выведет:\n"
        "```\n"
        "Привет, Алина\n"
        "```",
        parse_mode="Markdown"
    )


@dp.message(F.text == "sep")
async def sep_info(message: Message):
    await message.answer(
        " *sep* — это параметр функции *print()*, который задаёт символ (или строку), "
        "разделяющий элементы при выводе.\n\n"
        "По умолчанию *sep=' '* — между элементами ставится пробел.\n\n"
        " Пример:\n"
        "```python\n"
        "print('A', 'B', 'C')           # A B C\n"
        "print('A', 'B', 'C', sep='-')  # A-B-C\n"
        "print('1', '2', '3', sep='')   # 123\n"
        "```",
        parse_mode="Markdown"
    )



@dp.message(F.text == "range")
async def range_info(message: Message):
    await message.answer(
        " *range()* — это встроенная функция Python, которая создаёт последовательность чисел.\n\n"
        "Её часто используют в циклах *for*, чтобы выполнить действие несколько раз.\n\n"
        " Синтаксис:\n"
        "`range(конец)` — от 0 до конца (не включая конец)\n"
        "`range(начало, конец)` — от начала до конца (не включая конец)\n"
        "`range(начало, конец, шаг)` — с указанием шага между числами\n\n"
        " Примеры:\n"
        "```python\n"
        "for i in range(5):\n"
        "    print(i)\n"
        "# Вывод: 0 1 2 3 4\n\n"
        "for i in range(2, 6):\n"
        "    print(i)\n"
        "# Вывод: 2 3 4 5\n\n"
        "for i in range(1, 10, 2):\n"
        "    print(i)\n"
        "# Вывод: 1 3 5 7 9\n"
        "```",
        parse_mode="Markdown"
    )




@dp.message(F.text == "end")
async def end_info(message: Message):
    await message.answer(
        " *end* — это параметр функции *print()*, который определяет, что будет добавлено "
        "в конце вывода вместо перехода на новую строку.\n\n"
        "По умолчанию *end='\\n'* — то есть после каждого *print()* курсор переходит на новую строку.\n\n"
        " Пример:\n"
        "```python\n"
        "print('Привет', end='! ')\n"
        "print('Как дела?')\n"
        "# Вывод: Привет! Как дела?\n\n"
        "print('1', end='')\n"
        "print('2', end='')\n"
        "print('3')\n"
        "# Вывод: 123\n"
        "```",
        parse_mode="Markdown"
    )




@dp.message(F.text == "map()")
async def map_info(message: Message):
    await message.answer(
        " *map()* — это встроенная функция Python, которая применяет указанную функцию к каждому элементу последовательности.\n\n"
        "Она возвращает специальный объект *map*, который можно превратить в список или использовать в цикле.\n\n"
        " Синтаксис:\n"
        "`map(функция, последовательность)`\n\n"
        " Примеры:\n"
        "```python\n"
        "# Умножаем все числа на 2\n"
        "numbers = [1, 2, 3, 4]\n"
        "result = map(lambda x: x * 2, numbers)\n"
        "print(list(result))\n"
        "# Вывод: [2, 4, 6, 8]\n\n"
        "# Преобразуем строки в числа\n"
        "strings = ['1', '2', '3']\n"
        "nums = map(int, strings)\n"
        "print(list(nums))\n"
        "# Вывод: [1, 2, 3]\n"
        "```",
        parse_mode="Markdown"
    )





@dp.message(F.text == "sum()")
async def sum_info(message: Message):
    await message.answer(
        " *sum()* — это встроенная функция Python, которая считает сумму всех элементов последовательности (например, списка или кортежа).\n\n"
        " Синтаксис:\n"
        "`sum(последовательность, начальное_значение=0)`\n\n"
        "Если указать *начальное_значение*, оно прибавляется к результату.\n\n"
        " Примеры:\n"
        "```python\n"
        "numbers = [1, 2, 3, 4, 5]\n"
        "print(sum(numbers))\n"
        "# Вывод: 15\n\n"
        "print(sum(numbers, 10))\n"
        "# Вывод: 25 (так как 15 + 10)\n\n"
        "print(sum(range(4)))\n"
        "# Вывод: 6 (0 + 1 + 2 + 3)\n"
        "```",
        parse_mode="Markdown"
    )





@dp.message(F.text == "split()")
async def split_info(message: Message):
    await message.answer(
        " *split()* — это метод строк в Python, который разделяет строку на части (список слов) по указанному разделителю.\n\n"
        " Синтаксис:\n"
        "`строка.split(разделитель, макс_разбиений)`\n\n"
        "Если *разделитель* не указан, строка делится по пробелам.\n"
        "Если указать *макс_разбиений*, строка разделится только это количество раз.\n\n"
        " Примеры:\n"
        "```python\n"
        "text = 'яблоко банан вишня'\n"
        "print(text.split())\n"
        "# Вывод: ['яблоко', 'банан', 'вишня']\n\n"
        "data = '1,2,3,4'\n"
        "print(data.split(','))\n"
        "# Вывод: ['1', '2', '3', '4']\n\n"
        "info = 'имя:возраст:город'\n"
        "print(info.split(':', 1))\n"
        "# Вывод: ['имя', 'возраст:город']\n"
        "```",
        parse_mode="Markdown"
    )






@dp.message(F.text == "Вложенные циклы")
async def nested_loops_info(message: Message):
    await message.answer(
        " *Вложенные циклы* — это циклы, которые находятся внутри других циклов.\n\n"
        "Они используются, когда нужно выполнять повторяющиеся действия в нескольких измерениях, например, при работе с таблицами, матрицами или координатами.\n\n"
        " Синтаксис:\n"
        "```python\n"
        "for i in range(внешний_цикл):\n"
        "    for j in range(внутренний_цикл):\n"
        "        # действия\n"
        "```\n\n"
        " Примеры:\n"
        "```python\n"
        "for i in range(3):\n"
        "    for j in range(2):\n"
        "        print(i, j)\n"
        "# Вывод:\n"
        "# 0 0\n"
        "# 0 1\n"
        "# 1 0\n"
        "# 1 1\n"
        "# 2 0\n"
        "# 2 1\n\n"
        "for i in range(1, 4):\n"
        "    for j in range(1, 4):\n"
        "        print(i * j, end=' ')\n"
        "    print()\n"
        "# Вывод:\n"
        "# 1 2 3\n"
        "# 2 4 6\n"
        "# 3 6 9\n"
        "```",
        parse_mode="Markdown"
    )






@dp.message(F.text == "while")
async def while_info(message: Message):
    await message.answer(
        " *while* — это цикл в Python, который выполняет блок кода, пока условие остаётся истинным (*True*).\n\n"
        "Он используется, когда заранее неизвестно, сколько раз нужно повторить действие — цикл работает, пока выполняется условие.\n\n"
        " Синтаксис:\n"
        "```python\n"
        "while условие:\n"
        "    # действия, которые повторяются\n"
        "```\n\n"
        " Примеры:\n"
        "```python\n"
        "i = 0\n"
        "while i < 5:\n"
        "    print(i)\n"
        "    i += 1\n"
        "# Вывод: 0 1 2 3 4\n\n"
        "x = 10\n"
        "while x > 0:\n"
        "    print(x)\n"
        "    x -= 2\n"
        "# Вывод: 10 8 6 4 2\n"
        "```\n\n"
        " Если условие всегда остаётся *True*, программа зациклится (будет выполняться бесконечно).",
        parse_mode="Markdown"
    )




@dp.message(F.text == "lower()")
async def lower_info(message: Message):
    await message.answer(
        " *lower()* — это метод строк в Python, который возвращает копию строки, "
        "где все буквы преобразованы в нижний регистр (маленькие буквы).\n\n"
        " Синтаксис:\n"
        "`строка.lower()`\n\n"
        " Примеры:\n"
        "```python\n"
        "text = 'HELLO WORLD'\n"
        "print(text.lower())\n"
        "# Вывод: hello world\n\n"
        "word = 'PyThOn'\n"
        "print(word.lower())\n"
        "# Вывод: python\n"
        "```\n\n"
        " Часто используется для сравнения строк без учёта регистра, например:\n"
        "```python\n"
        "s = input('Введите да/нет: ')\n"
        "if s.lower() == 'да':\n"
        "    print('Вы согласились!')\n"
        "```\n"
        "Тогда неважно, как пользователь напишет — *ДА*, *Да* или *да*.",
        parse_mode="Markdown"
    )





@dp.message(F.text == "upper()")
async def upper_info(message: Message):
    await message.answer(
        " *upper()* — это метод строк в Python, который возвращает копию строки, "
        "где все буквы преобразованы в верхний регистр (большие буквы).\n\n"
        " Синтаксис:\n"
        "`строка.upper()`\n\n"
        " Примеры:\n"
        "```python\n"
        "text = 'hello world'\n"
        "print(text.upper())\n"
        "# Вывод: HELLO WORLD\n\n"
        "word = 'Python'\n"
        "print(word.upper())\n"
        "# Вывод: PYTHON\n"
        "```\n\n"
        " Часто используется, когда нужно привести текст к одному формату, например:\n"
        "```python\n"
        "s = input('Введите слово: ')\n"
        "print('Ваше слово в верхнем регистре:', s.upper())\n"
        "```\n"
        "Тогда ввод *python* или *PyThOn* будет выведен как *PYTHON*.",
        parse_mode="Markdown"
    )


@dp.message(F.text == "math")
async def math_info(message: Message):
    await message.answer(
        " *Библиотека math* — это стандартный модуль Python, который содержит множество математических функций и констант.\n\n"
        " С помощью команды:\n"
        "`from math import *`\n"
        "можно импортировать все функции из модуля math сразу, чтобы использовать их без указания `math.` перед именем.\n\n"
        " Примеры:\n"
        "```python\n"
        "from math import *\n\n"
        "print(sqrt(25))      # Квадратный корень → 5.0\n"
        "print(factorial(5))  # Факториал → 120\n"
        "print(pi)            # Константа числа π → 3.1415926535\n"
        "print(sin(0))        # Синус угла 0 → 0.0\n"
        "```\n\n"
        " Основные функции:\n"
        "- `sqrt(x)` — квадратный корень\n"
        "- `pow(x, y)` — возведение в степень\n"
        "- `sin(x), cos(x), tan(x)` — тригонометрия\n"
        "- `factorial(x)` — факториал числа\n"
        "- `pi, e` — математические константы\n\n"
        " Если ты используешь `import math`, то нужно писать `math.sqrt(25)` вместо просто `sqrt(25)`.",
        parse_mode="Markdown"
    )


@dp.message(F.text == "break")
async def break_info(message: Message):
    await message.answer(
        " *Оператор break* — используется в циклах `for` и `while`, чтобы *прервать выполнение цикла досрочно*.\n\n"
        "Когда программа встречает `break`, цикл сразу останавливается, даже если его условие ещё не стало ложным.\n\n"
        " Пример с циклом for:\n"
        "```python\n"
        "for i in range(1, 10):\n"
        "    if i == 5:\n"
        "        break\n"
        "    print(i)\n"
        "# Вывод: 1 2 3 4\n"
        "```\n"
        " Пример с while:\n"
        "```python\n"
        "count = 0\n"
        "while True:\n"
        "    count += 1\n"
        "    if count == 3:\n"
        "        break\n"
        "    print(count)\n"
        "# Вывод: 1 2\n"
        "```\n"
        " `break` удобно использовать, когда нужно остановить цикл при выполнении определённого условия.",
        parse_mode="Markdown"
    )

@dp.message(F.text == "continue")
async def continue_info(message: Message):
    await message.answer(
        " *Оператор continue* — используется в циклах `for` и `while`, чтобы *пропустить текущую итерацию* и перейти к следующей.\n\n"
        "Когда программа встречает `continue`, выполнение тела цикла прекращается только для текущего прохода, а цикл продолжается дальше.\n\n"
        " Пример с циклом for:\n"
        "```python\n"
        "for i in range(1, 6):\n"
        "    if i == 3:\n"
        "        continue\n"
        "    print(i)\n"
        "# Вывод: 1 2 4 5\n"
        "```\n"
        " Пример с while:\n"
        "```python\n"
        "i = 0\n"
        "while i < 5:\n"
        "    i += 1\n"
        "    if i == 2:\n" 
        "        continue\n"
        "    print(i)\n"
        "# Вывод: 1 3 4 5\n"
        "```\n"
        " `continue` полезен, когда нужно пропустить отдельные случаи, но не останавливать весь цикл.",
        parse_mode="Markdown"
    )

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())