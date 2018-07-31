#!/usr/bin/env python3

import psycopg2


def popular_articles(db_connection):
    """Function to print out the most popular 3 articles."""

    c = db_connection.cursor()

    query = """
         select * from viewedArticles
         order by num desc
         limit 3;
    """
    c.execute(query)
    result = c.fetchall()

    print("=" * 40)
    print("The most popular three articles:")
    print("-" * 40)
    for item in result:
        print('- "{}" __ {} viewed.'.format(item[1], item[2]))

    print("=" * 40 + '\n')


def popular_authors(db_connection):
    """Function to get the most popular 3 authors."""

    c = db_connection.cursor()

    query = """
        select author, sum(num) as num
        from viewedArticles
        group by author
        order by num desc
        limit 3;
    """
    c.execute(query)
    result = c.fetchall()

    print("=" * 40)
    print("The most popular article authors:")
    print("-" * 40)

    for item in result:
        print("- {} __ {} views.".format(item[0], item[1]))

    print("=" * 40 + '\n')


def over_error(db_connection):
    """Function to get the days with more than 1% request errors."""

    c = db_connection.cursor()

    query = """
        select daily_requests.day, (daily_errors.num * 100.0 / daily_requests.num)::decimal(8, 2) as errors
        from
        (
        select time::date as day, count(*) as num
        from log
        group by day
        ) daily_requests
        left join
        (
        select time::date as day, count(*) as num
        from log
        where status != '200 OK'
        group by day
        ) daily_errors
        on daily_requests.day = daily_errors.day
        where (daily_errors.num * 100.0 / daily_requests.num) > 1;
    """
    c.execute(query)
    result = c.fetchall()

    print("=" * 40)
    print("More than 1% error requests:")
    print("-" * 40)

    for item in result:
        print("- {} __ {}% errors.".format(item[0], item[1]))

    print("=" * 40 + '\n')


# to run the functions
conn = psycopg2.connect(database="news")
popular_articles(conn)
popular_authors(conn)
over_error(conn)
conn.close()
