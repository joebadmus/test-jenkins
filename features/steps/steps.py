@given(u'a dealer')
def step_impl(context):
    print("dealer")


@when(u'the round starts')
def step_impl(context):
    print('the round starts')


@then(u'the dealer gives itself two cards')
def step_impl(context):
    print('the dealer gives itself two cards')
