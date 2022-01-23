# Software Design

![alt text](https://github.com/eshelukhina/HSE2022-SD/blob/task1/cliArch.png?raw=true)

* **App** – Точка входа в приложение. Использует другие модули для обработки запросов.

* **I/O** – Компонента, отвечающая за работу с входным и выходным потоками данных (в нашем случае с консолью).

* **Parser** – Парсит строку и возвращает очередь команд для выполнения. Выполняет подстановку при помощи **Substitution**, запускает **Lexer** на получившейся строке, а затем преобразует выходные токены в классы **Command**. Если не получилось распарсить команду (токен не является ни одной из поддерживаемых команд), то она распознается как процедура.

* **Lexer** – Разбивает строку на токены, согласно следующей грамматике:

```
expr
expr | expr
cat text
echo args
wc text
pwd
exit
text=text
text

args
text | text args
```

* **Substitution** – Модуль, отвечающий за подстановку переменных в строку. Вырезает содержимое одинарных кавычек. Далее выполняет подстановку на всей строке: находит все переменные $text и выполняет подстановку из Environment. Возвращает в строку содержимое одинарных кавычек (по порядковому номеру). Выполняется для второй фазы.

* **Environment** – Хранилище переменных из окружения.

* **Executor** – Элемент программы, который отвечает за запуск команд из очереди, а также подстановку результата в последующие команды, смену входных и выходных потоков, обработку ошибок. Так же внутри себя содержит **FileManager** и обращается к нему в том случае, когда при работе с командой задействованы файлы .

* **FileManager** – Компонента, отвечающая за работу с файловой системой. Необходима для выполнения базовых операций с файлами.

* **Command** – Интерфейс от которого наследуются все команды.