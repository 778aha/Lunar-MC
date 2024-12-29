#!/usr/bin/env python3

import numpy as np
import random

# Pressure #bar
random_P = random.uniform(4000, 4000)
print("P", random_P)


# Temperature C
random_T = random.uniform(1100, 1300)
print("T", random_T)


#SiO2 TiO2 Al2O3 FeO MgO CaO wt.%
# Normalize to 100 wt.%
#a
LBS10 = [48.48, 6.18, 2.48, 21.16, 19.09, 2.62]
#b
LBS11 = [37.35, 15.24, 2.67, 28.99, 11.82, 3.94]
#c
aug_71597 = [49.39, 3.57, 4.85, 9.53, 14.60, 18.05 ]
#d
plag_15415 = [44.15, 0.00, 35.88, 0.07, 0.03, 19.88]

def generate_random_variables():
    # 随机生成c和d
    c = np.random.uniform(0, 0.15)
    d = np.random.uniform(0, 0.2)

    # 生成a和b，使得a + b = 1 - c - d
    remaining = 1 - c - d
    a = np.random.uniform(0, remaining)
    b = remaining - a
    
    return a, b, c, d

# 生成随机数
random_LBS10, random_LBS11, random_aug_71597, random_plag_15415 = generate_random_variables()

# 打印结果
print(f"random_LBS10 = {random_LBS10}")
print(f"random_LBS11 = {random_LBS11}")
print(f"random_aug_71597 = {random_aug_71597}")
print(f"random_plag_15415 = {random_plag_15415}")

# 计算随机组合
random_bulk = []
for i in range(len(LBS10)):
	random_bulk.append(LBS10[i]*random_LBS10+LBS11[i]*random_LBS11+aug_71597[i]*random_aug_71597+plag_15415[i]*random_plag_15415)

print(random_bulk)

# 生成输入列表字符串
input_list = f'Title: Exoplanets\n\
Initial Temperature: {random_T}\n\
Final Temperature: {random_T}\n\
Initial Pressure: {random_P}\n\
Final Pressure: {random_P}\n\
Increment Temperature: 0.00\n\
Increment Pressure: 0.00\n\
dp/dt: 0.00\n\
Log fO2 Path: “IW-1”\n\
Mode: Continuous Melting\n\
Initial Composition: SiO2 {random_bulk[0]}\n\
Initial Composition: TiO2 {random_bulk[1]}\n\
Initial Composition: Al2O3 {random_bulk[2]}\n\
Initial Composition: FeO {random_bulk[3]}\n\
Initial Composition: MgO {random_bulk[4]}\n\
Initial Composition: CaO {random_bulk[5]}\n\
Initial Composition: Fe2O3 {0}'


print(input_list)

fw = open('./input.txt','w')
fw.writelines(input_list)
fw.close()

fw= open('./random_bulk.txt', 'w')
fw.writelines(f'{random_bulk[0]} {random_bulk[1]} {random_bulk[2]} {random_bulk[3]} {random_bulk[4]} {random_bulk[5]}')
fw.close()

fw = open('./LBS10.txt','w')
fw.writelines(f'{random_LBS10}')
fw.close()

fw = open('./LBS11.txt','w')
fw.writelines(f'{random_LBS11}')
fw.close()

fw = open('./aug_71597.txt','w')
fw.writelines(f'{random_aug_71597}')
fw.close()

fw = open('./plag_15415.txt','w')
fw.writelines(f'{random_plag_15415}')
fw.close()