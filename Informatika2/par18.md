**ВОПРОСЫ**

1. Что такое запрос? Зачем используются запросы?

Запрос (Query) - это формализованное обращение к базе данных для получения, изменения или удаления данных.

Запросы используются для:

Выборки данных: Получение нужных данных из одной или нескольких таблиц.
Фильтрации данных: Отбора записей, удовлетворяющих заданным условиям.
Сортировки данных: Упорядочивания записей по одному или нескольким полям.
Группировки и агрегирования данных: Получение итоговых значений (например, сумм, средних, максимальных значений) для групп записей.
Обновления данных: Изменения значений в таблицах.
Вставки новых данных: Добавления новых записей в таблицы.
Удаления данных: Удаления записей из таблиц.
Создания новых таблиц: На основе данных из существующих.
2. Язык запросов к СУБД

Запросы к СУБД (в основном к реляционным) составляются на языке SQL (Structured Query Language). SQL - это стандартизированный язык, который позволяет взаимодействовать с базами данных, управлять данными и извлекать необходимую информацию.

3. Построение и изменение запроса без Конструктора

Да, запрос можно строить и изменять, не используя графический Конструктор. Можно использовать:

Режим SQL: В этом режиме запрос полностью описывается командами языка SQL. Пользователь самостоятельно пишет SQL-запрос (можно скопировать из текста, полученного в режиме конструктора). Это дает полную гибкость при работе с запросами.
Прямое редактирование: Режим отображения SQL запроса, полученного в режиме конструктора, который позволяет напрямую изменять SQL-запрос, без графического интерфейса.
4. Назначение строк в бланке запроса (режим конструктора)

Псевдоним (Alias): Позволяет задать временное имя полю, которое будет использоваться при выводе результатов запроса. Полезно, когда есть поля с одинаковыми именами, или когда имя поля неудобно использовать.
Сортировка (Sort): Позволяет указать порядок сортировки данных в результате запроса (по возрастанию или убыванию).
Критерий (Criteria): Позволяет задать условия, которым должны удовлетворять записи для включения в результат запроса. Позволяет осуществлять фильтрацию записей.
5. Ограничения бланка запроса и сложные запросы

Структура бланка запроса (одна строка “Критерий” и несколько строк “ИЛИ”) не ограничивает создание сложных запросов. Эта структура позволяет создавать сложные фильтры, используя логические операции.

Строка “Критерий”: Условия, которые должны выполняться одновременно (логическое “И”).
Строки “ИЛИ”: Условия, где должно выполняться хотя бы одно (логическое “ИЛИ”).
Используя комбинации строк “Критерий” и “ИЛИ” в бланке запроса можно построить сложное условие, которое соответствует логическим выражениям с операциями “И”, “ИЛИ” и “НЕ”, обеспечивая возможность создавать сложные запросы.

6. Результаты выполнения запроса

Чтобы увидеть результаты выполнения запроса, нужно:

Перейти в режим просмотра данных: После создания или изменения запроса нужно нажать кнопку “Выполнить запрос” или перейти в режим просмотра данных (результат запроса).
Использовать режим просмотра SQL: Нажать кнопку “Запрос в режиме SQL”, скопировать запрос в отдельную программу (например, MySQL Workbench), и выполнить запрос там.
7. Изменение существующего запроса

Чтобы изменить существующий запрос, нужно:

Выделить запрос в основном окне базы данных.
Выбрать “Правка” (Edit) в контекстном меню или нажать кнопку “Изменить” на панели инструментов.
После этого запрос откроется в режиме конструктора, где можно внести необходимые изменения (добавить или удалить поля, изменить условия отбора, сортировку и т.д.).
8. Результат SQL-запроса SELECT "Команда" FROM "Футбол" WHERE "Победы" > 10

Данный SQL-запрос выберет из таблицы “Футбол” все значения поля “Команда”, для которых значение поля “Победы” больше 10. В результате будет выведена таблица со списком команд, у которых количество побед превышает 10.

9. Запросы с параметрами

Запросы с параметрами позволяют делать запросы более гибкими. При выполнении таких запросов, СУБД запросит значения параметров, и будет фильтровать данные, используя эти значения, что позволяет менять фильтры без необходимости изменять запрос.

Запросы с параметрами используются, когда нужно:

Выполнять запросы с разными условиями: Например, выбирать клиентов по заданному городу, или товары, цена которых выше заданного значения.
Использовать данные, вводимые пользователем: Позволяют пользователю выбирать значения, которые будут использоваться в запросе.
Повысить гибкость: Сделать запросы более универсальными, применяемыми для разных условий.
10. Вычисляемое поле

Вычисляемое поле - это поле, значение которого вычисляется на основе значений других полей в таблице.

Построение вычисляемого поля в Конструкторе:

Добавьте новое поле в запрос.
В строку “Поле” введите выражение, которое вычисляет значение поля, используя SQL-функции и поля из таблицы.
В строку “Псевдоним” введите имя для этого поля.
В строку “Сортировка” введите порядок сортировки по этому полю.
В строку “Критерий” введите условие, если нужно фильтровать по этому полю.
Примеры выражений:

"Цена" * "Количество"
Date('now') - "Дата рождения"
UPPER("Имя")
11. Операции в SQL-запросах кроме выборки данных

С помощью SQL-запросов можно выполнить следующие операции:

INSERT: Добавление новых записей в таблицы.
INSERT INTO Товары (Название, Цена) VALUES ('Молоко', 70);


UPDATE: Изменение существующих записей в таблицах.
UPDATE Товары SET Цена = 80 WHERE Название = 'Молоко';


DELETE: Удаление записей из таблиц.
DELETE FROM Товары WHERE Название = 'Молоко';


CREATE TABLE: Создание новой таблицы.
    CREATE TABLE Новая_таблица (
        ID INT PRIMARY KEY,
        Название VARCHAR(255)
    );


ALTER TABLE: Изменение структуры существующей таблицы (добавление, удаление или изменение полей).
     ALTER TABLE Товары
          ADD COLUMN Производитель VARCHAR(255);


DROP TABLE: Удаление таблицы.
     DROP TABLE Новая_таблица;
     
Эти операции позволяют управлять данными в базе и выполнять широкий спектр задач по обработке информации.
