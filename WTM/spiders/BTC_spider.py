# -*- coding: utf-8 -*-
import scrapy
import json

class BtcSpiderSpider(scrapy.Spider):
    name = 'BTC_spider'
    allowed_domains = ['whattomine.com']
    start_urls = ['https://whattomine.com/coins/1.json/']


    def parse(self, response):
        jsonresponse = json.loads(response.body)

        yield { 'timestamp' : jsonresponse['timestamp'],
                'block_time' : jsonresponse['block_time'],
                'block_reward' : jsonresponse['block_reward'],
                'block_reward24hrs' : jsonresponse['block_reward24'],
                'block_reward3days' : jsonresponse['block_reward3'],
                'block_reward7days' : jsonresponse['block_reward7'],
                'last_block' : jsonresponse['last_block'],
                'difficulty' : jsonresponse['difficulty'],
                'difficulty24hrs' : jsonresponse['difficulty24'],
                'difficulty3days' : jsonresponse['difficulty3'],
                'difficulty7days' : jsonresponse['difficulty7'],
                'exchange_rate' : jsonresponse['exchange_rate'],
                'exchange_rate24hrs' : jsonresponse['exchange_rate24'],
                'exchange_rate3days' : jsonresponse['exchange_rate3'],
                'exchange_rate7days' : jsonresponse['exchange_rate7'],
                'exchange_rate_vol' : jsonresponse['exchange_rate_vol'],
                'exchange_rate_currency' : jsonresponse['exchange_rate_curr'],
                'pool_fee' : jsonresponse['pool_fee'],
                'estimated_rewards' : jsonresponse['estimated_rewards'],
                'btc_revenue' : jsonresponse['btc_revenue'],
                'revenue' : jsonresponse['revenue'],
                'cost' : jsonresponse['cost'],
                'profit' : jsonresponse['profit'],
                'status' : jsonresponse['status'],
                'lagging' : jsonresponse['lagging'],
                'testing' : jsonresponse['testing'],
                'listed' : jsonresponse['listed']

        }
