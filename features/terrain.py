#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

import multiprocessing

from lettuce import after, before, world
import lettuce_webdriver.webdriver
from selenium import webdriver

from src.testserver import app


# register setup_* functions in this order: server -> browser
@before.all
def setup_server():
    world.server = multiprocessing.Process(target=app.run, kwargs={'debug': False})
    world.server.daemon = True
    world.server.start()

@after.all
def teardown_browser(total):
    world.browser.close()

@before.all
def setup_browser():
    profile = webdriver.FirefoxProfile()
    profile.add_extension('autopagerize.xpi')
    world.browser = webdriver.Firefox(firefox_profile=profile)

@after.all
def teardown_server(total):
    world.server.join(timeout=1)
