from flask import Flask, render_template, request
import sys
import io

app = Flask(__name__)

# Главная страница
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
            result = str(e)  # Если ошибка, выводим её
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
