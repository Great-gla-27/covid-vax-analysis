import pandas as pd
import matplotlib.pyplot as plt

def load_data(path: str) -> pd.DataFrame:
    """Load vaccination dataset."""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(subset=["location", "date"])
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    return df



def plot_vaccination_curve(df: pd.DataFrame, country: str, output_path: str = None):
    """Plot vaccination curve for a given country."""
    country_data = df[df["location"] == country]

    plt.figure(figsize=(12, 6))
    plt.plot(
        country_data["date"],
        country_data["people_vaccinated_per_hundred"],
        label="At least one dose"
    )
    plt.plot(
        country_data["date"],
        country_data["people_fully_vaccinated_per_hundred"],
        label="Fully vaccinated"
    )

    plt.title(f"Vaccination Coverage Over Time - {country}")
    plt.xlabel("Date")
    plt.ylabel("Percentage of Population")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()


def plot_multiple_countries(df, countries, output_path=None):
    """Plot fully vaccinated coverage for multiple countries on the same chart."""
    plt.figure(figsize=(12, 6))
    for country in countries:
        subset = df[df["location"] == country]
        plt.plot(
            subset["date"],
            subset["people_fully_vaccinated_per_hundred"],
            label=f"{country}"
        )
    plt.title("COVID-19 Vaccination Coverage (Fully Vaccinated)")
    plt.xlabel("Date")
    plt.ylabel("Percentage of Population")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()


def export_summary(df, countries, output_csv):
    """Export final vaccination stats per country to CSV."""
    summary = []
    for country in countries:
        subset = df[df["location"] == country].dropna(
            subset=["people_fully_vaccinated_per_hundred",
                    "people_vaccinated_per_hundred"]
        )
        if not subset.empty:
            last_row = subset.iloc[-1]
            summary.append({
                "country": country,
                "date": last_row["date"],
                "at_least_one_dose": last_row["people_vaccinated_per_hundred"],
                "fully_vaccinated": last_row["people_fully_vaccinated_per_hundred"]
            })
    pd.DataFrame(summary).to_csv(output_csv, index=False)
    print(f"Summary exported to {output_csv}")




