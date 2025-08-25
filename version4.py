0.5 -2.0 25 3
0.4 -1.5 28 5
0.2 -0.5 30 2

with open("inputs_multiple.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = a * t**2 + b * t + c
        print(f"a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")
