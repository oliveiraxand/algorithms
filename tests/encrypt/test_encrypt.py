from challenges.challenge_encrypt_message import encrypt_message
import pytest

message = 'abraao'


def test_encrypt_message():
    assert encrypt_message(message=message, key=3) == 'rba_oaa'
    assert encrypt_message(message=message, key=-1) == 'oaarba'
    assert encrypt_message(message=message, key=2) == 'oaar_ba'

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message=message, key='lago')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(message=1, key=2)


# def test_encrypt_message_reversed():
#     key = -1
#     encrypted_message = 'oaarba'
#     assert encrypt_message(message=message, key=key) == encrypted_message


# def test_encrypt_message_impar():
#     key = 3
#     encrypted_message = 'rba_oaa'
#     assert encrypt_message(message=message, key=key) == encrypted_message


# def test_encrypt_message_par():
#     key = 2
#     encrypted_message = 'oaar_ba'
#     assert encrypt_message(message=message, key=key) == encrypted_message


# def test_encrypt_message_exception_key():
#     key = 'lago'
#     exception_message = 'tipo inválido para key'
#     with pytest.raises(TypeError, match=exception_message):
#         encrypt_message(message=message, key=key)


# def test_encrypt_message_exception_message():
#     key = 2
#     exception_message = 'tipo inválido para message'
#     with pytest.raises(TypeError, match=exception_message):
#         encrypt_message(message=1, key=key)
