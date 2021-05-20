from behave import *

use_step_matcher("parse")


@then('I\'m viewing the list of content')
def step_impl(context):
    is_presents = True
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        is_presents = is_presents and context.browser.is_text_present(row['film'])
    assert is_presents


@then('I\'m viewing the global rating for the content')
def step_impl(context):
    context.browser.visit(context.get_url('/profile'))


@then('I\'m viewing the platform added by an other user for a specific content')
def step_impl(context):
    context.browser.visit(context.get_url('/profile'))


@then('I\'m viewing the link added by an other user for a specific content')
def step_impl(context):
    context.browser.visit(context.get_url('/profile'))
