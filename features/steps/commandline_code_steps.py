from behave import *
import requests

@given("the user get the base url from command line")
def url(context):
    #import sys, pdb;
    #pdb.Pdb(stdout=sys.__stdout__).set_trace()
    context.base_url = context.config.userdata.get('url')

@when("the user perform the get operation")
def get(context):
    context.resp = requests.get(url=context.base_url)

@then("the user response status should be {status}")
def status(context, status):
    assert context.resp.status_code == int(status), "Status code issue...."
