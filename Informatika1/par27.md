
1.Представление целых чисел со знаком и без знака в компьютере отличается способом, которым отводится бит для обозначения знака числа. В числах со знаком старший бит (знаковый бит) используется для указания знака числа - 0 для положительных чисел и 1 для отрицательных чисел. В числах без знака все биты отводятся для представления самого числа, и они могут принимать только неотрицательные значения.

2.Примеры величин, которые всегда имеют целые неотрицательные значения, включают количество предметов, количество денег, количество людей и т.д. Такие величины никогда не могут быть отрицательными.

3.Целые числа без знака в компьютере представляются прямым кодом. Каждый бит в таком числе отображает определенную степень двойки (от 2^0 до 2^(n-1)), и значение числа получается путем сложения всех этих степеней двойки, которым соответствуют установленные биты.

4.Диапазон представления чисел увеличивается с увеличением количества разрядов. Если увеличить количество разрядов на 1, то диапазон будет увеличен в два раза (возможность хранения большего числа), так как каждый новый разряд может принимать значения либо 0, либо 1. Аналогично, если увеличить количество разрядов на 2 или n, то диапазон увеличится соответственно в 4 или в 2^n раз.

5.Максимальное целое беззнаковое число, которое можно записать с K двоичных разрядов, равно (2^K - 1), так как все разряды заполнены единицами. Если прибавить единицу к этому максимальному значению, то произойдет переполнение и получится число 0.

6.При переполнении процессор обычно отбрасывает старшие разряды результата, оставляя только младшие разряды. Это может привести к искажениям данных и неправильным результатам операций.

7.Максимальное положительное и минимальное отрицательное значения у целых двоичных чисел со знаком имеют разные абсолютные значения, так как старший бит (знаковый бит) в отрицательных числах отводится для обозначения знака, а не для представления значения числа. Это приводит к смещению диапазона значений в отрицательную сторону.

8.Нет, положительные числа не кодируются одинаково в знаковом и беззнаковом форматах. В знаковом формате старший бит используется для обозначения знака числа, в то время как в беззнаковом формате все биты отводятся для представления самого числа.

9.Существуют различные алгоритмы получения дополнительного кода для отрицательного числа. Например, можно инвертировать все биты положительного числа и затем прибавить к нему единицу, чтобы получить дополнительный код этого числа.

10.Алгоритмы Al, A2 и A3 дают один и тот же результат, так как они все основаны на применении операции инверсии (побитового отрицания) и операции сложения к положительному числу.

11.Минимальное отрицательное значение, которое можно записать с K двоичных разрядов, равно -2^(K-1), так как старший бит отведен для обозначения знака (равен 1).

12.Переполнение может возникнуть при сложении двух отрицательных чисел и в этом случае знак результата будет положительным. Например, если сложить -2 и -3, то получится -5, что превышает допустимый диапазон отрицательных чисел.

13.Если правила перевода в дополнительный код применить к отрицательному числу, то получится обратный код числа с добавлением к младшему разряду единицы.

14.Чтобы проверить правильность перевода отрицательного числа в дополнительный код, можно воспользоваться следующим алгоритмом: 1 Если старший (знаковый) разряд числа, записанного в прямом коде, равен 0, то число положительное и никаких преобразований не делается.

2.Если старший (знаковый) разряд числа, записанного в прямом коде, равен 1, то число отрицательное, все разряды числа, кроме знакового, инвертируются, а к результату прибавляется 1.

15.Его преимущество заключается в том, что он позволяет: — заменить операцию вычитания на операцию сложения; — сделать операции сложения и вычитания одинаковыми для знаковых и беззнаковых чисел, что упрощает архитектуру ЭВМ.

16.В источнике говорится, что вместо вычитания в компьютере используется сложение с дополнительным кодом вычитаемого. Это упрощает выполнение арифметических операций, и не нужно проектировать специальное устройство для вычитания чисел.

ЗАДАНИЯ:

2^16 = 65536, 2^24 = 16777216
2.4, 254

3.3

4.–32767

5.1111 1111, 1111 0110, 1001 1100

6.1000 0001, 1000 1010, 1110 0100

7.у отрицательных чисел старший бит равен 1, то есть, это числа, большие или равные 8016: 80, 90, A1, CC, F0, FF

8.максимальное положительное число 2^K‐1 ‐1, минимальное отрицательное ‐ «–2^K‐1 »

9.–126

107! = 5040; 8! = –25216