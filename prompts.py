# python file to get the most recent google trending searches
# gonna use beautiful soup 4? or maybe selenium

# -- ar aspect ration 2:1 is 2 units wide 1 unit high
# --creative will make it more unique, has to be used with --test and --testp
# --testp is more photographic and lifelike
# --stylize or --s 0 to 60,000 
# --no water will remove water from prompt
# --video is able to be done with an envelope icon reaction
# --q 0-5 will change quality of images
# --v 1-4 will change
# --chaos 0 to 100 will change predictability

import pandas as pd                        
from pytrends.request import TrendReq
from datetime import date, timedelta
pytrend = TrendReq(hl='en-US', tz=360)

# if custom keywords used, create payload
def create_payload(kw_list):
    pytrend.build_payload(kw_list=kw_list)

# daily trends
def get_daily_trends(country='US'):
    # realtime searches
    day_df = pytrend.realtime_trending_searches(pn=country)
    day_df = day_df.head(15)
    day_df.drop('title', axis=1, inplace=True)

    # today's searches SERIES of SERIES
    # gives actual http request
    today_searches_df = pytrend.today_searches(pn='US')
    print(today_searches_df.head(10))

    # united states no matter what
    today_df = pytrend.trending_searches(pn='united_states')
    print(today_df.head(10))
    return today_df

# weekly trends
# NOT WORKING
def get_weekly_trends(weeks=1, country='US'):
    today = date.today()
    start_date = today - timedelta(weeks=weeks)

    # Format the start date in 'YYYY' format
    start_date_str = start_date.strftime('%Y-%m-%d')

    # week_time = int(weeks)
    week_df = pytrend.top_charts(date=f'{start_date_str} {weeks}-w', hl='en-US', tz=300, geo=country)
    week_df = week_df.head(15)
    print(week_df)
    return week_df

# monthly trends
# NOT WORKING
def get_monthly_trends(months=1, country='US'):
    today = date.today()
    # month_df = pytrend.top_charts(timeframe=f'{today} {months}-m', hl='en-US', tz=300, geo=country)
    # month_df = month_df.head(15)
    last_month_start = (today - timedelta(days=months))  # First day of the last month
    last_month_end = last_month_start - timedelta(days=30)  # Last day of the last month

    # Format the dates in 'YYYY-MM-DD' format
    start_date_str = last_month_start.strftime('%Y-%m-%d')
    end_date_str = last_month_end.strftime('%Y-%m-%d')

    pytrend.build_payload(kw_list=[], timeframe=f'{start_date_str} {end_date_str}', geo=country)

    # Fetch the historical interest over time data
    month_df = pytrend.interest_over_time()

    print(month_df)
    return month_df

# yearly trends
def get_yearly_trends(year, country='US'):
    year_df = pytrend.top_charts(year, hl='en-US', tz=300, geo=country)
    year_df.drop('exploreQuery', axis=1, inplace=True)
    return year_df


# def get_trending():
#     # Get trending searches SERIES of a series
#     df = pytrend.realtime_trending_searches(pn='US')
#     df = df.head(15)
#     df.drop('title', axis=1, inplace=True)
#     print(df)
#     # print type of first item in df
#     print(type(df.iloc[0]))

#     # # today's searches SERIES
#     # # only printed 4...and gave me the actual http request
#     today_searches_df = pytrend.today_searches(pn='US')
#     print(today_searches_df.head(10))

#     today_df = pytrend.trending_searches(pn='united_states')
#     print(today_df.head(10))


# daily trends
# def get_daily_trends(country='united_states'):
    # series of realtime trending searches
    today_df = pytrend.trending_searches(pn=country)
    print(today_df.head(10))




# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
# pytrend.build_payload(kw_list=[liss[0:4]])

# Interest Over Time
# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())

# # Interest by Region
# interest_by_region_df = pytrend.interest_by_region()
# print(interest_by_region_df.head())