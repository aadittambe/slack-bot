import os
import pandas as pd
from slack import WebClient
from slack.errors import SlackApiError
pd.set_option('display.max_columns', None)

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

data = pd.read_json('https://healthdata.gov/resource/6xf2-c3ie.json')
data.info()

data = data[data.state != 'AS']
data = data[data.state != 'PR']
data = data[data.state != 'VI']
data.info()

total_beds = data['inpatient_beds'].sum()
total_beds

covid_occupied_beds = data['inpatient_beds_used_covid'].sum()
covid_occupied_beds

percent_covid_beds = round(((covid_occupied_beds/total_beds)*100), 2)
percent_covid_beds

test_msg = f"📢 Out of {total_beds} available hospital beds in the country 🛏, {covid_occupied_beds} beds are occupied by COVID-19 patients today 😷, which account for {percent_covid_beds} percent of all beds."

slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=test_msg
    )
except SlackApiError as e:
    assert e.response["error"]
