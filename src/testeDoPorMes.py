toMonth = [0,0,0,0,0,0,0,0,0,0,0,0]

record = [{"tempo_usado" : 1500, "mes" : '09' }, {"tempo_usado" : 100, "mes" : '05' }, {"tempo_usado" : 600, "mes" : '11' }]

for i in range(13):
    for rec in record:
        if int(rec["mes"]) == i:
            toMonth[i - 1] += rec["tempo_usado"]

print(toMonth, 'To month depois')