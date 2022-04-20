#!/usr/bin/env python3

# Most pandas methods return a DataFrame so that
# another pandas method can be applied to the result.
# This improves readability of code.

import pandas as pd

#
# Traceback (most recent call last):
#  File "./ex01.py", line 20, in <module>
#    func()
#  File "./ex01.py", line 12, in func
#    pd.melt(df)
# UnboundLocalError: local variable 'df' referenced before assignment
#


def func():
    df1 = pd.DataFrame(
        [[4, 7, 10], [5, 8, 11], [6, 9, 12]], index=[1, 2, 3], columns=["a", "b", "c"]
    )

    df2 = pd.DataFrame(
        [[44, 77, 100], [55, 88, 111], [66, 99, 122]],
        index=[1, 2, 3],
        columns=["a", "b", "c"],
    )

    df = pd.concat([df1, df2], axis=1)

    print(df)


if __name__ == "__main__":
    func()
