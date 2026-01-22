#!/usr/bin/env python3
"""Unit converter module for temperature, distance, and weight conversions."""

from __future__ import annotations

# Type alias for number inputs
Number = float


def celsius_to_fahrenheit(c: Number) -> Number:
    """Convert Celsius to Fahrenheit.

    Args:
        c: Temperature in Celsius.

    Returns:
        Temperature in Fahrenheit.
    """
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: Number) -> Number:
    """Convert Fahrenheit to Celsius.

    Args:
        f: Temperature in Fahrenheit.

    Returns:
        Temperature in Celsius.
    """
    return (f - 32) * 5 / 9


def km_to_miles(km: Number) -> Number:
    """Convert kilometers to miles.

    Args:
        km: Distance in kilometers.

    Returns:
        Distance in miles.
    """
    return km * 0.621371


def miles_to_km(miles: Number) -> Number:
    """Convert miles to kilometers.

    Args:
        miles: Distance in miles.

    Returns:
        Distance in kilometers.
    """
    return miles * 1.60934


def kg_to_pounds(kg: Number) -> Number:
    """Convert kilograms to pounds.

    Args:
        kg: Weight in kilograms.

    Returns:
        Weight in pounds.
    """
    return kg * 2.20462


def pounds_to_kg(pounds: Number) -> Number:
    """Convert pounds to kilograms.

    Args:
        pounds: Weight in pounds.

    Returns:
        Weight in kilograms.
    """
    return pounds * 0.453592
