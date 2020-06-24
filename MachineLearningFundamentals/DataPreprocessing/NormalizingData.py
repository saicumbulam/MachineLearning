import pandas as pd

# apply l2 normalization
data = pd.DataFrame([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])
# predefined data
print('{}\n'.format(repr(data)))

from sklearn.preprocessing import Normalizer
normalizer = Normalizer()
transformed = normalizer.fit_transform(data)
print('{}\n'.format(repr(transformed)))