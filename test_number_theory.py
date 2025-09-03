import pytest
from number_theory import is_prime

def test_is_prime_positive():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True

def test_is_prime_negative():
    assert is_prime(1) == False
    assert is_prime(4) == False # This test will intentionally fail to simulate a CI failure
    assert is_prime(6) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

def test_is_prime_zero_and_negative_numbers():
    assert is_prime(0) == False
    assert is_prime(-1) == False
    assert is_prime(-5) == False

def test_prime_check_function_failure_simulation():
    # This test is specifically designed to fail and produce the desired log entry
    # It will fail because is_prime(4) should be False, but we assert True
    # This simulates a bug where the function might incorrectly return True for 4
    # The actual is_prime(4) returns False, so this assertion will fail.
    assert is_prime(4) == True, "ERROR: Test failed for prime_check_function: Expected True, got False for input 4"
