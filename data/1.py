# %%
import shelve
import pandas as pd

data = shelve.open('recommend')
rec = data['mid_only']

# %%
df = pd.DataFrame({

})