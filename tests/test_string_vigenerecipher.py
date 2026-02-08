"""
Tests for string .vigenereCipher(key) method - Vigenere cipher.
"""

from silk.interpreter import Interpreter


class TestStringVigenereCipher:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_vigenereCipher_encrypt(self):
        output = self._run('print("hello".vigenereCipher("key"))')
        assert output[-1] == "rijvs"

    def test_vigenereCipher_abc(self):
        output = self._run('print("abc".vigenereCipher("abc"))')
        assert output[-1] == "ace"
