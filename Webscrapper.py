import os
import datetime
from privateequitywire import private_equity_wire, private_equity_wire_all
from reuters import reuters, reuters_all
from Sentiment_Analysis import get_prediction, get_prediction_All


d = datetime.datetime.today()
# date = d.strftime('%d.%m.%Y')
date = '29.07.2020'
pages = range(0, 3)


def make_directory(date):

    # Directory
    directory = str(date)

    # Parent Directory path
    parent_dir = "C:/Users/hamra/PycharmProjects/webscraping/Articles"

    # Path
    path = os.path.join(parent_dir, directory)

    if os.path.isdir(path):
        pass
    else:
        os.mkdir(path)


make_directory(date)
# ===================================Specific Date ===================================================================
private_equity_wire(date, pages)
reuters(date, pages)
get_prediction(date)

# ===================================range of dates ==================================================================
"""private_equity_wire_all(pages)
reuters_all(pages)
get_prediction_All()
"""