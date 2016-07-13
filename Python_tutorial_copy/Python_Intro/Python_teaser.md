
### PYTHON_teaser

In this tutorial we will see some of the probability based questions and their answers. Before that, lets understand what are the various terms and their concepts used in probability.

 * **Probability**: It is a possibility of outcome which may occur when we perform a random experiment.


 * **A random experiment**: Random experiment is a process that results in one of possible outcomes. The outcomes which can not be predicted with certainty.
Examples of such random experiment are flipping a coin, throwing a dice, drawing a card etc.


 * **Sample Space of a random experiment**: Sample space is a list of all possible outcomes of a random experiment. Sample space is denoted by S.


 * **An Event** : An event is a outcome of an experiment. It is a subset of sample space and denoted by upper case letter.


 * **Probability of an event happening** = (Number of ways an event can occur/ Total number of outcomes).

**Q.1 What is the AVERAGE VALUE if you threw a 6-sided die?** 


Answer:  For an experiment of a throw of single 6-sided die, the sample sapce S is
         S = {1, 2, 3, 4, 5, 6}.
        
Event A = Occurrence of number 1 on the face of a die = {1}.
Hence, probability of occurring number 1 on the face of a die = 1/6.
Similarly, probability of all other outcomes is same and it is 1/6.
        
Average value of all the possible outcomes of this experiment can be calculated in the following way:
        
Average value = (1 x 1/6)+ (2 x 1/6) + (3 x 1/6) + (4 x 1/6) + (5 x 1/6) + (6 x 1/6)
              = 21/6
              = 3.5

**Q.2 How many POSSIBLE DICE-THROW OUTCOMES are there if you threw a 6-sided die twice? Note that here getting a dice throw of 1 followed 2 is distinct from 2 followed by 1.**

Answer : Number of possible outcomes from a throw of single 6-sided die = 6.

First throw and second throw of a 6-sided die are independent of each other and so their outcomes too. Hence, for each outcome of 1st throw of a 6-sided die there will be 6 possible outcomes from a second throw of 6-sided die.
         
Therefore, Total number of POSSIBLE DICE-THROW OUTCOMES =
(Number of possible outcomes from a first throw of a die) X (Number of possible outcomes from a second throw of a die for each outcome of a first throw of a die) = 6x6 = 36.

The answer can be verified from the sample space given below.
The sample space S of this experiment is = 
         
{(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),

(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),

(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),

(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),

(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),

(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)}.

**Q.3 How many POSSIBLE DICE-THROW OUTCOMES are there if you threw a 6-sided die 10 times?**

Answer: From the answer to question 2 given above, we know that, for every throw of a single 6-sided die, the number of possible outcomes are 6. For each of these 6 outcomes from first throw there will be 6 independent possible outcomes for every subsequent throw of a single 6-sided die. Remember that each throw of a die is independent to other throw hence their outcomes also are independent.
So, in 10 throws of a single 6-sided die the possible outcomes = 6x6x6x6x6x6x6x6x6x6 = 6^10 = 60466176.

**Q.4 How many UNIQUE SUMS are there if you added the values of 2 throws of a 6-sided die?**

Answer: Consider the sample space S given in the answer to question 2.
From the sample space, we can see that **minimum sum is 2** from an event (1,1) and **maximum sum is 12** from an event (6,6).
The number of UNIQUE SUMS of outcomes of this experiment is between 2 and 12 (both 2 and 12 inclusive) which is 11.

You can arrive at this answer by using simplified formula,

**The number of UNIQUE SUMS for an experiment of throw of dice = (6xn)-(n-1)** = (6x2)-(2-1) = 12 -1 = 11. 

where n = Number of dice thrown at a time or number of times a die is thrown. 

**Q.5 How many UNIQUE SUMS are there if you added the values of 10 throws of a 6-sided die?**

Answer: For an experiment of 10 throws of a 6-sided die, the minimum sum will occur in the event (1,1,1,1,1,1,1,1,1,1) = 10
and the maximum sum will occur in the event (6,6,6,6,6,6,6,6,6,6) = 60. The sum of all other events will be between 10 and 60.

The number of UNIQUE SUMS of outcomes of this experiment is between 10 and 60(both 10 and 60 inclusive) which is 51.

Verifiy this answer using formula given in the answer to question 4.
The number of UNIQUE SUMS of outcomes of 10 throws of die = (6x10)-(10-1) = 60-1 = 51.

**Q.6 What is the most likely sum from 2 throws of a 6-sided die?**

Answer: Most likely sum from two throws of a 6-sided die is calculated using following formula:
        
**Most likely sum = N x (Average value of single throw of a 6-sided die)**

where N =  number of dice thrown concurrently or number of times a single die is thrown and Average value of single throw of a 6-sided die is 3.5 (refer answer to question 1)
                         
Therefore, Most likely sum = 2 X 3.5 = 7

Note: This method of calculating the most likely sum of an outcome is applicable only for an experiment of two or more throws of a 6-sided die that is N >= 2. In case of an experiment of one throw of a die, all the outcomes are eaqually likely to appear and the average value of a single throw is the most likely sum for single throw of a die experiment.                

**Q.7 What is the most likely sum from 100 throws of a 6-sided die?**

Answer : From the answer to question 6 above, 

Most likely sum from 100 throws of a 6-sided = 100 x 3.5 =350
