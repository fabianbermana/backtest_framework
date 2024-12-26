
import pandas as pd
import numpy as np


class Results:

    def __init__(
        self,
        total_return_indices: pd.DataFrame,
        portfolios: pd.DataFrame
    ):
        self._total_return_indices = total_return_indices
        self._portfolios = portfolios

        self._get_returns()

    def _get_returns(self):
        # compute the single-period percentage change of the total return indices
        self._asset_returns = self._total_return_indices.copy()

        for col in self._total_return_indices.columns:
            self._asset_returns[col] = (
                (self._asset_returns[col].shift(-1) - self._asset_returns[col]) / np.abs(self._asset_returns[col]) 
            )

        self._asset_returns = self._asset_returns.dropna()

        # compute the single-period return of the portfolios
        self._portfolio_returns = self._portfolios.copy() * (1 + self._asset_returns)

        self._portfolio_returns = self._portfolio_returns.sum(axis=1)

    def compute_performance(self):
        # compute the performance of the portfolio
        # by multiplying the total return indices with the portfolio weights
        # and summing the result
        portfolio_performance = None

        return portfolio_performance


if __name__ == "__main__":
    total_return_indices = pd.DataFrame(
        data = {
            "date": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "sp500": [100.0, 101.0, 102.0],
            "nasdaq": [100.0, 103.0, 106.0],
        }
    )

    total_return_indices['date'] = pd.to_datetime(total_return_indices['date'])

    total_return_indices.set_index("date", inplace=True)

    portfolios = total_return_indices.copy()
    portfolios = portfolios.iloc[:-1,:]
    portfolios = portfolios.dropna()
    portfolios.loc[:,:] = 0.5

    

    results = Results(total_return_indices, portfolios)

    print("Portfolios: \n", results._portfolios, '\n')
    print("Asset Returns: \n", results._asset_returns, '\n')
    print("Portfolio Returns: \n", results._portfolio_returns, '\n')