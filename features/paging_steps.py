#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

import urllib2

from lettuce import step, world
from nose.tools import assert_equals


@step(u'I scroll to bottom of the page')
def scroll_to_bottom(step):
    world.browser.execute_script('scrollTo(0, document.body.scrollHeight);')

@step(u'I should see a element "([^"]*)"')
def i_should_see_a_element_selector(step, selector):
    world.browser.find_element_by_css_selector(selector)

@step(u'Content-Type of the page should be "([^"]*)"')
def content_type_of_the_page_should_be(step, content_type):
    response = urllib2.urlopen(world.browser.current_url)
    assert_equals(response.info().type, content_type)
