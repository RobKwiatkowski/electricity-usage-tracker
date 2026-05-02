from datetime import date

import pytest

from app.domain.forecast import (
    build_usage_forecast,
    calculate_average_daily_usage,
    calculate_days_elapsed,
    calculate_total_days,
    calculate_usage,
    forecast_period_usage,
)


def test_calculate_usage():
    result = calculate_usage(
        start_meter_value=12765,
        current_meter_value=13234,
    )

    assert result == 469


def test_calculate_usage_raises_error_when_current_value_is_lower():
    with pytest.raises(ValueError):
        calculate_usage(
            start_meter_value=13234,
            current_meter_value=12765,
        )


def test_calculate_days_elapsed():
    result = calculate_days_elapsed(
        period_start=date(2026, 3, 16),
        current_date=date(2026, 4, 5),
    )

    assert result == 20


def test_calculate_days_elapsed_raises_error_for_same_day():
    with pytest.raises(ValueError):
        calculate_days_elapsed(
            period_start=date(2026, 3, 16),
            current_date=date(2026, 3, 16),
        )


def test_calculate_total_days():
    result = calculate_total_days(
        period_start=date(2026, 3, 16),
        period_end=date(2026, 5, 16),
    )

    assert result == 61


def test_calculate_average_daily_usage():
    result = calculate_average_daily_usage(
        usage_kwh=469,
        days_elapsed=20,
    )

    assert result == 23.45


def test_forecast_period_usage():
    result = forecast_period_usage(
        usage_so_far_kwh=469,
        days_elapsed=20,
        total_days_in_period=61,
    )

    assert result == pytest.approx(1430.45)


def test_build_usage_forecast():
    result = build_usage_forecast(
        period_start=date(2026, 3, 16),
        period_end=date(2026, 5, 16),
        current_date=date(2026, 4, 5),
        start_meter_value=12765,
        current_meter_value=13234,
    )

    assert result["usage_so_far_kwh"] == 469
    assert result["days_elapsed"] == 20
    assert result["total_days_in_period"] == 61
    assert result["average_daily_usage_kwh"] == pytest.approx(23.45)
    assert result["forecast_usage_kwh"] == pytest.approx(1430.45)