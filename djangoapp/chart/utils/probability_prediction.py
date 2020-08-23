import pandas as pd
from xgboost import XGBClassifier
import os

def predict_probability_of_winning(gold_diff_at_10, exp_diff_at_10, team):

    dirname = os.path.dirname(__file__)
    os.path.join(dirname, 'djangoapp/chart/utils/models/red_model.json')
    model = XGBClassifier()

    model.load_model(os.path.join(dirname, f'./models/{team}_model.json'))

    df = pd.DataFrame({
        team + 'GoldDiff': [gold_diff_at_10],
        team + 'ExperienceDiff': [exp_diff_at_10]
    })
    # values are casted into lists because pandas constructor doesnt allow scalars
    predicts = model.predict_proba(df)

    for i, col in enumerate(['redWin', 'blueWin']):
        df[col] = predicts[:, i]
    return df
# todo: create a model that extrapolates better, maybe ensemble of xgboost and lin reg
