from django.shortcuts import render
from watson import search as watson

def find(request):
    """A view to show search results"""

    user_query = request.GET["q"]
    print(user_query)
    print("new line")
    search_results = watson.search(user_query)

    context = {
        "user_query": user_query,
        "search_results": search_results,
    }

    return render(request, "find/search_results.html", context)
