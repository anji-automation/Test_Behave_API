from behave import *
import requests
from pages.users_page import UsersAPI


@given("the user gather the end url '{url}'")
def end_url(context, url):
    context.api_page = UsersAPI()
    context.api_page.set_url(url)

@when("the user send the API Get request")
def users_get(context):
    context.api_page.get_users_api()

@then("api response status code should be {status}")
def users_status(context, status):
    assert context.api_page.get_response_status() == int(status), "There is issue with response status...."

@then("the user api response text contains '{text}'")
def users_response(context, text):
    assert context.api_page.response_contains(text), "The response data is not matching with expected value"


#---Creating the new user----

@when("the user pass the below data to send POST API")
def get_inputs(context):
    data = {}
    for i in context.table:
        data[i['name']] = i['job']
    context.api_page.post_users_api(data)


#----Updating the created user----
@when("the user pass the below data to send PUT API")
def update_user(context):
    updated_data = {}
    for i in context.table:
        updated_data[i['updated_name']] = i['updated_job']
    context.api_page.put_users_api(updated_data)


#-----Deleting the user record----
@when("the user send the delete api request")
def delete_req(context):
    context.api_page.delete_users_api()

