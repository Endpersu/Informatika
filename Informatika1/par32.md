**ВОПРОСЫ**

1) -
2) Основные принципы архитектуры фон Неймана:
 1 Единое хранилище памяти. Инструкции и данные хранятся в одной и той же памяти, что облегчает модификацию программ во время их выполнения.
 2 Процессор. Предназначен для обработки данных и выполнения команд из памяти.
 3 Последовательное выполнение команд.Команды выполняются одна за другой, в строгой последовательности.
 4 Ввод-вывод. Устройства ввода-вывода обеспечивают интерфейс между компьютером и внешним миром.
 5 Адресуемая память. Все данные и инструкции имеют уникальные адреса в памяти, что позволяет процессору быстро получать доступ к нужной информации.
3) Основные компоненты вычислительного устройства (например, компьютера): 
 • Системный блок. Основной блок компьютерной системы, в котором располагаются внутренние устройства. 
 • Монитор. Устройство для визуального воспроизведения символьной и графической информации. 
 • Клавиатура. Клавишное устройство для управления работой компьютера и ввода в него информации. 
 • Мышь. Устройство «графического» управления. 
 • Процессор. Основная микросхема персонального компьютера, в которой выполняются вычисления. 
 • Оперативная память. Обширный массив ячеек, в которых хранятся числовые данные и команды в то время, когда компьютер включён. 
 • Жёсткий диск. Устройство для длительного хранения данных и программ. 
Да, я согласна с тем, что указанный набор основных компонентов можно использовать, так как он является базовым для многих вычислительных устройств. 
4) Принцип двоичного кодирования соблюдается: любые данные для обработки компьютером представляются последовательностью двух целых чисел — единицы и нуля. 
5) В компьютере числа, тексты и графика кодируются по принципу двоичного кодирования. 
Кодирование числовых данных. Числовая информация в памяти компьютера хранится и обрабатывается в двоичном коде. Применяется две формы кодирования двоичных чисел: с фиксированной и плавающей запятой. В форме с фиксированной запятой хранятся и обрабатываются целые числа, а в форме с плавающей запятой — вещественные. 
Кодирование текстовых (символьных) данных. Каждому символу ставится в соответствие двоичный код — совокупность нулей и единиц. Наиболее распространённый стандарт кодировки символов — ASСII-код. 
Кодирование графической информации. При растровом представлении вся область данных разбивается на множество точечных элементов — пикселей, каждый из которых имеет свой цвет. При векторном способе представления компонентам векторных изображений (точкам, прямым и другим геометрическим фигурам) присваивается двоичная последовательность, определяющая разнообразные параметры. 
Таким образом, принцип двоичного кодирования соблюдается для всех видов данных в компьютере: числа кодируются с помощью алфавита из двух знаков — 0 и 1, тексты — путём присвоения буквенным, цифровым и другим обозначениям определённого кода, а графика — присвоением каждому компоненту изображения определённого кодового значения. 
6) Чтобы перевести десятичное число во внутреннее двоичное представление в компьютере, можно использовать алгоритм замещения: 
 1 Разделить десятичное число на 2. Частное запомнить для следующего шага, а остаток записать как младший бит двоичного числа. 
 2 Если частное не равно 0, принять его за новое делимое и повторить процедуру. Каждый новый остаток (0 или 1) записать в разряды двоичного числа в направлении от младшего бита к старшему. 
 3 Алгоритм продолжать до тех пор, пока в результате не получится частное равно 0 и остаток равен 1. 
7) Ячейка памяти - это минимальнаяединица памяти, к которой можнообращаться из программы. Размер одной ячейки памяти зависит от модели компьютера (например, DEC PDP-15 работал с ячейками памяти, содержавшими по 18 бит в каждой). В персональных ЭВМ обычно используются ячейки памяти, состоящие из 8 бит.
Адрес ячейки (или ссылка на ячейку) – это местоположение ячейки в таблице. Адрес (ссылка) определяется из имени столбца (буква) и имени строки (цифра), на пересечении которых находится ячейка.
8) Разрядность ячеек оперативной памяти (количество битов в ячейке) у компьютеров разных поколений была различной. 
9) Байтовая память появилась по следующим причинам:
 • По мере появления всё более современных типов данных. Стало неудобно работать с ячейками памяти, которые должны были изначально содержать в себе максимально длинные числа для увеличения точности вычислений. А символы в количестве 4–5 занимали всю ячейку. 
 • Чтобы компьютер мог обрабатывать сигналы с клавиатуры, а также текстовые данные. Каждая буква — именно 8 чисел, чтоб компьютер не путался. 
10) Да, можно заменить в ячейке памяти содержимое одного бита, не затрагивая значения соседних. 
Это возможно, потому что ячейки памяти в компьютере хранят данные независимо друг от друга. Для замены можно использовать операцию XOR (исключающее ИЛИ) и подходящую маску. 
11) Примеры различных типов данных и их разрядность и объём требуемой памяти:
 1 short (короткий целый) — 16 бит, то есть 2 байта; 
 2 long (длинный целый) — 64 бита, то есть 8 байт; 
 3 float (с точностью до 7 цифр) — 32 бита, то есть 4 байта; 
 4 double (точность до 15–16 цифр) — 64 бита, то есть 8 байт; 
 5 decimal (точность до 28–29 цифр) — 128 бит, то есть 16 байт. 
12) Иерархическая организация памяти — концепция построения взаимосвязи классов разных уровней компьютерной памяти. 
13)  1 Если оперативной памяти будет очень много, то процессор не сможет справиться с таким объёмом данных, и компьютер начнёт тормозить.
 2 Оперативная память дороже в производстве, чем постоянная. Это связано как с особенностями производства, так и со скоростью работы памяти. ОЗУ работает всегда быстрее ПЗУ.
14) Принцип хранимой программы заключается в хранении программы в той же самой памяти, что и обрабатываемые ею числа.
15) Программа хранится во внешней памяти компьютера в виде исполняемого файла.
16) Арифметические операции можно выполнять только над числовыми данными, измеряемыми в одних единицах измерения.
17) Фраза «любая обработка данных в вычислительной машине происходит по программе» означает, что компьютер работает на основе заранее заданных последовательностей арифметических, логических и других операций.
18) Основной алгоритм выполнения команды в компьютере включает несколько фаз: 
 1 Выбор команды. Чтение из оперативной памяти нескольких байт команды, адрес начала определяет регистр EIP. 
 2 Декодирование команды. Определение её длины, полей, наличия и местоположения операндов и результата. 
 3 Выбор операндов. Извлечение необходимых данных из оперативной памяти или регистровой памяти. 
 4 Выполнение операции. Выполнение операции, закодированной в коде операции, установка флагов. 
 5 Запись результата.  Если предусмотрено операцией, результат записывается в оперативную память (ОЗУ). 
19) Счётчик команд — регистр процессора, который указывает, какую команду нужно выполнять следующей. Он содержит адрес ячейки памяти следующей для выполнения команды. 
Роль счётчика команд в основном алгоритме работы заключается в том, что он следит за тем, какая команда выполняется, а какая подлежит выполнению следующей. Для корректного выполнения программы её команды должны поступать в строго определённом порядке.
20) В момент включения компьютера с точки зрения принципа программного управления происходит следующее:
 1 Системный контроллер проверяет, нужно ли подавать электричество на остальные устройства внутри компьютера. Даже когда компьютер условно выключен, на самом деле он включён. 
 2 После нажатия кнопки включения системный контроллер получает от неё сигнал и говорит блоку питания: «Мне нужно больше тока». Блок начинает полноценно работать и подаёт питание на материнскую плату и остальные компоненты. 
 3 Начинают работать все основные компоненты компьютера: процессор, оперативная память, микросхемы BIOS или UEFI, жёсткий диск. 
 4 Системный контроллер берёт содержимое микросхемы BIOS, загружает его в оперативную память и передаёт управление BIOS. 
 5 BIOS запускает POST (Power On Self Test), самотестирование при включении.
Тест проверяет работу процессора, оперативной памяти, контроллеров, загрузчиков и всего остального оборудования, важного для загрузки компьютера. 
 6 Когда POST пройден, BIOS начинает искать загрузчик операционной системы. Для этого он смотрит у себя в настройках порядок загрузки — список дисков по очереди, с которых можно загрузиться. 
 7 Загрузчик находит ядро операционной системы, загружает его в память и передаёт управление ему. 
 8 Если процесс загрузки дошёл до этой точки, то компьютер понимает, что скоро загрузится операционная система, а значит, можно показать пользователю стартовый экран. 
 9 Последний шаг загрузки компьютера — вход пользователя в систему. Он может быть автоматическим, если нет пароля на вход — в противном случае система попросит его ввести. 
21) Да, последовательность выполнения команд в программе можно нарушить. Для этого используются специальные команды перехода, которые изменяют содержимое счётчика команд. 
Нарушение последовательности может потребоваться, например, для использования ветвлений и циклов. Чаще всего в программах используется условный переход, то есть переход происходит только при выполнении определённого условия. 
22) Производители могут устанавливать на новый компьютер различные программы, в зависимости от своих бизнес-партнёров. Например, антивирус или офисный пакет в тестовой версии. 
Также на любом пользовательском ПК, вне зависимости от исполняемых на нём задач, могут понадобиться следующие программы первой необходимости: 
 • интернет-браузеры; 
 • мультимедийные проигрыватели; 
 • офисные программы. 
Однако пользователь может и самостоятельно установить дополнительные программы для повседневного использования. При этом не стоит инсталлировать сразу много программ с похожим функционалом. Лучше выбрать одну-две программы из каждой нужной категории — те, которые наиболее полно подходят под задачи пользователя. 
23) Конвейер в вычислительной технике — это способ организации параллельной обработки процессором команд программы. Он основан на разделении процесса обработки команды на несколько этапов (ступеней, стадий конвейера) и выделении для каждого из них отдельного функционального блока аппаратуры.
24) Конфликты в конвейере снижают реальную производительность конвейера.
Существуют три класса конфликтов:
 1 Структурные конфликты. Возникают из-за конфликтов по ресурсам, когда аппаратные средства не могут поддерживать все возможные комбинации команд в режиме одновременного выполнения с совмещением.
 2 Конфликты по данным. Возникают в случае, когда выполнение одной команды зависит от результата выполнения предыдущей команды.
 3 Конфликты по управлению. Возникают при конвейеризации команд переходов и других команд, которые изменяют значение счётчика команд.
Конфликты в конвейере приводят к необходимости приостановки выполнения команд.
25) Вот некоторые принципы, предложенные в работе «Предварительное рассмотрение логической конструкции электронно-вычислительного устройства» американского математика Джона фон Неймана:
 1 Программное управление работой ЭВМ.Программа состоит из команд, которые образуют систему команд машины. Команды программы последовательно считываются из памяти и выполняются. Адрес очередной команды хранится в счётчике команд.
 2 Принцип хранимой программы. Команды представляются в числовой форме и хранятся в той же памяти, что и данные.
 3 Принцип условного перехода. Можно нарушить естественную последовательность команд в программе. Используется в командах безусловного и условного переходов.
 4 Использование двоичной системы счисления для представления информации в ЭВМ. Её просто реализовать технически для выполнения арифметических и логических операций.
26) Архитектура компьютера – это его устройство и принципы взаимодействия его основных элементов – логических узлов, среди которых основными являются
процессор
внутренняя память (основная и оперативная)
внешняя память
устройства ввода-вывода информации (периферийные)
27) Преимущества единой архитектуры семейств ЭВМ для пользователей:
• возможность легко разобраться с принципами работы большинства компьютеров; 
 • сохранение ранее созданного программного обеспечения, так как программы, написанные для одной модели, должны выполняться для других моделей семейства. 
Преимущества единой архитектуры для производителей:
 • возможность предоставлять свою продукцию широкому ряду потребителей без доработки под каждый единичный случай; 
 • возможность выпускать компьютеры большими партиями, что делает их производство проще и дешевле, так как одно и то же оборудование может быть перенастроено на выполнение новых задач простой заменой ПО. 
Единая архитектура предполагает информационную, программную, аппаратную, конструктивную и эксплуатационную совместимость моделей одного семейства. В пределах одного семейства основные принципы устройства и функционирования машин одинаковы, хотя отдельные модели могут существенно различаться по производительности, стоимости и другим параметрам. 
28) Вычислительные машины делятся на три больших класса:
 1 Аналоговые (АВМ). Эффективны для решения математических задач, содержащих дифференциальные уравнения, не требующих сложной логики.
 2 Цифровые (ЦВМ). Вычислительные машины дискретного действия, работают с информацией, представленной в дискретной, а точнее, в цифровой форме.
 3 Гибридные (ГВМ). Вычислительные машины комбинированного действия, работают с информацией, представленной и в цифровой, и в аналоговой форме.

**ЗАДАЧИ**

1) а) 1. прочитать байт в память X 
    2. X:= X or 1 
    3. записать байт X в память  
б) 1. прочитать байт в память X 
    2. X:= X and FE^16 
    3. записать байт X в память  
2) 5 
3) 2 байта, максимальное значение 65535. 
4) 41^16 = 'A' = 65
5) -
6) -