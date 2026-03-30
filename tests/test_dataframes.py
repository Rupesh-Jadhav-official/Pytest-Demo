import pytest

try:
    import pandas as pd
except ImportError:
    pd = None

@pytest.mark.skipif(pd is None, reason="pandas is not installed")
def test_dataframe_operations():
    assert pd is not None
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
    }

    df = pd.DataFrame(data)

    # Test DataFrame creation
    assert len(df) == 3
    assert list(df.columns) == ["Name", "Age"]

    # Test age column
    assert list(df["Age"]) == [25, 30, 35]

    # Test IsAdult column
    df["IsAdult"] = df["Age"] >= 18
    assert all(df["IsAdult"])

    # Test age statistics
    stats = df["Age"].describe()
    assert stats["mean"] == 30
