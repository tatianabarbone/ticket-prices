import gspread
from datetime_functions import get_datetime
from scraper import scrape

gc = gspread.service_account(filename='creds.json') # Replace with your generated credentials file

stubhub_ids = {"3day": "104405989",
                "friday": "104854839",
                "saturday": "104853923",
                "sunday": "104856133"}

def append_row(day):
    """
    Appends a row to the google sheet.
    """
    if day == "3day":
        sheet_num = 0
    elif day == "friday":
        sheet_num = 1
    elif day == "saturday":
        sheet_num = 2
    else:
        sheet_num = 3
    
    sheet = gc.open('ACL scrapetosheet').get_worksheet(sheet_num)

    date = get_datetime()[0]
    time = get_datetime()[1]

    data = scrape(stubhub_ids[day]) 
    sheet.append_row([date, time, data[0], data[1]])
    


for day in ["3day", "friday", "saturday", "sunday"]:
    append_row(day)
