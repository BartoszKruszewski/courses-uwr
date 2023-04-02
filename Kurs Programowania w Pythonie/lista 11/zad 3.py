data = open("wyniki_wyborow.txt","r",encoding="utf-8").readlines()
results = {}
region_size = {}
parties = data[0].rstrip().split("\t")[3:]
for line in data[1:]:
    inline_data = line.rstrip().split("\t")
    local_results = {}
    for i, result in enumerate(inline_data[3:]):
        if result != "–":
            local_results[parties[i]] = float(result.replace(",","."))
        else:
            local_results[parties[i]] = 0
    results[inline_data[1]] = local_results
    print(inline_data,len(inline_data[0]))
    region_size[inline_data[1]] = int(inline_data[2])

sum_results = {}
for party in parties:
    sum_results[party] = 0

region_counter = 0
for region in results:
    region_counter += 1
    for party in results[region]:
        sum_results[party] += results[region][party] * region_size[region]

for party in sum_results:
    sum_results[party] /= region_counter

print(sum_results)