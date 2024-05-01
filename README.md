# В этом репозитории вы можете посмотреть мой процесс познания и получения оффера на должность Middle Python Backend Dev'a в компанию <a href="agora.ru"> Agora </a>
![img.png](img%2Fimg.png)


# Пройдёмся последовательно по каждому пункту относительно теории и немного практики

![docker.png](img%2Fdocker.png)

| Команда                   | Описание                                                                  |
|--------------------------|---------------------------------------------------------------------------|
| `docker run <имя_образа>`| Запускает контейнер на основе указанного образа.                        |
| `docker build .`         | Собирает Docker образ из Dockerfile в текущей директории.                |
| `docker ps`              | Показывает запущенные контейнеры.                                        |
| `docker images`          | Показывает список сохраненных Docker образов на системе.                 |
| `docker stop <container>`| Останавливает работу контейнера.                                         |
| `docker rm <container>`  | Удаляет контейнер.                                                       |
| `docker rmi <image>`     | Удаляет Docker образ.                                                     |
| `docker pull <image>`    | Загружает Docker образ из репозитория.                                    |
| `docker exec -it <container> <command>` | Запускает команду внутри контейнера.                            |
| `docker-compose up`      | Запускает приложение согласно настройкам в файле docker-compose.yml.     |
| `docker logs <container>`                | Показывает логи указанного контейнера.                                        |
| `docker logs -f <container>`             | Отображает логи указанного контейнера в реальном времени (следит за логами).  |
| `docker logs --tail <number> <container>`| Показывает последние <number> строк логов указанного контейнера.             |
| `docker logs --since <time> <container>` | Показывает логи контейнера, начиная с указанного времени (например, 1h ago).  |
| `docker logs --until <time> <container>` | Показывает логи контейнера до указанного времени.                             |

![git.png](img%2Fgit.png) 
# (+ разрешение конфликтов)

| Команда                                     | Описание                                                                      |
|---------------------------------------------|-------------------------------------------------------------------------------|
| `git init`                                  | Инициализирует новый репозиторий Git в текущей директории.                   |
| `git clone <URL>`                           | Клонирует существующий репозиторий из указанного URL.                        |
| `git add <file>`                            | Добавляет изменения файла в индекс (staging area) для последующего коммита.  |
| `git commit -m "<message>"`                 | Создает коммит с зафиксированными изменениями и сообщением о коммите.        |
| `git status`                                | Показывает состояние рабочего каталога и индекса.                            |
| `git branch`                                | Показывает список локальных веток и текущую ветку.                           |
| `git checkout <branch>`                     | Переключается на указанную ветку.                                           |
| `git merge <branch>`                        | Объединяет указанную ветку в текущую ветку.                                  |
| `git pull`                                  | Получает изменения из удаленного репозитория и объединяет их с текущей веткой.|
| `git push`                                  | Отправляет локальные коммиты в удаленный репозиторий.                       |
| `git diff`                                  | Показывает различия между рабочим каталогом и индексом.                     |
| `git log`                                   | Показывает историю коммитов.                                                 |
| `git reset <file>`                          | Отменяет изменения файла в индексе.                                          |
| `git reset --hard HEAD`                     | Сбрасывает все изменения в рабочем каталоге и индексе до последнего коммита.|
| `git checkout -- <file>`                    | Восстанавливает файл до его состояния на момент последнего коммита.         |
| `git stash`                                 | Сохраняет текущие изменения во временном хранилище.                          |
| `git stash apply`                           | Применяет последние изменения из временного хранилища к текущему состоянию.  |
| `git stash pop`                             | Применяет и удаляет последние изменения из временного хранилища.             |
| `git rebase <branch>`                       | Перебазирует текущую ветку на указанную ветку.                              |
| `git mergetool`                             | Запускает внешнее приложение для разрешения конфликтов слияния.              |

Команды `git mergetool` и `git mergetool --tool-help` могут быть полезны при разрешении конфликтов слияния, так как они позволяют запускать внешние инструменты для удобного разрешения конфликтов.

### Конфликты слияния в Git
Системы контроля версий предназначены для управления дополнениями, вносимыми в проект множеством распределенных авторов (обычно разработчиков). Иногда один и тот же контент могут редактировать сразу несколько разработчиков. Если разработчик A попытается изменить код, который редактирует разработчик B, может произойти конфликт. Для предотвращения конфликтов разработчики работают в отдельных изолированных ветках. Основная задача команды git merge заключается в слиянии отдельных веток и разрешении любых конфликтующих правок.

### Общие сведения о конфликтах слияния
Обычно конфликты возникают, когда два человека изменяют одни и те же строки в файле или один разработчик удаляет файл, который в это время изменяет другой разработчик. В таких случаях Git не может автоматически определить, какое изменение является правильным. Конфликты затрагивают только того разработчика, который выполняет слияние, остальная часть команды о конфликте не знает. Git помечает файл как конфликтующий и останавливает процесс слияния. В этом случае ответственность за разрешение конфликта несут разработчики.

### Git прерывает работу в самом начале слияния
Выполнение команды слияния прерывается в самом начале, если Git обнаруживает изменения в рабочем каталоге или разделе проиндексированных файлов текущего проекта. Git не может выполнить слияние, поскольку иначе эти ожидающие изменения будут перезаписаны новыми коммитами. Такое случается из-за конфликтов не с другими разработчиками, а с ожидающими локальными изменениями. Локальное состояние необходимо стабилизировать с помощью команд `git stash`, `git checkout`, `git commit` или `git reset`. Если команда слияния прерывается в самом начале, выдается следующее сообщение об ошибке:
``` git
error: Entry '<fileName>' not uptodate. Cannot merge. (Changes in working directory)
```

### Git прерывает работу во время слияния
Сбой В ПРОЦЕССЕ слияния говорит о наличии конфликта между текущей локальной веткой и веткой, с которой выполняется слияние. Это свидетельствует о конфликте с кодом другого разработчика. Git сделает все возможное, чтобы объединить файлы, но оставит конфликтующие участки, чтобы вы разрешили их вручную. При сбое во время выполнения слияния выдается следующее сообщение об ошибке:
```
error: Entry '<fileName>' would be overwritten by merge. Cannot merge. (Changes in staging area)
```

### Создание конфликта слияния
Чтобы лучше разобраться в конфликтах слияния, в смоделируем конфликт для дальнейшего изучения и разрешения. Для запуска моделируемого примера будет использоваться интерфейс Git c Unix-подобной командной строкой.
```UNIX
$ mkdir git-merge-test
$ cd git-merge-test
$ git init .
$ echo "this is some content to mess with" > merge.txt
$ git add merge.txt
$ git commit -am"we are commiting the inital content"
[main (root-commit) d48e74c] we are commiting the inital content
1 file changed, 1 insertion(+)
create mode 100644 merge.txt
```

С помощью приведенной в этом примере последовательности команд выполняются следующие действия.

* Создается новый каталог с именем git-merge-test, выполняется переход в этот каталог и инициализация его как нового репозитория Git.
* Создается новый текстовый файл merge.txt с некоторым содержимым.
* В репозиторий добавляется файл merge.txt и выполняется коммит.

Теперь у нас есть новый репозиторий с одной веткой main и непустым файлом merge.txt. Далее создадим новую ветку, которая будет использоваться как конфликтующая при слиянии.

```UNIX
$ git checkout -b new_branch_to_merge_later
$ echo "totally different content to merge later" > merge.txt
$ git commit -am"edited the content of merge.txt to cause a conflict"
[new_branch_to_merge_later 6282319] edited the content of merge.txt to cause a conflict
1 file changed, 1 insertion(+), 1 deletion(-)
```

Представленная выше последовательность команд выполняет следующие действия.

* Создает новую ветку с именем new_branch_to_merge_later и выполняет переход в нее.
* Перезаписывает содержимое файла merge.txt.
* Выполняет коммит нового содержимого.

В этой новой ветке new_branch_to_merge_later мы создали коммит, который переопределил содержимое файла merge.txt.

```UNIX
git checkout main
Switched to branch 'main'
echo "content to append" >> merge.txt
git commit -am"appended content to merge.txt"
[main 24fbe3c] appended content to merge.tx
1 file changed, 1 insertion(+)
```
Эта последовательность команд выполняет переключение на ветку main, добавляет содержимое в файл merge.txt и делает коммит. После этого в нашем экспериментальном репозитории находятся два новых коммита, первый — в ветке main, а второй — в ветке new_branch_to_merge_later. Теперь запустим команду git merge new_branch_to_merge_later и посмотрим, что из этого выйдет!

```UNIX
$ git merge new_branch_to_merge_later
Auto-merging merge.txt
CONFLICT (content): Merge conflict in merge.txt
Automatic merge failed; fix conflicts and then commit the result.
```
БАХ! 💥 Возник конфликт. Хорошо, что система Git сообщил нам об этом.

## Команды Git, с помощью которых можно разрешить конфликты слияния
### Общие инструменты
`git status`

Команда status часто используется во время работы с Git и помогает идентифицировать конфликтующие во время слияния файлы.

`git log --merge`

При передаче аргумента --merge для команды git log будет создан журнал со списком конфликтов коммитов между ветками, для которых выполняется слияние.

`git diff`

Команда diff помогает найти различия между состояниями репозитория/файлов. Она полезна для выявления и предупреждения конфликтов слияния.

### Инструменты для случаев, когда Git прерывает работу в самом начале слияния
`git checkout`

Команда checkout может использоваться для отмены изменений в файлах или для изменения веток.

`git reset --mixed`

Команда reset может использоваться для отмены изменений в рабочем каталоге или в разделе проиндексированных файлов.

### Инструменты для случаев, когда конфликты Git возникают во время слияния
`git merge --abort`

При выполнении команды git merge с опцией --abort процесс слияния будет прерван, а ветка вернется к состоянию, в котором она находилась до начала слияния.

`git reset`

Команду git reset можно использовать для разрешения конфликтов, возникающих во время выполнения слияния, чтобы восстановить заведомо удовлетворительное состояние конфликтующих файлов.

![Python_logo_and_wordmark.svg](img%2FPython_logo_and_wordmark.svg)

## Типы данных (mutable и immutable)
1. **Mutable (изменяемый)**: Объекты, значения которых могут быть изменены после создания, считаются изменяемыми. Это означает, что после создания такого объекта его состояние может быть изменено без создания нового объекта с новым значением. Например, списки (list) в Python являются изменяемыми объектами: вы можете добавлять, удалять или изменять элементы списка без создания нового списка.
2. **Immutable (неизменяемый)**: Наоборот, объекты, значения которых не могут быть изменены после создания, считаются неизменяемыми. Это означает, что после создания такого объекта его значение не может быть изменено, и любые операции, направленные на изменение этого значения, создадут новый объект с новым значением. Например, в Python строки (str) являются неизменяемыми объектами: вы не можете изменить символ в строке, но можете создать новую строку с измененным значением.

В качестве самопроверки попробуйте ответить на вопрос:

Что выведет данный код и почему (имеется ввиду разные или одинаковые IDшники)?
```python
a = 'abc'
print(id(a))
a = 'aba'
print(id(a))
```
<details>
<summary> Ответик </summary>

Строка - immutable (т.е. неизменяемый тип данных, мы с вами об этом говорили), даже если учесть то, что имя переменной одно и то же, то при повторном определении значения переменной у нас произойдёт порождение нового объекта (да-да, питон грешен насиранием в оперативку)
</details>

| Mutable                     | Immutable                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| `lists`                     | `numbers`                                                                 |
| `dictionaries`              | `strings`                                                                 |
| `sets`                      | `tuples`                                                                   |

### Mixins

Это способ повторного использования кода путем комбинирования функциональности из нескольких классов. Они представляют собой специальные классы, которые содержат методы, предназначенные для добавления поведения к другим классам без необходимости множественного наследования.

Существует несколько основных характеристик Миксинов:
1. **Композиционный подход**: Mixins используются для добавления функциональности к существующим классам путем композиции, а не наследования.
2. **Несамостоятельные классы**: Mixins обычно не представляют собой полноценные самостоятельные классы и не предназначены для создания экземпляров.
3. **Использование с множественным наследованием**: Mixins используются в ситуациях, когда необходимо добавить функциональность к классам, которые уже наследуют от других классов.

Пример использования Mixin:
```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person, JSONMixin):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

emp = Employee("John", 30, 50000)

print(emp.to_json())
```
В этом примере `JSONMixin` содержит метод `to_json()`, который преобразует атрибуты объекта в строку _JSON_. Класс `Employee` наследует от класса `Person` и использует `JSONMixin`, чтобы получить метод `to_json()` для сериализации экземпляров класса в формат JSON.

### P.S. Что такое композиция?
Концепция в ООП, когда один объект содержит другой в качестве составной части

Например:
```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        print("Car started")
        self.engine.start()

my_car = Car()
my_car.start()
```
В этом примере класс `Car` содержит объект `Engine` в качестве своего атрибута. Это демонстрирует отношение композиции, где один объект (Car) содержит другой объект (Engine) в качестве своей составной части. Когда вызывается метод `start()` объекта `Car`, он также вызывает метод `start()` объекта `Engine`, что демонстрирует совместную работу компонентов в рамках композиции.

![OOP.png](img%2FOOP.png)

Плавно переходим к теме ООП, SOLID принципов и в целом оценке всей парадигмы.
Вначале рассмотрим общее понятие, что такое SOLID и как расшифровывается каждая буква данной аббревиатуры.

**SOLID** - это принципы разработки программного обеспечения, следуя которым Вы получите хороший код, который в дальнейшем будет хорошо масштабироваться и поддерживаться в рабочем состоянии.

**S - Single Responsibility Principle** - принцип единственной ответственности. Каждый класс должен иметь только одну зону ответственности.

**O - Open closed Principle** - принцип открытости-закрытости. Классы должны быть открыты для расширения, но закрыты для изменения.

**L - Liskov substitution Principle** - принцип подстановки Барбары Лисков. Должна быть возможность вместо базового (родительского) типа (класса) подставить любой его подтип (класс-наследник), при этом работа программы не должна измениться.

**I - Interface Segregation Principle** - принцип разделения интерфейсов. Данный принцип обозначает, что не нужно заставлять клиента (класс) реализовывать интерфейс, который не имеет к нему отношения.

**D - Dependency Inversion Principle** - принцип инверсии зависимостей. Модули верхнего уровня не должны зависеть от модулей нижнего уровня. И те, и другие должны зависеть от абстракции. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

### Рассмотрим каждый принцип на примере:

Допустим у нас есть класс **_RentCarService_** и в нем есть несколько методов: 
* найти машину по номеру
* забронировать машину
* распечатать заказ
* получить информацию о машине
* отправить сообщение

```python
class RentCarService:

    def find_car(self, car_no):
        # find car by number
        return car

    def order_car(self, car_no, client):
        # client order car
        return order

    def print_order(self, order):
        # print order
        pass

    def get_car_interest_info(self, car_type):
        if car_type == "sedan":
            # do some job
            pass
        if car_type == "pickup":
            # do some job
            pass
        if car_type == "van":
            # do some job
            pass

    def send_message(self, type_message, message):
        if type_message == "email":
            # write email
            # use smtplib or other email sending library
            pass
```
У данного класса есть несколько зон ответственности, что является нарушением первого принципа. Возьмем метод получения информации об машине. Теперь у нас есть только три типа машин sedan, pickup и van, но если Заказчик захочет добавить еще несколько типов, тогда придется изменять и дописывать данный метод.

Или возьмем метод отправки сообщения. Если кроме отправки сообщения по электронной почте необходимо будет добавить отправку смс, то также необходимо будет изменять данный метод.

Одним словом, данный класс нарушает принцип единой ответственности, так как отвечает за разные действия.

Необходимо разделить данный класс **RentCarService** на несколько, и тем самым, следуя принципу единой ответственности, предоставить каждому классу отвечать только за одну зону или действие, так в дальнейшем его будет проще дополнять и модифицировать.

Необходимо создать класс **PrinterService** и вынести там функционал по печати.
```python
class PrinterService:
    def printOrder(self, order):
        pass
```

Аналогично работа связанная с поиском информации о машине перенести в класс **CarInfoService**.
```python
class CarInfoService:
    def get_car_interest_info(self, car_type):
        if car_type == "sedan":
            # do some job
            pass
        if car_type == "pickup":
            # do some job
            pass
        if car_type == "van":
            # do some job
            pass
```

Метод по отправке сообщений перенести в класс **NotificationService**.

```python
class NotificationService:
    def send_message(self, type_message, message):
        if type_message == "email":
            # write email
            # use smtplib or other email sending library
            pass
```

А метод поиска машины в **CarService**.
```python
class CarService:
    def find_car(self, car_no):
        # find car by number
        return car
```

И в классе **RentCarService** останется только один метод.
```python
class RentCarService:
    def order_car(self, car_no, client):
        # client order car
        return order
```
Теперь каждый класс несет ответственность только за одну зону и есть только одна причина для его изменения.

**Принцип открытости-закрытости (Open-closed principle)** рассмотрим на примере только что созданного класса по отправке сообщений.
```python
class NotificationService:
    def send_message(self, type_message, message):
        if type_message == "email":
            # write email
            # use smtplib or other email sending library
            pass
```
Допустим нам необходимо кроме отправки сообщения по электронной почте отправлять еще смс сообщения. И мы можем дописать метод sendMessage таким образом:
```python
class NotificationService:
    def send_message(self, type_message, message):
        if type_message == "email":
            # write email
            # use smtplib or other email sending library
            pass
        if type_message == "sms":
            # write sms
            # send sms
            pass
```

Но в данном случае мы нарушим второй принцип, потому что класс должен быть закрыт для модификации, но открыт для расширения, а мы модифицируем (изменяем) метод.

Для того, чтобы придерживаться принципа открытости-закрытости, нам необходимо спроектировать наш код таким образом, чтобы каждый мог повторно использовать нашу функцию, просто расширив ее. Поэтому создадим интерфейс **NotificationService** и в нем поместим метод sendMessage.
```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass
```

Далее создадим класс EmailNotification, который имплементит интерфейс NotificationService и реализует метод отправки сообщений по электронной почте.
```python
class EmailNotification(NotificationService):
    def send_message(self, message):
        # write email
        # use smtplib or other email sending library
        pass
```
Создадим аналогично класс MobileNotification, который будет отвечать за отправку смс сообщений.
```python
class MobileNotification(NotificationService):
    def send_message(self, message):
        # write sms
        # send sms
        pass
```

Давайте сейчас рассмотрим третий принцип: принцип **подстановки Барбары Лисков (Liskov substitution Principle)**.

Данный принцип непосредственно связан с наследованием классов. Допустим у нас есть базовый класс Счет (Account), в котором есть три метода: просмотр остатка на счете, пополнение счета и оплата.
```python
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def balance(self, account_number):
        pass
    
    @abstractmethod
    def refill(self, account_number, amount):
        pass
    
    @abstractmethod
    def payment(self, account_number, amount):
        pass
```

Нам необходимо написать еще два класса: зарплатный счет и депозитный счет, при этом зарплатный счет должен поддерживать все операции, представленные в базовом классе, а депозитный счет - не должен поддерживать проведение оплаты.
```python
from decimal import Decimal
class SalaryAccount(Account):
    def balance(self, account_number):
        # logic
        return Decimal(0)  # placeholder for balance
        
    def refill(self, account_number, amount):
        # logic
        pass
        
    def payment(self, account_number, amount):
        # logic
        pass

class DepositAccount(Account):
    def balance(self, account_number):
        # logic
        return Decimal(0)  # placeholder for balance
        
    def refill(self, account_number, amount):
        # logic
        pass
        
    def payment(self, account_number, amount):
        raise NotImplementedError("Operation not supported")
```

Если сейчас в коде программы везде, где мы использовали класс **Account** заменить на его класс-наследник (подтип) **SalaryAccount**, то программа продолжит нормально работать, так как в классе SalaryAccount доступны все операции, которые есть и в классе **Account**.

Если же мы такое попробуем сделать с классом **DepositAccount**, то есть заменим базовый класс **Account** на его класс-наследник **DepositAccount**, то программа начнет неправильно работать, так как при вызове метода `payment()` будет выбрасываться исключение `new UnsupportedOperationException`. Таким образом произошло нарушение принципа подстановки Барбары Лисков.

Для того чтобы следовать принципу подстановки Барбары Лисков, необходимо в базовый (родительский) класс выносить только общую логику, характерную для классов наследников, которые будут ее реализовывать и, соответственно, можно будет базовый класс без проблем заменить на его класс-наследник.

В нашем случае класс **Account** будет выглядеть следующим образом.
```python
from decimal import Decimal

class Account:
    def balance(self, account_number):
        # логика получения баланса
        return Decimal(0)  # возвращаем заглушку для баланса
        
    def refill(self, account_number, amount):
        # логика пополнения счета
        pass
```

Мы сможем от него наследовать класс **DepositAccount**.
```python
from decimal import Decimal
from account import Account

class DepositAccount(Account):
    def balance(self, account_number):
        # логика для получения баланса депозитного счета
        return Decimal(0)  # возвращаем заглушку для баланса
    
    def refill(self, account_number, amount):
        # логика для пополнения депозитного счета
        pass
```

Создадим дополнительный класс **PaymentAccount**, который унаследуем от **Account** и его расширим методом проведения оплаты.
```python
from account import Account

class PaymentAccount(Account):
    def payment(self, account_number, amount):
        # логика для проведения платежа
        pass
```
И наш класс **SalaryAccount** уже унаследуем от класса **PaymentAccount**.
```python
from decimal import Decimal
from payment_account import PaymentAccount

class SalaryAccount(PaymentAccount):
    def balance(self, account_number):
        # логика для получения баланса зарплатного счета
        return Decimal(0)
        
    def refill(self, account_number, amount):
        # логика для пополнения зарплатного счета
        pass
        
    def payment(self, account_number, amount):
        # логика для проведения платежа со зарплатного счета
        pass
```

Сейчас замена класса PaymentAccount на его класс-наследник SalaryAccount не "поломает" нашу программу, так как класс **SalaryAccount** имеет доступ ко всем методам, что и **PaymentAccount**. Также все будет хорошо при замене класса Account на его класс-наследник **PaymentAccount**.

Принцип **подстановки Барбары Лисков** заключается в правильном использовании отношения наследования. Мы должны создавать наследников какого-либо базового класса тогда и только тогда, когда они собираются правильно реализовать его логику, не вызывая проблем при замене родителей на наследников.

### Рассмотрим теперь принцип **разделения интерфейсов**.

Допустим у нас имеется интерфейс **Payments** и в нем есть три метода: оплата _WebMoney_, _оплата банковской карточкой_ и _оплата по номеру телефона_.
```python
from abc import ABC, abstractmethod

class Payments(ABC):
    @abstractmethod
    def pay_webmoney(self):
        pass
    
    @abstractmethod
    def pay_credit_card(self):
        pass
    
    @abstractmethod
    def pay_phone_number(self):
        pass
```

Далее нам надо реализовать два класса-сервиса, которые будут у себя реализовывать различные виды проведения оплат (класс **InternetPaymentService** и **TerminalPaymentService**). При этом **TerminalPaymentService** не будет поддерживать проведение оплат по номеру телефона. Но если мы оба класса имплементим от интерфейса **Payments**, то мы будем "заставлять" **TerminalPaymentService** реализовывать метод, который ему не нужен.
```python
from payments import Payments  # предположим, что у вас есть модуль payments, содержащий интерфейс Payments

class InternetPaymentService(Payments):
    def pay_webmoney(self):
        # логика оплаты через WebMoney
        pass
    
    def pay_credit_card(self):
        # логика оплаты кредитной картой
        pass
    
    def pay_phone_number(self):
        # логика оплаты по номеру телефона
        pass

class TerminalPaymentService(Payments):
    def pay_webmoney(self):
        # логика оплаты через WebMoney
        pass
    
    def pay_credit_card(self):
        # логика оплаты кредитной картой
        pass
    
    def pay_phone_number(self):
        # логика оплаты по номеру телефона
        pass
```
Таким образом произойдет нарушение принципа разделения интерфейсов.

Для того чтобы этого не происходило необходимо разделить наш исходный интерфейс **Payments** на несколько и, создавая классы, имплементить в них только те интерфейсы с методами, которые им нужны.

```python
from abc import ABC, abstractmethod

class WebMoneyPayment(ABC):
    @abstractmethod
    def pay_webmoney(self):
        pass

class CreditCardPayment(ABC):
    @abstractmethod
    def pay_credit_card(self):
        pass

class PhoneNumberPayment(ABC):
    @abstractmethod
    def pay_phone_number(self):
        pass
```

```python
from webmoney_payment import WebMoneyPayment 
from creditcard_payment import CreditCardPayment
from phonenumber_payment import PhoneNumberPayment

class InternetPaymentService(WebMoneyPayment, CreditCardPayment, PhoneNumberPayment):
    def pay_webmoney(self):
        # логика оплаты через WebMoney
        pass
    
    def pay_credit_card(self):
        # логика оплаты кредитной картой
        pass
    
    def pay_phone_number(self):
        # логика оплаты по номеру телефона
        pass
```
```python
from webmoney_payment import WebMoneyPayment 
from creditcard_payment import CreditCardPayment

class TerminalPaymentService(WebMoneyPayment, CreditCardPayment):
    def pay_webmoney(self):
        # логика оплаты через WebMoney
        pass
    
    def pay_credit_card(self):
        # логика оплаты кредитной картой
        pass
```

### Принцип инверсии зависимостей (Dependency Inversion Principle)
Давайте сейчас рассмотрим последний принцип: **принцип инверсии зависимостей**.

Допустим мы пишем приложение для магазина и решаем вопросы с проведением оплат. Вначале это просто небольшой магазин, где оплата происходит только за наличные. Создаем класс Cash и класс Shop.
```python
from decimal import Decimal

class Cash:
    def do_transaction(self, amount):
        # логика транзакции
        pass

class Shop:
    def __init__(self, cash):
        self.cash = cash
    
    def do_payment(self, order, amount):
        self.cash.do_transaction(amount)
```

Вроде все хорошо, но мы уже нарушили принцип инверсии зависимостей, так как мы тесно связали оплату наличными к нашему магазину. И если в дальнейшем нам необходимо будет добавить оплату еще банковской картой и телефоном ("100% понадобится"), то нам придется переписывать и изменять много кода. Мы в нашем коде модуль верхнего уровня тесно связали с модулем нижнего уровня, а нужно чтобы оба уровня зависели от абстракции.

Поэтому создадим интерфейс **Payments**.
```python
from abc import ABC, abstractmethod
from decimal import Decimal

class Payments(ABC):
    @abstractmethod
    def do_transaction(self, amount):
        pass
```

Теперь все наши классы по оплате будут имплементить данный интерфейс.   
```python
class Cash(Payments):
    def do_transaction(self, amount):
        # логика для оплаты наличными
        pass

class BankCard(Payments):
    def do_transaction(self, amount):
        # логика для оплаты банковской картой
        pass

class PayByPhone(Payments):
    def do_transaction(self, amount):
        # логика для оплаты через телефон
        pass
```

Теперь надо перепроектировать реализацию нашего магазина.
```python
class Shop:
    def __init__(self, payments):
        self.payments = payments
    
    def do_payment(self, order, amount):
        self.payments.do_transaction(amount)
```

Сейчас наш магазин слабо связан с системой оплаты, то есть он зависит от абстракции и уже не важно каким способом оплаты будут пользоваться (наличными, картой или телефоном) все будет работать.

## WEB компонента
Теперь перейдём к Web-составляющей нашей подготовки (Django, DjangoREST, MVC, Migrations, ORM, PostgreSQL, HTTP, Rest, SOAP)
