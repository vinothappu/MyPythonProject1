# main.py
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create x values from 0 to 2*pi
    x = np.linspace(0, 2 * np.pi, 500)
    # Compute sine of x
    y = np.sin(x)

    # Plot
    plt.plot(x, y, label='sin(x)')
    plt.title("Sine Wave Plot")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()