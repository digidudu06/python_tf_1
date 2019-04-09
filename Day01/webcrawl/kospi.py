from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

if __name__ == '__main__':
    print('{}에 코스피 지수는{}'.format(soup.select('#time3')[0].text, soup.select('#KOSPI_now')[0].text))
