import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# title, types, countries, release_years, genres, durations, ratings
n = 200
titles = [f'show_{i}' for i in range(1, n+1)]

types = np.random.choice(['TV', 'Movie'], n, p=[0.65, 0.35])

countries = np.random.choice(
    ['USA', 'UK', 'India', 'South Korea', 'Japan', np.nan], n, p=[0.65, 0.05, 0.15, 0.03, 0.02, 0.1])
release_years = np.random.randint(1990, 2026, n)

genre_pool = ["Drama", "Comedy", "Action",
              "Thriller", "Romance", "Documentary", "Horror"]

genres = [','.join(np.random.choice(
    genre_pool, np.random.randint(1, 4), replace=False)) for _ in range(n)]

durations = []

for i in range(n):
    if types[i] == 'TV':
        durations.append(f"{np.random.randint(1, 8)} Season" +
                         ("s" if np.random.randint(1, 8) > 1 else ""))
    if types[i] == "Movie":
        durations.append(f'{np.random.randint(70, 180)} min')

ratings = np.random.choice(["TV-MA", "TV-14", "PG-13", "R",
                           "TV-PG", np.nan], n, p=[0.3, 0.25, 0.15, 0.15, 0.05, 0.1])

df = pd.DataFrame({
    "title": titles,
    "type": types,
    "country": countries,
    "release_year": release_years,
    "rating": ratings,
    "duration": durations,
    "genre": genres
})

df.replace('nan', np.nan, inplace=True)

print(df.isnull().sum())
print(df.info())
print(df.shape)


print(df.head(10))


def cleaning_data(df):
    df = df.copy()
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna(df['rating'].mode()[0])


cleaning_data(df)


def year_trend(df):
    yearly = df.groupby(["release_year", "type"]).size().unstack(fill_value=0)
    print(yearly.tail(10))

    yearly.plot(kind="line", figsize=(10, 5), marker="o")
    plt.title("বছরের সাথে Content Release Trend")
    plt.xlabel("Year")
    plt.ylabel("Number")
    plt.legend(title="Type")
    plt.show()


# year_trend(df)


def movie_duration_in_min(df):
    movies = df[df['type'] == 'Movie'].copy()
    movies['movie_duration'] = movies['duration'].str.extract(
        r"(\d+)").astype(int)
    print(movies)


# movie_duration_in_min(df)
df['genre'] = df['genre'].str.split(",")

df = df.explode('genre')

popular = df.groupby('genre')['release_year'].mean(
).sort_values(ascending=False)
print(popular.head(5))

print(df.head(5))


def country_type_breakdown(df):
    """
    Pivot table ব্যবহার করে প্রতিটি দেশে Movie এবং TV Show এর সংখ্যা বের করে।
    """
    pivot = df.pivot_table(
        index="country",     # সারি (row) বরাবর দেশের নাম থাকবে
        columns="type",      # কলাম (column) বরাবর type (Movie/TV Show) থাকবে
        # এটি গুনে দেখবে কোনটিতে কয়টি ডেটা আছে (count-এর মতো কাজ করে)
        aggfunc="size",
        # যদি কোনো দেশে মুভি বা টিভি শো না থাকে, সেখানে ফাঁকা (NaN) এর বদলে 0 বসাবে
        fill_value=0
    )

    print(pivot)


country_type_breakdown(df)

tvs = df[df['type'] == 'TV'].copy()

tvs['season_count'] = tvs['duration'].str.extract(
    r"(\d+)").astype(int).reset_index(drop=True)
print(tvs.head(4))
