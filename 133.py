profits = [45, 67, 89, 23, 56]

for p in profits:
    if p < 30:
        label = "Loss"
    elif p < 60:
        label = "Low Margin"
    elif p < 80:
        label = "Healthy"
    else:
        label = "Peak"

    print(p, "=>", label)