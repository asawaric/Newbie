
## Python Teaser on Probability and Statistics 

In this teaser we will deal with problems on fair six-sided dice. The goal of this teaser is to write a Python code to find the likelihood for each possible number of dice given the specific sum is observed. This task is mentioned in question 3 and 4 of exercise 4. In order to achieve this final goal, workout exercise 1 through 3 which will build up your understanding of logical steps to be followed that are required to write a code for the final goal. 

To start with, workout exercise 1 using pen and paper.

#### Note: Throwing two dice simultaneously or one after another is the same as an experiment of throwing one die twice.

### Exercise 1: Finding possible outcomes of die throws.

1. How many possible die throw outcomes are there if you threw a six-sided die twice? Note that here getting a die throw of 1 followed 2 (i.e [1, 2]) is distinct from 2 followed by 1 (i.e.[2, 1]).

   * Hint 1: The outcome of one die throw has no effect on the outcome of another die throw. Hence die throws are independent.

   * Hint 2: Use list comprehension to create a list of possible outcomes.

2. From the above exercise, can you find a relation between the number of die throws and the number of possible outcomes of these throws?

3. How many possible die throw outcomes are there if you threw *n* dice simultaneously? Write a pseudocode to solve this problem?

   * Hint1 : Following is an example of a pseudocode to wrtie a possible outcomes of *n* die throws:
           
           
            1. Write an outcome of one die throw.

            2. For given number of dice

                   Loop to create possible outcomes by adding all the outcomes of one die throw to each outcome of outcomes of one die throw. 

4. Implement this pseudocode in Python using only standard Python functions. Do not import any of the Python modules to solve this problem. 

   * Hint 2: Use list comprehension to create a list of outcomes of die throws.

5. Do this exercise for generating all possible outcomes of different number of dice throw. 

6. What is the biggest number of dice for which you can generate possible outcomes?

### Exercise 2: Finding unique sums of die throws.
    This exercise makes use of the sample space created in exercise 1 to find the unique sums of die throws.

#### For the following questions, write a pseudocode and implement it in Python using only standard Python functions. 

1. How many unique sums are there if you added the values of two throws of a six-sided die?

   * Hint: Use function sum() to sum the outcomes and create a list of sums from a list of possible outcomes.

2. Following the logic in the above exercise find the number of unique sums for *n* number of dice.

   * Hint: Define a function that takes *n* arguments and gives a list of unique sums.

### Exercise 3: Finding the average value of sum of outcomes of die throws.
    This exercise is a self-check of your understanding of pseudocode and its implementation in Python.

#### For following questions, write a pseudocode and implement it in Python using only standard Python functions. 

1. What is the most likely sum from two-throws of a six-sided die? Most likely sum is the average value of sums of outcomes of die throws.

   * Hint: $$Average value = \sum\limits_{S} [S \times P(S)]$$
           ;Where S is a sum and P(S) is the probability of occurrence of a sum.

2. Write a Python code for finding average value of sums of *n* dice throw.

3. What is the biggest number of dice for which you can get the average value of sums of *n* throws? Note the time taken by computer to generate the average value of sums of throw of the biggest number of dice.

4. Can you explain why it took longer time by computer in generating the average value of a throw for greater than 8 dice? 

### Exercise 4: Using the Monte Carlo method.

1. Write a pseudocode for defining *Black_box* which takes following two inputs:
    1. *n* number of dice.
    2. *m* number of throws.

   and generates sum and its respective probability for *m* number of throws of *n* number of dice.
    
2. Implement this pseudocode in Python. 

   * Hint: For each throw of *n* dice, you will get a random outcome. Hence create a list of only random outcomes. This will avoid creating a list of all outcomes and circumvent the CPU memory bottleneck.

3. Using the function *Black_box* defined above, find the most likely number of dice if their throws summed to *k* (for example k = 51). 

4. What is the likelihood for each possible number of dice given that sum = *k* is observed? 




    
