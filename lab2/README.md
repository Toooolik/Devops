# Lab-2

1. За допомогою пакетного менеджера *PIP* встановив *pipenv* та створив ізольоване середовище для Python:

     *pip3 install pipenv*
     *pipenv --python 3.8*
     *pipenv shell*
2. Встановив бібліотеки:

     *pipenv install requests
     *pipenv install ntplib
3. Створив файл *app.py*, протестував та запустив, програма працює правильно.
4. Для тестування встановив бібліотеку *pytest*, запустив тести, всі тести виконались успішно:
     *pipenv install pytest
     *pytest tests/tests.py
5. Дописав у програмі функцію, яка буде перевіряти час доби AM/PM та відповідно друкувати "Доброго дня/ночі". Також написав тест, який перевіряє правильність роботи функції.
6. Виконання функції та тестів перенаправив у файл *results.txt*:
     *pipenv run pytest tests/tests.py > results.txt
     *pipenv run python app.py append >> results.txt
7. Написав makefile для сховища. 
