def find_maxima (a):
    maxima = []
    index = []
    n = len(a)
    for i in range(n):
        if a[0] > a[1]:
            maxima.append(a[0])
            index.append(i)
        elif i == n - 1 :
            if a[-1] > a[-2]:
                maxima.append(a[-1])
                index.append(i)
        else:
            if a[i] >=a[i-1] and a[i]>a[i+1]:
                maxima.append(a[i])
                index.append(i)
                