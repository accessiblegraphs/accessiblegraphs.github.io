# Checks and installs all packages needed for UpdatePlots.py to run

import pip

def main():
    import_or_install("selenium")
    import_or_install("beautifulsoup4")
    import_or_install("matplotlib")
    import_or_install("Plotly")

    
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package]) 

if __name__ == '__main__':
    main()