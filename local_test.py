import workplace_client
from workplace_client.models.standard_response import StandardResponse
from workplace_client.models.workplace_create_emails import WorkplaceCreateEmails
from workplace_client.rest import ApiException
from pprint import pprint
import os


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = workplace_client.Configuration(
    host = "http://127.0.0.1:8001/api",
    access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjo0OTAzMzIyNzM3LCJpYXQiOjE3NDk3MjI3MzcsImp0aSI6ImExMzI2Nzc0OTc0ZjQ0NGNhOTUyZTdiZjQ1YWI5MmIxIiwidXNlcl9pZCI6MX0.O_yR8Bk-kSKQtPcbz7YPbb3psGs3fsGK5RlmfIggw10"
)



with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.ResetPasswordApi(api_client)
    password_reset = workplace_client.ResetEmailPassword(
        email="olitt@igiranezapat.org",
        password="HelloDear"
    )

    try:
        # Reset subscription email password
        api_response = api_instance.reset_email_password(password_reset)
        print("The response of ResetPasswordApi->reset_password_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResetPasswordApi->reset_password_create: %s\n" % e)