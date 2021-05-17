from behave import *

use_step_matcher("parse")


@given('Exists a user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=user, email='user@user.com', password=password)
    # context.browser.visit('http://localhost:8000/register/')
    # context.browser.fill("username", user)
    # context.browser.fill("password1", password)
    # context.browser.fill("password2", password)
    # context.browser.find_by_value('Create my account').click()


@given('I login as user "{user}" with password "{password}"')
def step_impl(context, user, password):
    context.browser.visit(context.get_url('/'))
    form = context.browser.find_by_css('.login-form')
    context.browser.fill("username", user)
    context.browser.fill("password", password)

    form.find_by_value('Log-in').click()
    assert context.browser.is_text_present('User Profile')
