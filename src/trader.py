
import pandas as pd

class Trader():

    def __init__(self):
        pass

    def produce_portfolio(
        self,
        current_market_data: pd.DataFrame,
        current_additional_data: pd.DataFrame | None
    ) -> pd.DataFrame:
        
        raise NotImplementedError("Method produce_portfolio() is not implemented.")
