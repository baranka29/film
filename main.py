from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def main():
    return render_template('main.html')


class MyDB:
    def __init__(self, filename='comedy.txt'):
        self.comedy = filename
        with open(filename, 'a', encoding='UTF-8') as f:
            f.write('')

    def add(self, data: str):
        with open(self.comedy, 'a', encoding='UTF-8') as f:
            f.write(data + '\n')

    def output(self):
        with open(self.comedy, encoding='UTF-8') as f:
            return f.readlines()


"""
Список комедий
"""


class Comedy:
    def __init__(self, comedy_name: str):
        # я храню базу данных
        self.comedy = MyDB(comedy_name)

    def push_new_buy(self, filme, URL):
        # я делаю из записей строку
        record = filme + ' ' + f"<a href=\"{URL}\">Смотреть</a>"
        #     record=filme + URL
        # с помощью ранее написанного класса мы добавляем запись в хранилище
        self.comedy.add(record)

    def __str__(self):
        s = ''
        # с помощью ранее написанного класса мы читаем всё из хранилища
        # и просто возращаем
        for el in self.comedy.output():
            s += el + " <br>"
        return s

comedy = Comedy("comedy.txt")
    # comedy.push_new_buy("Отпетые мошенницы", "https://130223.lordfilm.black/3087-film-otpetye-moshennicy-2019.html")
    # comedy.push_new_buy("Отель «Белград»", 'https://w.lordfilmls-lu.site/filmy-2020/14607-otel-belgrad-2020-smotret-online-besplatno.html')comedy.push_new_buy("Как стать принцессой", 'https://2022-c30.lordfilm0.com/films/10191-kak-stat-princessoj.html')
    # comedy.push_new_buy("Круэлла", "https://cr.mwfilm.ru/filmy/41297-krujella-2021-7926-92224.html")
    # comedy.push_new_buy("Стажёр", "https://2022-v20.lordfilm0.com/films/8858-stazher-24-11.html")
    # comedy.push_new_buy("Один дома", 'https://cr.mwfilm.ru/filmy/6406-odin-doma-home-alone-1990-1266-82043.html')
    # comedy.push_new_buy("Иван Васильевич меняет профессию", "https://cr.mwfilm.ru/filmy/21429-ivan-vasilevich-menjaet-professiju-1973.html")
    # comedy.push_new_buy("Холоп", "https://ww19.lordsfilm.win/25298-holop-film-2019-17-02-21.html")
    # comedy.push_new_buy("Самый лучший день", "https://lo-rd20.lordfilm6.zone/29068-2201-samyj-luchshij-den-2015.html")
from flask import Flask
from flask import redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def pokupki():
    return "<h1>Список жанров:</h1>" + "<a href=\"http://localhost:5000/com\">Комедия</a> <br>" + "<a href=\"http://localhost:5001/com\">Мелодрама</a> <br>" + "<a href=\"http://localhost:5002/com\">Ужасы</a> <br>" + "<a href=\"http://localhost:5003/com\">Детективы</a> <br>" + "<a href=\"http://localhost:5004/com\">Боевики</a> <br>" + "<a href=\"http://localhost:5005/com\">Триллеры</a> <br>" + "<a href=\"http://localhost:5006/com\">Фантастика</a> <br>"

@app.route('/com')
def get_com():
    return str(comedy )
app.run()