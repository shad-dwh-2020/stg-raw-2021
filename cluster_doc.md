# Инструкция по работе с кластером
## Общие характеристики
Данный кластер настроен с помощью сервиса Yandex.Dataproc и обладает такими характеристиками:

|Роль|Внутренний FQDN|HDD|RAM|CPU|
|--|--|--|--|--|
|Proxy|dwh-client|50 Gb|8 Gb|4 vCores|
|Клиент, рабочая нода|rc1b-dataproc-d-lzm4o9chywpb41wf|256 Gb|32 Gb|8 vCores|
|Рабочая нода|rc1b-dataproc-d-mqvc5o0r3nj3495n|256 Gb|32 Gb|8 vCores|
|Рабочая нода|rc1b-dataproc-d-wslss4xenr8yflcj|256 Gb|32 Gb|8 vCores|
|Рабочая нода|rc1b-dataproc-d-wslss4xenr8yflcj|256 Gb|32 Gb|8 vCores|
|Мастер|rc1b-dataproc-m-92h20458xqb2ed5k|384 Gb|64 Gb|16 vCores|

## Как получить доступ
В данной [таблице](https://docs.google.com/spreadsheets/d/e/2PACX-1vTh0gOlurM1Sd7ViwwCIlkSY4BupTmGJ8zj1MEXSGYdzhkqXvhAUYooUhVU9TnkMJlBJCy60TZ4y0rr/pubhtml?gid=2075869425&single=true) доступен список логинов. Пароль у всех одинковый: `writtenonce`, поэтому первым делом сбросьте его.
#### Как сбросить пароль
1. Зайдите на сервер dwh-client.velkerr.ru: `ssh <USER>@dwh-client.velkerr.ru`
2. Введите команду `passwd`, введите старый пароль (`writtenonce`) и 2 раза новый пароль.
3. Не выходя из dwh-client.velkerr.ru, введите `ssh rc1b-dataproc-d-lzm4o9chywpb41wf.mdb.yandexcloud.net`.
4. В открывшейся сессии повторите пункт 2.
5. Выйдите из всех сессий (2 раза Ctrl+D).
#### Как войти
1. Создайте файл `.ssh/config`.
2. Запишите туда строчки:
```
Host dwh-hadoop
    User dwh2021XX
    ProxyCommand ssh -o IdentitiesOnly=yes dwh2021XX@dwh-client.velkerr.ru -W rc1b-dataproc-d-lzm4o9chywpb41wf.mdb.yandexcloud.net:22
```
где XX - 01, 02...

3. Заходите командой `ssh dwh-hadoop` и вводите пароль 2 раза.
4. **Troubleshooting**. 
  - при первой авторизации сервер будет сохранять fingerprint. Выдастся 2 диалоговых окна, где нужно 2 раза ввести yes.
  - Если выдается ошибка "Too many authentication failures", заходите так: `ssh -o IdentitiesOnly=yes dwh-hadoop`.

#### Проброс портов

Список доступных портов можно увидеть [здесь](https://cloud.yandex.ru/docs/data-proc/concepts/interfaces#port-numbers). На курсе вам в основном понадобятся UI Hadoop и Spark. Для их проброса используйте такую команду
```bash
ssh -o IdentitiesOnly=yes -A -J <USER>@dwh-client.velkerr.ru -L 19888:rc1b-taproc-m-92h20458xqb2ed5k:19888 -L 18080:rc1b-dataproc-m-92h20458xqb2ed5k:18080 -L 8088:rc1b-dataproc-m-92h20458xqb2ed5k:8088 -L 8188:rc1b-dataproc-m-92h20458xqb2ed5k:8188 -L 9870:rc1b-dataproc-m-92h20458xqb2ed5k:9870 <USER>@rc1b-dataproc-d-lzm4o9chywpb41wf.mdb.yandexcloud.net
```

