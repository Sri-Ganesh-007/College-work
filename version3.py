0.3
-2.5
26
4
with open("inputs_single.txt", "r") as f:
    lines = f.readlines()

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

T = a * t**2 + b * t + c
print(f"Predicted temperature at t={t}: {T:.2f}°C")
