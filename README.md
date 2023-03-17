в колонке Тестовые кейсы / задачи DS

Описание
Тестовое задание по графовым базам данных

1.Установить графовую базу из списка DB-Engines Ranking
Предпочтительные - nebula
Предпочтительный язык запросов cypher
===
docker run -e ARANGO_RANDOM_ROOT_PASSWORD=1 -p 8529:8529 -d arangodb
docker run --publish=7474:7474 --publish=7687:7687 -v=d:\db\neo4j\data:/data -v d:\db\neo4j\data:/import neo4j

2.Создать ipynb ноутбук в котором:
===
pip install pandas
jupyter.ipynb

3.Считать данные из источника https://disk.yandex.ru/d/s6wWqd8Ol_5IvQ
===
data_test.csv

4.Внести данные из таблицы в графовую БД
===
http://localhost:7474
user/pass=neo4j/neo4j
http://localhost:7474/browser/
LOAD CSV WITH HEADERS FROM "file:///data_test.csv" AS line
MERGE (n:Person {id: toInteger(line[0]))
SET n.name = line[1]
RETURN n

5.Построить графовое представление в БД, осуществить несколько запросов на языке запросов к графовой БД
===
MATCH(n) RETURN n

:auto LOAD CSV WITH HEADERS FROM 'file:///data_test.csv' AS line FIELDTERMINATOR ';'
CALL {
  WITH line
  MERGE (:Person {name: line['ФИО участника события 1']})
  MERGE (:Person {name: line['ФИО участника события 2']})
} IN TRANSACTIONS OF 500 ROWS

:auto LOAD CSV WITH HEADERS FROM 'file:///data_test.csv' AS line FIELDTERMINATOR ';'
CALL {
  WITH line
  MATCH (a:Person),(b:Person)
  WHERE a.name = line['ФИО участника события 1'] AND b.name = line['ФИО участника события 2']
  MERGE (a)-[:PARENT]->(b)
} IN TRANSACTIONS OF 500 ROWS

MATCH p = (:Person)-[*]->(:Person)
WHERE length(p)>1
RETURN p

6.Важный пункт. Найти взаимосвязи визуально и с помощью алгоритмов (алгоритмы на ваше усмотрение). Обратить внимание на сложные сообщества, провести анализ сложных сообществ, сделать выводы.
===
MATCH p = (:Person)-[*]->(:Person)
WHERE length(p)>1
RETURN p

Большинство участников событий связаны 1 ребром.
Displaying 86 nodes, 1,684 relationships. - формируют 5 автономных групп с количеством ребер > 1
1 группа кольцевая, 2 группы звезда, 2 группы комбинированные

7.Написать rest сервис на python к графовой БД в котором на вход поступает ФИО, на выходе graphml или json
===
pip install flask
rest.py
http://127.0.0.1:5000/?fio=Медведева%20Дарья%20Алексеевна
вывод json:
Медведева Дарья Алексеевна <- [
    {
        "name": "Кондратьев Борис Германович"
    },
    {
        "name": "Помыкалова Тамара Федоровна"
    },
    {
        "name": "Безгачий Денис Ефимович"
    },
    {
        "name": "Дуброва Анжелика Григорьевна"
    },
    {
        "name": "Пчелинцев Артур Глебович"
    }
]

8.Результаты представить на гитхаб и в виде кода + небольшой презентации
===
Сделано. Презентация - непонятно в каком виде.

9.Прислать ссылку на решение и резюме в телеграм @frankshikhaliev
===
git clone https://github.com/may65/mindset.git
https://kraskovo.hh.ru/resume/5134faa0ff0ba4f7de0039ed1f7034374c386a

10.Также надо будет заполнить форму
Стажировка datascience в Mindset (основная форма)
===
Сделано

11.Срок выполнения задания - около 10 дней, если вы не успеваете можете взять больше времени
===
Потрачено больше 10 дней. Графовые БД изучал.

Действия
Фрэнк Шихалиев добавил(а) эту карточку в список Тестовые кейсы / задачи DS
