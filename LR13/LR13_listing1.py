import time

start_time = time.time()
c=0

for i in range(10):

    for j in range(10):

        for l in range(10):

            for k in range(10):

                for m in range(10):

                    for n in range(10):

                        if i+j+l==k+m+n:

                            c=c+1


print(c)

end_time = time.time()
execution_time = end_time - start_time

print("Час виконання лістингу 1:", execution_time, "секунд")