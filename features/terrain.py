#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

from lettuce import after, before, world
from selenium import webdriver
import lettuce_webdriver.webdriver


@before.all
def setup_browser():
    profile = webdriver.FirefoxProfile()
    profile.add_extension('autopagerize.xpi')

    world.browser = webdriver.Firefox(firefox_profile=profile)

@after.all
def teardown_browser(total):
    world.browser.close()
