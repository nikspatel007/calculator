"""Tests for the converter module."""

import pytest

from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    km_to_miles,
    miles_to_km,
    kg_to_pounds,
    pounds_to_kg,
)


class TestCelsiusToFahrenheit:
    """Tests for celsius_to_fahrenheit function."""

    def test_freezing_point(self):
        """0°C should equal 32°F."""
        assert celsius_to_fahrenheit(0) == 32

    def test_boiling_point(self):
        """100°C should equal 212°F."""
        assert celsius_to_fahrenheit(100) == 212

    def test_negative_temperature(self):
        """-40°C should equal -40°F (the crossover point)."""
        assert celsius_to_fahrenheit(-40) == -40

    def test_body_temperature(self):
        """37°C should be approximately 98.6°F."""
        result = celsius_to_fahrenheit(37)
        assert abs(result - 98.6) < 0.1

    def test_room_temperature(self):
        """20°C should equal 68°F."""
        assert celsius_to_fahrenheit(20) == 68


class TestFahrenheitToCelsius:
    """Tests for fahrenheit_to_celsius function."""

    def test_freezing_point(self):
        """32°F should equal 0°C."""
        assert fahrenheit_to_celsius(32) == 0

    def test_boiling_point(self):
        """212°F should equal 100°C."""
        assert fahrenheit_to_celsius(212) == 100

    def test_negative_temperature(self):
        """-40°F should equal -40°C (the crossover point)."""
        assert fahrenheit_to_celsius(-40) == -40

    def test_body_temperature(self):
        """98.6°F should be approximately 37°C."""
        result = fahrenheit_to_celsius(98.6)
        assert abs(result - 37) < 0.1

    def test_room_temperature(self):
        """68°F should equal 20°C."""
        assert fahrenheit_to_celsius(68) == 20


class TestKmToMiles:
    """Tests for km_to_miles function."""

    def test_one_km(self):
        """1 km should be approximately 0.621371 miles."""
        result = km_to_miles(1)
        assert abs(result - 0.621371) < 0.0001

    def test_zero_km(self):
        """0 km should equal 0 miles."""
        assert km_to_miles(0) == 0

    def test_marathon_distance(self):
        """42.195 km (marathon) should be approximately 26.22 miles."""
        result = km_to_miles(42.195)
        assert abs(result - 26.22) < 0.01

    def test_hundred_km(self):
        """100 km should be approximately 62.1371 miles."""
        result = km_to_miles(100)
        assert abs(result - 62.1371) < 0.001

    def test_negative_km(self):
        """Negative km values should still work (for relative distances)."""
        result = km_to_miles(-10)
        assert abs(result - (-6.21371)) < 0.0001


class TestMilesToKm:
    """Tests for miles_to_km function."""

    def test_one_mile(self):
        """1 mile should be approximately 1.60934 km."""
        result = miles_to_km(1)
        assert abs(result - 1.60934) < 0.0001

    def test_zero_miles(self):
        """0 miles should equal 0 km."""
        assert miles_to_km(0) == 0

    def test_marathon_distance(self):
        """26.2 miles (marathon) should be approximately 42.16 km."""
        result = miles_to_km(26.2)
        assert abs(result - 42.16) < 0.1

    def test_hundred_miles(self):
        """100 miles should be approximately 160.934 km."""
        result = miles_to_km(100)
        assert abs(result - 160.934) < 0.01

    def test_negative_miles(self):
        """Negative mile values should still work (for relative distances)."""
        result = miles_to_km(-10)
        assert abs(result - (-16.0934)) < 0.001


class TestKgToPounds:
    """Tests for kg_to_pounds function."""

    def test_one_kg(self):
        """1 kg should be approximately 2.20462 pounds."""
        result = kg_to_pounds(1)
        assert abs(result - 2.20462) < 0.0001

    def test_zero_kg(self):
        """0 kg should equal 0 pounds."""
        assert kg_to_pounds(0) == 0

    def test_hundred_kg(self):
        """100 kg should be approximately 220.462 pounds."""
        result = kg_to_pounds(100)
        assert abs(result - 220.462) < 0.01

    def test_average_person(self):
        """70 kg (average person) should be approximately 154.32 pounds."""
        result = kg_to_pounds(70)
        assert abs(result - 154.32) < 0.1

    def test_negative_kg(self):
        """Negative kg values should still work (for weight differences)."""
        result = kg_to_pounds(-5)
        assert abs(result - (-11.0231)) < 0.001


class TestPoundsToKg:
    """Tests for pounds_to_kg function."""

    def test_one_pound(self):
        """1 pound should be approximately 0.453592 kg."""
        result = pounds_to_kg(1)
        assert abs(result - 0.453592) < 0.0001

    def test_zero_pounds(self):
        """0 pounds should equal 0 kg."""
        assert pounds_to_kg(0) == 0

    def test_hundred_pounds(self):
        """100 pounds should be approximately 45.3592 kg."""
        result = pounds_to_kg(100)
        assert abs(result - 45.3592) < 0.01

    def test_average_person(self):
        """150 pounds should be approximately 68.04 kg."""
        result = pounds_to_kg(150)
        assert abs(result - 68.04) < 0.1

    def test_negative_pounds(self):
        """Negative pound values should still work (for weight differences)."""
        result = pounds_to_kg(-10)
        assert abs(result - (-4.53592)) < 0.001


class TestRoundTripConversions:
    """Tests to verify round-trip conversions are accurate."""

    def test_celsius_fahrenheit_roundtrip(self):
        """Converting C to F and back should give the original value."""
        original = 25.5
        converted = celsius_to_fahrenheit(original)
        back = fahrenheit_to_celsius(converted)
        assert abs(back - original) < 0.0001

    def test_km_miles_roundtrip(self):
        """Converting km to miles and back should give approximately the original value."""
        original = 50.0
        converted = km_to_miles(original)
        back = miles_to_km(converted)
        assert abs(back - original) < 0.01

    def test_kg_pounds_roundtrip(self):
        """Converting kg to pounds and back should give approximately the original value."""
        original = 75.0
        converted = kg_to_pounds(original)
        back = pounds_to_kg(converted)
        assert abs(back - original) < 0.01
