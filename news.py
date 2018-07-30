import psycopg2


def popular_articles():

    # function to print out the most popular 3 articles
    db = psycopg2.connect(database="news")
    c = db.cursor()

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
        print('- "%s" __ %d viewed.' % (item[1], item[2]))
    print("=" * 40)
    print("")


def popular_authors():

    # function to get the most popular 3 authors
    db = psycopg2.connect(database="news")
    c = db.cursor()

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
        print("- %s __ %d views." % (item[0], item[1]))
    print("=" * 40)
    print("")


def over_error():

    # function to get the days with more than 1% request errors
    db = psycopg2.connect(database="news")
    c = db.cursor()

    query = """
        select a.day, (b.num * 100.0 / a.num)::decimal(8, 2) as errors
        from
        (
        select time::date as day, count(*) as num
        from log
        group by day
        ) a
        left join
        (
        select time::date as day, count(*) as num
        from log
        where status != '200 OK'
        group by day
        ) b
        on a.day = b.day
        where (b.num * 100.0 / a.num) > 1;
    """
    c.execute(query)
    result = c.fetchall()

    print("=" * 40)
    print("More than 1% error requests:")
    print("-" * 40)

    for item in result:
        print("- %s __ %.2f%s errors." % (item[0], item[1], '%'))
    print("=" * 40)
    print("")


# to run the functions
popular_articles()
popular_authors()
over_error()
