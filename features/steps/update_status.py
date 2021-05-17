from behave import *
from django.contrib.auth.models import User
from entertainment_db.models import StatusUserContent, Content

use_step_matcher("parse")


@when("I update the status")
def step_impl(context):
    for row in context.table:
        context.browser.visit('http://localhost:8000/profile/')
        status_values = {
            "Watching": "a",
            "Watched": "b",
            "Favourite": "c",
            "Pending": "d"
        }
        context.browser.find_by_id('select2-search_bar-container').click()
        context.browser.find_by_css('input.select2-search__field').fill(row['film'])
        context.browser.find_by_css('.select2-result-repository__title').click()
        context.browser.find_by_id('search_button').click()
        context.browser.find_by_id('id_type').find_by_value(status_values[row['status']]).click()
        context.browser.find_by_value('Save').click()


@then('I\'m viewing the status update for content by "{user}"')
def step_impl(context, user):
    username = User.objects.get(user)
    is_update = True
    for row in context.table:
        content = Content(title=row['film'])
        status_user_content = StatusUserContent(user=username, content=content)
        is_update = is_update and status_user_content.type == row['status']
    assert is_update
