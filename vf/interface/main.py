import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import datetime
import base64
import requests

from vf.params import *
from vf.utils import *

# Function to generate a download link
def get_download_link(file_path):
    with open(file_path, "rb") as file:
        # Read file data
        data = file.read()
        # Encode the file data into base64
        b64 = base64.b64encode(data).decode()
    return f"data:file/csv;base64,{b64}"


def update_location(df):
    most_frequent_location = df["location"].mode()[0]

    # Replace all other locations with 'Elsewhere'
    df["location"] = df["location"].apply(
        lambda x: x if x == most_frequent_location else "Elsewhere"
    )
    return df

def start_end_date_slider(df):
    old_date = df.index.max()
    new_date = df.index.min()
    return [old_date, new_date]

def make_dropdown_list(data):
    return data["location"].unique().to_list()


def current_year():
    current_year = datetime.datetime.now().year
    return int(current_year)


def to_timeseries(df, column, time_period="M"):
    # Resample and count occurrences in each period
    m_count = df.resample(time_period, on=column).size()

    # Convert to DataFrame
    m_count_df = m_count.reset_index()

    # Rename columns
    m_count_df.columns = ["date", "count"]

    return m_count_df





def count_last_year(df):
    filtered_df = df[
        (df["date"] > pd.Timestamp(f"{current_year()-1}-09-01"))
        & (df["date"] < pd.Timestamp(f"{current_year()}-02-28"))
    ]
    # Count vaccines for each age group
    children_count = filtered_df[filtered_df["age_at_vaccine"] <= 18]["pt_count"].sum()
    adult_count = filtered_df[
        (filtered_df["age_at_vaccine"] > 18) & (filtered_df["age_at_vaccine"] < 65)
    ]["pt_count"].sum()
    senior_count = filtered_df[filtered_df["age_at_vaccine"] >= 65]["pt_count"].sum()

    return [children_count, adult_count, senior_count]


def count_previous_year(df):
    filtered_df = df[
        (df["date"] > pd.Timestamp(f"{current_year()-2}-09-01"))
        & (df["date"] < pd.Timestamp(f"{current_year()-1}-02-28"))
    ]
    # Count vaccines for each age group
    children_count = filtered_df[filtered_df["age_at_vaccine"] <= 18]["pt_count"].sum()
    adult_count = filtered_df[
        (filtered_df["age_at_vaccine"] > 18) & (filtered_df["age_at_vaccine"] < 65)
    ]["pt_count"].sum()
    senior_count = filtered_df[filtered_df["age_at_vaccine"] >= 65]["pt_count"].sum()

    return [children_count, adult_count, senior_count]


def age_groups(data, display_years=20):
    c_year = data[
        (data["date"] > pd.Timestamp(f"{current_year()-display_years}-02-01"))
        & (data["date"] < pd.Timestamp(f"{current_year()}-02-28"))
    ]
    children = c_year[c_year["age_at_vaccine"] <= 18]
    over = c_year[c_year["age_at_vaccine"] >= 65]
    under = c_year[(c_year["age_at_vaccine"] > 18) & (c_year["age_at_vaccine"] < 65)]

    # Ensure the 'date' column is in datetime format
    children_ts = to_timeseries(children, "date", "M")
    children_ts.set_index("date", inplace=True)

    over_ts = to_timeseries(over, "date", "M")
    over_ts.set_index("date", inplace=True)

    under_ts = to_timeseries(under, "date", "M")
    under_ts.set_index("date", inplace=True)

    data_ts = to_timeseries(data, "date", "M")
    return [children_ts, under_ts, over_ts, data_ts]


def age_histplot(df):
    c_year = df[
        (df["date"] > pd.Timestamp(f"{current_year()-1}-02-01"))
        & (df["date"] < pd.Timestamp(f"{current_year()}-01-31"))
    ]
    children = c_year[c_year["age_at_vaccine"] <= 18]
    over = c_year[c_year["age_at_vaccine"] >= 65]
    under = c_year[(c_year["age_at_vaccine"] > 18) & (c_year["age_at_vaccine"] < 65)]

    children_series = children["age_at_vaccine"]
    over_series = over["age_at_vaccine"]
    under_series = under["age_at_vaccine"]

    fig, axes = plt.subplots(
        1, 3, figsize=(15, 2)
    )  # Adjusted figsize for better visibility

    # Plot each series in a different subplot
    sns.histplot(children_series, kde=True, ax=axes[0], color="#d59c0d")
    axes[0].set_title("Children - Age Histogram")

    sns.histplot(under_series, kde=True, ax=axes[1], color="#d59c0d")
    axes[1].set_title("18 - 64 yrs - Age Histogram")

    sns.histplot(over_series, kde=True, ax=axes[2], color="#d59c0d")
    axes[2].set_title("Over 65yrs - Age Histogram")

    # Customize each plot in the loop
    for ax in axes:
        # Remove top, right, and left spines
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)

        # Add grid
        ax.yaxis.grid(True, linestyle="--", linewidth=0.5, color="#888888")
        ax.set_xlabel("Age at vaccination")
        ax.set_ylabel("Count")

    # Adjust the layout for better spacing
    plt.tight_layout()

    # Show the plot in Streamlit
    st.pyplot(fig)


def plot_age_groups(children_under_over_list, max_ylim):
    # Create a figure with subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Loop through each subplot and plot the data
    for ax, data, title in zip(
        axes,
        children_under_over_list,
        ["Children (< 18 yrs)", "18 - 64 yrs", "Over 65 yrs"],
    ):
        sns.lineplot(data=data, x=data.index, y="count", ax=ax, color="#184e77")
        ax.set_title(title)
        ax.yaxis.grid(True, linestyle="--", linewidth=0.5, color="#888888")
        ax.xaxis.grid(True, linestyle="--", linewidth=0.5, color="#888888")

        # Customize the plot - remove the top, right, and left spines
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        # Set y-axis limits to 0 and 140
        ax.set_ylim(0, max_ylim - 40)
        ax.set_xlabel("")
        ax.set_ylabel("Vaccine Count")

    # Adjust the layout and display the plot
    plt.tight_layout()
    st.pyplot(fig)


def fetch_markdown_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Failed to fetch content"
