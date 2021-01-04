# Houzz Scrapy

Crawl [houzz.com](houzz.com) data by scrapy. I used  **scrapy-user-agent** and **scrapy-proxy-pool** libraries to bypass the restriction.

## Settings

You can change `start_urls` list and `CLOSESPIDER_PAGECOUNT` at <u>/houzz/spiders/houzz_spider.py</u> 

## Setup and Run

1. Clone the repo by `$ git clone https://github.com/mhmp98/Houzz-Scrapy.git`
2. Go to cloned directory and create a virtual environment `$ python3 -m virtualenv venv`
3. Activate the virtual environment using `$ source /venv/bin/activate` 
4. Install the requirements using `$ pip3 install -r requirements.txt`
5. Run project using `$ scrapy crawl houzz -o houzz.csv --loglevel=INFO` 

