import pytest

from self_storage import access_allowed, payment_status, rent_due


def test_rent_due_validation_branches():
    with pytest.raises(ValueError, match="unknown unit size"):
        rent_due("extra-large", 2, False, False)

    with pytest.raises(ValueError, match="invalid months"):
        rent_due("small", -1, False, False)


def test_rent_due_membership_and_deposit_branches():
    assert rent_due("small", 1, False, False) == 0
    assert rent_due("small", 2, False, True) == 0
    assert rent_due("large", 4, True, True) == 120


def test_rent_due_climate_and_discount_branches():
    assert rent_due("medium", 3, False, False) == 80
    assert rent_due("small", 8, False, False) == 490
    assert rent_due("small", 8, True, False) == 735


def test_access_owner_branches():
    assert access_allowed(2, 4, True) is True
    assert access_allowed(2, 5, True) is False


def test_access_non_owner_time_and_visitor_branches():
    assert access_allowed(5, 1, False) is False
    assert access_allowed(23, 1, False) is False
    assert access_allowed(12, 2, False) is True
    assert access_allowed(12, 3, False) is False


def test_payment_status_cutoff_branches():
    assert payment_status(0, True, False) == "current"
    assert payment_status(5, False, False) == "current"
    assert payment_status(-9, False, False) == "grace"
    assert payment_status(-11, False, False) == "lien"


def test_payment_status_prior_late_branches():
    assert payment_status(15, False, True) == "current"
    assert payment_status(0, False, True) == "grace"
    assert payment_status(-1, False, True) == "lien"
