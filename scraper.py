import requests

def scrape(event_id):
    """
    Makes an API call to retrieve min ticket price and num tickets left.
    """
    access_token = "YOUR_ACCESS_TOKEN" # Replace with your stubhub access token. Instructions: https://developer.stubhub.com/oauth/apis/post/accesstoken

    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Accept': 'application/json',
    }

    params = (
        ('id', event_id), 
    )

    response = requests.get('https://api.stubhub.com/sellers/search/events/v3', headers=headers, params=params)
    json = response.json()

    min_price = "NULL"
    total_tickets = "NULL"
    try:
        min_price = json['events'][0]['ticketInfo']['minListPrice']
        total_tickets = json['events'][0]['ticketInfo']['totalTickets']
    except KeyError:
        print("KeyError encountered\n")
        print(json)
        exit()

    return (min_price, total_tickets)