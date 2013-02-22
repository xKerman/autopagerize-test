#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

from lettuce import *


@step('I scroll to bottom of the page')
def scroll_to_bottom(step):
    world.browser.execute_script('scrollTo(0, document.body.scrollHeight);')
