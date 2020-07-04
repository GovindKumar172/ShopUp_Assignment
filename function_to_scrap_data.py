import const as ct


# Get data for books scarping
def get_books_attributed(page_soup):
    try:
        containers = page_soup.find_all(ct.BOOK_TAG, {"class": ct.BOOK_CLASS})
    except KeyError as error:
        print(error)
    """
    container = containers[0]
    print(container.div.img['alt'])
    book_name = container.div.img['alt']
    print(book_name)
    image_link = container.div.img['src']
    print(image_link)
    rating = container.article.p['class']
    print(rating[1])
    price = container.find_all("p", {"class": "price_color"})
    print(price[0].text)
    in_stock = container.find_all("p", {"class": "instock availability"})
    print((in_stock[0].text).strip())
    """
    # write into file
    fileName = ct.BOOK_FILE
    f = open(fileName, 'w')
    headers = ct.BOOK_FILE_HEADER
    f.write(headers)

    for container in containers:
        try:
            book_name = container.div.img['alt']
            image_link = container.div.img['src']
            rating = container.article.p['class'][1]
            price = container.find_all("p", {"class": "price_color"})
            price = price[0].text
            in_stock = container.find_all("p", {"class": "instock availability"})
            in_stock = in_stock[0].text.strip()
            f.write(book_name.replace(",", "|") + "," + "'" + image_link.replace("../",
                                                                            "") + "'" + "," + rating + "," + price + "," + in_stock + "\n")
        except KeyError as error:
            print(error)
    # Close file after write
    f.close()

    return "Books data scraping is completed !!"


# Get category data
def get_category_data(page_soup):
    # category name and link scrapping
    try:
        containers = page_soup.find_all(ct.CAT_TAG, {"class": ct.CATEGORY_CLASS})
    except KeyError as error:
        print(error)
    # write into file
    fileName = ct.CAT_FILE
    f = open(fileName, 'w')
    headers = ct.CAT_FILE_HEADER
    f.write(headers)

    for container in containers:
        try:
            for i in range(ct.CAT_LIMIT):
                category = container.find_all('a')[i].text.strip()
                link = container.find_all('a')[i]['href']
                f.write(category + "," + "'" + link.replace(".", "") + "'" + "\n")
        except KeyError as error:
            print(error)
    # Close file after write
    f.close()

    return "Category data scraping is completed !!!"
