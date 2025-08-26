a = 0.5
b = -3
c = 28
t = 5  # e.g., 5th hour or 5th day

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")
