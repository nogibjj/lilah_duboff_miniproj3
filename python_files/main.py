"""Takes a csv file, reads it, and creates graphs"""

import matplotlib.pyplot as plt
import polars as pl


# create a function that loads in a dataset
def load_dataset(path):
    """Takes a string URL path to a csv file,
    loads it into the script for analysis,
    returns a dataframe"""
    try:
        data = pl.read_csv(path)
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None


def full_describe(bwt_data):
    """function that sets a new df variable equal to the summary stats"""
    desc_stats = bwt_data.describe()
    bwt_df = pl.DataFrame(desc_stats)
    with pl.Config(
    tbl_formatting="ASCII_MARKDOWN",
    tbl_hide_column_data_types=True,
    tbl_hide_dataframe_shape=True,
    ):
        print(desc_stats)


def build_bar_chart(bwt_data):
    """builds a histogram out of the target columns"""
#can add in code here to build a bar chart


def build_scatterplot(bwt_data):
    """builds a scatterplot out of the target columns"""
    plt.bar(bwt_data["gestation"], bwt_data["bwt.oz"])
    plt.xlabel("Gestation Length")
    plt.ylabel("Birth Weight(oz)")
    plt.title("Gestation length and average birth weight")
    plt.savefig("./outputs/gestation_and_bwt.png")
    plt.show


def main():
    bwt_data = load_dataset(
        "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/refs/heads/master/smoking.csv"
    )
    print(full_describe(bwt_data))

    plt.scatter(bwt_data["gestation"], bwt_data["bwt.oz"])
    plt.xlabel("Gestation Length (days)")
    plt.ylabel("Birth Weight(oz)")
    plt.title("Gestation and average birth weight")
    plt.savefig("./outputs/gest_and_bwt.png")
    plt.show

if __name__ == "__main__":
    main()
