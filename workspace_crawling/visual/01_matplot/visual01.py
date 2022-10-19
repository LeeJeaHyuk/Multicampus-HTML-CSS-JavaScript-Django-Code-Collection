import matplotlib.pyplot as plt

# figure 생성 : 틀
fig = plt.figure()

# subplot 배치 : 틀 나누기
ax = fig.subplots()

ax.plot([1,2,3,4,5])

# 그래프 출력
plt.show()