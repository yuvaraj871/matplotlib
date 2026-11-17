
import matplotlib.pyplot as plt

# Create a 2x3 grid
fig, ax = plt.subplots(2, 3, figsize=(12, 9))

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 3. Horizontal Bar Chart
ax[0, 2].barh(x, y, color='orange')
ax[0, 2].set_title("Horizontal Bar Chart")
ax[0, 2].set_xlabel("Values")
ax[0, 2].set_ylabel("Categories")

# 1. Line Chart
ax[0, 0].plot(x, y, marker='^')
ax[0, 0].set_title("Line Chart")
ax[0, 0].set_xlabel("X Values")
ax[0, 0].set_ylabel("Y Values")
ax[0, 0].grid(True)

# 2. Bar Chart
ax[0, 1].bar(x, y)
ax[0, 1].set_title("Bar Chart")
ax[0, 1].set_xlabel("X Values")
ax[0, 1].set_ylabel("Y Values")


# 4. Pie Chart
subjects = ['Python', 'Java', 'C', 'SQL']
marks = [40, 30, 20, 10]

ax[1, 0].pie(marks, labels=subjects, autopct='%1.1f%%')
ax[1, 0].set_title("Pie Chart")

# 5. Scatter Plot
ax[1, 1].scatter(x, y)
ax[1, 1].set_title("Scatter Plot")
ax[1, 1].set_xlabel("X Values")
ax[1, 1].set_ylabel("Y Values")

# 6. Repeated Line Chart
ax[1, 2].plot(x, y, color='purple', marker='s')
ax[1, 2].set_title("Repeated Line Chart")
ax[1, 2].set_xlabel("X Values")
ax[1, 2].set_ylabel("Y Values")
ax[1, 2].grid(True)

# Adjust spacing
#plt.tight_layout()

# Display all charts
plt.show()
