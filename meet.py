from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import keyboard

class Bot:
	def __init__(self):
		self.bot = webdriver.Chrome("chromedriver.exe")
obj = meet_bot()