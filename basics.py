#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pandas

sns.set_theme()

data = pandas.read_csv("data/table-1-1-mf.csv")

data.columns = ["Age Group", "None","1st - 4th grade","5th - 6th grade","7th - 8th grade","9th grade","10th grade","11th grade","High school graduate","Some college, no degree","Associate's degree, occupational","Associate's degree, academic","Bachelor's degree","Master's degree","Professional degree","Doctoral degree"]
plt.scatter(data["Age Group"], data["1st - 4th grade"])
plt.scatter(data["Age Group"], data["5th - 6th grade"])
plt.scatter(data["Age Group"], data["7th - 8th grade"])
plt.scatter(data["Age Group"], data["9th grade"])
plt.scatter(data["Age Group"], data["10th grade"])
plt.scatter(data["Age Group"], data["11th grade"])
plt.scatter(data["Age Group"], data["High school graduate"])
plt.scatter(data["Age Group"], data["Some college, no degree"])
plt.scatter(data["Age Group"], data["Associate's degree, occupational"])
plt.scatter(data["Age Group"], data["Associate's degree, academic"])
plt.scatter(data["Age Group"], data["Bachelor's degree"])
plt.scatter(data["Age Group"], data["Master's degree"])
plt.scatter(data["Age Group"], data["Professional degree"])
plt.scatter(data["Age Group"], data["Doctoral degree"])
plt.show()
# %%
