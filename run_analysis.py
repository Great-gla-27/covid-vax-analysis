import argparse
import os
from src.analysis import (
    load_data,
    clean_data,
    plot_vaccination_curve,
    plot_multiple_countries,
    export_summary,
)

def main():
    parser = argparse.ArgumentParser(description="COVID Vaccination Analysis")
    parser.add_argument("--data", type=str, required=True, help="Path to dataset CSV")
    parser.add_argument("--country", type=str, required=True,
                        help="Country name or comma-separated list of countries")
    parser.add_argument("--output", type=str, required=True,
                        help="Output PNG path (CSV will be created alongside)")
    args = parser.parse_args()

    df = load_data(args.data)
    df = clean_data(df)

    countries = [c.strip() for c in args.country.split(",")]

    # Create both PNG and CSV outputs
    png_path = args.output
    csv_path = os.path.splitext(args.output)[0] + "_summary.csv"

    if len(countries) == 1:
        plot_vaccination_curve(df, countries[0], png_path)
        export_summary(df, countries, csv_path)
    else:
        plot_multiple_countries(df, countries, png_path)
        export_summary(df, countries, csv_path)

if __name__ == "__main__":
    main()
