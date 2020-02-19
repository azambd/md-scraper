# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver


class MdReviewSpider(scrapy.Spider):
    name = 'md_review'
    allowed_domains = ['md.com']
    start_urls = ['https://www.md.com/doctor/vk-puppala-1-md']

    def parse(self, response):
        self.driver = webdriver.Chrome('/home/azam/Documents/chromedriver')
        self.driver.get(response.url)

        name = self.driver.find_element_by_css_selector(
            'span[itemprop="name"]').text
        address = self.driver.find_element_by_css_selector(
            'div.office-address').text
        if address != None:
            address = address.replace('map', '').strip()

        profile_pics = driver.find_element_by_css_selector(
            'img[itemprop="photo"]').get_attribute('src')

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
            print('\n\n', name, '\n\n', address, '\n\n', review_date, '\n\n',
                  review_numbers, '\n\n', review, '\n\n\n', response.url, '\n\n')
            print('\n\n')

        self.driver.quit()
