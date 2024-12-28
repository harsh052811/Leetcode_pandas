import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    join=customers.merge(orders,how='left',left_on='id',right_on='customerId')
    null_val=join['customerId'].isna()
    df=join[null_val]
    final_df=df[['name']].rename(columns={'name':'Customers'})
    return final_df