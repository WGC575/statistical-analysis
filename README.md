# statistical-analysis

Codes for statistical anlaysis

significance.py provide a way to deal with statistical significance of a set of data using Games-Howell

#installation of rpy2
1. Install R, set your R_HOME (...\R\R-3.0.2\) and PATH (...\R\R-3.0.2\bin\x64)
2. Find the correct version of rpy2 you need in https://www.lfd.uci.edu/~gohlke/pythonlibs/
3. Move the file to the Python directory and install rpy2 with "pip install rpy2-......whl"
4. Set the R_USER (...\Python\Python36\site-packages\rpy2)
5. Restart your machine to get the configuration finalized

#Games-Howell Test
For usage, see https://pypi.org/project/squaad/
The proposed input should be:
Two groups of values, basically representing the same thing.
For example, the expected quality score of 10 products to the actual quality score of 10 real products
The G.H. posthoc test will give the result whether the two groups is significantly different. 
