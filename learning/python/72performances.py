from time import time
mx = 6600 # max reached on author computer

t = time() # start time for the for loop
dmloop = []
for a in range(1, mx):
    for b in range(a, mx):
        dmloop.append(divmod(a, b))
print('for loop: {:.4f}s'.format(time() -t)) # elapsed time


t = time() # start time for the list comprehension
dmlist = [
    divmod(a, b) for a  in range(1, mx) for b in range(a, mx)
]
print('list comprehension: {:.4f}s'.format(time() -t))


t = time() # start time for the generator expression
dmgen = list(
    divmod(a, b) for a in range(1, mx) for b in range(a, mx)
)
print('generator expression: {:.4f}s'.format(time() -t))

# verify correctness of result and number of items in each list
print(dmloop == dmlist == dmgen, len(dmloop))
