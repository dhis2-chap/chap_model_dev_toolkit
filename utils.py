import pandas as pd

def get_df_per_location(csv_fn):
    full_df = pd.read_csv(csv_fn)
    unique_locations_list = full_df['location'].unique()
    locations = {location: full_df[full_df['location'] == location] for location in unique_locations_list}
    return locations

def create_lagged_feature(df, feature, num_lags):
    for lag in range(1, num_lags + 1):
        df[f'{feature}_lag_{lag}'] = df[feature].shift(lag)


def make_valid_df(df, int_remove_rows):
    assert int_remove_rows >= 0
    if int_remove_rows == 0:
        df = df.fillna(0)
    else:
        df = df.iloc[int_remove_rows:].reset_index(drop=True)
