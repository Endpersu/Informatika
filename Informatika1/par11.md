**ВОПРОСЫ**

1.Как мы уже говорили, конечные десятичные дроби могут не иметь конечного представления в двоичной системе. Точно (без округления) в памяти компьютера в двоичном коде могут быть представлены только те дробные числа, которые могут быть выражены в виде дроби, знаменатель которой является степенью двойки.

Другими словами, десятичная дробь должна быть представлена в виде несократимой дроби m/n, где n - это степень 2 (2k, где k - целое неотрицательное число).

Примеры:

0.5: 1/2 (21) - представимо точно
0.25: 1/4 = 1/22 - представимо точно
0.75: 3/4 = 3/22 - представимо точно
0.125: 1/8 = 1/23 - представимо точно
0.1: 1/10 - не представимо точно, так как 10 не является степенью 2 (10 = 2 * 5)
0.2: 2/10 = 1/5 - не представимо точно, так как 5 не является степенью 2
В чем причина:

В двоичной системе все числа представляются в виде суммы степеней двойки. Если знаменатель дроби не является степенью двойки, то при переводе в двоичную систему неизбежно возникает бесконечная дробь, которую компьютер может сохранить только с некоторой ограниченной точностью, что приводит к округлению.
2.Это связано с тем, что операции с целыми числами в компьютерах выполняются абсолютно точно и намного быстрее, чем операции с числами с плавающей точкой.

Вот основные причины:

Точность: Целые числа представляются в памяти компьютера точно, без округлений (в пределах их диапазона). Операции сложения, вычитания, умножения целых чисел дают точные результаты.
Скорость: Процессоры оптимизированы для работы с целыми числами. Операции с целыми числами выполняются быстрее, чем операции с числами с плавающей точкой.
Избежание ошибок округления: Операции с числами с плавающей точкой часто приводят к ошибкам округления из-за неточного представления в памяти. Эти ошибки могут накапливаться и приводить к значительным отклонениям от ожидаемого результата при сложных вычислениях.
Упрощение отладки: Программы, работающие с целыми числами, обычно проще отлаживать, так как результаты операций предсказуемы и точны.
Когда это возможно:

Рекомендуется избегать использования чисел с плавающей точкой в тех случаях, когда:

Речь идет о денежных расчетах (где точность важна)
Нужно проводить вычисления, требующие высокой точности
Можно преобразовать задачу к операциям с целыми числами (например, работать с целыми центами вместо рублей)
3.Если вы хотите работать с дробными числами без потери точности, можно использовать следующие подходы:

Представление в виде рациональных чисел (дробь): Вместо чисел с плавающей точкой можно хранить дробные числа в виде пары целых чисел — числителя и знаменателя. При этом каждая операция будет выполняться над числителем и знаменателем, сохраняя точное представление.

Пример: 1/3 + 1/4 = 7/12

Преимущества:

Точное представление (без ошибок округления).
Можно представить любые рациональные числа (в пределах диапазона целых чисел).
Недостатки:

Сложность реализации арифметических операций (умножение, деление, сложение, вычитание требуют более сложных алгоритмов).
Возможен рост числителя и знаменателя при операциях, что может привести к переполнению, если не принимать меры (сокращение).
Сложность сравнения чисел (требуется приведение к общему знаменателю).
Менее эффективно по производительности, чем работа с числами с плавающей точкой (требует больше времени на вычисления).
Фиксированная запятая (Fixed-Point Arithmetic): Используется заранее определенное количество разрядов для целой и дробной частей. Фактически, это представление целых чисел, но подразумевается, что определенная часть разрядов соответствует дробной части.

Пример: Представление числа 1.25 в фиксированной точке с 2 разрядами для дробной части может выглядеть как 125 / 100.

Преимущества:

Проще и быстрее в вычислениях, чем операции с рациональными числами.
Определенная точность.
Недостатки:

Ограниченный диапазон представления чисел (нельзя представить очень большие или очень маленькие числа).
Необходимо заранее знать количество разрядов для целой и дробной частей.
Возможны ошибки округления, но меньшие, чем при работе с числами с плавающей точкой.

**ЗАДАНИЯ**

1. 25: 25 = 16 + 8 + 1 = 24 + 23 + 20 = 110012
31: 31 = 16 + 8 + 4 + 2 + 1 = 24 + 23 + 22 + 21 + 20 = 111112
37: 37 = 32 + 4 + 1 = 25 + 22 + 20 = 1001012
63: 63 = 32 + 16 + 8 + 4 + 2 + 1 = 25 + 24 + 23 + 22 + 21 + 20 = 1111112
85: 85 = 64 + 16 + 4 + 1 = 26 + 24 + 22 + 20 = 10101012
127: 127 = 64 + 32 + 16 + 8 + 4 + 2 + 1 = 26 + 25 + 24 + 23 + 22 + 21 + 20 = 11111112
128: 128 = 27 = 100000002
2. 1000112: 1 * 25 + 0 * 24 + 0 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 32 + 2 + 1 = 3510
1011012: 1 * 25 + 0 * 24 + 1 * 23 + 1 * 22 + 0 * 21 + 1 * 20 = 32 + 8 + 4 + 1 = 4510
1101112: 1 * 25 + 1 * 24 + 0 * 23 + 1 * 22 + 1 * 21 + 1 * 20 = 32 + 16 + 4 + 2 + 1 = 5510
10010112: 1 * 26 + 0 * 25 + 0 * 24 + 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 64 + 8 + 2 + 1 = 7510
10111112: 1 * 26 + 0 * 25 + 1 * 24 + 1 * 23 + 1 * 22 + 1 * 21 + 1 * 20 = 64 + 16 + 8 + 4 + 2 + 1 = 9510
11010012: 1 * 26 + 1 * 25 + 0 * 24 + 1 * 23 + 0 * 22 + 0 * 21 + 1 * 20 = 64 + 32 + 8 + 1 = 10510
3. 173: 173 = 128 + 32 + 8 + 4 + 1 = 101011012 - 5 единиц
195: 195 = 128 + 64 + 2 + 1 = 110000112 - 4 единицы
126: 126 = 64 + 32 + 16 + 8 + 4 + 2 = 11111102 - 6 единиц
208: 208 = 128 + 64 + 16 = 110100002 - 3 единицы
4.Значащие нули - это нули, расположенные между старшей единицей и младшей.

48: 48 = 32 + 16 = 1100002 - 4 нуля
73: 73 = 64 + 8 + 1 = 10010012 - 2 нуля
96: 96 = 64 + 32 = 11000002 - 5 нулей
254: 254 = 128 + 64 + 32 + 16 + 8 + 4 + 2 = 111111102 - 1 ноль
5.Чётность: Число чётное, если его младший бит равен 0.
Делимость на 4: Число делится на 4, если два младших бита равны 0.
Делимость на 8: Число делится на 8, если три младших бита равны 0.
Делимость на 32: Число делится на 32, если пять младших битов равны 0.
6.При сложении нужно помнить: 0 + 0 = 0 0 + 1 = 1 1 + 0 = 1 1 + 1 = 10 (0 в результат, 1 в перенос)
7. 0 - 0 = 0 1 - 0 = 1 1 - 1 = 0 0 - 1 = 1 (заём из старшего разряда) a) 10110112 - 11112 = 10011002 b) 11011012 - 101012 = 10100002 c) 1011102 - 101102 = 111002 d) 1010112 - 110112 = 100002 e) 10111002 - 1012= 10110012 f) 10010012 - 1011012 = 1111002 Для проверки можно перевести в десятичную, вычесть и перевести обратно.
8. 18,125:

Целая часть (18): 18 = 16 + 2 = 24 + 21 = 100102
Дробная часть (0,125): 0,125 = 1/8 = 2-3 = 0,0012
Итого: 18,12510 = 10010,0012
23,25:

Целая часть (23): 23 = 16 + 4 + 2 + 1 = 24 + 22 + 21 + 20 = 101112
Дробная часть (0,25): 0,25 = 1/4 = 2-2 = 0,012
Итого: 23,2510 = 10111,012
37,375:

Целая часть (37): 37 = 32 + 4 + 1 = 25 + 22 + 20 = 1001012
Дробная часть (0,375): 0,375 = 3/8 = 3 * 2-3= 0,0112
Итого: 37,37510 = 100101,0112
48,625:

Целая часть (48): 48 = 32 + 16 = 25 + 24 = 1100002
Дробная часть (0,625): 0,625 = 5/8 = 0,1012
Итого: 48,62510 = 110000,1012
78,875:

Целая часть (78): 78 = 64 + 8 + 4 + 2 = 26 + 23 + 22 + 21 = 10011102
Дробная часть (0,875): 0,875 = 7/8 = 0,1112
Итого: 78,87510 = 1001110,1112
9.11,8:

Целая часть (11): 11 = 8 + 2 + 1 = 23 + 21 + 20 = 10112
Дробная часть (0,8): 0,8 * 2 = 1,6 (1) 0,6 * 2 = 1,2 (1) 0,2 * 2 = 0,4 (0) 0,4 * 2 = 0,8 (0) Дальше пойдет повторение, т.е. 0,810 = 0,1100(1100)…2 = 0,1(100)2
Итого: 11,810 = 1011,1(100)2
15,3:

Целая часть (15): 15 = 8 + 4 + 2 + 1 = 23 + 22 + 21 + 20 = 11112
Дробная часть (0,3): 0,3 * 2 = 0,6 (0) 0,6 * 2 = 1,2 (1) 0,2 * 2 = 0,4 (0) 0,4 * 2 = 0,8 (0) 0,8 * 2 = 1,6 (1) 0,6 * 2 = 1,2 (1) Дальше пойдет повторение, т.е. 0,3 = 0,010011(0011)…. = 0,0(1001)
Итого: 15,310 = 1111,0(1001)2
22,7:

Целая часть (22): 22 = 16 + 4 + 2 = 24 + 22 + 21 = 101102
Дробная часть (0,7): 0,7 * 2 = 1,4 (1) 0,4 * 2 = 0,8 (0) 0,8 * 2 = 1,6 (1) 0,6 * 2 = 1,2 (1) 0,2 * 2 = 0,4 (0) 0,4 * 2 = 0,8 (0) Дальше пойдет повторение, т.е. 0,7 = 0,1011001100… = 0,10(1100)
Итого: 22,710 = 10110,10(1100)2
10.Пусть у нас есть 100 целых чисел. Мы хотим проверить, верно ли, что их среднее арифметическое превышает 0,2. Вместо того, чтобы считать среднее, а потом сравнивать его с 0,2, мы можем сделать следующее:

Суммируем числа: Найдем сумму всех 100 целых чисел. Пусть эта сумма будет sum.
Умножаем 0,2 на 100: 0,2 * 100 = 20
Сравниваем: Если sum больше 20, то среднее арифметическое превышает 0,2. Иначе, оно не превышает 0,2.