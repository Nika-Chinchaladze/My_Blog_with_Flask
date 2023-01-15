import requests
from datetime import date, datetime


class GetPost:
    def __init__(self):
        self.my_api = "https://api.npoint.io/f1abd09f73b3fe4bf742"

    def get_data(self):
        respond = requests.get(url=self.my_api)
        data = respond.json()
        return data

    def get_current_date(self):
        year = date.today().year
        day = date.today().day
        month = date.today().month
        month_name = datetime.strptime(str(month), "%m")
        month_long_name = month_name.strftime("%B")
        answer = {
            "year": year,
            "month": month_long_name,
            "day": day
        }
        return answer

