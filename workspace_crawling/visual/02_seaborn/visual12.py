import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')

# 경험적 누적분포함수 (반복된 시행을 통해 확률 변수가 일정 값을 넘지 않을 확률을 유추)
sns.displot(data=penguins, x='bill_length_mm')

plt.show()


