# ITBA - Métodos Numéricos Avanzados - Grupo 10
Second Advanced Numerical Methods Project: Hear Beat Rate


## Getting Started
These instructions will install the development environment into your local machine.

### Prerequisites
1. Clone the repository
	```
	$ git clone https://github.com/lobo/mna-tp1.git
	```
2. Install Python3 and pip3
	#### MacOS
	A. Install packages
	```
	$ brew install python3
	```
	B. Update the ```PATH``` variable to use the Homebrew's python packages
	```
	$ echo 'export PATH="/usr/local/opt/python/libexec/bin:$PATH" # Use Homebrew python' >> ~/.bash_profile
	$ source ~/.bash_profile
	```  
	#### Ubuntu
	```
	$ sudo apt-get install python3.6 python3-pip
	```

## Usage

**IMPORTANT:** First of all, create a folder in the root of this project called `recolected_info`. 

There are four different ways of using this application. These are listed below:

1. To run the basic usage of this program, run: `python3 main.py [path_to_video]`. The output will be inserted in `recolected_info`.
2. To have a more exact representation, run: `python3 main.py [path_to_video] --filter true`. The output will be inserted in `recolected_info`.
2. To run the time window analyzer, run: `python3 ./time_window_analizer.py [path_to_video]`. The output will be displayed on the terminal.
3. To run the window size analyzer, run: `python3 ./window_size_analizer.py [path_to_video]`. The output will be displayed on the terminal.


## Authors
* [Axel Fratoni](https://github.com/axelfratoni)
* [Daniel Lobo](https://github.com/lobo)
* [Fernán Oviedo](https://github.com/foviedoITBA)
* [Gastón Rodríguez](https://github.com/gastonrod)

