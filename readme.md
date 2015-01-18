
Test case for a problem I'm having with cryptography

I can execute from the Python code directly no problem, but when I try to freeze it and make an executable with either
cx_freeze or py2exe, I get:

Traceback (most recent call last):
  File "testcase.py", line 24, in <module>
  File "J:\James\Projects\cryptographybugtestcase\core\crypto.py", line 17, in encrypt
    token = __fernet.encrypt(in_file.read())
  File "c:\python34\lib\site-packages\cryptography\fernet.py", line 51, in encrypt
    return self._encrypt_from_parts(data, current_time, iv)
  File "c:\python34\lib\site-packages\cryptography\fernet.py", line 61, in _encrypt_from_parts
    ).encryptor()
  File "c:\python34\lib\site-packages\cryptography\hazmat\primitives\ciphers\base.py", line 43, in encryptor
    self.algorithm, self.mode
  File "c:\python34\lib\site-packages\cryptography\hazmat\backends\multibackend.py", line 57, in create_symmetric_encryption_ctx
    _Reasons.UNSUPPORTED_CIPHER
cryptography.exceptions.UnsupportedAlgorithm: cipher AES in CBC mode is not supported by this backend.