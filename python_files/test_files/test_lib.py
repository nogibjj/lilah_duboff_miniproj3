"""
Testing the library file functions

"""
import io
import sys

sys.path.append("python_files")

from lib import (
    load_dataset,
    full_describe,
    build_scatterplot,
)

# Shortened mock CSV data as a string (only "gestation" and "bwt.oz" columns)
mock_csv_data = """
,gestation,bwt.oz
1,265,120
2,257,110
3,283,115
4,263,150
5,270,143
6,300,130
7,325,155
8,296,127
9,288,99
"""
test_path = io.StringIO(mock_csv_data)


def test_load_dataset():
    """test that loading the CSV will work"""
    result = load_dataset(test_path)
    assert result is not None
    assert result.shape == (9, 3)


def test_full_describe():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)

    result = full_describe(test_df)
    assert result is not None


# def test_build_bar_chart():
#     test_path = io.StringIO(mock_csv_data)
#     test_df = load_dataset(test_path)

#     result = build_bar_chart(test_df, False)
#     assert result is None

def test_build_scatterplot():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)

    result = build_scatterplot(test_df)
    assert result is None


if __name__ == "__main__":
    test_load_dataset()
    test_full_describe()
    test_build_scatterplot()