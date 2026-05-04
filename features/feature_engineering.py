import pandas as pd

df = pd.read_csv("../data/logs.csv")

failed_logins = df[df['status'] == 'failed'].groupby('ip').size()
request_count = df.groupby('ip').size()

features = pd.DataFrame({
   'failed_logins': failed_logins,
   'request_count': request_count
}).fillna(0)

features.to_csv("features.csv")

print("Features created")