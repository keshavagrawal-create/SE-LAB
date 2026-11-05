from hypothesis import given, settings, strategies as st
from car_insurance_premium_parser import normalize_registration, total_claim_amount, driver_age

# Extra strategies that look like real user input, so Hypothesis also tries
# near-valid values (empty parts, missing separators, symbols, non-ASCII digits).
claim_like = st.lists(st.text(alphabet="0123456789-+ .;²٣", max_size=6), max_size=5).map(";".join)
dob_like = st.text(alphabet="0123456789/-.² ", max_size=12)


@settings(max_examples=300)
@given(st.text() | st.none() | st.integers())
def test_normalize_registration_no_crash(s):
    try:
        result = normalize_registration(s)
    except Exception as e:
        assert False, f"normalize_registration crashed on {s!r} with: {e!r}"
    # Property: output is a string with no spaces, dashes or dots left in it.
    assert isinstance(result, str)
    assert not any(ch in result for ch in " -.")


@settings(max_examples=300)
@given(st.text() | st.none() | claim_like)
def test_total_claim_amount_no_crash(s):
    try:
        result = total_claim_amount(s)
    except Exception as e:
        assert False, f"total_claim_amount crashed on {s!r} with: {e!r}"
    # Property: either a valid non-negative total, or None for invalid input.
    assert result is None or (isinstance(result, int) and result >= 0)


@settings(max_examples=300)
@given(st.text() | st.none() | dob_like)
def test_driver_age_no_crash(s):
    try:
        result = driver_age(s)
    except Exception as e:
        assert False, f"driver_age crashed on {s!r} with: {e!r}"
    # Property: either a realistic age, or None for an invalid date of birth.
    assert result is None or (isinstance(result, int) and 0 <= result <= 120)
