from hypothesis import given, strategies as st
import math

from self_storage import parse_rental, duration_average, payable_rent


FUZZ_INPUTS = st.one_of(st.none(), st.integers(), st.text())


def assert_controlled_result(call, value, predicate):
    """Every arbitrary input must either be rejected cleanly or meet invariants."""
    try:
        result = call(value)
    except ValueError:
        return
    assert predicate(result), f"unexpected result for {value!r}: {result!r}"


@given(FUZZ_INPUTS)
def test_parse_rental_is_robust(value):
    assert_controlled_result(
        parse_rental,
        value,
        lambda result: (
            isinstance(result, tuple)
            and len(result) == 2
            and isinstance(result[0], str)
            and isinstance(result[1], float)
            and math.isfinite(result[1])
            and result[1] >= 0
        ),
    )


@given(FUZZ_INPUTS)
def test_duration_average_is_robust(value):
    assert_controlled_result(
        duration_average,
        value,
        lambda result: isinstance(result, int) and result >= 0,
    )


@given(FUZZ_INPUTS)
def test_payable_rent_is_robust(value):
    assert_controlled_result(
        payable_rent,
        value,
        lambda result: isinstance(result, (int, float))
        and math.isfinite(result)
        and result >= 0,
    )
