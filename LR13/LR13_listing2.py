import time

start_time = time.time()


c=0

a=[0]*28

for i in range(10):

    for j in range(10):

        for l in range(10):

            a[i+j+l]=a[i+j+l]+1

S=0

for i in range(28):

    S=S+a[i]*a[i]

print(S)


end_time = time.time()
execution_time = end_time - start_time

print("Час виконання лістингу 2:", execution_time, "секунд")

