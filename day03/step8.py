import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)

x = np.linspace(0, 1, 30)
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.2, 30)   # a wave plus noise (noise size 0.2)

idx = rng.permutation(30)
train, test = idx[:20], idx[20:]        # 20 dots to learn from, 10 hidden

xs = np.linspace(0, 1, 200)
plt.figure(figsize=(13, 4))

for i, d in enumerate([1, 3, 15]):
    p = np.polynomial.Polynomial.fit(x[train], y[train], d)
    mse_train = np.mean((p(x[train]) - y[train]) ** 2)
    mse_test = np.mean((p(x[test]) - y[test]) ** 2)
    print(f"degree {d:2d}: train error {mse_train:.3f}   test error {mse_test:.3f}")

    plt.subplot(1, 3, i + 1)
    plt.scatter(x[train], y[train], c="blue", label="train")
    plt.scatter(x[test], y[test], c="red", label="test")
    plt.plot(xs, p(xs), c="green")
    plt.ylim(-2, 2)
    plt.title(f"degree {d}")
    plt.legend()

plt.show()