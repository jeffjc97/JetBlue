from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def query(request, airports=None):
    # response = {
    #     'dashboard_stats': dashboard_stats,
    #     'organization_newsfeed': organization_newsfeed,
    #     'user_newsfeed': user_newsfeed,
    #     'assignments_newsfeed': assignments_newsfeed
    # }
    # response = json.dumps(response)

    response = HttpResponse(airports, content_type="application/json")

    return response
