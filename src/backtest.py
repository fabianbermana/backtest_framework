
import pandas as pd

class Backtest():

    def __init__(
        self,
        total_return_indices: pd.DataFrame,
        additional_data: pd.DataFrame | None = None
    ):
    
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

    Backtest = Backtest(total_return_indices=total_return_indices)


