from behave import *

use_step_matcher("parse")


@given('Exists a user "{user}" with password "{password}"')
def step_impl(context, user, password):
    from django.contrib.auth.models import User
    User.objects.create_user(username=user, email='user@example.com', password=password)

@given('I login as user "user" with password "password"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login as user "user" with password "password"')