import sys

class Cipher:

    """
        Cipher
    """

    MAX_LEN = 26
    encoder = [None] * MAX_LEN * 2 # encoding reference from ABC...XYZabc...xyz after shift
    decoder = [None] * MAX_LEN * 2 # decoding reference from ABC...XYZabc...xyz after shift
    default_shift = 0
    upperCase = False
    lowerCase = False

    def __init__(self):
        self.default_shift = 1
        upperCase = False
        lowerCase = False

    def encode(self, plaintext, shift=1):
        message = list(plaintext)
        encrypted = ''
        for i in range(len(message)):
            if (message[i].isupper()):
                newChar = chr((ord(message[i]) + shift - ord('A')) % self.MAX_LEN + ord('A'))
                self.upperCase = True
            elif (message[i].islower()):
                newChar = chr((ord(message[i]) + shift - ord('a')) % self.MAX_LEN + ord('a'))
                self.lowerCase = True
            else:
                raise Exception("Invalid input")

            # print("newchar: " + newChar)
            encrypted += encrypted.join(newChar)

        # handle mix of cases, convert into lower case
        if ( self.upperCase and self.lowerCase):
            encrypted = encrypted.lower()

        return encrypted

    def decode(self, ciphertext, shift=1):
        message = list(ciphertext)
        decrypted = ''
        for i in range(len(message)):
            if (message[i].isupper()):
                newChar = chr((ord(message[i]) - shift - ord('A')) % self.MAX_LEN + ord('A'))
            elif (message[i].islower()):
                newChar = chr((ord(message[i]) - shift - ord('a')) % self.MAX_LEN + ord('a'))
            else:
                raise Exception("Inavlid input")

            decrypted += decrypted.join(newChar)

        print(decrypted)

        # handle mix of cases, convert back into upper case for these at ODD index
        if ( self.upperCase and self.lowerCase):
            decrypted = ''
            for i in range(len(message)):
                if ( i % 2 != 0):
                    # convert to upper case
                    newChar = str(message[i]).upper()
                else :
                    newChar = message[i]
                decrypted += decrypted.join(newChar)

        print(decrypted)
        return decrypted

    def encodeV2(self, plaintext, shift = 1):
        for i in range(self.MAX_LEN):
            self.encoder[i] = chr((i + shift) % self.MAX_LEN + ord('A'))

        for i in range(self.MAX_LEN):
            self.encoder[i + self.MAX_LEN] = chr((i + shift) % self.MAX_LEN + ord('a'))

        forwardBuf = ''.join(self.encoder)
        return self.convertMsg(plaintext, forwardBuf)

    def decodeV2(self, ciphertext, shift = 1):
        for i in range(self.MAX_LEN):
            self.decoder[i] = chr((i - shift) % self.MAX_LEN + ord('A'))

        for i in range(self.MAX_LEN):
            self.decoder[i + self.MAX_LEN] = chr((i - shift) % self.MAX_LEN + ord('a'))

        backwardBuf = ''.join(self.decoder)
        return self.convertMsg(ciphertext, backwardBuf)

    def convertMsg(self, fromMsg, toMsg):
        message = list(fromMsg)
        for i in range(len(message)):
            if (message[i].isupper()):
                idxJ = (ord(message[i]) - ord('A')) % self.MAX_LEN
                message[i] = toMsg[idxJ]
            elif (message[i].islower()):
                idxJ = (ord(message[i]) - ord('a')) % self.MAX_LEN + self.MAX_LEN
                message[i] = toMsg[idxJ]
            else:
                raise

        return ''.join(message)


if __name__ == '__main__':
    cipher = Cipher()

    # with pytest.raises(Exception):
    #     cipher.encode(plaintext)

    #case two: can not pass, how can cases are changed???
    # need to convert the character on ODD position to be "downcase"???
    testMsg = "BcDeFgHiJk"

    coded = cipher.encode(testMsg, 1)
    print('Secret: ', coded)
    answer = cipher.decode(coded, 1)
    print('Plain: ', answer)

    assert coded == "abcdefghij"
    assert answer == "BcDeFgHiJk"

