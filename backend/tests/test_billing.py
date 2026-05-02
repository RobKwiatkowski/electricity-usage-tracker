import pytest

from app.domain.billing import (
    DEFAULT_TARIFF,
    calculate_bill,
    calculate_bill_gross,
    calculate_bill_net,
)


def test_calculate_bill_net():
    result = calculate_bill_net(
        usage_kwh=500,
        tariff=DEFAULT_TARIFF,
    )

    expected = (
        500 * 0.795
        + 500 / 1000 * 3.0
        + 500 / 1000 * 7.3
        + 500 * 0.0331
        + 500 * 0.2568
        + 153.53
    )

    assert result == pytest.approx(expected)


def test_calculate_bill_gross():
    result = calculate_bill_gross(
        net_amount=700,
        tariff=DEFAULT_TARIFF,
    )

    assert result == pytest.approx(861)


def test_calculate_bill():
    result = calculate_bill(
        usage_kwh=500,
        tariff=DEFAULT_TARIFF,
    )

    assert result["usage_kwh"] == 500
    assert result["bill_net"] > 0
    assert result["bill_gross"] > result["bill_net"]


def test_calculate_bill_net_raises_error_for_negative_usage():
    with pytest.raises(ValueError):
        calculate_bill_net(
            usage_kwh=-10,
            tariff=DEFAULT_TARIFF,
        )


def test_calculate_bill_gross_raises_error_for_negative_net_amount():
    with pytest.raises(ValueError):
        calculate_bill_gross(
            net_amount=-100,
            tariff=DEFAULT_TARIFF,
        )