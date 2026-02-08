import pdb
import pandas as pd

# Load spreadsheet
df = pd.read_csv("with_rating.csv")

# Note this auto removes any pairs that don't have ratings.

# Compute correlation of each column with rating
correlations = df.corr(numeric_only=True)["rating"].drop("rating")

# Sort by absolute strength
correlations = correlations.reindex(correlations.sort_values(ascending=False).index)

print(correlations.head(50))

# import pandas as pd
# from scipy.stats import pearsonr

# df = pd.read_csv("data.csv")

# # Drop filename since it's not numeric
# numeric_df = df.drop(columns=["filename"])

# # Compute correlations + p-values for each sound event vs. rating
# results = []
# for col in numeric_df.drop(columns=["rating"]).columns:
#     r, p = pearsonr(numeric_df[col], numeric_df["rating"])
#     results.append((col, r, p))

# # Put in DataFrame, sorted by |correlation|
# results_df = pd.DataFrame(results, columns=["event", "correlation", "p_value"])
# results_df = results_df.reindex(results_df["correlation"].abs().sort_values(ascending=False).index)

# print(results_df)
