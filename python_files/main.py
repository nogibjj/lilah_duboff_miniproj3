import lib
import polars as pl
import matplotlib.pyplot as plt


def main():
    bwt_data = lib.load_dataset(
        "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/refs/heads/master/smoking.csv"
    )
    summary_stats = lib.full_describe(bwt_data)
    lib.build_scatterplot(bwt_data)


if __name__ == "__main__":
    main()
