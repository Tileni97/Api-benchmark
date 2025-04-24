# visualizers.py
"""
Functions for creating visualizations of benchmark results.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def create_latency_chart(latency_results, output_path):
    """
    Create a bar chart comparing API latencies across exchanges.

    Args:
        latency_results (dict): Nested dictionary with latency results
        output_path (str): Where to save the chart
    """
    # Extract endpoint types
    endpoint_types = set()
    for exchange in latency_results:
        endpoint_types.update(latency_results[exchange].keys())

    # Set up the plot with multiple groups
    fig, ax = plt.subplots(figsize=(12, 8))

    # Set width of bars
    bar_width = 0.2

    # Set positions of bars on X axis
    exchanges = list(latency_results.keys())
    x_pos = np.arange(len(exchanges))

    # Create bars for each endpoint type
    for i, endpoint in enumerate(sorted(endpoint_types)):
        values = []
        for exchange in exchanges:
            if endpoint in latency_results[exchange]:
                values.append(latency_results[exchange][endpoint])
            else:
                values.append(0)  # No data

        offset = bar_width * (i - len(endpoint_types) / 2 + 0.5)
        ax.bar(x_pos + offset, values, bar_width, label=endpoint)

    # Add labels and title
    ax.set_xlabel("Exchange")
    ax.set_ylabel("Latency (ms)")
    ax.set_title("API Response Latency by Exchange and Endpoint")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(exchanges)
    ax.legend()

    # Highlight Gate.io's position
    if "Gate.io" in exchanges:
        gateio_index = exchanges.index("Gate.io")
        plt.axvline(x=gateio_index, color="green", linestyle="--", alpha=0.3)
        plt.text(
            gateio_index,
            ax.get_ylim()[1] * 0.95,
            "Gate.io",
            rotation=90,
            verticalalignment="top",
            color="green",
        )

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def create_success_rate_charts(success_rate_results, output_path):
    """
    Create pie charts showing API request success rates.

    Args:
        success_rate_results (dict): Nested dictionary with success rate data
        output_path (str): Where to save the chart
    """
    # Get all exchanges and endpoint types
    exchanges = list(success_rate_results.keys())
    endpoint_types = set()
    for exchange in success_rate_results:
        endpoint_types.update(success_rate_results[exchange].keys())

    # Create a grid of subplots
    fig, axes = plt.subplots(len(exchanges), len(endpoint_types), figsize=(12, 10))
    fig.suptitle("API Request Success Rates", fontsize=16)

    # If there's only one endpoint or exchange, make sure axes is a 2D array
    if len(exchanges) == 1 and len(endpoint_types) == 1:
        axes = np.array([[axes]])
    elif len(exchanges) == 1:
        axes = np.array([axes])
    elif len(endpoint_types) == 1:
        axes = np.array([[ax] for ax in axes])

    # Iterate through exchanges and endpoints to create pie charts
    for i, exchange in enumerate(exchanges):
        for j, endpoint in enumerate(sorted(endpoint_types)):
            ax = axes[i, j]

            if endpoint in success_rate_results[exchange]:
                data = success_rate_results[exchange][endpoint]

                # Create pie chart
                if "successful" in data and "failed" in data:
                    values = [data["successful"], data["failed"]]
                    labels = ["Successful", "Failed"]
                    ax.pie(
                        values,
                        labels=labels,
                        autopct="%1.1f%%",
                        startangle=90,
                        colors=["#66b3ff", "#ff9999"],
                    )
                    ax.set_title(f"{exchange} - {endpoint}")
                else:
                    ax.text(
                        0.5,
                        0.5,
                        "No data",
                        horizontalalignment="center",
                        verticalalignment="center",
                    )
                    ax.axis("off")
            else:
                ax.text(
                    0.5,
                    0.5,
                    "No data",
                    horizontalalignment="center",
                    verticalalignment="center",
                )
                ax.axis("off")

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.savefig(output_path)
    plt.close()


def create_data_completeness_chart(fields_results, output_path):
    """
    Create a horizontal bar chart showing data field counts across exchanges.

    Args:
        fields_results (dict): Nested dictionary with field count information
        output_path (str): Where to save the chart
    """
    # Extract endpoint types
    endpoint_types = set()
    for exchange in fields_results:
        endpoint_types.update(fields_results[exchange].keys())

    # Create subplots for each endpoint type
    fig, axes = plt.subplots(
        len(endpoint_types), 1, figsize=(10, 4 * len(endpoint_types))
    )

    # If there's only one endpoint, make sure axes is iterable
    if len(endpoint_types) == 1:
        axes = [axes]

    # Iterate through endpoint types
    for i, endpoint in enumerate(sorted(endpoint_types)):
        ax = axes[i]

        # Collect data for this endpoint
        exchanges = []
        field_counts = []

        for exchange in fields_results:
            if endpoint in fields_results[exchange]:
                exchanges.append(exchange)
                field_counts.append(
                    fields_results[exchange][endpoint].get("field_count", 0)
                )

        # Sort by field count
        sorted_data = sorted(zip(exchanges, field_counts), key=lambda x: x[1])
        exchanges = [x[0] for x in sorted_data]
        field_counts = [x[1] for x in sorted_data]

        # Create horizontal bar chart
        y_pos = range(len(exchanges))
        ax.barh(y_pos, field_counts, align="center")
        ax.set_yticks(y_pos)
        ax.set_yticklabels(exchanges)
        ax.invert_yaxis()  # Labels read top-to-bottom
        ax.set_xlabel("Number of Fields")
        ax.set_title(f"Data Completeness: {endpoint} Endpoint")

        # Highlight Gate.io's position
        if "Gate.io" in exchanges:
            gateio_index = exchanges.index("Gate.io")
            ax.get_yticklabels()[gateio_index].set_color("green")
            ax.get_yticklabels()[gateio_index].set_weight("bold")
            gate_count = field_counts[gateio_index]
            ax.axvline(x=gate_count, color="green", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
