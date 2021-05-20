from behave import *

use_step_matcher("parse")

status_values = {
    "Watching": "a",
    "Watched": "b",
    "Favourite": "c",
    "Pending": "d"
}


def goto_content_info(context, film):
    context.browser.visit(context.get_url('/profile'))
    context.browser.find_by_id('select2-search_bar-container').click()
    context.browser.find_by_css('input.select2-search__field').fill(film)
    context.browser.find_by_css('.select2-result-repository__title').click()
    context.browser.find_by_id('search_button').click()


@when("I edit the status")
def step_impl(context):
    for row in context.table:
        goto_content_info(context, row['film'])
        context.browser.find_by_id('id_type').find_by_value(status_values[row['status']]).click()
        context.browser.find_by_value('Save').click()


@when("I edit the review")
def step_impl(context):
    for row in context.table:
        goto_content_info(context, row['film'])
        context.browser.fill('review', row['review'])
        context.browser.find_by_value('Save').click()


@when("I edit the rating")
def step_impl(context):
    for row in context.table:
        goto_content_info(context, row['film'])
        context.browser.find_by_css(f'span[data-value="{row["rating"]}"]').click()
        context.browser.find_by_value('Save').click()
