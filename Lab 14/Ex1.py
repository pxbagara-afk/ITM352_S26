
import matplotlib.pyplot as plt

def check_packages(packages):
    print("Checking package status...\n" + "-"*30)
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} is installed.")
        except ImportError:
            print(f"❌ {package} is NOT installed.")

# List of packages to verify
required_libs = ['scipy', 'statsmodels', 'matplotlib']

if __name__ == "main":
    check_packages(required_libs)

    
# 1. Define the first set of x and y values
x1 = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]

# 2. Define a second set of x and y values
x2 = [1, 2, 3, 4, 5]
y2 = [15, 20, 35, 30, 35]

# 3. Plot the first set as a line graph and a scatter plot
plt.plot(x1, y1, label='Series 1 (Line)', color='blue')
plt.scatter(x1, y1, color='blue', marker='o') # Scatter points for first set

# 4. Add the second set as a line graph
plt.plot(x2, y2, label='Series 2 (Line)', color='red', linestyle='--')

# 5. Add a title and axis labels
plt.title('Comparison between two data')
plt.xlabel('X Axis (Units)')
plt.ylabel('Y Axis (Value)')

# Add a legend to distinguish the lines
plt.legend()

# Display the plot
plt.show()