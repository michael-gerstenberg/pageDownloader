# webpageDownloadBuffer

This little script downloads (and buffers) web pages.

Buffering can be interesting for instance...

... to reduce the amount of requests made to a website.

... to scrape pages much faster.

... to reduce the amount of captchas needed to be solved.


To start just download/clone this repo and integrate it into your application.
It is alawys recommended to work inside an virtual environment (`venv`).
Install all dependencies:

` pip install -r requirements.txt `

Rename the config_example.py into config.py and replace the MongoDB connection string. I recommend to use a MongoDB Atlas cluster. You can get a free one here: https://www.mongodb.com/cloud/atlas

Include the script in your application:

` from load_page import get_page_soup `

Make use of the method like that:

` page_soup = get_page_soup('https://deepl.com') `

` page_soup = get_page_soup('https://newspaper.com', 60) `

The method will return the page content as BeautifulSoup object. Webpages will be downloaded into a specific folder and the corresponding meta data is stored into a MongoDB collection. Both can be specified in the `config.py`.

Just open an issue if something doesn't fit or you wish more functionality.

Cheers,

Michael