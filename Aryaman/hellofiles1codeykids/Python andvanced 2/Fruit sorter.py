import matplotlib.pyplot as plt

for i in range(len(widths)):
    if labels[i] == "lemon":
        plt.scatter(widths[i], heights[i], color="gold")
    else:
        plt.scatter(widths[i], heights[i], color="green")

plt.xlabel("Width (cm)")
plt.ylabel("Height (cm)")
plt.title("The Fruit Universe")
plt.show()
print(len(widths), len(heights), len(labels))

