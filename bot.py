import os
import pandas as pd
from slack import WebClient
from slack.errors import SlackApiError
pd.set_option('display.max_columns', None)

data = pd.read_json('https://healthdata.gov/resource/6xf2-c3ie.json')

data = data[data.state != 'AS']
data = data[data.state != 'PR']
data = data[data.state != 'VI']

total_beds = data['inpatient_beds'].sum()
covid_occupied_beds = data['inpatient_beds_used_covid'].sum()
percent_covid_beds = round(((covid_occupied_beds/total_beds)*100),2)

critical_staffing_shortage_today_yes = data['critical_staffing_shortage_today_yes'].sum()
critical_staffing_shortage_today_no = data['critical_staffing_shortage_today_no'].sum()
critical_staffing_shortage_today_not_reported = data['critical_staffing_shortage_today_not_reported'].sum()
total_hospitals = critical_staffing_shortage_today_yes + critical_staffing_shortage_today_no + critical_staffing_shortage_today_not_reported

percent_hospitals_critical_shortages = round(((critical_staffing_shortage_today_yes/total_hospitals)*100),2)

msg = f"""📢 Daily COVID-19 hospitalization update 📢
🛏 Out of {(format (total_beds, ',d'))} available hospital beds in the country, {(format(covid_occupied_beds, ',d'))} beds are occupied by COVID-19 patients today, which account for {percent_covid_beds} percent of all beds.
🧑‍⚕️ {percent_hospitals_critical_shortages} percent hospitals in the country are reporting critical staffing shortages today.
"""

SLACK_API_TOKEN = os.environ("SLACK_API_TOKEN")
client = WebClient(token=SLACK_API_TOKEN)

try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg
    )
    print("success!")
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    # str like 'invalid_auth', 'channel_not_found'
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
