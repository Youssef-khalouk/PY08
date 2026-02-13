

def main():
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("[KO] pandas could not be imported!")

    try:
        import requests
        print(f"[OK] requests ({requests.__version__}) - Network access ready")
    except ImportError:
        print("[KO] requests could not be imported!")

    try:
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
    except ImportError:
        print("[KO] matplotlib could not be imported!")


if __name__ == "__main__":
    main()

# $> python loading.py
# LOADING STATUS: Loading programs...
# Checking dependencies:
# [OK] pandas (2.1.0) - Data manipulation ready
# [OK] requests (2.31.0) - Network access ready
# [OK] matplotlib (3.7.2) - Visualization ready
# Analyzing Matrix data...
# Processing 1000 data points...
# Generating visualization...
# Analysis complete!
# Results saved to: matrix\_analysis.png}