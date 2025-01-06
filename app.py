from flask import Flask, render_template_string, request
import sys
import io

app = Flask(__name__)

# HTML-шаблон для страницы
html_template = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chald School</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f9;
        }
        textarea {
            width: 100%;
            height: 200px;
            font-size: 16px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        pre {
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 5px;
            font-size: 16px;
            color: #333;
        }
    </style>
</head>
<body>

    <h1>Рабочая Площадь Python</h1>
    <form method="post">
        <textarea name="user_code" placeholder="Введите код Python здесь..."></textarea><br>
        <button type="submit">Выполнить</button>
    </form>

    {% if result %}
        <h3>Результат выполнения:</h3>
        <pre>{{ result }}</pre>
    {% endif %}

</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        user_code = request.form['user_code']
        try:
            # Перехватываем вывод программы
            old_stdout = sys.stdout
            sys.stdout = io.StringIO()
            exec(user_code)  # Выполнение кода пользователя
            result = sys.stdout.getvalue()  # Получаем результат выполнения
            sys.stdout = old_stdout  # Восстановление вывода
        except Exception as e:
            result = f"Ошибка выполнения: {e}"  # Если ошибка, выводим её
    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
