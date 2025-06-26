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

# Enter a context with an instance of the API client
with workplace_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = workplace_client.SubscriptionsApi(api_client)
    workplace_create_emails = workplace_client.WorkplaceCreateEmails(

            domain_name="igiranezapat.org",
            subscription=1,
            emails=["olitt@igiranezapat.org"],
            new_subscription=True,
            user_password="HelloDear",
            email_quota_gb=1,
            display_name="Hi Dev",
            client_id=2,
    ) 

    try:
        # Create a new emails
        api_response = api_instance.emails_create(workplace_create_emails)
        print("The response of SubscriptionsApi->emails_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->emails_create: %s\n" % e)