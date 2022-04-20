#!/usr/bin/env python3

import pandas as pd


def main():
    df = pd.DataFrame(
        {"a": [4, 5, 6], "b": [7, 8, 9], "c": [10, 11, 12]}, index=[1, 2, 3]
    )

    print(df)


if __name__ == "__main__":
    main()
