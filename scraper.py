from requests import get
from bs4 import BeautifulSoup


def scrape_movie(movie_name):
    ##### For Fetching Link of First Title From Results ######
    url = "https://www.imdb.com/find?q="+movie_name+"&ref_=nv_sr_sm"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    result = html_soup.find('td', class_='result_text')

    ##### For Scraping Movie Info ######

    movie_url = 'https://www.imdb.com'+result.a['href']
    response = get(movie_url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    movieInfo = {'title': '', 'rating': '', 'duration': '', 'categories': [], 'summary': '',
                 'directors': [], 'writers': [], 'stars': [], 'casts': [], 'storyline': '', 'genres': []}
    ##### For Scraping Title ######

    title = html_soup.find('h1').text
    movieInfo['title'] = title.replace('\xa0', ' ')

    ##### For Scraping Rating ######

    rating = html_soup.find('span', itemprop='ratingValue').text
    movieInfo['rating'] = rating+"/10"

    ##### For Scraping Duration ######

    duration = html_soup.find('time').text.strip()
    movieInfo['duration'] = duration

    ##### For Scraping Category ######

    categories_data = html_soup.find('div', class_='subtext').find_all('a')
    categories_data.pop()
    categories = []
    for category in categories_data:
        categories.append(category.text)

    movieInfo['categories'] = categories

    ##### For Scraping Summary ######

    plot = html_soup.find('div', class_='plot_summary').find_all('div')

    summary = plot[0].text.strip()
    movieInfo['summary'] = summary

    ##### For Scraping List of Directors ######
    directors = []
    for director in plot[1].find_all('a'):
        directors.append(director.text)

    movieInfo['directors'] = directors

    ##### For Scraping List of Writers ######
    writers = []
    for writer in plot[2].find_all('a'):
        writers.append(writer.text)
    movieInfo['writers'] = writers

    ##### For Scraping List of Stars ######
    stars = []
    for star in plot[3].find_all('a'):
        stars.append(star.text)
    stars.pop()
    movieInfo['stars'] = stars

    ###### For Scraping Cast ######
    casts_html = html_soup.find('table', class_='cast_list').find_all('tr')
    casts_html.pop(0)

    casts = []
    for cast_html in casts_html:
        casts.append(cast_html.find_all('td')[1].a.text.replace("\n", ""))
    movieInfo['casts'] = casts

    ##### For Scraping Storyline ######

    storyline = html_soup.find(
        'div', class_='inline canwrap').p.span.text.strip()
    movieInfo['storyline'] = storyline

    ######## For Scraping Genres #######
    genres_html = html_soup.find_all(
        'div', class_='see-more inline canwrap')[1].find_all('a')
    genres = []

    for genre_html in genres_html:
        genres.append(genre_html.text)
    movieInfo['genres'] = genres

    ########## FINAL RESULT ###########
    return movieInfo
