# -*- coding: utf-8 -*-
import os
import numpy as np
from pandas import read_csv, DataFrame
import click


@click.option("--option", default=1, help="1:◖─◦─◗ 2: ▁╭─╴╶─╮▁ 3: ▁▂ ▂▁ 4:[=*=]")
@click.option("--g", help="provide the grouping column with --g <column_name>")
@click.option("--y", help="provide the main column of interest with --y <column_name>")
@click.option("--table", default=1, help="1. solid table ▁▁▁ 2: barred table ___ ")
@click.option("--clip", default=1, help="set clipping level for ends of boxplots: 1. min, max 2. 2% to 98% 3: 9% to 91% 4: 20% to 80%")
@click.command()
def main(option, g, y, table, clip):

    tmp_location = "/tmp/termplot_summary.csv"
    # for first run
    # os.system('apt list --installed miller')
    if g is not None:
        if y is None:
            print("the --y option is required with --g")
        else:
            if clip == 1:
                mi = "min"
                ma = "max"
            elif clip == 2:
                mi = "p1"
                ma = "p99"
            elif clip == 3:
                mi = "p8"
                ma = "p92"
            elif clip == 4:
                mi = "p20"
                ma = "p80"
            else:
                mi = "min"
                ma = "max"
            os.system(
                "mlr --csv stats1 -a "
                + mi
                + ",p25,p50,p75,"
                + ma
                + " -f "
                + y
                + " -g "
                + g
                + " > "
                + str(tmp_location)
            )
            array_raw = read_csv(tmp_location).to_numpy()
            array_numerics = array_raw[:, 1:]
    else:
        if y is None:
            print("the --y option is required")
        else:
            if clip == 1:
                mi = "min"
                ma = "max"
            elif clip == 2:
                mi = "p1"
                ma = "p99"
            elif clip == 3:
                mi = "p8"
                ma = "p92"
            elif clip == 4:
                mi = "p20"
                ma = "p80"
            else:
                mi = "min"
                ma = "max"
            os.system(
                "mlr --csv stats1 -a "
                + mi
                + ",p25,p50,p75,"
                + ma
                + " -f "
                + y
                + " > "
                + str(tmp_location)
            )
            array_raw = read_csv(tmp_location).to_numpy()
            array_numerics = array_raw[:, 0:]

    option = option
    width = 60

    overall_min = np.min(array_numerics)
    overall_max = np.max(array_numerics)

    def scale(x):
        scaleXwidth = (x - overall_min) / (overall_max - overall_min) * width
        ints = np.array(scaleXwidth, dtype=int)
        return ints

    array_scaled = scale(array_numerics)
    d = np.diff(array_scaled)
    start = array_scaled[:, 0].reshape(array_scaled.shape[0], 1)
    array_5num = np.hstack((start, d))

    option1 = [" ", "─", "◖", "─", "◦", "─", "◗", "─"]
    option2 = [" ", "▁", "╭", "─", "╴╶", "─", "╮", "▁"]
    option3 = [" ", "▁", "▂", " ", "▂", "▁"]
    option4 = [" ", "─", "[", "=", "*", "=", "]", "─"]
    rows = array_numerics.shape[0]

    print("\n")
    if option == 1:

        for i in range(rows):
            print(
                "{:<3}".format(str(i + 1))
                + "│ "
                + option1[0] * array_5num[i, 0]
                + option1[1] * array_5num[i, 1]
                + option1[2]
                + option1[3] * array_5num[i, 2]
                + option1[4]
                + option1[5] * array_5num[i, 3]
                + option1[6]
                + option1[7] * array_5num[i, 4]
            )
    elif option == 2:

        for i in range(rows):
            print(
                "{:<3}".format(str(i + 1))
                + "│ "
                + option2[0] * array_5num[i, 0]
                + option2[1] * array_5num[i, 1]
                + option2[2]
                + option2[3] * array_5num[i, 2]
                + option2[4]
                + option2[5] * array_5num[i, 3]
                + option2[6]
                + option2[7] * array_5num[i, 4]
            )
    elif option == 3:

        for i in range(rows):
            print(
                "{:<3}".format(str(i + 1))
                + "│ "
                + option3[0] * array_5num[i, 0]
                + option3[1] * array_5num[i, 1]
                + option3[2] * array_5num[i, 2]
                + option3[3]
                + option3[4] * array_5num[i, 3]
                + option3[5] * array_5num[i, 4]
            )
    else:

        for i in range(rows):
            print(
                "{:<3}".format(str(i + 1))
                + "│ "
                + option4[0] * array_5num[i, 0]
                + option4[1] * array_5num[i, 1]
                + option4[2]
                + option4[3] * array_5num[i, 2]
                + option4[4]
                + option4[5] * array_5num[i, 3]
                + option4[6]
                + option4[7] * array_5num[i, 4]
            )

    if table == 1:

        os.system("cat " + str(tmp_location) + " | mlr --icsv --opprint --barred cat")

    else:

        print("▁" * 70)
        os.system("cat " + str(tmp_location) + " | mlr --icsv --opprint cat")
        print("▁" * 70)

    print("\n")


if __name__ == "__main__":
    main()
