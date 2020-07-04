from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import const as ct
import function_to_scrap_data as fn


# calling main function
def main():
    # Get URL to request to scrap data
    URL = ct.URL
    uClient = urlopen(URL)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    # calling function for scarping books data
    print(fn.get_books_attributed(page_soup))
    # calling function to get category dara
    print(fn.get_category_data(page_soup))


if __name__ == '__main__':
    main()
