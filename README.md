# Logs Analysis Project
You can easily explore a brief summary of all the important activities happened to the website.
It's very simple, and with one click you have all the results you need :wink: !

The project consists of one ```python``` file.
I have also enclosed a ```text``` file showing a result sample.

## Installation
1. You need to have a [python 2 or 3](https://python.org/downloads/) installed.
2. Open your terminal application (I prefere [Git Bash](https://git-scm.com/downloads)), and connect to your vm using code ```vagrant ssh```.
3. Login into ```news``` database by typing ```psql news```.
4. Create the following database view:
   ```
   create view viewedArticles as
   select a.name as author, b.title as article, count(c.*) as num
   from authors a, articles b, log c
   where a.id = b.author
   and b.slug = replace(c.path, '/article/', '')
   group by a.name, b.title;
   ```
5. Quit from the database by typing ```\q```.
6. Put the source code [news.py](https://github.com/walidpiano/LogsAnalysis/blob/master/news.py) inside the vm shared folders.
7. Run the source code by typing ```python python news.py```
8. You should get log analysis like in [this file](https://github.com/walidpiano/LogsAnalysis/blob/master/result.txt).


## Application Running:
Note that once you run the code, within few seconds you will get the following:
1. The most popular three articles of all time
2. The most popular article authors of all time.
3. On which days did more than 1% of requests lead to errors.

## Requirements
[python 2 or 3](https://python.org/downloads/) is required.