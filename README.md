# search.py

Программа создаёт список из 10 случайных четных чисел, меньше 100. Список сортируется по возрастанию.
Затем просит пользователя ввести своё число.  

Вызывает функцию s передавая ей на вход список rand_list и число введенное пользователем target.
Функция s проверяет является ли число target равным, одному из чисел из списка rand_list и возвращает позицию числа в списке, если оно там есть. Иначе возвращает none.  

Затем программа выводит список пользователю. Проверяет значение переменной target_index. Если там есть какое-нибудь значение не равное none, то выводит его и число введенное пользователем. Иначе выводит пользователю сообщение, что не может найти введенное им число в списке.  

В программе также есть проверка введенного пользователем значения на корректность. Если введенное значение не является целым числом, то срабатывает исключение и выводится сообщение что значение не подходит.   
