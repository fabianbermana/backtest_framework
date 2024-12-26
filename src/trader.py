
import pandas as pd

class Trader():

    def __init__(self):
        pass

    def produce_portfolio(
        self,
        current_market_data: pd.DataFrame,
        current_additional_data: pd.DataFrame | None
    ) -> pd.DataFrame:
        
        # print("trader current market data\n", current_market_data)

        # print("trader current additional data\n", current_additional_data)


        # NOTE: This is a dummy implementation with even weights for all assets. Replace this with your own implementation.
        output = pd.DataFrame(
            data=[current_market_data.shape[1]*[1/current_market_data.shape[1]]],
            columns = current_market_data.columns,
        )

        return output
