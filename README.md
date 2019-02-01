
# Problem Description: 
For each drug, find the total number of unique prescriber and the total costs, which must be listed in descending order based on the total costs and if there is a tie, drug name in ascending order. 


# Method:
Since the input data has been cleaned and organized, it is only needed to scan the entries and combine those with same prescriber name, and then count the unique entries and sum up the costs. To avoid duplication, I used a dictionary structure to store the data: {drug: [Count(prescriber), Sum(cost), prescriber name]}. 

### Things to notice:
#### 1. There are entries with comma ',' in drug names or prescriber names. For example: 
1285720516,GEBHARDT,KATHERINE,"PANCRELIPASE 5,000",2575.02

1316987928,"BERMAN, MD, PA",BRUCE,ALPRAZOLAM,76.4

Thus it is necessary to transfer those comma into underline before processing the data and restore it afterward. Specifically, we need to get rid of comma (,) between double quotes ("). 

#### 2. Sometimes there are multiple entries of a same kind of drug for one prescriber. In this case, the prescriber name should be checked in order to avoid overcalculating the number of unique prescribers. When the prescriber name is the same as the previous entry, only add the costs; in case of a new prescriber, also change the number of unique prescribers. 


## Please use run.sh to run the code, or use command:
python ./src/pharmacy_counting.py ./input/itcont.txt ./output/top_cost_drug.txt
