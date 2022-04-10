pip install numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example: Buckets A and B
# Bucket A: 30 blue, 10 yellow balls
# Bucket B: 20 blue, 20 yellow balls
# choose one ball, what is chance we choose from bucket A

hypos = 'bucket a', 'bucket b'
probs = 1/2, 1/2

prior = pd.Series(probs,hypos)
print(prior)

# Say we chose a blue ball
likelihood = 3/4, 1/2
unnorm = prior*likelihood

prob_data = unnorm.sum()

posterior = unnorm / prob_data