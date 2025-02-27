from app.split_integer import split_integer
import pytest


class TestSplitInteger:
    @pytest.mark.parametrize(
        "value, number_of_parts, expected_result",
        [
            pytest.param(
                18,
                6,
                [3, 3, 3, 3, 3, 3],
                id=("should split into equal parts "
                    "when value divisible by parts")
            ),
            pytest.param(
                10,
                1,
                [10],
                id=("should return part equals to value "
                    "when split into one part")
            ),
            pytest.param(
                20,
                3,
                [6, 7, 7],
                id="parts should be sorted when they are not equal"
            ),
            pytest.param(
                4,
                7,
                [0, 0, 0, 1, 1, 1, 1],
                id="should add zeros when value is less than number of parts"
            )
        ]
    )
    def test_split_integer_correctly(
        self,
        value: int,
        number_of_parts: int,
        expected_result: list[int]
    ) -> None:
        assert split_integer(value, number_of_parts) == expected_result
