from behave import *
from calculator import *

@given(u'Calculator app is running')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given calculator is running')
    pass

@when(u' I input 2 + 3')
def step_impl(context):
  context.result = addition(2, 3)

@Then(u'I get result 5')
def step_impl(context):
    assert context.result == 5



