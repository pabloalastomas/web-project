import time
from datetime import datetime
from behave import *
from pip._vendor import requests

from entertainment_db.models import *

use_step_matcher("parse")

status_values = {
    "Watching": "a",
    "Watched": "b",
    "Favourite": "c",
    "Pending": "d"
}


@when("I create the status")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        context.browser.find_by_id('select2-search_bar-container').click()
        context.browser.find_by_css('input.select2-search__field').fill(row['film'])
        context.browser.find_by_css('.select2-result-repository__title').click()
        context.browser.find_by_id('search_button').click()
        context.browser.find_by_id('id_type').find_by_value(status_values[row['status']]).click()
        context.browser.find_by_value('Save').click()


@then('I\'m viewing the status created for content by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    is_update = True
    for row in context.table:
        content = Content.objects.get(title=row['film'])
        status_user_content = StatusUserContent.objects.get(user=user, content=content)
        is_update = is_update and status_user_content.type == status_values[row['status']]
    assert is_update


@step("There are {count:n} content in DB.")
def step_impl(context, count):
    assert count == Content.objects.count()


@when("I create the review")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        context.browser.find_by_id('select2-search_bar-container').click()
        context.browser.find_by_css('input.select2-search__field').fill(row['film'])
        context.browser.find_by_css('.select2-result-repository__title').click()
        context.browser.find_by_id('search_button').click()
        context.browser.find_by_id('id_type').find_by_value(status_values[row['status']]).click()
        context.browser.fill('review', row['review'])
        context.browser.find_by_value('Save').click()


@then('I\'m viewing the review created for content by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    is_update = True
    for row in context.table:
        content = Content.objects.get(title=row['film'])
        status_user_content = StatusUserContent.objects.get(content=content, user=user)
        is_update = is_update and row['review'] == status_user_content.review
    assert is_update


@when("I create the rating")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        context.browser.find_by_id('select2-search_bar-container').click()
        context.browser.find_by_css('input.select2-search__field').fill(row['film'])
        context.browser.find_by_css('.select2-result-repository__title').click()
        context.browser.find_by_id('search_button').click()
        context.browser.find_by_id('id_type').find_by_value(status_values[row['status']]).click()
        context.browser.find_by_value('Save').click()
        context.browser.find_by_css(f'span[data-value="{row["rating"]}"]').click()
        context.browser.find_by_value('Save').click()


@then('I\'m viewing the rating created for content by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    is_update = True
    for row in context.table:
        content = Content.objects.get(title=row['film'])
        assessment = Assessment.objects.get(user=user, content=content)
        is_update = is_update and assessment.rating == int(row['rating'])
    assert is_update


@step("Exists streaming platforms")
def step_impl(context):
    for row in context.table:
        StreamingPlatforms.objects.create(name=row["platform"])


@then("I create the platform link")
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/profile'))
        context.browser.find_by_id('select2-search_bar-container').click()
        context.browser.find_by_css('input.select2-search__field').fill(row['film'])
        context.browser.find_by_css('.select2-result-repository__title').click()
        context.browser.find_by_id('search_button').click()
        context.browser.find_by_text('Add Link').click()
        context.browser.find_by_id('id_platform').find_by_text(row['platform']).click()
        context.browser.fill("url", row['link'])
        context.browser.find_by_value('Save').click()


@then('I\'m viewing the platform link created for content by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    is_update = True
    for row in context.table:
        content = Content.objects.get(title=row['film'])
        platform = StreamingPlatforms.objects.get(name=row['platform'])
        platform_content = PlatformContent.objects.get(user=user, content=content, platform=platform)
        is_update = is_update and platform_content.url == row['link']
    assert is_update


@step('Exist content registered by "{username}"')
def step_impl(context, username):
    for row in context.table:
        user = User.objects.get(username=username)
        content = create_content_model(row['film'])
        streaming_platform = StreamingPlatforms.objects.get(name=row['platform'])
        PlatformContent.objects.create(content=content, platform=streaming_platform, user=user, url=row['link'])
        Assessment.objects.create(user=user, content=content, rating=row['rating'])
        StatusUserContent.objects.create(user=user, content=content, review=row['review'],
                                         type=status_values[row['status']])


def create_content_model(film):
    response = requests.get(f'https://www.omdbapi.com/?t={film}&apikey=329c0d5e').json()

    content = Content.objects.create(title=response['Title'], synopsis=response['Plot'],
                                     airdate=datetime.strptime(response['Released'], "%d %b %Y"),
                                     type=response['Type'], id_in_api=response['imdbID'], poster_url=response['Poster'])
    content.save()
    return content
