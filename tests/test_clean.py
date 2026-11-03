import pandas as pd
import pytest
from ingestion.clean import validate_weather_data

def test_valid_weather_data():
    df = pd.DataFrame({
        "time": [pd.Timestamp("2026-10-30 16:15:00")],
        "temperature_2m": [15.8],
        "relative_humidity_2m": [49],
        "apparent_temperature": [13.0],
        "precipitation": [0.0],
        "weather_code": [0],
        "wind_speed_10m": [10.7],
    })
    validate_weather_data(df)

def test_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="empty"):
        validate_weather_data(df)

def test_invalid_humidity():
    df = pd.DataFrame({
        "time": [pd.Timestamp("2026-10-30 16:15:00")],
        "temperature_2m": [15.8],
        "relative_humidity_2m": [120],
        "apparent_temperature": [13.0],
        "precipitation": [0.0],
        "weather_code": [0],
        "wind_speed_10m": [10.7],
    })
    with pytest.raises(ValueError, match="Humidity"):
        validate_weather_data(df)
