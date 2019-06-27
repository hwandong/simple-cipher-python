import pytest
import unittest
import re

from simple_cipher import Cipher

class SimpleCipherTest(unittest.TestCase):
    # @pytest.mark.skip
    def test_encode_letter_with_default_shift_distance(self):
        cipher = Cipher()
        plaintext = 'a'
        ciphertext = 'b'
        self.assertEqual(ciphertext, cipher.encode(plaintext))

    # @pytest.mark.skip
    def test_decode_letter_with_default_shift_distance(self):
        cipher = Cipher()
        plaintext = 'b'
        ciphertext = 'a'
        self.assertEqual(ciphertext, cipher.decode(plaintext))

    # @pytest.mark.skip
    def test_encode_wraps_z_to_a(self):
        cipher = Cipher()
        plaintext = 'z'
        ciphertext = 'a'
        self.assertEqual(ciphertext, cipher.encode(plaintext))

    # @pytest.mark.skip
    def test_decode_wraps_a_to_z(self):
        cipher = Cipher()
        plaintext = 'a'
        ciphertext = 'z'
        self.assertEqual(ciphertext, cipher.decode(plaintext))

    # @pytest.mark.skip
    def test_encode_string_with_default_shift_distance(self):
        cipher = Cipher()
        plaintext = 'wxyzabcd'
        ciphertext = 'xyzabcde'
        self.assertEqual(ciphertext, cipher.encode(plaintext))

    # @pytest.mark.skip
    def test_decode_string_with_default_shift_distance(self):
        cipher = Cipher()
        plaintext = 'xyzabcde'
        ciphertext = 'wxyzabcd'
        self.assertEqual(ciphertext, cipher.decode(plaintext))

    # @pytest.mark.skip
    def test_encode_with_10_shift_distance(self):
        cipher = Cipher()
        plaintext = 'wxyzabcd'
        ciphertext = 'ghijklmn'
        self.assertEqual(ciphertext, cipher.encode(plaintext, 10))

    # @pytest.mark.skip
    def test_decode_with_10_shift_distance(self):
        cipher = Cipher()
        plaintext = 'ghijklmn'
        ciphertext = 'wxyzabcd'
        self.assertEqual(ciphertext, cipher.decode(plaintext, 10))

    # @pytest.mark.skip
    def test_encode_with_26_shift_distance(self):
        cipher = Cipher()
        plaintext = 'abcdefghij'
        ciphertext = 'abcdefghij'
        self.assertEqual(ciphertext, cipher.encode(plaintext, 26))

    # @pytest.mark.skip
    def test_decode_with_26_shift_distance(self):
        cipher = Cipher()
        plaintext = 'klmnopqrst'
        ciphertext = 'klmnopqrst'
        self.assertEqual(ciphertext, cipher.decode(plaintext, 26))

    # @pytest.mark.skip
    def test_encode_with_27_shift_distance(self):
        cipher = Cipher()
        plaintext = 'wxyzabcd'
        ciphertext = 'xyzabcde'
        self.assertEqual(ciphertext, cipher.encode(plaintext, 27))

    # @pytest.mark.skip
    def test_decode_with_27_shift_distance(self):
        cipher = Cipher()
        plaintext = 'xyzabcde'
        ciphertext = 'wxyzabcd'
        self.assertEqual(ciphertext, cipher.decode(plaintext, 27))

    # @pytest.mark.skip
    def test_encode_always_returns_downcase_string(self):
        cipher = Cipher()
        plaintext = 'AbCdEfGhIj'
        ciphertext = 'bcdefghijk'
        self.assertEqual(ciphertext, cipher.encode(plaintext))

    # @pytest.mark.skip
    def test_decode_always_returns_downcase_string(self):
        cipher = Cipher()
        plaintext = 'BcDeFgHiJk'
        ciphertext = 'abcdefghij'
        self.assertEqual(ciphertext, cipher.decode(plaintext))

    # @pytest.mark.skip
    def test_encode_raise_error_if_non_letter_characters(self):
        cipher = Cipher()
        plaintext = 'az4'
        with pytest.raises(Exception):
            cipher.encode(plaintext)

    # @pytest.mark.skip
    def test_decode_raise_error_if_non_letter_characters(self):
        cipher = Cipher()
        plaintext = 'az4'
        with pytest.raises(Exception):
            cipher.decode(plaintext)

if __name__ == '__main__':
    unittest.main()
