**ВОПРОСЫ**

1) Символьной строкой называется набор нумерованных символов, которые хранятся в оперативной памяти компьютера под одним именем и располагаются последовательно друг за другом.
2) Заменять строки массивами символов неудобно по нескольким причинам: 

Перемещение памяти. При замене или перемещении строк в массиве символов нужно копировать или перемещать каждый символ в новую позицию. Это занимает много времени и ресурсов процессора. 

Изменение размера строки. Если нужно добавить новый символ в строку или удалить символ из неё, придётся пересоздать массив символов и скопировать все символы из старого массива в новый. Это также ресурсоёмкая операция. 

Ограничение длины строки. Массивы символов имеют фиксированную длину, которую нужно определить заранее. Если строка превышает этот предопределённый размер, придётся создать новый массив с большей длиной и скопировать туда все символы. 

Работа с различными типами данных. При работе с массивами символов может потребоваться преобразовывать их в другие типы данных или использовать различные функции для обработки текстовой информации. Это также может усложнить процесс изменения строки.
3) В школьном алгоритмическом языке строки объявляются с использованием литерного типа данных, который обозначается «лит» (от слова «литерный» — буквенный). Пример объявления строки: лит s. 

В Паскале строки объявляются с использованием строкового типа данных, который обозначается «string» (в переводе с англ. — строка). 

 Пример объявления и инициализации строковой переменной: var a:string; begin a:='Привет всем!'; writeln(a); end.
4) Чтобы обратиться к определённому элементу строки с заданным номером, нужно указать его индекс в квадратных скобках. 
5)  Длина строки вычисляется как количество содержащихся в ней символов, включая пробелы.
6) Операция + применительно к строкам означает конкатенирование (то есть склейку). Это пример перегрузки операции: изначальному оператору сложения чисел в стандартной библиотеке для строки придали новый смысл.
7) Со строками можно выполнять следующие арифметические операции:= - присваивание значения.+= - добавление в конец строки другой строки или символа.+ - конкатенация двух строк, конкатенация строки и символа.==, != - посимвольное сравнение.<, >, <=, >= - лексикографическое сравнение.
8) Чтобы определить, что при поиске в строке образец не найден, обычно функция поиска подстроки возвращает -1 или что-то в этом роде. 
9) Средства школьного алгоритмического языка и Паскаля для работы со строками различаются по набору доступных функций. 

Школьный алгоритмический язык обычно предоставляет только базовые функции, например, возможность объединения строк или получения длины строки. 

Паскаль обычно предоставляет более разнообразные функции для работы со строками, включая поиск символов в строке, замену подстрок и т. д.
10) Для преобразования числа из символьного вида в числовой и обратно можно использовать следующие методы:

Для преобразования в числовой вид можно применить функцию atoi (ASCII to integer). Она преобразует строку, содержащую цифры, в целое число. Пример использования: int num = atoi("12345"); // Преобразует строку "12345" в число 12345. 

Для преобразования в символьную строку можно использовать функцию itoa (integer to ASCII). Она конвертирует целое число в строковое представление в указанной системе счисления. Пример использования: char buffer[33]; itoa(255, buffer, 16); // Преобразует число 255 в строку "FF" в шестнадцатеричной системе
11) Строку не всегда можно преобразовать в число, если параметр функции не является строковым представлением числа. 
Например, ошибки могут возникать, если в строковом представлении число разделяется на триады, а в качестве символа разделения используется как обычный пробел, так и неразрывной. Также проблемы могут возникнуть, если в строковом представлении дробная часть отделяется от целой части либо точкой, либо запятой.

Определить, что преобразование закончилось неудачно, можно по появлению ошибки, например, «Преобразование значения к типу Число не может быть выполнено». Она означает, что разработчик пытается преобразовать в число значение, которое в число преобразовано быть не может.
12) Рекурсивный перебор — это метод решения задачи перебора всех возможных вариантов путём последовательного выбора вариантов и проверки их на соответствие заданным условиям.
13) Рекурсивные и нерекурсивные методы решения переборных задач имеют свои особенности и примеры применения. 

Нерекурсивные методы могут быть более простыми, поскольку они не требуют создания стека вызовов функций. Например, задача состоит в том, чтобы найти сумму нечётных чисел от 1 до 10. Нерекурсивное решение можно представить в виде цикла, который будет увеличивать сумму на каждом нечётном числе от 1 до 10. Рекурсивное решение же было бы сложнее реализовать и потенциально менее эффективно. 

В некоторых случаях рекурсивные методы могут быть более удобными.

 Например, если задача состоит в переборе всех возможных комбинаций символов в строке, то рекурсивный метод с использованием стека вызовов может представлять более лаконичное и понятное решение, чем нерекурсивный.