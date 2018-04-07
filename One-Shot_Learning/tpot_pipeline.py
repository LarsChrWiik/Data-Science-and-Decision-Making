import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from tpot.builtins import StackingEstimator
from xgboost import XGBClassifier

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:0.6354333333333333
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=XGBClassifier(booster="dart", learning_rate=0.2, max_depth=5, n_estimators=100, n_jobs=-1, objective="reg:linear")),
    RandomForestClassifier(criterion="entropy", max_depth=2, max_features="auto", n_estimators=50, n_jobs=-1)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
