# Быстрый старт

## Последовательность подготовки к работе

1. Установка компонентов
2. Активируйте окружение и все сопутствующие компоненты
3. Приступите к решению задания, используя клиентскую часть окружения

## Установка компонентов

### 0. Установка всего и сразу

  Для Windows:
  ```shell
  powershell -ExecutionPolicy ByPass -c "irm https://gitflic.ru/project/lct-prefinal/lct-prefinal/blob/raw?file=scripts%2Finstall_win.ps1 | iex"
  ```

  Для Linux:
  ```shell
  curl -LsSf "https://gitflic.ru/project/lct-prefinal/lct-prefinal/blob/raw?file=scripts%2Finstall_linux.sh" | sh
  ```
  > После этого можете сразу переходить к использованию - всё уже готово.

### 1. Установка ЦД - вручную

  Для Windows:
  ```
  # Используйте готовый бинарный файл twin.exe, расположенный в директории с ЦД
  ```

  Для Linux:
  ```shell
  sudo chmod +x LCT.x86_64
  ```

### 2. Установка АСО - вручную

  Для Windows:
  ```shell
    # Разрешение нужно для запуска скрипта установки
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  
    git clone https://gitflic.ru/project/lct-prefinal/lct-ats.git
    cd lct-ats
    uv sync
  ```

  Для Linux:
  ```shell
    curl -LsSf https://astral.sh/uv/install.sh | sh
  
    git clone https://gitflic.ru/project/lct-prefinal/lct-ats.git
    cd lct-ats
    uv sync
  ```

### 3. Установка Клиента - вручную

  Для Windows:
  ```shell
    git clone https://gitflic.ru/project/lct-prefinal/lct-client.git
    cd lct-client
    uv sync
  ```

  Для Linux:
  ```shell
    git clone https://gitflic.ru/project/lct-prefinal/lct-client.git
    cd lct-client
    uv sync
  ```

## Активация окружения

### 0. Запуск всего и сразу

Для Windows:
  ```shell
  # В директории с папками lct-prefinal, LCT_win64, ltc-ats и lct-client
  powershell -ExecutionPolicy ByPass -c "./lct-prefinal/scripts/start_win.ps1"
  ```

Для Linux:
  ```shell
  # В директории с папками lct-prefinal, LCT_linux, ltc-ats и lct-client
  ./lct-prefinal/scripts/start_linux.sh
  ```
> После этого можете сразу переходить к использованию - всё уже готово.

### 1. Запуск Цифрового двойника

  Для Windows:
  ```shell
  # В директории с ЦД
  ./twin.exe
  ```
  
  Для Linux:
  ```shell
  # В директории с ЦД
  ./twin.x86_64
  ```

### 2. Запуск АСО
  ```shell
  # В директории с АСО
  uv run launcher.py --twin
  ```

### 3. Запуск Клиента
  ```shell
  # В директории с Клиентом
  uv run jupyter notebook
  ```
> Скрипт запуска отобразит адрес, по которому вы сможете подключиться к серверу Jupyter Notebook клиента.

> Для работы вам нужен файл `whole_code.ipynb`.

## Решение задания

### 1. Изучите полигон и роботов
### 2. Изучите дополнительную документацию

В зависимости от того, где и как вы работаете с данным окружением, вы можете получить дополнительные данные от:

- организаторов, на очном этапе
- администрации, на дистанционном этапе
- в папке с примерами (см. ```docs```)

Так или иначе, полученный вами список документов будет содержать карту полигона с обозначением координатной системы и
разметку зон воздействия киберпрепятствий на этом полигоне.

> Тщательно изучите этот документ - это потребуется вам при выполнении основной соревновательной задачи!

### 3. Приступите к решению задачи

И вот, практическая часть вашей работы - написание систем безопасности для доверенного модуля!
Собственно, на ваши плечи возлагается задача по созданию кибериммунитета для АНТС.
Для этого вам нужно будет открыть Jupyter Notebook и следовать инструкциям внутри него.


