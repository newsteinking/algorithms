"""
When make reliable means, we need to neglect best and worst values.
For example, when making average score on athletes we need this option.
So, this algorithm affixes some percentage to neglect when making mean.
For example, if you suggest 20%, it will neglect the best 10% of values
and the worst 10% of values.
This algorithm takes an array and percentage to neglect. After sorted,
if index of array is larger or smaller than desired ratio, we don't
compute it.
Compleity: O(n)
"""
from algorithms.arrays import trimmean
import random

alist=[random.randint(1,10) for i in range(100)]

print(trimmean(alist,20))

### 박제준 3/25
