#!python3

# progress.py - This subroutine is to calculate how I am progressing this will
#               read in data and crunch metrics on how I am doing
#


from datetime import date
import pandas as pd


def progressDaily():
    # read in the csv containing all my body data
    df_dailyBodyStats = pd.read_csv(
        "src/databases/dailyProgressStats.csv", encoding="utf-8")
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
        "src/databases/dailyProgressStats.csv", encoding="utf-8"
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
