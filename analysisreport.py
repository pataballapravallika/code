import matplotlib.pyplot as plt
# given data
x = ['United States', 'China', 'United Kingdom', 'Japan', 'Germany', 'France', 'India', 'Canada', 'Australia', 'South Korea']
y = [12.4, 12.4, 11.9, 8.8, 10.6, 9.9, 23.3, 15.2, 9.9, 9.7]
# Create a line plot
plt.plot(x, y)
# Add labels and title
plt.xlabel('Country')
plt.ylabel('YoY Growth (2020-2023) (%)')
plt.title('E-commerce YoY Growth by Country')
# Rotate x-axis labels if needed
plt.xticks(rotation=45)
# Display the plot
plt.show()
