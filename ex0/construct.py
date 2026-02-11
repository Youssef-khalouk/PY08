import sys
import os
import site

# to get the python envirment run
#  python -m venv matrix_env

# to activate it ( switch the global envirment variable of python to this env)
# source matrix_env/bin/activate

# to change back the global env to the reall python run
# deactivate


def main():
    in_venv = sys.prefix != sys.base_prefix

    print("\nMATRIX STATUS: ", end='')
    if in_venv:
        print("Welcome to the construct\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment:", os.path.basename(sys.prefix))
        print("Environment Path:", sys.prefix)
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")

        site_packages_path = site.getsitepackages()[0]
        print("Package installation path:", site_packages_path)
    else:
        print("You're still plugged in\n")
        print("Current Python:", sys.executable)
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate     # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
