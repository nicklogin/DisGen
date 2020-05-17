import pandas as pd

from .distractor_models import *
from .config import distractor_models

from datetime import datetime


def get_distractors(df):
    result_dfs = []
    d = datetime.now()
    for error_type, (Model_class, model_init_params) in distractor_models.items():
        needed_subset = df[df['Error type'] == error_type]
        model = Model_class(**model_init_params)
        new_df = model.get_distractors(needed_subset)
        result_dfs.append(new_df)
        print(datetime.now()-d)
    output_df = pd.concat(result_dfs, axis=0, sort=False)
    output_df.sort_index(inplace=True)
    return output_df
