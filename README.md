# Portfolio Optimisation

A Python project exploring portfolio allocation using historical stock prices. The goal is to compare a minimum-variance portfolio with an equally weighted portfolio and evaluate both on data outside the training period.

Currently in development.

## Approach

- Download adjusted historical prices using `yfinance` and cache them locally.
- Calculate daily returns and examine volatility and correlations.
- Find portfolio weights that minimise estimated variance, with no short selling and weights summing to 100%.
- Compare performance against an equally weighted portfolio on a later test period.
- Evaluate cumulative returns, volatility and maximum drawdown.

## Setup

Create and activate a Conda environment:

```bash
conda create -n portofolio-optimisation python=3.14 pip
conda activate portofolio-optimisation
```

Install dependencies and start JupyterLab:

```bash
python -m pip install -r requirements.txt
python -m jupyterlab
```

## Tools

Python, pandas, NumPy, SciPy, Matplotlib, yfinance and JupyterLab.

## Scope

This is a learning project. Results will depend on the assets, dates and assumptions used. Historical performance does not establish how a portfolio will perform in the future.