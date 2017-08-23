from queue import Queue

class CaesarCipher:
    def __init__(self, plain="", key=""):
        self.q = Queue()
        self.plain = plain
        self.key = key
        self.cipher = ""

    def encode(self):
        self.cipher = ""
        for i, j in zip(self.plain, self.key):
            if i.isalpha():
                if i.isupper():
                    shift = 65
                else:
                    shift = 97
                self.cipher += chr((ord(i) +int(j) -shift)%26 +shift)
            else:
                self.cipher += i

    def decode(self):
        self.plain = ""
        for i, j in zip(self.cipher, self.key):
            if i.isalpha():
                if i.isupper():
                    shift = 65
                else:
                    shift = 97
                self.plain += chr((ord(i) -int(j) -shift)%26 +shift)
            else:
                self.plain += i

if __name__ == "__main__":
    plain = "I love Python"
    key = "2 5618 325618"

    print("plaintext  : ", plain)
    print("secrettext : ", key)

    c = CaesarCipher(plain, key)
    c.encode()
    print("ciphertext : ", c.cipher)
    c.decode()
    print("decodetext : ", c.plain)
