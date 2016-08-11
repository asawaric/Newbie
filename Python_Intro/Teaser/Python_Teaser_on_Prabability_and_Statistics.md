
## Python Teaser on Probability and Statistics 

In this teaser we will deal with problems on fair 6-sided dice. To start with, workout the exercise 1 using pen and paper:

####Note: An experiment of throwing two dice simultaneously is same as an experiment of throwing one die two times.

###Exercise 1: Finding all possible outcomes of a die throws.

1.How many Possible DICE THROW OUTCOMES are there if you threw a 6-sided die twice? Note that here getting a dice throw of 1 followed 2 i.e (1,2) is disctinct from 2 followed by 1 i.e.(2,1).

* Hint 1: Write the possible outcomes for 1 throw of a fair 6-sided die. For every outcome of 1 throw of a die, write the possible outcomes of second throw of a die.

* Hint 2: You can use list comprehenion to create a list of possible outcomes.

2.From above exercise, can you find a relation between number of throws of a die and number of all possible outcomes of those throws?

* If you have noticed the relation between a number of throws and its respective number of all possible outcomes then proceed :

3.How many Possible DICE THROW OUTCOMES are there if you threw 'n' dice simultaneously? Write a psuedocode to solve this problem.


4.Implement this pseudocode in python using only standard python functions. At this stage do not use any of the python modules to solve this problem. 

* Do this exercise for generating all possible outcomes of different number of dice throw. 
* What is the biggest number of dice for which you can generate all possible outcomes?

###Exercise 2: Finding unique sums of die throws.

####For following questions, write psuedocode and implement it in python using only standard python functions. 

1.How many UNIQUE SUMS are there if you added the values of 2 throws of a 6-sided die?

* Hint: Use function sum() to create list of sums from a list of possible outcomes.

2.Following the logic in exercise above find the number of UNIQUE SUMS for 'n' number of dice.

* Hint: Define a function that takes 'n' arguments and gives a list of unique sums.

###Exercise 3: Finding Average value of die throws.


#####For following questions, write psuedocode and implement it in python using only standard python functions. 

1.What is the most likely sum from 2-throws of a 6-sided die? Most likely sum is the average value of die throws.

* Hint: Average value = $\sum [Sum \times P(X = x)]$
        Where P(X = x) is probability of occurrence of Sum.

2.Write a python code for finding average value for 'n' dice throw.

* What is the biggest number of dice for which you can get Average value of throw? Note the time taken by computer to generate the Average vaue of a throw of the biggest number of dice.

* Can you explain why there is a long delay by computer in generating average value of throw for greater than 8 dice? 

###Exercise 4: Using Monte_Carlo method.

1.Write a pseudocode for defining 'Black_box' which takes following two input:
    1. 'n' number of dice
    2. 'm' number of throws
and generates sum and its respective probability for 'm' number of throws of 'n' number of dice.
    
2.Implement this pseudocode in python. Define a function named  'Black_box' to find the sums and probability of each sum from 'm' number of throws of 'n' number of dice.

* Hint: For each throw of 'n' dice, you will get a random outcome. Hence create list of random outcomes only. This will avoid creating list of all possible outcomes and circumvent the CPU memory bottleneck.

3.Using the Black_box defined above, find the most likely number of dice if their throws summed to 'k' (for example k = 51). 

* What is the likelihood for each possible number of dice given that sum = 'k' is observed? 




    
