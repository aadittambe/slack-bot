# 🤖 First Slack bot

This is a Slack Bot created for my news apps class that reports each day's COVID-19 hospitalizations numbers for the U.S. and the state of Maryland. The bot uses numbers from [healthdata.gov](https://healthdata.gov/dataset/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/6xf2-c3ie) and GitHub Actions for automation.

1. Do I need to store this data somehow? What would that look like?

The data is being logged to two CSVs in this repository [here](https://github.com/aadittambe/slack-bot/blob/main/md_data.csv) and [here](https://github.com/aadittambe/slack-bot/blob/main/us_data.csv).

Every day, the bot looks at the present days statistics, and is built to also report data from a week ago for comparison. The CSVs don't have enough data to report numbers from a week ago, and sends a message saying, "Not enough data to report." Once data is collected, it will start reporting those figures.

2. If this bot were able to accept input from users, what would that look like and how might it respond?

Ah, I tried doing this before submission, but didn't have enough time to figure it out. In an ideal case, it would be able to accept user input in the form of states, "Maryland" or "Ohio" for instance, and reply with that state's statistics — percentage of beds occupied by COVID-19 patients, as well as percentage of hospitalizations reporting critical staffing shortages.

To take it a step further, I would have liked to use [Altair](https://altair-viz.github.io/) to make a **very simple** line chart showing the trends in that state. 

3. What's the best schedule for updates?

The data is updated daily, so I think the best schedule for this is at the beggining of every day. I have converted the cron expression from UTC to EDT. 

**How I would improve the bot**

In addition to accepting user input, I would also have liked to added functionality to report which states are reporting staffing shortages or COVID-19-occupied beds, when the number went above a certain level.