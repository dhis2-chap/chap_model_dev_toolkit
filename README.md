# CHAP-model toolkit
A collection of reusable utility functions designed to simplify common programming tasks. Suitable for quick integration into various projects.

## Overview over util functions

### get_df_per_location(csv_fn)
A function that takes a csv file with data as argument, and returns a dictionary whith the locations as keys and their respective dataframes as values. In `minimalist example with multiple regions <https://github.com/dhis2-chap/minimalist_multiregion>`_ you can find an example of its usage.

### create_lagged_feature(df, feature, num_lags)
A function that takes a dataframe, a feature(string) and the number of periods(int) you want to lag the feature. E.g. if you call the function create_lagged_feature(X, "rainfall", 3), and the function will add three columns to X: "Rainfall_lag_1", "Rainfall_lag_2" and "Rainfall_lag_3", with respectively 1, 2 and 3 periods of lag. In minimalist_example_lag (insert link) you can find an example of its usage.

### make_valid_df(df, int_remove_rows):
  A function that if int_remove_rows == 0, changes all the "Na" to 0, or if int_remove_rows > 0, removes the first int_remove_rows rows of the df.  In minimalist_example_lag (insert link) you can find an example of its usage.
 
