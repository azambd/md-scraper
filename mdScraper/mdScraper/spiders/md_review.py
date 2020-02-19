# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver

import pandas as cv


class MdReviewSpider(scrapy.Spider):
    name = 'md_review'
    allowed_domains = ['md.com']
    start_urls = ['https://www.md.com/doctor/vk-puppala-1-md']

    def parse(self, response):
        # set this w.r.t your environment
        self.driver = webdriver.Chrome('/home/azam/Documents/chromedriver')

        self.driver.get(response.url)

        name_list = []
        address_list = []
        profile_pics_list = []
        address_list = []
        review_numbers_list = []
        review_date_list = []
        reviewer_name_list = []
        review_list = []
        hash_key_list = []

        name = self.driver.find_element_by_css_selector(
            'span[itemprop="name"]').text
        address = self.driver.find_element_by_css_selector(
            'div.office-address').text
        if address != None:
            address = address.replace('map', '').strip()

        profile_pics = self.driver.find_element_by_css_selector(
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
            print('\n\nName:', name, '\n\nAddress:', address, '\n\nReview Date:', review_date, '\n\nTotal Reviews:',
                  review_numbers, '\n\nReview:', review, '\n\nProfile Link:', response.url, '\n\n')
            print('\n\n')

            name_list.append(name)
            address_list.append(address)
            profile_pics_list.append(profile_pics)
            address_list.append(address)
            review_numbers_list.append(review_numbers)
            review_date_list.append(review_date)
            reviewer_name_list.append(reviewer_name)
            review_list.append(review)
            hash_key_list.append(hash_key)

        df = cv.DataFrame(list(zip(name_list, address_list, profile_pics_list, address_list, review_numbers_list, review_date_list, reviewer_name_list, review_list, hash_key_list)), columns=[
                          'name', 'address', 'profile_pics', 'address', 'review_numbers', 'review_date', 'reviewer_name', 'review', 'hash_key'])

        df.to_csv('md_test_result.csv', index=False)
        self.driver.quit()
