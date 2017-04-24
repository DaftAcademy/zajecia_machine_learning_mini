from hashlib import sha1
import pandas as pd

from sklearn.base import TransformerMixin
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


class SimplisticHasher(TransformerMixin):
    def __init__(self, cols, mod=100000):
        self.mod = mod
        self.cat_names = cols

    def fit(self, X, y=None):
        return self

    def _hash(self, value):
        return pd.np.nan if pd.isnull(value) else hash(value) % self.mod

    def transform(self, X):
        if len(self.cat_names) > 0:
            sub_X = X[self.cat_names].applymap(self._hash)
            X[self.cat_names] = sub_X
        return X

