# -*- coding: utf-8 -*-
__author__ = 'Bill'
import unittest
from PO import Base,searchPage
import time

class Search(unittest.TestCase):

	def setUp(self):
		self.driver=Base.driver
		self.searchPage=searchPage.searchPage()
	def test_Search(self):
		self.searchPage.sear_click()
		self.asser_searPage()
	def tearDown(self):
		self.driver.quit()
	def asser_searPage(self):
		self.searchPage.asser_search()
if __name__ == '__main__':
	unittest.main()

