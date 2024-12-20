**ВОПРОСЫ**

1) Что такое процедуры? В чём смысл их использования? Процедуры — это именованные фрагменты кода, которые выполняют определённую задачу. Они позволяют структурировать программу, повторно использовать код и улучшать его читаемость.
2) Как оформляются процедуры в школьном алгоритмическом языке и в Паскале? В школьном алгоритмическом языке процедуры могут оформляться как "Процедура имя(параметры) ... КонецПроцедуры". В Паскале они оформляются аналогично с ключевым словом "procedure": pascal procedure MyProcedure(parameter: type); begin // тело процедуры end;
3) Достаточно ли включить процедуру в текст программы, чтобы она «сработала»? Нет, нужно также вызвать процедуру в тексте основной программы. В противном случае код процедуры не выполнится.
4) Что такое параметры? Зачем они используются? Параметры — это значения, которые передаются в процедуру. Они позволяют обрабатывать входные данные и делать процедуру более универсальной.
5) Какие переменные называются локальными? Где они объявляются? Локальные переменные объявляются внутри процедуры и доступны только в пределах этой процедуры.
6) Как оформляются процедуры, имеющие несколько параметров? Процедуры с несколькими параметрами оформляются, перечисляя параметры через запятую в заголовке процедуры: pascal procedure MyProcedure(param1: type1; param2: type2);
7) Что такое изменяемые параметры? Зачем они используются? Изменяемые параметры позволяют процедуре изменять значения переменных, переданных ей в качестве аргументов. Это полезно, когда нужно возвращать несколько значений из процедуры.
8) Как в заголовке процедуры отличить изменяемый параметр от неизменяемого? Приведите примеры. В Питоне все параметры неизменяемые по умолчанию, кроме объектов. В Паскале изменяемые параметры обозначаются ключевым словом "var":

pascal procedure MyProcedure(var param: type);
9) Какие типы параметров выделяются в школьном алгоритмическом языке? Как они объявляются? В школьном алгоритмическом языке можно выделить простые, массивные и структурные параметры. Они объявляются через соответствующий тип данных.

**ЗАДАНИЯ**

1) Процедура для вывода числа в восьмеричной системе: pascal procedure PrintOctalNumber(num: Integer); begin if num < 810 then WriteLn(Octal(num)); end;
2) Процедура для вывода числа в шестнадцатеричной системе: pascal procedure PrintHexadecimalNumber(num: Integer); begin if num < 65536 then WriteLn(Hex(num)); end;
3) Процедура для вывода квадрата из звёздочек: pascal procedure PrintStarSquare(N: Integer); var i, j: Integer; begin for i := 1 to N do begin for j := 1 to N do Write('*'); WriteLn; end; end;
4) Процедура для вывода возраста с правильными окончаниями: pascal procedure PrintAge(age: Integer); begin if (age mod 10 = 1) and (age mod 100 <> 11) then WriteLn(age, ' год') else if (age mod 10 >= 2) and (age mod 10 <= 4) and (age mod 100 <> 12) and (age mod 100 <> 13) and (age mod 100 <> 14) then WriteLn(age, ' года') else WriteLn(age, ' лет'); end;
5) Процедура для вывода числа прописью:

procedure PrintNumberInWords(num: Integer);
begin
// Реализация вывода числа прописью
end;
6) Процедура для вывода первых N чисел Фибоначчи: pascal procedure PrintFibonacci(N: Integer); var a, b, temp, i: Integer; begin a := 0; b := 1; for i := 1 to N do begin Write(a, ' '); temp := a; a := b; b := temp + b; end; end;
7) Процедура для проверки простоты числа: pascal procedure CheckPrime(var num: Integer; var isPrime: Boolean); var i: Integer; begin isPrime := True; if num < 2 then isPrime := False; for i := 2 to Trunc(Sqrt(num)) do if (num mod i = 0) then begin isPrime := False; Break; end; end;
8) Процедура для вывода цифр числа, начиная с последней: pascal procedure PrintDigitsReversed(num: Integer); begin while num > 0 do begin WriteLn(num mod 10); num := num div 10; end; end;
9) Процедура для вывода цифр числа, начиная с первой: pascal procedure PrintDigitsForward(num: Integer); var digits: array of Integer; i: Integer; begin while num > 0 do begin SetLength(digits, Length(digits) + 1); digits[High(digits)] := num mod 10; num := num div 10; end; for i := High(digits) downto 0 do WriteLn(digits[i]); end;
10) Процедура для вывода делителей числа: pascal procedure PrintDivisors(num: Integer); var i: Integer; begin for i := 1 to num do if (num mod i = 0) then Write(i, ' '); WriteLn; end;
11) Процедура для вывода линии из символов: pascal procedure PrintLine(M: Integer); var i: Integer; begin for i := 1 to M do Write('-'); WriteLn; end;
12) Процедура для вывода числа в римской системе счисления: pascal procedure PrintRoman(num: Integer); var roman: array[1..13] of String = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'L', 'C', 'D', 'M'); begin // Реализация для преобразования числа в римские цифры end;