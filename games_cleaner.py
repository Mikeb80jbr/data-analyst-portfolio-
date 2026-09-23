import pandas as pd
df_games = pd.read_csv('games_description(in).csv')
print(df_games.head())
df_review = pd.read_csv('games_reviews(in).csv')
print(df_review.head())
df_revenue = pd.read_csv('games_revenue(in).csv')
print(df_revenue.head())
#merge df_games and df_review on 'game_id'
df_merged = pd.merge(df_games, df_review, on='game_id', how='left')
#merge df_merged and df_revenue on 'game_id'
df_final = pd.merge(df_merged, df_revenue, on='game_id', how='left')
print(df_final.head(200))
total_rows = len(df_final)
print(f"Total number of rows in the final merged DataFrame: {total_rows}")
#finding if the other tables are having more rows than the final merged table 
print(f"Number of rows in df_games: {len(df_games)}")
print(f"Number of rows in df_review: {len(df_review)}")
print(f"Number of rows in df_revenue: {len(df_revenue)}")
