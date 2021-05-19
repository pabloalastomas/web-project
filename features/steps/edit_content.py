import time

from behave import *

use_step_matcher("re")


@when("I edit the status content")
def step_impl(context):
    context.browser.visit(context.get_url('/profile'))
    time.sleep(100)