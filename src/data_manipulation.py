def manipulate_data(dataset):

    # importing dependecies
    import pandas as pd
    import numpy as np

    # reading the data
    data = pd .read_csv(dataset)

    # convert hour to string
    data['hour'] = data.hour.astype('str')

    # create newdatetime data columns
    data["newdatetime"] = data['date'] + ' ' + data['hour'] + ':00'

    # convert the newdatetime column to data time
    data["newdatetime"] = pd.to_datetime(data["newdatetime"])

    # feature enginering
    data["hour_of_day"] = data["newdatetime"].dt.hour
    data["day_of_month"] = data["newdatetime"].dt.day
    data["month_of_year"] = data["newdatetime"].dt.month
    data["year"] = data["newdatetime"].dt.year
    data['quarter_of_year'] = data["newdatetime"].dt.quarter
    data['week_of_year'] = data["newdatetime"].dt.week
    data['day_of_year'] = data["newdatetime"].dt.dayofyear
    data['day_of_week'] = data["newdatetime"].dt.dayofweek

    data.drop(["date", "hour", "newdatetime"], axis = 1)

    return data
