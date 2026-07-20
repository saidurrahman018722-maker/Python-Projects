import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "name": ["Rafi", "Nila", "Tanvir", "Mim", "Sadia", "Arif", "Priya", "Kabir"],
    "math": [30, 45, 92, 38, 45, 50, 38, 47],
    "science": [78, 52, 88, 41, 72, 65, 60, 95],
    "english": [90, 60, 85, 45, 80, 70, 58, 88]
}

df = pd.DataFrame(data)
print(df)


def add_total_and_add_avarage(df):
    cols = ['math', 'science', 'english']
    df["total"] = df[cols].sum(axis=1)
    df["avarage"] = df[cols].mean(axis=1).round(2)
    print(df)


add_total_and_add_avarage(df)


def assign_grade(number):
    if number >= 80:
        return "A"
    if number >= 60:
        return "B"
    if number <= 60 and number >= 50:
        return "C"
    if number >= 40:
        return "D"
    if number < 40:
        return "F"


df["grade"] = df["avarage"].apply(assign_grade)
print(df)


def check_pass_fail(df):
    subject_cols = ["math", "science", "english"]

    df["status"] = "Pass"
    for col in subject_cols:
        df.loc[df[col] < 40, "status"] = "Fail"
    return df


df = check_pass_fail(df)
print(df)


def class_summary(df):
    print("=" * 40)
    print("📊 CLASS SUMMARY")
    print("=" * 40)
    print(f"মোট Student: {len(df)}")
    print(f"Pass : {(df['status'] == 'Pass').sum()}")
    print(f"Fail : {(df['status'] == 'Fail').sum()}")
    print(f"\nClass Average: {df['avarage'].mean():.2f}")
    print(f"\nGrade Distribution:\n{df['grade'].value_counts()}")

    top_student = df.loc[df["avarage"].idxmax()]
    print(
        f"\n🏆 Top Student: {top_student['name']} (Average: {top_student['avarage']:.2f})")


class_summary(df)


def visualize_data(df):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    df["grade"].value_counts().sort_index().plot(
        kind="bar", ax=axes[0], color="steelblue")
    axes[0].tick_params(axis='x', rotation=0)
    axes[0].set_title("Grade Graph")

    df.plot(kind="bar", ax=axes[1], x="name",
                 y='avarage', color="coral")
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].set_title("Avarage Marks")

    # axes[1].bar(df["name"], df["avarage"], color="coral")
    # axes[1].set_title("Student-wise Avarage")
    # axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()


# visualize_data(df)

def top_student(df, subject):
    top_student_in_that_sub = df.loc[df[subject].idxmax()]
    return top_student_in_that_sub['name']


print(top_student(df, 'math'))
print(top_student(df, 'science'))
print(top_student(df, 'english'))

data = df.groupby('grade')['avarage'].mean().round(2)
print(data)
df['rank'] = df['avarage'].rank(ascending=False)


def tracks_the_weakest_sub(df):

    colomns = ['math', 'science', 'english']
    for col in colomns:
        print(f"the avarage of {col} is {df[col].mean():.2f}")
        if df[col].mean() < 50:
            print(
                f"Most of the sutdent got below 50 marks in this Sub the avarage in {col} is {df[col].mean():.2f}")


tracks_the_weakest_sub(df)
