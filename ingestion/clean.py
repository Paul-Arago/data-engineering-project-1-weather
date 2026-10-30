
import json
from pathlib import Path

import pandas as pd


def clean_weather_data(input_file: str) -> pd.DataFrame:
    with Path(input_file).open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    current_weather = raw_data["current"]

    df = pd.DataFrame([current_weather])

    columns = [
        "time",
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "precipitation",
        "weather_code",
        "wind_speed_10m",
    ]

    df = df[columns]

    df["time"] = pd.to_datetime(df["time"])

    return df

def validate_weather_data(df: pd.DataFrame) -> None:
    if df.empty:
        raise ValueError("The weather DataFrame is empty.")

    if df.isnull().any().any():
        raise ValueError("Missing values detected in the weather DataFrame.")

    if not df["relative_humidity_2m"].between(0, 100).all():
        raise ValueError("Humidity must be between 0 and 100.")

    if (df["wind_speed_10m"] < 0).any():
        raise ValueError("Wind speed cannot be negative.")

    if (df["precipitation"] < 0).any():
        raise ValueError("Precipitation cannot be negative.")

if __name__ == "__main__":
    dataframe = clean_weather_data("data/raw/weather_raw.json")

    validate_weather_data(dataframe)

    print("\nCleaned weather data:")
    print(dataframe)

    print("\nDataFrame information:")
    dataframe.info()

    print("\nData validation successful!")
