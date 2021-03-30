import matplotlib
import matplotlib.pyplot as plt
overs=[1,2,3,4,5,6,7,8,9,10]
india=[3,4,6,5,7,8,10,5,6,4]
australia=[5,6,8,9,10,12,4,6,8,8]
plt.plot(overs,india,'k--',label='india')
plt.plot(overs,australia)
plt.legend(['india','australia'])
plt.title('Runs scored by indian and australian teams in first 10 overs')
plt.xlabel('overs')
plt.ylabel('runs')
plt.show()
