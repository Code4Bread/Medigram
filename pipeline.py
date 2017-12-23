import sqlite3
import feedparser
import schedule
import telegram

conn = sqlite3.connect('data.db')
c = conn.cursor()

def DB_create():
    c.execute('''CREATE TABLE data (id INTEGER PRIMARY KEY,title TEXT,link TEXT)''')
    conn.commit()

def DB_insert(article_title,link):
    c.execute('''SELECT id FROM data WHERE title="{}"'''.format(article_title))
    exist = c.fetchone()

    if exist is None:
        c.execute('''SELECT MAX(Id) FROM data''')
        id = c.fetchone()

        if id[0] is None:
            id = 1
        else:
            id = int(id[0]) + 1

        c.execute('''INSERT INTO data(id, title, link) VALUES({},"{}","{}")'''.format(id,article_title,link))
        conn.commit()
        send_update(article_title, link)
        print('Update Sent')

def send_update(article_title, link):
    bot = telegram.Bot("{TOKEN}")
    bot.send_message('{Reply_ID}','<b>{}</b>\n<a href="{}">Read Now</a>'.format(article_title,link),parse_mode='HTML')


def get_update():
    url = 'https://medium.com/feed/@{USERID}'
    feed = feedparser.parse(url)
    for item in feed['items']:
        DB_insert(item['title'],item['link'])
    print('No more new update to send')

def get_updateInterval():
    schedule.every(5).minutes.do(get_update)

    while True:
        schedule.run_pending()
