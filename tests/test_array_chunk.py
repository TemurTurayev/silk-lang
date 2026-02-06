"""
Tests for array .chunk(size) method.
"""

from silk.interpreter import Interpreter


class TestArrayChunk:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_chunk_even(self):
        output = self._run('''
let chunks = [1, 2, 3, 4].chunk(2)
print(chunks.length)
print(chunks[0])
print(chunks[1])
''')
        assert output[-3] == "2"
        assert output[-2] == "[1, 2]"
        assert output[-1] == "[3, 4]"

    def test_chunk_uneven(self):
        output = self._run('''
let chunks = [1, 2, 3, 4, 5].chunk(2)
print(chunks.length)
print(chunks[2])
''')
        assert output[-2] == "3"
        assert output[-1] == "[5]"

    def test_chunk_size_larger(self):
        output = self._run('''
let chunks = [1, 2].chunk(5)
print(chunks.length)
print(chunks[0])
''')
        assert output[-2] == "1"
        assert output[-1] == "[1, 2]"

    def test_chunk_size_one(self):
        output = self._run('''
let chunks = [1, 2, 3].chunk(1)
print(chunks.length)
''')
        assert output[-1] == "3"
