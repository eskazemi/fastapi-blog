from passlib.hash import sha256_crypt
from passlib.context import CryptContext

_pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashController:

    @classmethod
    def hashing(cls, password: str):
        return _pwd_cxt.hash(password)
