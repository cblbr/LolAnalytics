def predict_probability_of_winning(gold_diff_at_10, exp_diff_at_10, team):
    from joblib import load
    import numpy as np
    import pandas as pd
    from xgboost import XGBClassifier

    model_blue = XGBClassifier()
    model_red = XGBClassifier()
    model_red.load_model('C:/Users/asd/PycharmProjects/ShouldWeSurrender15/djangoapp/chart/utils/models/red_model.json')
    model_blue.load_model('C:/Users/asd/PycharmProjects/ShouldWeSurrender15/djangoapp/chart/utils/models/blue_model.json')

    models = {'red': model_red, 'blue': model_blue}
    dictionary = {team + 'GoldDiff': [gold_diff_at_10], team + 'ExperienceDiff': [
        exp_diff_at_10]}  # values are casted into lists because pandas constructor doesnt allow scalars

    df = pd.DataFrame(dictionary)

    predicts = models[team].predict_proba(df)

    cols2 = ['redWin', 'blueWin']
    for i, col in enumerate(cols2):
        df[col] = predicts[:, i]
    return df
# todo: create a model that extrapolates better, maybe ensemble of xgboost and lin reg
