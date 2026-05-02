from dataclasses import dataclass


@dataclass(frozen=True)
class Tariff:
    energy_price_per_kwh: float
    cogeneration_fee_per_mwh: float
    oze_fee_per_mwh: float
    quality_fee_per_kwh: float
    network_fee_per_kwh: float
    fixed_fees_net: float
    vat_rate: float


DEFAULT_TARIFF = Tariff(
    energy_price_per_kwh=0.795,
    cogeneration_fee_per_mwh=3.0,
    oze_fee_per_mwh=7.3,
    quality_fee_per_kwh=0.0331,
    network_fee_per_kwh=0.2568,
    fixed_fees_net=153.53,
    vat_rate=0.23,
)


def calculate_bill_net(
    usage_kwh: float,
    tariff: Tariff = DEFAULT_TARIFF,
) -> float:
    """
    Calculate estimated net electricity bill.
    """
    if usage_kwh < 0:
        raise ValueError("Usage cannot be negative.")

    energy = usage_kwh * tariff.energy_price_per_kwh
    cogeneration = usage_kwh / 1000 * tariff.cogeneration_fee_per_mwh
    oze = usage_kwh / 1000 * tariff.oze_fee_per_mwh
    quality = usage_kwh * tariff.quality_fee_per_kwh
    network = usage_kwh * tariff.network_fee_per_kwh

    return (
        energy
        + cogeneration
        + oze
        + quality
        + network
        + tariff.fixed_fees_net
    )


def calculate_bill_gross(
    net_amount: float,
    tariff: Tariff = DEFAULT_TARIFF,
) -> float:
    """
    Calculate gross bill using VAT rate.
    """
    if net_amount < 0:
        raise ValueError("Net amount cannot be negative.")

    return net_amount * (1 + tariff.vat_rate)


def calculate_bill(
    usage_kwh: float,
    tariff: Tariff = DEFAULT_TARIFF,
) -> dict:
    """
    Calculate both net and gross estimated bill.
    """
    net = calculate_bill_net(
        usage_kwh=usage_kwh,
        tariff=tariff,
    )

    gross = calculate_bill_gross(
        net_amount=net,
        tariff=tariff,
    )

    return {
        "usage_kwh": usage_kwh,
        "bill_net": net,
        "bill_gross": gross,
    }