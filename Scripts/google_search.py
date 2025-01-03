

from serpapi import GoogleSearch

def google_search(query: str):
    """
    Search Google using a query.

    Args:
        query (str): The search query.

    Returns:
        str: A concatenated list of the top search results.
    """
    
    # 可以用 https://serpapi.com/playground 一键生成Query代码
    params = {
      "api_key": "Replace with your serpapi_key here https://serpapi.com/dashboard",
      "engine": "google",
      "q": query,
      "location": "XXX",
      "google_domain": "google.com",
      "gl": "us",
      "hl": "en",
      "cr": "countryCN|countryUS|countryTW|countryHK|countryJP",
      "device": "desktop",
      "lr": "lang_zh-CN|lang_zh-TW|lang_en|lang_ja"
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()
    return results
    
    # TODO replace this with a real query to Google, e.g. by using serpapi (https://serpapi.com/integrations/python)
    # dummy_message = "The search tool is currently offline for regularly scheduled maintenance."
    # return dummy_message