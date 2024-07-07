# Pytest - тестування API з використанням Python `requests`

#### Pytest - це зрілий і повнофункціональний фреймворк для написання та запуску тестів на Python.

#### Модуль `requests` дозволяє відправляти HTTP-запити за допомогою Python.

## Початок роботи

       
* Для завантаження та встановлення `pytest`, виконайте цю команду в терміналі: `python3.9 -m venv venv`
* Для завантаження та встановлення `pytest`, виконайте цю команду в терміналі: `pip install pytest`
* Для завантаження та встановлення `requests`, виконайте цю команду в терміналі: `pip install requests`

Щоб забезпечити вирішення всіх залежностей у CI-середовищі, додайте їх до файлу `requirements.txt`.
* Потім виконайте наступну команду: `pip install -r requirements.txt`

За замовчуванням pytest визначає файли тестів за іменами, що починаються на `test_` або закінчуються на `_test`.

Pytest вимагає, щоб назви методів тестів починалися з `test`. Усі інші назви методів будуть проігноровані, навіть якщо ми явно вказуємо на їх виконання.

Приклад тесту:

```python
def test_fetch_user():
    path = "api/users/2"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert jsonpath.jsonpath(responseJson, '$.data.first_name')[0] == 'Janet'
    assert jsonpath.jsonpath(responseJson, '$.data.id')[0] == 2
