**ВОПРОСЫ**

1.Трудности представления вещественных чисел вызваны конечностью памяти компьютеров и ограниченностью битов, отведённых для хранения чисел. Вещественные числа в математике являются непрерывными, тогда как в цифровых системах они представлены в дискретной форме, что приводит к необходимости округления. В результате, не все вещественные числа можно точно представить в двоичной системе, и возникают проблемы с прерываниями и потерями точности.
2.Вещественные числа с фиксированной запятой хранятся с определённым количеством разрядов после запятой, что позволяет точно представлять дробные значения. Например, число 12.34 может храниться как 1234 со смещением запятой на два разряда. Однако этот метод не используется в современных компьютерах, так как не позволяет обрабатывать широкий диапазон значений динамически, что является важным для большинства вычислений.
3.Плавающая запятая – это метод представления вещественных чисел, при котором запятая может «плавать», то есть перемещаться в зависимости от значения числа. Число при кодировании с плавающей запятой состоит из трех частей: знака, мантиссы и порядка. Мантисса содержит значащие цифры, а порядок определяет, насколько уходит запятая влево или вправо.
4.Примеры физических величин, обычно записываемых в форме с плавающей запятой, включают:
Температуру, измеряемую в градусах Цельсия или Кельвина.
Скорость (например, скорость света).
Углы (например, в радианах).
Величины, которые требуют высокой точности, такие как Einstein's mass-energy equivalence (E=mc²).
5.Метод представления чисел с плавающей запятой неоднозначен, так как одно и то же вещественное число можно представить несколькими способами. Если запятую сместить на один разряд влево, порядок уменьшится на один, а мантисса станет меньше, что приведет к изменению значения числа. Обратное происходит при смещении запятой вправо.
6.Нормализованная форма записи числа – это представление числа, при котором мантисса имеет фиксированное значение (например, для двоичного представления она начинается с 1). Это позволяет максимизировать точность, используя доступное число разрядов.
7.Требования нормализации связаны с точностью представления вещественных чисел, так как они обеспечивают оптимальное использование разрядов, минимизируя риск потери значимости в представлении чисел.
8.Нормализованное представление не является единственным для всех чисел. Некоторые числа, например, ноль, могут быть представлены только ненормализованным образом (например, мантисса и порядок равны нулю).
9.Старший бит значащей части нормализованного двоичного числа всегда равен единице из-за принципа нормализации. Это позволяет не сохранять его в памяти, тем самым экономя разряд, что практично на уровне памяти и вычислений.
10.Числа, сохраняющиеся в памяти с нулевой значащей частью, это, как правило, числа с плавающей запятой, такие как ноль или подстановочные значения для "неизвестных" данных.
11.Разрядность значащей части и разрядность порядка влияют на диапазон представляемых значений и точность. Большее количество разрядов в значащей части позволяет хранить более точные значения, тогда как больший порядок позволяет представлять числа на более широком диапазоне.
12.Для целых чисел разрядность однозначно определяет их свойства, так как количество разрядов определяет максимальное и минимальное представимое значение. Для вещественных чисел такая однозначная зависимость отсутствует, из-за чего одно и то же число можно выразить разными способами, что делает свойства не столь очевидными.
13.В современных компьютерных системах используются разные форматы для представления вещественных чисел. Наиболее распространённые из них:

Single Precision (32-битный формат): Занимает 4 байта. Он состоит из 1 бита для знака, 8 бит для порядка и 23 бит для мантиссы. Это дает возможность представлять числа с ограниченной точностью и диапазоном.
Double Precision (64-битный формат): Занимает 8 байт. Он включает 1 бит для знака, 11 бит для порядка и 52 бита для мантиссы. Это увеличивает точность и диапазон по сравнению с форматом single.
Extended Precision: В зависимости от архитектуры может занимать от 80 до 128 бит (например, 80-битный формат в x87 архитектуре). Обычно включает 1 бит для знака, 15 бит для порядка и 64 бита для мантиссы. Увеличенный размер позволяет высокую точность.
14.Во всех рассмотренных форматах вещественных чисел порядок хранится с соответствующим смещением. Это значит, что фактическое значение порядка (экспоненты) не хранится напрямую, а добавляется к заранее установленному значению (смещению). Например, в формате single порядок кодируется в диапазоне от -126 до 127, что соответствует смещению 127. Это позволяет избавиться от необходимости хранить знак порядка, так как все значения представляются как неотрицательные.
15.Отрицательные целые числа обычно хранятся в формате дополнительного кода. В этом формате, для представления отрицательного числа его модуль инвертируется и прибавляется 1 к результату. Например, для -5, если 5 представляется как 0000 0101, то -5 будет 1111 1011 в 8-битном представлении.
Отрицательные вещественные числа также используют дополнительный код для знака (1 бит для знака), однако сами мантиссы и порядок представляются в формате плавающей запятой. Здесь важно, что мантисса всегда хранится в неотрицательном виде (без учета знака), а знак числа определяется отдельным битом.
16.Чтобы определить, положительное или отрицательное вещественное число, следует проверить бит знака, который находится в самом старшем бите (bit 31) для формата single. Если этот бит равен 0, число положительное; если 1, оно отрицательное.

Этот метод также подходит для целых чисел, где старший бит указывает знак. Однако для целых чисел потребуется применять дополнительный код, чтобы получить реальное значение.
17.Пользовательские форматы с плавающей запятой, например, логические форматы или целочисленные представления, не используют «скрытую единицу». Обычно «скрытая единица» используется для нормализованных чисел в форматах с плавающей запятой, чтобы оптимизировать использование битов мантиссы. В формате "денормализованных" чисел (или "не нормализованных"), где порядок равен минимальному значению, скрытая единица не используется, так как мантисса представляется полностью (то есть, начиная с нуля).
18.а) Чтобы выделить значащую часть, сбросив порядок и знаковый бит, необходимо применить маску. В формате single значащая часть занимает биты с 0 до 22, а порядок с 23 до 30, знак на 31. Используем маску 0x7FFFFF (в шестнадцатеричном формате) для извлечения значащей части.
б) Для восстановления скрытой единицы в полученной значащей части, нужно сдвинуть мантиссу на один бит влево и добавить единицу
19.Чтобы выделить смещённый порядок из числа типа single, необходимо применить маску, чтобы получить нужные биты. Порядок в формате single занимает биты с 23 по 30, то есть 8 бит.
20.В формате single (32-битное представление) один из 32 бит используется для хранения знака числа. Этот бит — самый старший бит, который имеет значение 1, если число отрицательное, и 0, если положительное.
21.NaN (Not a Number) — это специальное значение в стандарте IEEE 754, которое используется для представления неопределённых или недопустимых числовых операций. Например, NaN может возникнуть в следующих ситуациях:

Деление нуля на ноль.
Неправильные операции с вещественными числами, например, извлечение квадратного корня из отрицательного числа (в вещественной арифметике).
Результаты, которые не могут быть определены как числа, например, операции с NaN.
NaN не равен никакому числу, включая самого себя, и его использование позволяет программам обрабатывать ошибки в вычислениях, не вызывая сбоев.
22.Хотя целое число и вещественное число с нулевой дробной частью могут представлять одно и то же значение (например, 12 и 12.0), в памяти они хранятся по-разному:

Целое число (например, 12):
В зависимости от типа хранения (например, int, long и т.д.) занимает фиксированное количество бит (обычно 32 или 64 бита).
Представляется в виде дополнительного кода, где наиболее значимый бит представляет знак (0 для положительных, 1 для отрицательных).
Вещественное число (например, 12.0):
Хранится в формате IEEE 754, который включает в себя знаковый бит, порядок и мантиссу.
В случае single precision формат будет занимать 32 бита: 1 бит для знака, 8 бит для порядка и 23 бита для мантиссы.
Для числа 12.0 в формате single будет использоваться мантисса и порядок, который определяет масштаб, в отличие от непосредственного представления целого числа.

**ЗАДАЧИ**

1.256
2.-
3.-
4.Диапазон целых чисел со знаком в 32 бита:
От -2,147,483,648 до 2,147,483,647.
Диапазон чисел типа single (IEEE 754):
От примерно -3.4 × 10^{38} до 3.4 × 10^{38}.
5.-
6.-
7.-
8.-
9.-