def frequency_analysis(line):
    frequency_data={}
    for x in line:
        frequency_data[x]=frequency_data.get(x,0) + 1
    end = sorted(frequency_data.keys(),key = lambda x: frequency_data[x],reverse=True)
    frequency = {}
    for x in end:
        frequency[x]=frequency_data[x]
    return frequency
print(frequency_analysis(input()))