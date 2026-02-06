"""
Tests for array .compact() and .chunked() methods.
"""

from silk.interpreter import Interpreter


class TestArrayCompact:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_compact_nulls(self):
        output = self._run('''
let arr = [1, null, 2, null, 3]
print(arr.compact())
''')
        assert output[-1] == "[1, 2, 3]"

    def test_compact_no_nulls(self):
        output = self._run('''
print([1, 2, 3].compact())
''')
        assert output[-1] == "[1, 2, 3]"

    def test_compact_all_nulls(self):
        output = self._run('''
print([null, null].compact())
''')
        assert output[-1] == "[]"

    def test_compact_preserves_falsy(self):
        """compact only removes null, not false or 0."""
        output = self._run('''
let arr = [0, null, false, "", 1]
print(arr.compact())
''')
        assert output[-1] == "[0, false, , 1]"

    def test_compact_empty(self):
        output = self._run('''
print([].compact())
''')
        assert output[-1] == "[]"


class TestArrayChunked:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_chunked_even(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5, 6]
let chunks = arr.chunked(2)
print(chunks.length)
print(chunks[0])
print(chunks[1])
print(chunks[2])
''')
        assert output[0] == "3"
        assert output[1] == "[1, 2]"
        assert output[2] == "[3, 4]"
        assert output[3] == "[5, 6]"

    def test_chunked_uneven(self):
        output = self._run('''
let chunks = [1, 2, 3, 4, 5].chunked(2)
print(chunks.length)
print(chunks[-1])
''')
        assert output[0] == "3"
        assert output[1] == "[5]"

    def test_chunked_size_one(self):
        output = self._run('''
print([1, 2, 3].chunked(1).length)
''')
        assert output[-1] == "3"

    def test_chunked_larger_than_array(self):
        output = self._run('''
print([1, 2].chunked(5))
''')
        assert output[-1] == "[[1, 2]]"
