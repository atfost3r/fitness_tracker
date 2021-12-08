#!python3

# progress.py - This subroutine is to calculate how I am progressing this will
#               read in data and crunch metrics on how I am doing
#


from datetime import date
import pandas as pd


def progressDaily():
    # read in the csv containing all my body data
    df_dailyBodyStats = pd.read_csv(
        "src/databases/dailyBodyStats.csv", encoding="utf-8")
    df_dailyBodyStats["weight_delta"] = round(
        df_dailyBodyStats["weight"].diff(), 2)
    df_dailyBodyStats["calories_delta"] = (
        df_dailyBodyStats["calories_goal"] -
        df_dailyBodyStats["calories_actual"]
    )
    df_dailyBodyStats["protein_delta"] = (
        df_dailyBodyStats["protein_goal"] - df_dailyBodyStats["protein_actual"]
    )
    df_dailyBodyStats["carbs_delta"] = (
        df_dailyBodyStats["carbs_goal"] - df_dailyBodyStats["carbs_actual"]
    )
    df_dailyBodyStats["fat_delta"] = (
        df_dailyBodyStats["fat_goal"] - df_dailyBodyStats["fat_actual"]
    )
    # Save daily progress stats
    df_dailyBodyStats.to_csv(
        "src/databases/dailyProgressStats.csv", encoding="utf-8", mode='a', header=False
    )
    return


def progressWeekly():
    # read in the csv containing all my body data
    df_weeklyBodyStats = pd.read_csv(
        "src/databases/dailyProgressStats.csv", encoding="utf-8")
    week = date.today().isocalendar()[1]

    # Weekly Rolling Average calculating of the relevant Daily stats
    df_weeklyBodyStats["weight_weekly"] = df_weeklyBodyStats.weight.rolling(
        7, min_periods=1).mean()
    df_weeklyBodyStats["calories_weekly"] = df_weeklyBodyStats.calories_actual.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["calories_weekly_delta"] = df_weeklyBodyStats.calories_delta.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["protein_weekly"] = df_weeklyBodyStats.protein_actual.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["carbs_weekly"] = df_weeklyBodyStats.carbs_actual.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["fat_weekly"] = df_weeklyBodyStats.fat_actual.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["protein_weekly_delta"] = df_weeklyBodyStats.protein_delta.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["carbs_weekly_delta"] = df_weeklyBodyStats.carbs_delta.rolling(
        7, min_periods=1
    ).mean()
    df_weeklyBodyStats["protein_weekly"] = df_weeklyBodyStats.fat_delta.rolling(
        7, min_periods=1
    ).mean()
    # print(df_weeklyBodyStats.head())
    df_weeklyBodyStats.to_csv(
        "src/databases/weeklyProgressStats.csv",
        header=False,
        encoding="utf-8",
    )
    return df_weeklyBodyStats

def bodyFat_weightLoss(bodyfat):
    #This funtion is for using the r/leangains table for weight loss rate to minimize muscle loss while  cutting.
    #Body fat assumed to be input into this as a decimal but if that is not the case...
    if bodyfat > 1:
        bodyfat = bodyfat / 100
    if bodyfat >.2:
        loss_rate = 1.7 #pounds/week
    elif bodyfat >.15 and bodyfat < .17:
        loss_rate = 1.5
    elif bodyfat >.12 and bodyfat < .14:
        loss_rate =1.3
    elif bodyfat >.09 and bodyfat < .11:
        loss_rate = 1.0
    elif bodyfat < .08:
        loss_rate = .7
    return loss_rate
