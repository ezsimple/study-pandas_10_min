#!/usr/bin/env python3

import pandas as pd


def main():
    df = pd.DataFrame(
        [[4, 7, 10], [5, 8, 11], [6, 9, 12]],
        index=[1, 2, 3],  # 라인번호
        columns=["a", "b", "c"],
    )  # 컬럼명

    print(df)


if __name__ == "__main__":
    main()
