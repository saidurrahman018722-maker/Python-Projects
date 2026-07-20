import matplotlib.pyplot as plt
import pandas as pd
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 130, 180, 200]

# plt.plot(months, sales)
# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales(IN Thousands)")
# # plt.show()

departments = ["Sales", "IT", "HR", "Marketing"]
employee_count = [45, 30, 15, 20]

# plt.bar(departments, employee_count)
# plt.title("The Employee Count")
# plt.xlabel("department")
# plt.ylabel("employee_Count")

# # plt.show()


# ages = [22, 25, 28, 22, 30, 35, 28, 40, 25, 22, 30, 28]

# plt.hist(ages, bins=5)   # bins = কতগুলো ভাগে ভাগ করবে
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Number of People")
# # plt.show()


# study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
# marks = [35, 40, 50, 55, 65, 70, 85, 90]

# plt.scatter(study_hours, marks)
# plt.title("Study time vs Mark")
# plt.xlabel("Study time (Hours)")
# plt.ylabel("Marks")
# plt.show()


# df = pd.DataFrame({
#     "month": ["Jan", "Feb", "Mar", "Apr"],
#     "sales": [120, 150, 130, 180]
# })

# # df.plot(x="month", y="sales", kind="line")
# # # plt.show()

# # Just call plot(kind="hist") directly on the column
# df["sales"].plot(kind="hist", bins=5, edgecolor="black")
# plt.title("Sales Frequency Distribution")
# plt.xlabel("Sales Amount")
# plt.ylabel("Frequency")
# plt.show()


# ১ row, ২ column-এ ২টা chart
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

axes[0].plot(months, sales)
axes[0].set_title("Line Chart")

axes[1].bar(departments, employee_count)
axes[1].set_title("Bar Chart")

plt.tight_layout()
plt.show()
