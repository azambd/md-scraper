# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver


class MdReviewSpider(scrapy.Spider):
    name = 'md_review'
    allowed_domains = ['md.com']
    # start_urls = ['https://www.md.com/doctor/vk-puppala-1-md']

    def start_requests(self):
        self.driver = webdriver.Chrome('/home/azam/Documents/chromedriver')
        self.driver.get('https://www.md.com/doctor/vk-puppala-1-md')

        review_numbers = self.driver.find_element_by_css_selector('h4').text

        divs = self.driver.find_elements_by_css_selector(
            'div.list-reviews blockquote[itemprop="review"]')

        for div in divs:
            review_date = div.find_element_by_css_selector(
                'span[itemprop="datePublished"]').get_attribute('content')
            reviewer_name = div.find_element_by_css_selector(
                'span[itemprop="author"]').text
            review = div.find_element_by_css_selector(
                'div[itemprop="reviewBody"]').text
            hash_key = div.get_attribute('id')
            # print('\n\n', review_date, '\n\n',
            #       review_numbers, '\n\n', review, '\n\n\n')
            print('\n\n')
            yield{'reviewer_name:', reviewer_name,
                  'review_date:', review_date,
                  'review:', review,
                  'review_numbers:', review_numbers,
                  'hash_key:', hash_key}
            print('\n\n')

        self.driver.quit()

    def parse(self, response):
        pass
