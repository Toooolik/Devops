# lab-4
1. Перенаправив вивід в my_work.log:
   - sudo docker -v > my_work.log
   - sudo docker -h >> my_work.log
   - sudo docker run docker/whalesay cowsay Docker is fun >> my_work.log
1. 
    - **Виконав команди:**
        - "sudo docker pull python:3.8-slim"
        - "sudo docker images"
        - "sudo docker inspect python:3.8-slim"
   - **Створив файл з іменем Dockerfile;**
   - **Замінив посилання на власний Git репозиторій**
   - **Виконав команди:**
        - sudo docker build -t toooolik/lab4:django .
        - sudo docker images
        - sudo docker push toooolik/lab4:django 
1. Посилання на репозиторій та імедж:
    - [repo](https://hub.docker.com/repository/docker/toooolik/lab4)
    - [django image](https://hub.docker.com/layers/131234949/toooolik/lab4/django/images/sha256-aeefaf7f2f51ff7d6429addf914f6f74321bd4d87f2e9c84e87db766b9325ce9?context=explore)

1. Веб-сайт працює

1. Створив Dockerfile.site
1. Виконав білд імеджа:
   - sudo docker build -f Dockerfile.site -t toooolik/lab4:monitoring .
   - sudo docker images
   - sudo docker push  toooolik/lab4:monitoring

1. Посилання на імедж:
    - [monitoring image](https://hub.docker.com/layers/131235795/toooolik/lab4/monitoring/images/sha256-65598b2a58a03402832937dc394ea054d21477ade95cf9ca4def24df425a8132?context=explore)
   
1. Логи:   
   - sudo docker run -it --rm -p 8000:8000 toooolik/lab4:django
   - sudo docker run -it --rm --net=host -v $(pwd)/server.log:/app/server.log toooolik/lab4:monitoring
   
