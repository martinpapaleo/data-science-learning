def save_data(data_, debug=False):
    data_.to_parquet()
    return True