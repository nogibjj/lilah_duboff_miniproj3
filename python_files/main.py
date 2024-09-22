"""Takes a csv file, reads it, and creates graphs"""

import matplotlib.pyplot as plt
import polars as pl 

csv_url = "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/refs/heads/master/smoking.csv"



# create a function that loads in a dataset
def load_dataset(path):
    """Takes a string URL path to a csv file,
    loads it into the script for analysis,
    returns a dataframe"""
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None


def full_describe(driving_df):
    """function that sets a new df variable equal to the summary stats"""
    summary_stats = driving_df.describe()
    stats_markdown = summary_stats.to_markdown()
    with open("driving_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(stats_markdown)
        file.write("\n\n")
        file.write(
            "![driving_fatalities](python_files/outputs/driving_fatalities.png)\n"
        )

    return stats_markdown


def build_bar_chart(driving_df, is_jupyter):
    """builds a histogram out of the target columns"""

    plt.bar(driving_df["year"], driving_df["fatal"])
    plt.xlabel("Year")
    plt.ylabel("Number of Fatalities")
    plt.title("Number of Car Crash Fatalities by Year")

    if is_jupyter is True:
        plt.savefig("./outputs/driving_fatalities.png")
    if is_jupyter is False:
        plt.savefig("python_files/outputs/output.png")
        plt.show()


def build_scatterplot():
    """builds a scatterplot out of the target columns"""
    # can be used to build scatterplots