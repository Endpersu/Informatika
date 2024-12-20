**ВОПРОСЫ**

1) Функция — это блок кода, который выполняет определённую задачу и возвращает результат. В отличие от процедуры, которая выполняет действия, но не возвращает значение, функция должна иметь возвращаемый тип данных. 
2) Пример функции в Паскале:


pascal

 Копировать код
function NameOfFunction(parameters): returnType;
begin
  // body of the function
  Result := someValue;
end;
Пример функции в школьном алгоритмическом языке:


scss

 Копировать код
Функция NameOfFunction(parameters) : returnType
  body of the function
  Вернуть someValue
КонецФункции
3) На Паскале возвращаемое значение функции указывается через специальную переменную Result или может быть указано в конце блока функции:


pascal

 Копировать код
function Add(a, b: Integer): Integer;
begin
  Result := a + b; // Возвращает сумму
end;

В этом примере функция Add возвращает значение типа Integer, которое является суммой a и b.
4) Логические функции — это функции, которые возвращают значения типа Boolean (Истина или Ложь). Они необходимы для проверки условий, например, для валидации данных или выполнения логических операций.