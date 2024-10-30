import matplotlib.pyplot as plt
import numpy as np

# Function to read values from a text file
def read_values_from_file(file_path):
    with open(file_path, 'r') as file:
        values = [float(line.strip()) for line in file]
    return values

# Function to calculate moving average
def moving_average(values, window_size):
    return np.convolve(values, np.ones(window_size)/window_size, mode='valid')

# Path to your text file
file_path = 'loss2.txt'  # Change this to your file path

# Read values from the file
values = read_values_from_file(file_path)

# Generate x values (line numbers)
x_values = list(range(1, len(values) + 1))

# Calculate the moving average (adjust window size as needed)
window_size = 5  # You can change this value for more or less smoothing
smoothed_values = moving_average(values, window_size)

# Adjust x values for the smoothed data
x_smoothed = x_values[window_size - 1:]

# Create the line graph
plt.plot(x_smoothed, smoothed_values, marker='o')

# Add titles and labels
plt.title('Training Loss')
plt.xlabel('Epoch % 100')
plt.ylabel('Loss')

# Set y-axis limits
plt.ylim(0, 0.25)

# Show grid
plt.grid()

# Display the graph
plt.show()
