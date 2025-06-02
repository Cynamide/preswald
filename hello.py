from preswald import connect, get_df

connect()  # Initialize connection to preswald.toml data sources
df = get_df("sample_csv")  # Load data

from preswald import query

sql = "SELECT * FROM sample_csv"
filtered_df = query(sql, "sample_csv")

from preswald import table, text

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

from preswald import plotly
import plotly.express as px

fig = px.scatter(df, x="job_title", y="salary_usd", color="category")
plotly(fig)
