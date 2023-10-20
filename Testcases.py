import pytest
from version import *

# Test the generateOTP function
def test_generateOTP():
    otp = generateOTP()
    assert isinstance(otp, str)  # Check if the generated OTP is a string
    assert len(otp) == 4  # Check if the generated OTP is of length 4
    assert otp.isdigit()  # Check if the generated OTP consists of only digits

# Test the validateEmail function
def test_validateEmail():
    # Test with a valid email address
    valid_email = "test@gmail.com"
    assert validateEmail(valid_email) is True

    # Test with an invalid email address
    invalid_email = "invalid_email"
    assert validateEmail(invalid_email) is False

    # Test with a non-Gmail address
    non_gmail_email = "example@yahoo.com"
    assert validateEmail(non_gmail_email) is False

if __name__ == "__main__":
    pytest.main()
