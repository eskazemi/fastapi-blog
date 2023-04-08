from passlib.context import CryptContext

_pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashController:

    @classmethod
    def hashing(cls, password: str):
        return _pwd_cxt.hash(password)

    @classmethod
    def verify(cls, hash_password, plain_password):
        return _pwd_cxt.verify(plain_password, hash_password)
