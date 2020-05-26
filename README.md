# bellman-ford
Найти  кратчайший v-w путь в сети с произвольными весами.

     Метод решения: алгоритм Форда-Беллмана.
 
Пример.   Для сети                 -25
     -------                      1 ---> 2      4
                                  |      ^      ^
                                 4|      |0     |7
                                  +----> 3 -----+
     файл данных должен быть следующим:
     4
     0
     1 -25   3   0   0
     1   4   0
     3   7   0
     1
     4
 
Файл входных данных:
 Сеть, заданная списками ПРЕДШ[].

     N - количество вершин.
     Далее последовательно  расположены  списки  предшествующих для каждой
вершины. В список заносится номер вершины и вес дуги. Список заканчивается
0 ( ВНИМАНИЕ ! не путать с нулевым весом). В конце файла записаны источник
и цель.
 
Файл выходных данных:
 В случае  отсутствия пути в файл результатов необходимо записать "N",
при наличии пути - "Y" и далее с новой строки весь путь.  Путь начинается
источником и заканчивается целью. Узлы отделяются друг от друга пробелами,
вес пути вычисляется как сумма весов всех дуг, входящих в него и записыва-
ется в третьей строке.