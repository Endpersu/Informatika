**ВОПРОСЫ**
Что такое информационная система (ИС)? Из каких компонентов она состоит?

Информационная система (ИС) - это система, предназначенная для сбора, хранения, обработки, передачи и предоставления информации. ИС использует компьютерные технологии и организационные методы для удовлетворения информационных потребностей организации или пользователей.

Компоненты информационной системы:

Аппаратное обеспечение (Hardware): Физические компоненты компьютерной системы (компьютеры, серверы, сети, принтеры, сканеры).
Программное обеспечение (Software): Набор программ и инструкций, позволяющих аппаратному обеспечению выполнять нужные функции (операционные системы, СУБД, прикладное ПО).
Данные (Data): Информация, которая хранится и обрабатывается в системе (тексты, числа, изображения, звук).
Персонал (People): Люди, которые используют, разрабатывают, управляют и обслуживают систему (пользователи, администраторы, разработчики).
Процедуры (Procedures): Набор правил, инструкций и методов, определяющих, как система работает (правила ввода данных, обработки информации, резервного копирования).
Сетевая инфраструктура (Network infrastructure): Совокупность оборудования и программного обеспечения, обеспечивающих взаимодействие между компонентами системы (протоколы, маршрутизаторы, коммутаторы).
2. Что такое база данных (БД)? Какими свойствами она должна обладать?

База данных (БД) - это организованная структура для хранения и управления данными, обеспечивающая доступность, целостность и безопасность данных.

Свойства БД:

Организованность: Данные должны быть организованы структурированно, чтобы к ним было легко обращаться.
Структурированность: Данные хранятся в виде таблиц, записей, полей и связей между ними.
Целостность: Обеспечивается корректность и непротиворечивость данных.
Доступность: Данные должны быть доступны для пользователей в любое время и при этом защищены от несанкционированного доступа.
Безопасность: Данные должны быть защищены от потери, повреждения и несанкционированного доступа.
Актуальность: Данные должны быть актуальными и обновляться по мере необходимости.
Эффективность: Система должна обеспечивать быстрый доступ к данным и их обработку.
Независимость данных: Структура данных не должна зависеть от используемого программного обеспечения.
Минимизация избыточности: Хранение данных должно быть организовано так, чтобы исключить или минимизировать дублирование данных.
3. Является ли бумажная картотека базой данных?

Бумажная картотека в библиотеке можно считать аналогом базы данных, но не является полноценной базой данных в современном понимании.

Аналог:
Содержит структурированную информацию (карточки с информацией о книгах).
Позволяет производить поиск информации.
Предоставляет механизмы для доступа и управления данными.
Не является полноценной БД:
Ручной ввод и поиск: Работа с картотекой полностью ручная и требует много времени.
Ограниченная масштабируемость: Сложно хранить и искать в больших объёмах данных.
Низкая скорость: Поиск нужной информации может быть долгим и неэффективным.
Невозможность автоматизированной обработки: Сложно автоматизировать анализ и обработку данных.
Неизбыточность: Данные на карточках могут повторяться.
Проблемы с целостностью: Легко допустить ошибки при заполнении карточек.
Уязвимость: Бумажные карточки подвержены повреждению и потере.
4. Функции СУБД

Система управления базами данных (СУБД) выполняет следующие функции:

Создание и определение структуры БД: Предоставляет инструменты для определения таблиц, полей, связей и типов данных.
Управление данными: Позволяет добавлять, изменять, удалять и просматривать данные в базе.
Управление доступом: Обеспечивает разграничение прав доступа для разных пользователей.
Управление целостностью данных: Следит за корректностью и непротиворечивостью данных, применяя ограничения и правила.
Управление транзакциями: Обеспечивает надежность операций с данными, гарантируя их целостность при сбоях.
Защита данных: Предоставляет механизмы для резервного копирования и восстановления данных, а также для защиты от несанкционированного доступа.
Предоставление интерфейса: Обеспечивает интерфейс для взаимодействия с БД (графический интерфейс, язык запросов).
Оптимизация запросов: Оптимизирует выполнение запросов для ускорения доступа к данным.
5. Переход к универсальным СУБД

Переход от разнообразия форматов хранения к универсальным СУБД произошёл из-за:

Проблем с совместимостью: Различные форматы данных несовместимы, что затрудняет обмен и интеграцию данных.
Сложности разработки: Разработка отдельных приложений для работы с каждым форматом данных сложна и требует больших затрат.
Неэффективности: Разнообразные форматы могут быть неэффективными с точки зрения хранения и обработки данных.
Универсальность СУБД: СУБД обеспечивают унифицированный интерфейс для работы с данными, независимо от их формата и структуры.
Более эффективное управление: СУБД предоставляют механизмы для эффективного управления данными (управление доступом, целостностью, резервным копированием).
Масштабируемость: СУБД позволяют легко масштабировать базы данных по мере увеличения объема данных.
Пример: Ранее организации использовали множество отдельных таблиц, текстовых файлов и т.д. для хранения информации о сотрудниках, товарах, клиентах и т.д. Переход к реляционной СУБД позволил хранить все данные в единой структурированной базе, эффективно их обрабатывать, связывать и управлять ими.

6. Метаданные

Метаданные - это данные о данных. Они описывают структуру, свойства и контекст данных.

Примеры метаданных:

Название таблицы.
Имена и типы полей.
Ограничения целостности.
Связи между таблицами.
Даты создания и изменения данных.
Описание данных.
7. Схема работы пользователя с БД

Схема работы пользователя с БД:

Пользовательское приложение: Пользователь работает с пользовательским приложением, которое предоставляет интерфейс для работы с БД (например, форма для ввода данных).
Запрос к СУБД: Приложение формирует запрос к СУБД на языке запросов (например, SQL) для добавления, изменения, удаления или получения данных.
СУБД: СУБД принимает запрос, анализирует его, находит нужные данные, выполняет запрошенные операции и формирует результат.
Ответ пользователю: Результат запроса возвращается приложению, которое преобразует его в удобный для пользователя вид.
Повтор: Пользователь может снова выполнить какие-либо действия в ИС, и всё начнется с первого пункта.
8. Достоинства и недостатки локальных ИС

Локальные ИС - это ИС, которые установлены на одном компьютере или в пределах небольшой локальной сети.

Достоинства:
Простота установки и настройки: Легко устанавливать и настраивать.
Независимость от сети: Работает автономно, не зависит от сети.
Быстрый доступ к данным: Быстрый доступ к данным, т.к. они хранятся локально.
Низкая стоимость: Не требуется дорогостоящее сетевое оборудование.
Недостатки:
Ограниченный доступ: Доступ к данным возможен только с локального компьютера или из локальной сети.
Сложности в совместной работе: Сложно организовать совместную работу нескольких пользователей с одними и теми же данными.
Ограниченная масштабируемость: Сложно наращивать мощности и объем данных.
Ненадежность: Зависит от работоспособности одного компьютера.
9. Достоинства и недостатки файл-серверных СУБД

Файл-серверные СУБД - СУБД, в которых данные хранятся на файловом сервере, а клиентские приложения сами обрабатывают данные и производят необходимые манипуляции с файлами.

Достоинства:
Простота: Просты в установке и использовании.
Невысокая стоимость: Не требуют сложного сетевого оборудования и дорогих серверов.
Доступность: Данные доступны для всех пользователей из локальной сети.
Недостатки:
Высокий сетевой трафик: Большой сетевой трафик, так как вся обработка данных ведется на клиентской стороне.
Проблемы с целостностью: Велика вероятность конфликтов при одновременном обращении к данным.
Низкая производительность: Производительность зависит от мощности клиентских компьютеров.
Сложность в управлении доступом: Сложно разграничить права доступа пользователей.
Сложности в масштабировании: Сложно поддерживать работу системы при увеличении объема данных и количества пользователей.
10. Использование файл-серверных СУБД

Файл-серверные СУБД можно рекомендовать в следующих ситуациях:

Небольшие рабочие группы: Для небольших рабочих групп с небольшим объемом данных, где не требуется высокая производительность и строгая защита данных.
Небольшие проекты: Для небольших проектов, где не требуется сложная обработка данных и не важна скорость доступа к данным.
Ограниченный бюджет: Когда бюджет ограничен и нет возможности приобрести дорогое оборудование для клиент-серверных СУБД.
Простота использования: В случаях, когда требуются простые решения, которые легко установить и использовать.
Сообщение: Файл-серверные СУБД - это простые решения для небольших рабочих групп и проектов, где не важна скорость и не требуется высокий уровень защиты данных. При использовании таких СУБД, нужно учитывать ограничение их масштабируемости, и не использовать их в случаях, где требуется высокая производительность и надежность системы.

11. Достоинства и недостатки клиент-серверных СУБД

Клиент-серверные СУБД - это СУБД, в которых большая часть обработки данных выполняется на сервере, а клиентские приложения выполняют лишь функцию интерфейса.

Достоинства:
Высокая производительность: Высокая производительность за счет распределения нагрузки между клиентом и сервером.
Надежность: Надежная защита данных и высокая отказоустойчивость.
Централизованное управление: Удобное централизованное управление доступом и безопасностью данных.
Масштабируемость: Легко масштабируются при увеличении объема данных и количества пользователей.
Снижение сетевого трафика: Сетевой трафик снижен за счет обработки данных на сервере.
Поддержка транзакций: Поддерживают транзакции, обеспечивая целостность данных.
Недостатки:
Высокая стоимость: Требуют более дорогого оборудования и программного обеспечения.
Сложность установки и настройки: Сложнее устанавливать и настраивать.
Зависимость от сети: Зависит от работоспособности сети и сервера.
Требуются квалифицированные специалисты: Требуют квалифицированных специалистов для обслуживания и администрирования.
12. Разделение функций в клиент-серверных СУБД

В клиент-серверных СУБД функции разделяются так:

Сервер:
Хранение данных.
Обработка запросов.
Управление доступом и безопасностью.
Управление транзакциями.
Оптимизация запросов.
Обеспечение целостности данных.
Клиент:
Предоставление пользовательского интерфейса.
Формирование запросов к серверу.
Отображение результатов запросов.
Ввод и редактирование данных.
Передача запросов серверу.
13. SQL (Structured Query Language)

SQL (Structured Query Language) - это стандартизированный язык запросов, используемый для работы с реляционными базами данных. SQL используется для:

Создания и изменения структуры БД (таблиц, полей).
Добавления, изменения, удаления и просмотра данных.
Выполнения запросов к БД для получения нужной информации.
Управления доступом к данным.
14. Распределённые базы данных

Распределенные базы данных (РБД) - это базы данных, в которых данные хранятся на нескольких компьютерах, но представляются пользователю как единая база данных. РБД обеспечивают высокую доступность, масштабируемость и отказоустойчивость.

15. Транзакция

Транзакция - это логическая последовательность операций с данными, которая рассматривается как единое целое. Либо все операции выполняются успешно, либо ни одна. Транзакция обеспечивает целостность данных при параллельном доступе или сбоях.

16. Защита данных при сбоях с использованием транзакций

Транзакции обеспечивают защиту данных при сбоях благодаря следующим свойствам (ACID):

Atomicity (атомарность): Либо все операции транзакции выполняются, либо ни одна. Если происходит сбой, то все изменения отменяются.
Consistency (согласованность): Транзакция переводит базу данных из одного согласованного состояния в другое.
Isolation (изолированность): Параллельные транзакции не влияют друг на друга.
Durability (долговечность): После успешного завершения транзакции, изменения данных сохраняются и не могут быть отменены при сбоях.
