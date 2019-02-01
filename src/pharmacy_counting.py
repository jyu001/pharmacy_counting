
import sys

def pharmacy_counting():
    dct = {}
    # input
    with open(sys.argv[1], 'r') as infile:
        # skip the first line: 
        next(infile)
        # read data line by line:
        for line in infile:
            # in case of special characters in drug name/ prescriber name: 
            # For example: 1285720516,GEBHARDT,KATHERINE,"PANCRELIPASE 5,000",2575.02
            # need to get rid of comma (,) between double quotes (")
            
            # first, find the index of double quotes
            pos_quotes = [pos for pos, char in enumerate(line) if char == '\"']
            if pos_quotes:
                # find the index of comma
                pos_comma = [pos for pos, char in enumerate(line) if char == ',']
                for i in range(len(pos_quotes)//2):
                    left, right = pos_quotes[i], pos_quotes[i+1]
                    for p in pos_comma: 
                        if p>left and p<right: line = line[:p] + '_' + line[p+1:]
            # split line
            lst = line.split(',')
            prescriber, drug, cost = (lst[1],lst[2]), lst[3], lst[4]
            # restore drug names
            drug.replace('_', ',')
            # update drug information, add up count of prescribers and total costs:
            # the dict has such structure: {drug: [Count(prescriber), Sum(cost), prescriber name]}
            if drug not in dct: dct[drug] = [0, 0, ('','')]
            dct[drug][1] += int(float(cost))
            # only update Count(prescriber) when prescriber name is new:
            if prescriber != dct[drug][2]:
                dct[drug][0] += 1
                dct[drug][2] = prescriber
            
    sorted_by_value = sorted(dct.items(), key=lambda kv: kv[1][1], reverse = True)
    # transform data into strings for output
    res = [x[0] + ',' + str(x[1][0]) + ',' + str(x[1][1]) for x in sorted_by_value]
    # write into output file
    with open(sys.argv[2], 'w') as outfile:
        outfile.write('drug_name,num_prescriber,total_cost\n')
        outfile.write('\n'.join(res))

if __name__ == "__main__":
    pharmacy_counting()