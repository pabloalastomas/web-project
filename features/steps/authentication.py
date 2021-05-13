from behave import *

use_step_matcher("re")


@given('Exists a user "user" with password "password"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given Exists a user "user" with password "password"')