from time import sleep

from behave import *

use_step_matcher("parse")


def goto_content_info(context, film):
    context.browser.visit(context.get_url('/profile'))
    context.browser.find_by_id('select2-search_bar-container').click()
    context.browser.find_by_css('input.select2-search__field').fill(film)
    context.browser.find_by_css('.select2-result-repository__title').click()
    context.browser.find_by_id('search_button').click()


@then('I\'m viewing the list of content')
def step_impl(context):
    is_presents = True
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        is_presents = is_presents and context.browser.is_text_present(row['film'])
    assert is_presents


@then('I\'m viewing the platform added by an other user for a specific content')
def step_impl(context):
    is_presents = True
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        goto_content_info(context, row['film'])
        is_presents = is_presents and context.browser.is_text_present(row['platform'])
    assert is_presents


@then('I\'m viewing the link added by an other user for a specific content')
def step_impl(context):
    is_presents = True
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        goto_content_info(context, row['film'])
        is_presents = is_presents and context.browser.is_text_present(row['link'])
    assert is_presents
