import pandas as pd
import os

def load_configured_data(config):
    path = os.path.join(config.data_dir, config.data_file)
    return pd.read_csv(path)
