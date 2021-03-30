import numpy as np
import matplotlib
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10]
india=[3,4,6,5,7,8,10,5,6,4]
x_index = np.arange(len(india))
width=0.25
australia=[5,6,8,9,10,12,4,6,8,8]
plt.bar(overs,x_index-width,width=width,label='india')
plt.legend(['india','australia'])
plt.title('Runs scored by indian and australian teams in first 10 overs')
plt.xlabel('overs')
plt.ylabel('runs')
plt.tight_layout()
plt.grid(True)
plt.show()
