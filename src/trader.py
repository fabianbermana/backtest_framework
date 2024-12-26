
import pandas as pd

class Trader:

    def __init__(self):
        pass

    def produce_portfolio(
        self,
        current_market_data: pd.DataFrame,
        current_additional_data: pd.DataFrame | None
    ) -> pd.DataFrame:
        """Output the trader's portfolio for the current time step, 
        based on the current market data and additional data. This method should be
        overridden in a subclass of Trader to implement their own trading strategy.
        
        This function will be called at each time step of the backtest by the Backtest class. Each time it is called,
        it should return a DataFrame with a single row, containing the weights of each asset in the portfolio at the current time step.
        Ensure that this output has the same columns as the total_return_indices, else the backtest will raise an error.

        Weights do not need to sum to 1, as this will represent leverage.

        Args:
            current_market_data (pd.DataFrame): Current total return indices of available assets
            current_additional_data (pd.DataFrame | None): Current additional data available for desicion making

        Returns:
            pd.DataFrame: The output weights of each asset in the portfolio at the current time step.
        """


        # print("trader current market data\n", current_market_data)
        # print("trader current additional data\n", current_additional_data)

        # NOTE: This is a dummy implementation with even weights for all assets. Replace this with your own implementation.
        output = pd.DataFrame(
            data=[current_market_data.shape[1]*[1/current_market_data.shape[1]]],
            columns = current_market_data.columns,
        )

        return output
