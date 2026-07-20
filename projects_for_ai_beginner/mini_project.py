import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# data = {
#     "employee_Number": range(1, 21),
#     "employee_Name": [f'Employee_{i}' for i in range(1, 21)],
#     "department": np.random.choice(["IT", "Sales", "PR", "Backend", "Frontend"], 20),
#     "age": np.random.randint(25, 65, 20),
#     "salary": np.random.randint(25000, 30000000, 20),
#     "years_of_experience": np.random.randint(2, 20, 20)
# }

# df = pd.DataFrame(data)
# df.loc[10, 'salary'] = np.nan
# df.iloc[15, 2] = np.nan

# df = pd.concat([df, df.iloc[[2]]], ignore_index=True)


# df.to_csv(r"D:\Backend\Learning Python\employee.csv", index=False)
# print("the CSV file has been created.")


def cvs_analizer(filepath):
    print("="*50)
    print("CVS file Analize Report")
    print("="*50)
    df = pd.read_csv(filepath)

    print(f"the CVS file has {df.shape[0]} rows and {df.shape[1]} coloms\n")
    print(f"the coloms which are in the file are : {list(df.columns)}")
    print(df)

    return df


def check_data_quality(df):
    print("=="*50)
    print("Cecking the data quality of the CSV file")
    print("\n")

    missing = df.isnull().sum()
    percentage = (missing/len(df))*100

    for col in df.columns:
        if missing[col] > 0:
            print(
                f"{col} has {missing[col]} missing values. And the percentage of missing value is {percentage[col]:.1f}")
    if missing.sum() == 0:
        print("no missing value here....")

    duplicate = df.duplicated().sum()
    print(f"Duplicated rows {duplicate}")

    return missing, duplicate

    # print(missing)
    # print(percentage)


def cleaningData(df):
    print("Performing Data Cleaning...")
    df["salary"] = df['salary'].fillna(df["salary"].mean())
    df["department"] = df["department"].fillna('Unassigned')
    df = df.drop_duplicates()
    # print(df.groupby("department")["salary"].mean().round(2))
    print("Cleaning Done.\n\n")
    print("This data looks like after Cleaning..\n\n")
    print(df)

    return df


def outlier(df):
    mean_value = df["salary"].mean()
    std_value = df['salary'].std()
    lower_limit = mean_value - 2*std_value
    higher_limit = mean_value + 2*std_value

    outliers = df[(df["salary"] < lower_limit) | (
        df["salary"] > higher_limit)]

    print("=== Outlier Detector ===")
    if outliers.empty:
        print("No salary outliers found in the dataset.")
    else:
        print(outliers[["employee Name", "department", "salary"]])


def statistical_view(df):

    print("The Statistical Date Analysis\n\n")

    numerical_data = df.select_dtypes(include=[np.number]).columns

    for col in numerical_data:
        if col == "employee_Number":
            continue
        print(f"mean of {col} is {df[col].mean():.2f}")
        print(f"median of {col} is {df[col].median():.2f}")
        print(f"maximum of {col} is {df[col].max()}")
        print(f"minimum of {col} is {df[col].min()}")
        print(f"std of {col} is {df[col].std():.2f}")


def create_visualizations(df):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # ১. Salary distribution (histogram)
    # axes[0, 0].hist(df["salary"].dropna(), bins=10, color="steelblue")
    df["salary"].plot(kind="hist", ax=axes[0, 0], bins=10, color="steelblue")
    axes[0, 0].set_title("Salary Distribution")
    axes[0, 0].set_xlabel("Salary")

    # ২. Department-wise employee count (bar chart)
    df["department"].value_counts().plot(
        kind="bar", ax=axes[0, 1], color="coral")
    axes[0, 1].set_title("Department-wise Employee Count")

    # ৩. Age vs Salary (scatter - সম্পর্ক আছে কিনা দেখতে)
    axes[1, 0].scatter(df["age"], df["salary"], alpha=0.6)
    axes[1, 0].set_title("Age vs Salary")
    axes[1, 0].set_xlabel("Age")
    axes[1, 0].set_ylabel("Salary")

    # ৪. Experience distribution
    axes[1, 1].hist(df["years_of_experience"], bins=8, color="seagreen")
    axes[1, 1].set_title("Years of Experience Distribution")

    plt.tight_layout()
    plt.savefig("csv_analysis_report.png")
    print("\n📊 Visualization saved as 'csv_analysis_report.png'")
    plt.show()


def full_csv_analysis(filepath):
    df = cvs_analizer(filepath)
    print("\n\n\n\n")
    check_data_quality(df)
    print('\n\n\n\n')
    cleaned = cleaningData(df)
    print("\n\n\n\n")
    outlier(cleaned)
    print("\n\n\n\n")
    statistical_view(cleaned)
    print("\n\n\n\n")
    create_visualizations(cleaned)
    print("\n\n\n\n")
    print("data analysis completed")


filename = input("Enter the filePath for the CSV file:=")

df = full_csv_analysis(filename)
