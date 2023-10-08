import bs4
import requests
import json
from bs4 import BeautifulSoup


base_url = "https://www.rottentomatoes.com/browse/movies_in_theaters"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}

movies = []


def getdata(page):
    global movies
    if page == 0:
        response = requests.get(url=base_url, headers=header)
    else:
        response = requests.get(url=base_url + "?page=" + str(page), headers=header)
    soup = BeautifulSoup(response.text, features="html.parser")
    movie_items = soup.findAll("a", attrs={"class": "js-tile-link"})
    for item in movie_items:
        movie = {}
        span_element_name = item.find("span", attrs={"class": "p--small"})
        span_element_date = item.find("span", attrs={"class": "smaller"})
        audience_score = item.find("score-pairs").get('audiencescore')
        tomato_meter = item.find("score-pairs").get('criticsscore')
        if span_element_name:
            span_text = span_element_name.text.strip()
            movie['电影名称'] = span_text
        if span_element_date:
            span_text = span_element_date.text.strip()
            movie['上映日期'] = span_text
        if tomato_meter:
            movie['烂番茄分数'] = tomato_meter
        else:
            movie['烂番茄分数'] = "暂无"
        if audience_score:
            movie['爆米花指数'] = audience_score
        else:
            movie['爆米花指数'] = "暂无"
        movies.append(movie)


def write_data():
    f = open("./rottentomatoes.txt", 'w', encoding="utf-8")
    for movie in movies:
        f.write(json.dumps(movie, ensure_ascii=False))
        f.write("\n")
    f.close()


if __name__ == "__main__":
    for i in range(0, 100):
        print(f"正在爬取第{i+1}页")
        getdata(i)
    write_data()
    # for i in movies:
    #     print(i)