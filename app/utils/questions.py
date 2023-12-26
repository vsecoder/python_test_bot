questions = [
    {
        "text": (
            "Что будет показано в результате?\n"
            "<pre><code class=\"language-python\">name = \"John\"\nprint('Hi, %s' % name)</code></pre>"
        ),
        "variants": ["Hi, ", "Error", "Hi, John", "Hi, name"],
        "answer": "Hi, John"
    },
    {
        "text": (
            "Какая библиотека отвечает за время?"
        ),
        "variants": ["clock", "time", "localtime", "telebot"],
        "answer": "time"
    },
    {
        "text": (
            "Какая функция выводит что-либо в консоль?"
        ),
        "variants": ["write", "print", "out", "log"],
        "answer": "print"
    },
    {
        "text": (
            "Что покажет этот код?\n"
            "<pre><code class=\"language-python\">for j in 'Hi! I\\'m mister Robert':\n	if j == '\\'':\n	  print("
            "\"Найдено\")\n	  break\nelse:\n	print(\"Готово\")</code></pre>"
        ),
        "variants": ["Готово", "Найдено", "Ошибка", "Ничего"],
        "answer": "Найдено"
    },
    {
        "text": (
            "Где правильно создана переменная?"
        ),
        "variants": ["int num = 2", "нет правильного", "$num = 2", "num = float(2)"],
        "answer": "num = float(2)"
    },
    {
        "text": (
            "Что покажет этот код?\n"
            "<pre><code class=\"language-python\">x = 23\nnum = 0 if x > 10 else 11\nprint(num)</code></pre>"
        ),
        "variants": ["0", "11", "23", "Ошибка"],
        "answer": "0"
    },
    {
        "text": (
            "Сколько библиотек можно импортировать в один проект?"
        ),
        "variants": ["< 3", "< 10", "< 50", "Неограниченное количество"],
        "answer": "Неограниченное количество"
    },
    {
        "text": (
            "Имеется кортеж вида <code>T = (4, 2, 3)</code>. Какая из операций приведёт к тому, "
            "что имя T будет ссылаться на кортеж <code>(1, 2, 3)</code>?"
        ),
        "variants": ["T[0] = 1", "T = (1) + T[1:]", "T = (1,) + T[1:]", "T.startswith(1)"],
        "answer": "T = (1) + T[1:]"
    },
    {
        "text": (
            "Необходимо собрать и вывести все уникальные слова из строки рекламного текста. Какой из перечисленных "
            "типов данных Python подходит лучше всего?"
        ),
        "variants": ["tuple", "list", "set", "dict"],
        "answer": "set"
    },
    {
        "text": (
            "Как можно более кратко представить следующую запись?"
            "<pre><code class=\"language-python\">if X:\n    A = Y\nelse:\n    A = Z</code></pre>"
        ),
        "variants": ["A = Y if Z else Y", "A = Y if X else Z", "A = X if Z else Y", "A = X if Y else Z"],
        "answer": "A = Y if X else Z"
    }
]
