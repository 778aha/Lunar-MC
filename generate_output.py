

# Pressure Temperature mass SiO2 TiO2 Al2O3 Fe2O3 FeO MgO CaO 
fr_liq = open('./Liquid_comp_tbl.txt','r').readlines()
P = fr_liq[4].split()[0]
T = float(fr_liq[4].split()[1]) - 273.16
liqwt = fr_liq[4].split()[2]
liq_SiO2 = fr_liq[4].split()[3]
liq_TiO2 = fr_liq[4].split()[4]
liq_Al2O3 = fr_liq[4].split()[5]
liq_Fe2O3 = fr_liq[4].split()[6]
liq_FeO = fr_liq[4].split()[7]
liq_MgO = fr_liq[4].split()[8]
liq_CaO = fr_liq[4].split()[9]

fr_LBS10 = open('./LBS10.txt','r').readlines()
LBS10 = fr_LBS10[0].split()[0]
fr_LBS11 = open('./LBS11.txt','r').readlines()
LBS11 = fr_LBS11[0].split()[0]
fr_aug_71597 = open('./aug_71597.txt','r').readlines()
aug_71597 = fr_aug_71597[0].split()[0]
fr_plag_15415 = open('./plag_15415.txt','r').readlines()
plag_15415 = fr_plag_15415[0].split()[0]


# SiO2 TiO2 Al2O3 Fe2O3 FeO MgO CaO 
fr_starting = open('./random_bulk.txt','r').readlines()
SiO2 = fr_starting[0].split()[0]
TiO2 = fr_starting[0].split()[1]
Al2O3 = fr_starting[0].split()[2]
FeO = fr_starting[0].split()[3]
MgO = fr_starting[0].split()[4]
CaO = fr_starting[0].split()[5]


tip = True

if float(liq_SiO2)<38.12 or float(liq_SiO2)>42.12:
 	tip = False
if float(liq_TiO2)<8.38 or float(liq_TiO2)>13.38:
 	tip = False
if float(liq_Al2O3)<7.28 or float(liq_Al2O3)>11.28:
 	tip = False
if float(liq_FeO)<17.07 or float(liq_FeO)>21.07:
 	tip = False
if float(liq_MgO)<6.12 or float(liq_MgO)>10.12:
	tip = False
if float(liq_CaO)<9.01 or float(liq_CaO)>13.01:
 	tip = False

if tip:
	fw = open('./sum_output_true.txt','a+')
	fw.writelines(f'{P} {T} {LBS10} {LBS11} {aug_71597} {plag_15415} {liqwt} {liq_SiO2} {liq_TiO2} {liq_Al2O3} {liq_Fe2O3} {liq_FeO} {liq_MgO} {liq_CaO}\n')
	fw.close()
	fw = open('./sum_starting_true.txt','a+')
	fw.writelines(f'{SiO2} {TiO2} {Al2O3} {FeO} {MgO} {CaO}\n')
	fw.close()

else:
	fw = open('./sum_output_false.txt','a+')
	fw.writelines(f'{P} {T}  {LBS10} {LBS11} {aug_71597} {plag_15415} {liqwt} {liq_SiO2} {liq_TiO2} {liq_Al2O3} {liq_Fe2O3} {liq_FeO} {liq_MgO} {liq_CaO}\n')
	fw.close()
	fw = open('./sum_starting_false.txt','a+')
	fw.writelines(f'{SiO2} {TiO2} {Al2O3} {FeO} {MgO} {CaO}\n')
	fw.close()