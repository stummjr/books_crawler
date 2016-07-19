# -*- coding: utf-8 -*-

BOT_NAME = 'books'

SPIDER_MODULES = ['books.spiders']
NEWSPIDER_MODULE = 'books.spiders'

ROBOTSTXT_OBEY = True
HTTPCACHE_ENABLED = True

SPIDER_MIDDLEWARES = {
    'scrapy_deltafetch.DeltaFetch': 100,
    'scrapy_magicfields.MagicFieldsMiddleware': 200,
}

DELTAFETCH_ENABLED = True

MAGICFIELDS_ENABLED = True
MAGIC_FIELDS = {
    "timestamp": "$time",
    "spider": "$spider:name",
    "url": "scraped from $response:url",
    "domain": "$response:url,r'https?://([\w\.]+)/']",
}
