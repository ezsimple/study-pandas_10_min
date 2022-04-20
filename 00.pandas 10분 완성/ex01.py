#!/usr/bin/env python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    s = pd.Series([1, 3, 4, np.nan, 6, 8])
    print(s)


def sub1():
    date = pd.date_range("20220401", periods=6)
    print(date)
    return date


def sub2():
    dates = sub1()
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print(df)


def sub3():
    df2 = pd.DataFrame(
        {
            "A": 1.0,
            "B": pd.Timestamp("20130102"),
            "C": pd.Series(1, index=list(range(4)), dtype="float32"),
            "D": np.array([3] * 4, dtype="int32"),
            "E": pd.Categorical(["test", "train", "test", "train"]),
            "F": "foo",
        }
    )
    print(df2)
    print(df2.index)  # 라인수
    print(df2.columns)  # 컬럼명
    print(df2.values)  # 값들
    print(df2.describe())  #  통계요약
    print(df2.T)  # 데이터 전치(피보팅)
    print(df2.sort_index(axis=1, ascending=False))  # 축별 정렬
    print(df2.sort_values(by="B"))  # 값별 정렬


def sub4():
    df = pd.DataFrame(
        {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
    )
    print(df)

    # if-then
    df.loc[df.AAA >= 5, "BBB"] = -1
    print(df)


def sub5():
    df = pd.DataFrame({"AAA": [True] * 4, "BBB": [False] * 4, "CCC": [True, False] * 2})
    df = df.where(df, -1000)
    print(df)


def sub6():
    df = pd.DataFrame(
        {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
    )
    print(df)
    df["logic"] = np.where(df["AAA"] > 5, "high", "low")
    print(df)


def sub7():
    s = pd.Series(np.random.randint(0, 7, size=10))
    print(s.value_counts())


def sub8():
    s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
    print(s.str.lower())


def sub9():
    df = pd.DataFrame(np.random.randn(10, 4))
    print(df)

    # break it into pieces
    pieces = [df[:3], df[3:7], df[7:]]
    # print(pieces)
    print(pd.concat(pieces))


def sub10():
    left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
    right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
    print(left)
    print(right)
    print(pd.merge(left, right, on="key"))


def sub11():
    df = pd.DataFrame(np.random.randn(8, 4), columns=["A", "B", "C", "D"])
    print(df)


def sub12():
    df = pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
        }
    )
    print(df)
    print(df.groupby("A").sum())
    print(df.groupby(["A", "B"]).sum())


def sub13():
    tuples = list(
        zip(
            *[
                ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
                ["one", "two", "one", "two", "one", "two", "one", "two"],
            ]
        )
    )
    index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
    df2 = df[:4]
    print(df2)

    stacked = df2.stack()
    print(stacked)
    print(stacked.unstack())


def sub14():
    df = pd.DataFrame(
        {
            "A": ["one", "one", "two", "three"] * 3,
            "B": ["A", "B", "C"] * 4,
            "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
            "D": np.random.randn(12),
            "E": np.random.randn(12),
        }
    )
    print(df)

    df2 = pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
    print(df2)


def sub15():
    rng = pd.date_range("1/1/2012", periods=100, freq="S")
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    res = ts.resample("5Min").sum()
    print(res)


def sub16():
    rng = pd.date_range("1/1/2012", periods=5, freq="M")
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    print(ts)


if __name__ == "__main__":
    sub16()
