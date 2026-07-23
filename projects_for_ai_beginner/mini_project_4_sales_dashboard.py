import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)


products = pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphone"],
    "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "price": [55000, 800, 1500, 12000, 2500]
})

dates = pd.date_range(start="2026-01-01", end="2026-03-31", freq="D")
orders = pd.DataFrame({
    "order_id": range(1, 101),
    "product_id": np.random.choice([101, 102, 103, 104, 105], 100),
    "quantity": np.random.randint(1, 5, 100),
    "order_date": np.random.choice(dates, 100)
})

# print(products)
# print(orders.head())


def dashboard(prducts, orders):
    df = orders.merge(prducts, on='product_id', how='left')

    df['total_amount'] = df['quantity'] * df['price']

    df['month'] = df['order_date'].dt.month
    df['weekday'] = df['order_date'].dt.day_name()
    print(df.head(10))

    print(f"Overall Revenue  = {df["total_amount"].sum()}")

    print("\n\n Monthly Sales \n\n")
    monthly_sales = df.groupby(['month', "category", 'product_name'])[
        'total_amount'].sum()
    print(monthly_sales)

    top_products = df.groupby('product_name')[
        "total_amount"].sum().sort_values(ascending=False)
    print(f"\n\nTop 3 Sold Products are \n {top_products.head(3)}\n\n\n")

    category_sales = df.groupby(
        'category')['total_amount'].sum().sort_values(ascending=False)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    top_products.plot(kind="bar", ax=axes[0], color="steelblue")
    axes[0].set_title("Product-wish Total Sales")
    axes[0].set_xlabel("Product Name")
    axes[0].set_ylabel("Total Amount")
    axes[0].tick_params(axis="x", rotation=45)

    category_sales.plot(kind="pie", ax=axes[1], autopct="%1.1f%%")
    axes[1].set_title("Category-wise Total Sales")

    plt.tight_layout()
    plt.show()


dashboard(products, orders)
