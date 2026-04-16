import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 创建2x1的子图
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# ========== 1. 连续信号 ==========
t = np.linspace(0, 4*np.pi, 1000)  # 连续时间
cos_signal = np.cos(t)  # 余弦信号
exp_signal = np.exp(-0.5 * t) * np.sin(2*t)  # 指数衰减正弦信号

axes[0].plot(t, cos_signal, 'b-', linewidth=2, label='cos(t)')
axes[0].plot(t, exp_signal, 'g--', linewidth=2, label='e^{-0.5t}sin(2t)')
axes[0].set_xlabel('时间 t (s)')
axes[0].set_ylabel('幅度')
axes[0].set_title('连续信号示例')
axes[0].legend()
axes[0].grid(True)

# ========== 2. 离散信号 ==========
n = np.arange(-10, 11)  # 离散时间点
u_n = np.where(n >= 0, 1, 0)  # 单位阶跃信号 u[n]
delta_n = np.where(n == 0, 1, 0)  # 单位冲激信号 δ[n]

axes[1].stem(n, u_n, linefmt='r-', markerfmt='ro', basefmt='k-', label='u[n]')
axes[1].stem(n, delta_n, linefmt='b--', markerfmt='bo', basefmt='k-', label='δ[n]')
axes[1].set_xlabel('时间 n')
axes[1].set_ylabel('幅度')
axes[1].set_title('离散信号示例')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()