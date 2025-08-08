import matplotlib.pyplot as plt

# Data
labels = ['Admin & Licenses', 'App Development', 'Marketing', 'Equipment & Vehicles']
sizes = [10, 20, 30, 40]
colors = ['#D71940', '#F9BE3F', '#228BE6', '#4CAF50']

# Plot
fig, ax = plt.subplots()
fig.patch.set_alpha(0.0)  # Make figure background transparent
ax.set_facecolor('none')  # Make plot background transparent

wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct='%1.0f%%',
    startangle=90,
    wedgeprops=dict(width=0.4),
    textprops=dict(color="white", weight='bold')
)

# Set label text color to white
for text in texts:
    text.set_color("white")

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')

# Save with transparent background
plt.savefig("donut_chart_transparent.png", transparent=True)

# Show the plot
plt.show()
plt.show()
plt.show()
plt.show()
