import requests

class UsersAPI:

    def __init__(context):
        context.url = None
        context.response = None

    def set_url(context,url):
        context.url = url

    def get_users_api(context):
        context.response = requests.get(context.url)

    def post_users_api(context, payload):
        context.response = requests.post(url=context.url, data=payload)

    def put_users_api(context,updated_payload):
        context.response = requests.put(url=context.url, data=updated_payload)

    def delete_users_api(context):
        context.response = requests.delete(url=context.url)

    def get_response_status(context):
        return context.response.status_code

    def response_contains(context, text):
        return text in context.response.text

