import time

from behave import *
from entertainment_db.models import *

use_step_matcher("parse")


def goto_content_info(context, film):
    context.browser.visit(context.get_url('/profile'))
    context.browser.find_by_id('select2-search_bar-container').click()
    context.browser.find_by_css('input.select2-search__field').fill(film)
    context.browser.find_by_css('.select2-result-repository__title').click()
    context.browser.find_by_id('search_button').click()


@when("I delete the content")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        context.browser.find_by_css('input[aria-controls="datatable_status"]').fill(row['film'])
        context.browser.find_by_css('table a.button').click()
        context.browser.find_by_value('Delete').click()


@then('I\'m viewing not exist the content of the "{username}"')
def step_impl(context, username):
    user = User.objects.get(username=username)
    not_exist = True
    for row in context.table:
        content = Content.objects.get(title=row['film'])
        not_exist = not_exist and not StatusUserContent.objects.filter(user=user, content=content).exists()
    assert not_exist


@when("I delete the platform link")
def step_impl(context):
    for row in context.table:
        goto_content_info(context, film=row['film'])
        context.browser.find_by_css('tbody a.button').click()
        context.browser.find_by_value('Delete').click()


@then('I\'m viewing not exist the platform link of the "{username}"')
def step_impl(context, username):
    user = User.objects.get(username=username)
    not_exist = True
    for row in context.table:
        content = Content.objects.get(title=row['film'])
        not_exist = not_exist and not PlatformContent.objects.filter(user=user, content=content).exists()
    assert not_exist
