
import cryptography.fernet


def new_key():
    return cryptography.fernet.Fernet.generate_key()


class Crypto():
    def __init__(self, key):
        self.__key = key

    def encrypt(self, in_path, out_path):
        print('encrypt : %s to %s' % (in_path, out_path))
        __fernet = cryptography.fernet.Fernet(self.__key)
        with open(in_path, 'rb') as in_file:
            token = __fernet.encrypt(in_file.read())
            with open(out_path, 'wb') as out_file:
                out_file.write(token)

    def decrypt(self, in_path, out_path):
        print('decrypt : %s to %s' % (in_path, out_path))
        __fernet = cryptography.fernet.Fernet(self.__key)
        with open(in_path, 'rb') as in_file:
            b = __fernet.decrypt(in_file.read())
            with open(out_path, 'wb') as out_file:
                out_file.write(b)




