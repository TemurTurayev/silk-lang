"""
Tests for array .mapShuffle() method - return shuffled copy.
"""

from silk.interpreter import Interpreter


class TestArrayMapShuffle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapShuffle_length(self):
        output = self._run("""
let arr = [1, 2, 3, 4, 5]
let shuffled = arr.mapShuffle()
print(shuffled.length)
""")
        assert output[-1] == "5"

    def test_mapShuffle_same_elements(self):
        output = self._run("""
let arr = [1, 2, 3]
let shuffled = arr.mapShuffle()
print(shuffled.sort())
""")
        assert output[-1] == "[1, 2, 3]"
