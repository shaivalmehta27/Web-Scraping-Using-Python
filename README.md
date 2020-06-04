# Web-Scraping-Using-Python
In this repository, I have covered that how we could perform scraping and get significant information using Python libraries like Request and Pandas.

### Scraping Overview and HTML

The process of Web scraping can be widely divided into various steps:

1. First and Foremost, Understand and inspect(You can right click on any website and can click Inspect to check HTML markers) the web page to find HTML tags which is associated with exact information we want.
2. Use various libraries like Requests and Pandas to scrape websites.
3. Convert scraped data to get it in the form we want(csv, excel, json, html).

### Getting Started

Before scraping, make sure you have Python(version 3+), requests, HTML and Pandas installed on your system. If you have not installed, then open Terminal/Command Prompt on your system and type following commands-

```
pip3 install requests
pip3 install requests-HTML
pip3 install pandas
```

### Let’s Scrape!!!

1. **Import Libraries:**

```
import requests
from requests_htmlimport HTML 
import pandas as pd
```

2. **Get the URL, Connecting to Website, Checking Status Code:**

```
def url_to_txt(url):
    req = requests.get(url)
    if req.status_code == 200:
        html_text = req.text
        return html_text
    return None
url = "<https://www.imdb.com/chart/toptv>"
html_text = url_to_txt(url)
r_html = HTML(html=html_text)
```

- “*req*”variable stores the HTML content of our web page into request object.
- Now, we will check for status. If **status_code** is **200** then connection is **OK Success**, If not it will give us *None* in return.
- Variable “*r_html*” will contain data of the webpage and when we print(r_html.text) it will give us below output:

![https://cdn-images-1.medium.com/max/1500/1*WqsAvOinFBjx9DzriPepZg.png](https://cdn-images-1.medium.com/max/1500/1*WqsAvOinFBjx9DzriPepZg.png)

Output: When we print(r_html.text) — — — Actual data of the webpage

3. **Inspecting whole data:**

```
table_class = r_html.find(".lister")
parsed_table = table_class[0]
rows = parsed_table.find("tr")
```

![https://cdn-images-1.medium.com/max/1000/1*MeVRtE12Mwj1xD8ySEnQkw.png](https://cdn-images-1.medium.com/max/1000/1*MeVRtE12Mwj1xD8ySEnQkw.png)

Inspect and look up for exact HTML tags

- Variable “*table_class*” will find “*lister*” division class inspecting the web page.

> Note: It is very important to inspect correct HTML tags to grab exact information we want

- I have taken “*table_class[0]*” because length of table_class is only 1.
- Now, we will find “*tr*” tag in the “*parsed_table*” variable to get more precise information.

4. **Extracting required elements:**

```
for row in rows[1:]:
    cols = row.find("td")
    only_title = [titles.text.split('.', 1) for titles in cols[1:2]]
    ranks = only_title[0][0]
    title = only_title[0][1]

    ratings = [rating.text for rating in cols[2:3]]
```

- As we want to scrape only 3 things from this website: Rank, Title, Ratings. We will extract elements that are relevant to our scraping data.
- We have sliced our list from [1:] just because row[0] contained below information:

![https://cdn-images-1.medium.com/max/1000/1*BUNmvyp5LHTvN1AS7JphcQ.png](https://cdn-images-1.medium.com/max/1000/1*BUNmvyp5LHTvN1AS7JphcQ.png)

And it was not necessary because it contains only header text.(I’ll show you later why we skipped this)

- There are many sub tags inside parent tag. Now, we will find “*td*” tag inside our rows variable which will give us 3 exact information that we want.
- The reason we splitted(‘.’) is because website data containing rank was denoted as — Example(20. The Vietnam War (2017) so in order to seperate rank from title we used split method.)
- We have stored precise data and divided variables into: ranks, title, ratings respectively.

5. **Converting our Scraped data to .csv file using Pandas:**

```
movies_stuff =pd.DataFrame({
            'Rank': ranks,
            'Title Of Tv Show': title,
            'IMDb Rating': ratings
    })
    print(movies_stuff)
    movies_stuff.to_csv('BestTvShows.csv', encoding='utf-8', index=False, mode='a')
```

- The reason we skipped our header text is because I wanted to show that we can write header names according to our choices too.
- Printing movie_stuff will give below output:

![https://cdn-images-1.medium.com/max/1000/1*WtCgy_eGFcPqr9Fo8bp0Cw.png](https://cdn-images-1.medium.com/max/1000/1*WtCgy_eGFcPqr9Fo8bp0Cw.png)

Screenshot is just captured for first 7 TV shows from total 250 shows.

- “*variablename.to_csv*” will convert scraped data into csv file.
- Index = False means when .csv file is created, it will not use it’s own index numbers, rather it will use default index numbers.
- There are basically 3 modes to store data into .csv file:
1. Write(W): It writes into the file and creates new file every time program runs. Default method
2. Read(R): It reads data line by line.
3. Append(A): It appends data and it doesn’t create new file. It add data to the existing data present inside it.

### The Entire Code:

```
import requests
from requests_html import HTML
import pandas as pd

def url_to_txt(url):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text
    return ""

url = "<https://www.imdb.com/chart/toptv>"
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
```

### Output:

![https://cdn-images-1.medium.com/max/1000/1*GQFlLkFg6VeKO1_DjgZBGQ.png](https://cdn-images-1.medium.com/max/1000/1*GQFlLkFg6VeKO1_DjgZBGQ.png)

Thank you Everyone. Stay Safe and Happy Scraping!!
