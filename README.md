# COVID-19 Vaccination Analysis

A Python-based data analysis project that explores global COVID-19 vaccination progress using open-source datasets.  
The project demonstrates a reproducible workflow with modular code, a clean report notebook, and static demo outputs.

Disclaimer: This repository is for research and educational purposes only. Data is historical and may no longer reflect current vaccination rates.

---

## TL;DR
- Core idea: Track and visualize COVID-19 vaccination trends across countries.  
- Built with: Python (pandas, matplotlib, numpy).  
- Demo: Run the pipeline with one command or view the static HTML report.  
- Outcome: A structured report showing vaccination coverage curves and country-level insights.

---

## Features
- Load and clean vaccination datasets from CSV/Excel sources.  
- Compute metrics such as vaccination coverage and population percentages.  
- Visualize progress with time-series plots for specific countries.  
- Export results as PNGs and HTML reports for easy sharing.  

---

## Demo Instructions

### Quickstart (local run)
```bash
git clone https://github.com/Great-gla-27/covid-vax-analysis.git
cd covid-vax-analysis
pip install -r requirements.txt
python run_analysis.py --data data/covidVaccinations.csv --country "United Kingdom" --output demo/uk_vax_curve.png
