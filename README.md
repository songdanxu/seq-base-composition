# seq-base-composition
### fuction
You can use this script to calcaulate the overall base composition and (A+T) or (C+G) bias.
### example
In the command line interface,enter the following command.
~~~shell
python3 seq_base_composition.py --input path/1.fasta --output path/1.txt
~~~
### remark
This script fuction is not perfect yet. I currently think of three areas that need to be improved.<br>
First, only one sequence can be passed in, how to process multiple lines,this a problem;<br>
Second, the base composition of the incoming sequence must be clear, if there are N bases, it will affect the result, i haven't figured out how to judge N bases and fuzzy bases;<br>
Third, i am going to pass in parameters to select the number of decimal places.
