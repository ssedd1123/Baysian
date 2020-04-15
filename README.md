This is a gaussian emulator and Baysiean analysis with PyMC <br />
 <br />
 
 Installation with anaconda
 ---
 
 1. Install anaconda/miniconda for python3 by following instruction on https://docs.conda.io/en/latest/miniconda.html.
 2. Update conda and add installation channel:
 ```
     $> conda update --all
     $> conda config --append channels conda-forge
 ```
 2. Go to /path/to/Bayesian-package and create virtual environment by running the following command:
 ```
     $> conda env create -f environment.yml
 ```
 3. Activate the environment:
 ```
     $> conda activate Bayesian2
 ```
 4. Start the program with 
 ```
     $> ./Bayesian.sh <number of cores>
 ```

 Running GUI on HPCC
 ---
 
 This section only talks about running GUI in HPCC. Some changes to the installation procedure are needed because some version of MPI are not compatible with HPCC. 
 
TBD
 
 Using GUI
 ---

TBD
