import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "ABCDEF"
    wrongMessage = 10
    oddKey = 3
    evenKey = 4
    wrongKey = '1'
    overKey = 10
    odd_encrypt = "CBA_FED"
    even_encrypt = "FE_DCBA"
    overKey_encrypt = "FEDCBA"

    # correct message, odd key
    assert encrypt_message(message, oddKey) == odd_encrypt

    # correct message, even key
    assert encrypt_message(message, evenKey) == even_encrypt

    # correct message, over range key
    assert encrypt_message(message, overKey) == overKey_encrypt

    # wrong message, wrong key
    with pytest.raises(TypeError): 
        encrypt_message(wrongMessage, wrongKey)

