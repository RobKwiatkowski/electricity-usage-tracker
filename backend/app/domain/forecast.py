from datetime import date


def calculate_usage(
    start_meter_value: float,
    current_meter_value: float,
) -> float:
    """
    Calculate electricity usage in kWh based on meter readings.
    """
    if current_meter_value < start_meter_value:
        raise ValueError("Current meter value cannot be lower than start meter value.")

    return current_meter_value - start_meter_value


def calculate_days_elapsed(
    period_start: date,
    current_date: date,
) -> int:
    """
    Calculate number of elapsed days in the billing period.
    """
    days_elapsed = (current_date - period_start).days

    if days_elapsed <= 0:
        raise ValueError("Current date must be after period start date.")

    return days_elapsed


def calculate_total_days(
    period_start: date,
    period_end: date,
) -> int:
    """
    Calculate total number of days in the billing period.
    """
    total_days = (period_end - period_start).days

    if total_days <= 0:
        raise ValueError("Period end date must be after period start date.")

    return total_days


def calculate_average_daily_usage(
    usage_kwh: float,
    days_elapsed: int,
) -> float:
    """
    Calculate average daily electricity usage.
    """
    if days_elapsed <= 0:
        raise ValueError("Days elapsed must be greater than zero.")

    return usage_kwh / days_elapsed


def forecast_period_usage(
    usage_so_far_kwh: float,
    days_elapsed: int,
    total_days_in_period: int,
) -> float:
    """
    Forecast total usage for the whole billing period.
    """
    if usage_so_far_kwh < 0:
        raise ValueError("Usage cannot be negative.")

    if days_elapsed <= 0:
        raise ValueError("Days elapsed must be greater than zero.")

    if total_days_in_period <= 0:
        raise ValueError("Total days in period must be greater than zero.")

    average_daily_usage = usage_so_far_kwh / days_elapsed

    return average_daily_usage * total_days_in_period


def build_usage_forecast(
    period_start: date,
    period_end: date,
    current_date: date,
    start_meter_value: float,
    current_meter_value: float,
) -> dict:
    """
    Build full usage forecast for the active billing period.
    """
    usage_so_far_kwh = calculate_usage(
        start_meter_value=start_meter_value,
        current_meter_value=current_meter_value,
    )

    days_elapsed = calculate_days_elapsed(
        period_start=period_start,
        current_date=current_date,
    )

    total_days_in_period = calculate_total_days(
        period_start=period_start,
        period_end=period_end,
    )

    average_daily_usage_kwh = calculate_average_daily_usage(
        usage_kwh=usage_so_far_kwh,
        days_elapsed=days_elapsed,
    )

    forecast_usage_kwh = forecast_period_usage(
        usage_so_far_kwh=usage_so_far_kwh,
        days_elapsed=days_elapsed,
        total_days_in_period=total_days_in_period,
    )

    return {
        "period_start": period_start,
        "period_end": period_end,
        "current_date": current_date,
        "start_meter_value": start_meter_value,
        "current_meter_value": current_meter_value,
        "usage_so_far_kwh": usage_so_far_kwh,
        "days_elapsed": days_elapsed,
        "total_days_in_period": total_days_in_period,
        "average_daily_usage_kwh": average_daily_usage_kwh,
        "forecast_usage_kwh": forecast_usage_kwh,
    }