# lab-5
---
## Makefile
---
1. Створив папки `my_app`, `tests`.
2. Перевірив проект на працездатність , виконуючи наступні команди:
   - pipenv --python 3.8
   - pipenv install -r requirements.txt
   - pipenv run python3 app.py
   - pipenv run pytest test_app.py --url http://localhost:5000
   
3. Видалив всі файли, що створились в процесі запуску.
   - Веб-сайт не працює
   
4. Створив Dockerfile.app, Dockerfile.tests, Makefile.
5. Ознайомився із вмістом Dockerfile та Makefile та його директивами:
    - `STATES` - змінні які містить назви тегів
    - `REPO` -  містить назву Docker Hub репозиторію;
    - `.PHONY` - вказує файлу, що переліченні нище цілі не є файлами;
    - `$(STATES)` - ціль, призначення для білду контейнера;
    - `run` - ціль, призначення для створення мережі, у якій буде працювати додаток; запуску додатку і сховища `redis`;
    - `test-app` - запуск контейнера тестової програми;
    - `docker-prune` -очистка ресурсів, що бути використанні при роботі `Docker`.
6. Створив Docker імеджі для додатку та для тестів:
    - sudo make .PHONY
7. Запустив додаток, відкрив новий термінал та запустив тести:
    - sudo make run
    - sudo make test-app
    - sudo тести пройшли успішно:
    - sudo кожна сторінка веб-сайту працює:

8. Очистив всі ресурси Docker:
    - sudo make docker-prune
9. Створив директиву в `Makefile` для завантаження створених імеджів у Docker Hub репозиторій:
    ```
    push:
	  @docker push $(REPO):app
	  @docker push $(REPO):tests
    ```
    - [lab-5](https://hub.docker.com/repository/docker/toooolik/lab5);

10. Створив директиву `delete-images`:
   ```
   delete-images:
      @docker rmi --force $$(docker images -q)
   ```

## Docker-compose
---
1. Створив файл `docker-compose.yaml`.
2. Запустив `docker-compose`:
    - sudo docker-compose -p lab-5 up
3. Веб-сайт працює. 
   - адреса:
     - http://0.0.0.0:80.

4. Імеджі мають теги `compose-tests`, `compose-app`.
5. Зупинив проект і очистив ресурси скомандою:
   - sudo `docker-compose down`.
6. Завантажив створені імеджі до `Docker Hub` репозиторію за допомогою команди:
    - docker-compose push
## Home task
---
1. Для багатоконтейнерної структури краще використовувати `docker-compose`, А для простіших випадків підійде `Makefile`
2. Створив `docker-compose.yaml` для лабораторної №4:
   - Запустив `docker-compose.yaml`:
        - sudo docker-compose -p lab-4 up
   - Веб-сайт працює
   - Зупинив проект і очистив ресурси:
      - sudo docker-compose down
           
   - Завантажив створені імеджі до `Docker Hub`
      - docker-compose push
      - [lab-4](https://hub.docker.com/repository/docker/toooolik/lab5)
