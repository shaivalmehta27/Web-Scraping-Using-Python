import requests
from requests_html import HTML
import pandas as pd


def url_to_txt(url):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text
    return ""

url = "https://www.imdb.com/chart/toptv"
html_text = url_to_txt(url)
r_html = HTML(html=html_text)
table_class = r_html.find(".lister")
parsed_table = table_class[0]
rows = parsed_table.find("tr")


for row in rows[1:]:
    cols = row.find("td")

    only_title = [titles.text.split('.', 1) for titles in cols[1:2]]
    ranks = only_title[0][0]
    title = only_title[0][1]

    ratings = [rating.text for rating in cols[2:3]]

    movies_stuff =pd.DataFrame({
            'Rank': ranks,
            'Title Of Tv Show': title,
            'IMDb Rating': ratings
    })
    print(movies_stuff)
    movies_stuff.to_csv('BestTvShows.csv', encoding='utf-8', index=False, mode='a')
