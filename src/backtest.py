
import pandas as pd
from trader import Trader

class Backtest():

    def __init__(
        self,
        total_return_indices: pd.DataFrame,
        trader: Trader,
        additional_data: pd.DataFrame | None = None
    ):
        """Initializes the backtest object with the total return indices, the trader object and additional data.
        Requires the index of total_return_indices to be a datetime index and sorted.

        Args:
            total_return_indices (pd.DataFrame): The total return index of each asset in the portfolio. Each
                column represents the total return index of an asset. The index of the DataFrame is a datetime index.
                if non-total return indices are used, user must to convert them to total return indices, otherwise
                effects such as dividend payments, carry, repo, etc will not be accounted for.

            trader (Trader): _description_

            additional_data (pd.DataFrame | None, optional): _description_. Additional data that the trader can use
                to make decisions. The index of the DataFrame is a datetime index. Defaults to None. The index of the
                additional_data DataFrame must match the index of the total_return_indices DataFrame.

        Raises:
            ValueError: if the index of total_return_indices is not a datetime index.
            ValueError: if the index of total_return_indices is not sorted.
            ValueError: if the index of total_return_indices and additional_data do not match.
        """        
    
        # check if index is a datetime index
        if not pd.api.types.is_datetime64_any_dtype(total_return_indices.index):
            raise ValueError("Index of total_return_indices is not a datetime index.")

        # check if index is sorted
        if not total_return_indices.index.is_monotonic_increasing:
            raise ValueError("Index of total_return_indices is not sorted.")

        # check if indices of total_return_indices and additional_data match
        if additional_data is not None:
            if (total_return_indices.index != additional_data.index): 
                raise ValueError("Indices of total_return_indices and additional_data do not match.")


        self._total_return_indices: pd.DataFrame = total_return_indices
        self._additional_data: pd.DataFrame = additional_data

        self._trader: Trader = trader

        self._time_idx: int = 0
        self._max_time_idx: int = len(total_return_indices) - 1

    def run(self):
        while self._time_idx <= self._max_time_idx:
            
            # at time step t, the trader receives the market data and additional data up to time step t
            self._current_market_data = self._total_return_indices.iloc[self._time_idx,:]
            self._current_additional_data = self._additional_data.iloc[self._time_idx,:] if self._additional_data is not None else None

            # the trader makes a portfolio based on the market data and additional data
            current_portfolio = self._trader.produce_portfolio(
                current_market_data=self._current_market_data,
                current_additional_data=self._current_additional_data
            )

            # increment the time index
            self._time_idx += 1



if __name__ == "__main__":

    total_return_indices = pd.DataFrame(
        data = {
            "date": ["2021-01-01", "2021-01-02", "2021-01-03"],
            "sp500": [100, 101, 102]
        }
    )

    total_return_indices['date'] = pd.to_datetime(total_return_indices['date'])

    total_return_indices.set_index("date", inplace=True)

    print(total_return_indices)

    trader = Trader()

    Backtest = Backtest(
        trader=trader, 
        total_return_indices=total_return_indices
    )


