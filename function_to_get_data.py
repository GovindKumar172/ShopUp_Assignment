from urllib.request import urlopen as ure
from bs4 import BeautifulSoup as soup
import const as ct

# Get URL to request to scrap data
URL = ct.URL
uClient = ure(URL)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all(ct.BOOK_TAG, {"class": ct.BOOK_CLASS})

# container = containers[0]
# print(container.div.img['alt'])
# book_name = container.div.img['alt']
# print(book_name)
# image_link = container.div.img['src']
# print(image_link)
# rating = container.article.p['class']
# print(rating[1])
# price = container.find_all("p", {"class": "price_color"})
# print(price[0].text)
# in_stock = container.find_all("p", {"class": "instock availability"})
# print((in_stock[0].text).strip())

# write into file
fileName = 'bookScrap.csv'
f = open(fileName, 'w')
headers = "book_name,image_link,rating,price,in_stock\n"
f.write(headers)

for container in containers:

    book_name = container.div.img['alt']
    image_link = container.div.img['src']
    rating = container.article.p['class'][1]
    price = container.find_all("p", {"class": "price_color"})
    price = price[0].text
    in_stock = container.find_all("p", {"class": "instock availability"})
    in_stock = in_stock[0].text.strip()

    # print('book_name:', book_name)
    # print('image_link:', image_link)
    # print('rating:', rating)
    # print('price:', price)
    # print('in_stock:', in_stock)
    # print(book_name.replace(",", "|") + "," + image_link.replace("../","") + "," + rating + "," + price + "," + in_stock + "\n")

    f.write(book_name.replace(",", "|") + "," + "'" + image_link.replace("../","") + "'" + "," + rating + "," + price + "," + in_stock + "\n")

# Close file after write
f.close()


# category name

containers = page_soup.find_all("ul", {"class": "nav nav-list"})
# print(len(containers))

# write into file
fileName = 'category.csv'
f = open(fileName, 'w')
headers = "cat_name,link\n"
f.write(headers)

for container in containers:
    for i in range(0, 51):
        category = container.find_all('a')[i].text.strip()
        link = container.find_all('a')[i]['href']
        f.write(category + "," + "'" + link.replace(".", "") + "'" + "\n")

# Close file after write
f.close()
