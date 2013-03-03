#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

from lettuce import after, before, world
import lettuce_webdriver.webdriver
from selenium import webdriver


@before.all
def setup_browser():
    profile = webdriver.FirefoxProfile()
    profile.add_extension('autopagerize.xpi')

    world.browser = webdriver.Firefox(firefox_profile=profile)

@after.all
def teardown_browser(total):
    world.browser.close()
