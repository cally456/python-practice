x=2
n=5
idx=1
total=0
for counter in range(1,n+1):
    series_elem = x ** idx
    if counter%2 == 0:
        #series_elem *= -1
        series_elem = -series_elem
    # print(series_elem)
    total += series_elem
    idx +=2
print(total)