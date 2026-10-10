import pandas as pd
import numpy as np
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

combine=[]
for i in range(16):
    year=2000+i
    filename=str(year)+"_combine.csv"
    combine.append(pd.read_csv(filename))

playernames=[]
position=[]
yd40=[]
vert=[]
bench=[]
broadjump=[]
cone_3=[]
shuttle=[]
drafted=[]

#combine stats + performance stat(receiving yards) for WR position will be stored in these arrays
yd40_wr=[]
vert_wr=[]
bench_wr=[]
broadjump_wr=[]
cone_3_wr=[]
shuttle_wr=[]
draftposition_wr=[]
performance_wr=[]

#combine stats+performance stat() for RB position will be stored in these arrays
yd40_rb=[]
vert_rb=[]
bench_rb=[]
broadjump_rb=[]
cone_3_rb=[]
shuttle_rb=[]
draftposition_rb=[]
performance_rb=[]

for i in range(16):
    indexlist=[]
    combineadd=combine[i]
    playernames_new=combineadd["Player"].values.astype(str)
    position_new=combineadd["Pos"].values.astype(str)
    yd40_new=combineadd["40yd"].values
    vert_new=combineadd["Vertical"].values
    bench_new=combineadd["Bench"].values
    broadjump_new=combineadd["Broad Jump"].values
    cone_3_new=combineadd["3Cone"].values
    shuttle_new=combineadd["Shuttle"].values
    drafted_new=combineadd["Drafted (tm/rnd/yr)"].values
    for j in range(len(playernames_new)):
        if  math.isnan(yd40_new[j]) or math.isnan(vert_new[j]) or math.isnan(bench_new[j]) or math.isnan(broadjump_new[j]) or math.isnan(cone_3_new[j]) or math.isnan(shuttle_new[j]) or not isinstance(drafted_new[j],str): 
            indexlist.append(j)
    
    playernames_new=np.delete(playernames_new,indexlist)
    position_new=np.delete(position_new,indexlist)
    yd40_new=np.delete(yd40_new,indexlist)
    vert_new=np.delete(vert_new,indexlist)
    bench_new=np.delete(bench_new,indexlist)
    broadjump_new=np.delete(broadjump_new,indexlist)
    cone_3_new=np.delete(cone_3_new,indexlist)
    shuttle_new=np.delete(shuttle_new,indexlist)
    drafted_new=np.delete(drafted_new,indexlist)

    playernames.append(playernames_new)
    position.append(position_new)
    yd40.append(yd40_new)
    vert.append(vert_new)
    bench.append(bench_new)
    broadjump.append(broadjump_new)
    cone_3.append(cone_3_new)
    shuttle.append(shuttle_new)
    drafted.append(drafted_new)

# qbstats=[]
# for i in range(16):
#     year=2000+i
#     filename=str(year)+"_qbstats.csv"
#     qbstats.append(pd.read_csv(filename))

wrstats=[]
for i in range(16):
    year=2000+i
    filename=str(year)+"_wrstats.csv"
    wrstats.append(pd.read_csv(filename))

rbstats=[]
for i in range(16):
    year=2000+i
    filename=str(year)+"_rushingstats.csv"
    rbstats.append(pd.read_csv(filename))

for i in range(16):
    #qbstats_check=qbstats[i]
    #qb_names=qbstats_check["Player"].values
    #qb_pyards=qbstats_check["Yds"].values
    wrstats_check=wrstats[i]
    wr_names=wrstats_check["Player"].values
    wr_yards=wrstats_check["Yds▼"].values
    rbstats_check=rbstats[i]
    rb_names=rbstats_check["Player"].values
    rb_yards=rbstats_check["Yds"].values
    
    for j, char1 in enumerate(playernames[i]):
        # if position[i][j]=="QB":
        #     for k, char2 in enumerate(qb_names):
        #         if char1==char2:
        #             counterslash=0
        #             index1=0
        #             counter=0
        #             while counterslash<2:
        #                 if drafted[i][j][index1]=="/":
        #                     counterslash+=1
        #                 index1+=1
        #             index1+=1
        #             index2=index1
        #             while counter==0:
        #                 if drafted[i][j][index2]=="r" or drafted[i][j][index2]=="s" or drafted[i][j][index2]=="t":
        #                     counter=1
        #                 else:
        #                     index2+=1
        #             draftposition=drafted[i][j][index1:index2]
        #             break
        if position[i][j]=="WR":
            for k, char2 in enumerate(wr_names):
                if char1==char2:
                    counterslash=0
                    index1=0
                    counter=0
                    while counterslash<2:
                        if drafted[i][j][index1]=="/":
                            counterslash+=1
                        index1+=1
                    index1+=1
                    index2=index1
                    while counter==0:
                        if drafted[i][j][index2]=="p":
                            counter=1
                        else:
                            index2+=1
                    index2=index2-3
                    draftposition=drafted[i][j][index1:index2]
                    draftposition=int(draftposition)
                    yd40_wr.append(yd40[i][j])
                    vert_wr.append(vert[i][j])
                    bench_wr.append(bench[i][j])
                    broadjump_wr.append(broadjump[i][j])
                    cone_3_wr.append(cone_3[i][j])
                    shuttle_wr.append(shuttle[i][j])
                    draftposition_wr.append(draftposition)
                    performance_wr.append(wr_yards[k])
                    break
        elif position[i][j]=="RB":
            for k, char2 in enumerate(rb_names):
                if char1==char2:
                    counterslash=0
                    index1=0
                    counter=0
                    while counterslash<2:
                        if drafted[i][j][index1]=="/":
                            counterslash+=1
                        index1+=1
                    index1+=1
                    index2=index1
                    while counter==0:
                        if drafted[i][j][index2]=="p":
                            counter=1
                        else:
                            index2+=1
                    index2=index2-3
                    draftposition=drafted[i][j][index1:index2]
                    draftposition=int(draftposition)
                    yd40_rb.append(yd40[i][j])
                    vert_rb.append(vert[i][j])
                    bench_rb.append(bench[i][j])
                    broadjump_rb.append(broadjump[i][j])
                    cone_3_rb.append(cone_3[i][j])
                    shuttle_rb.append(shuttle[i][j])
                    draftposition_rb.append(draftposition)
                    performance_rb.append(rb_yards[k])
                    break        

        
def linear_fit(metric,m,c):
    return m*metric+c

def r2(performance,predicted):
    ss_res=np.sum((performance-predicted)**2)
    ss_tot=np.sum((performance-np.mean(performance))**2)
    r2=1-ss_res/ss_tot
    return r2

k0=[0,0,0,0,0,0,0]
alpha=0.00000001
length_wr=len(yd40_wr)
for i in range(int(1E6)):
    metric=np.ones(length_wr)*k0[0]+np.multiply(yd40_wr,k0[1])+np.multiply(vert_wr,k0[2])+np.multiply(bench_wr,k0[3])+np.multiply(broadjump_wr,k0[4])+np.multiply(cone_3_wr,k0[5])+np.multiply(shuttle_wr,k0[6])
    delta=performance_wr-metric
    dL=[0,0,0,0,0,0,0]
    dL[0]=-np.mean(delta)
    dL[1]=-np.mean(delta*yd40_wr)
    dL[2]=-np.mean(delta*vert_wr)
    dL[3]=-np.mean(delta*bench_wr)
    dL[4]=-np.mean(delta*broadjump_wr)
    dL[5]=-np.mean(delta*cone_3_wr)
    dL[6]=-np.mean(delta*shuttle_wr)
    k0=k0-np.multiply(alpha,dL)

k1=[0,0,0,0,0,0,0,0]
alpha=0.00000001
for i in range(int(1E6)):
    metric_new=np.ones(length_wr)*k1[0]+np.multiply(yd40_wr,k1[1])+np.multiply(vert_wr,k1[2])+np.multiply(bench_wr,k1[3])+np.multiply(broadjump_wr,k1[4])+np.multiply(cone_3_wr,k1[5])+np.multiply(shuttle_wr,k1[6])+np.multiply(draftposition_wr,k1[7])
    delta=performance_wr-metric_new
    dL=[0,0,0,0,0,0,0,0]
    dL[0]=-np.mean(delta)
    dL[1]=-np.mean(delta*yd40_wr)
    dL[2]=-np.mean(delta*vert_wr)
    dL[3]=-np.mean(delta*bench_wr)
    dL[4]=-np.mean(delta*broadjump_wr)
    dL[5]=-np.mean(delta*cone_3_wr)
    dL[6]=-np.mean(delta*shuttle_wr)
    dL[7]=-np.mean(delta*draftposition_wr)
    k1=k1-np.multiply(alpha,dL)

k2=[0,0,0,0,0,0,0]
alpha=0.00000001
length_rb=len(yd40_rb)
for i in range(int(1E6)):
    metric=np.ones(length_rb)*k2[0]+np.multiply(yd40_rb,k2[1])+np.multiply(vert_rb,k2[2])+np.multiply(bench_rb,k2[3])+np.multiply(broadjump_rb,k2[4])+np.multiply(cone_3_rb,k2[5])+np.multiply(shuttle_rb,k2[6])
    delta=performance_rb-metric
    dL=[0,0,0,0,0,0,0]
    dL[0]=-np.mean(delta)
    dL[1]=-np.mean(delta*yd40_rb)
    dL[2]=-np.mean(delta*vert_rb)
    dL[3]=-np.mean(delta*bench_rb)
    dL[4]=-np.mean(delta*broadjump_rb)
    dL[5]=-np.mean(delta*cone_3_rb)
    dL[6]=-np.mean(delta*shuttle_rb)
    k2=k2-np.multiply(alpha,dL)

k3=[0,0,0,0,0,0,0,0]
alpha=0.00000001
for i in range(int(1E6)):
    metric_new=np.ones(length_rb)*k3[0]+np.multiply(yd40_rb,k3[1])+np.multiply(vert_rb,k3[2])+np.multiply(bench_rb,k3[3])+np.multiply(broadjump_rb,k3[4])+np.multiply(cone_3_rb,k3[5])+np.multiply(shuttle_rb,k3[6])+np.multiply(draftposition_rb,k3[7])
    delta=performance_rb-metric_new
    dL=[0,0,0,0,0,0,0,0]
    dL[0]=-np.mean(delta)
    dL[1]=-np.mean(delta*yd40_rb)
    dL[2]=-np.mean(delta*vert_rb)
    dL[3]=-np.mean(delta*bench_rb)
    dL[4]=-np.mean(delta*broadjump_rb)
    dL[5]=-np.mean(delta*cone_3_rb)
    dL[6]=-np.mean(delta*shuttle_rb)
    dL[7]=-np.mean(delta*draftposition_rb)
    k3=k3-np.multiply(alpha,dL)

print("Values for 2000-2015")
print("WR R2 values")
draftposition_wr=np.array(draftposition_wr,dtype=float)
parameters_pos, covariant_matrix_pos=curve_fit(linear_fit, draftposition_wr, performance_wr)
m_pos_wr=parameters_pos[0]
c_pos_wr=parameters_pos[1]
fit_pos_wr=m_pos_wr*draftposition_wr+c_pos_wr
r2_wr_pos=r2(performance_wr,fit_pos_wr)

plt.figure()
print("Draft Position: ", r2_wr_pos)
plt.scatter(draftposition_wr, performance_wr)
plt.plot(draftposition_wr,fit_pos_wr)
plt.xlabel("Draft Position for WR")  
plt.ylabel("Receiving Yards for WR")

fit_metric_wr=np.ones(length_wr)*k0[0]+np.multiply(yd40_wr,k0[1])+np.multiply(vert_wr,k0[2])+np.multiply(bench_wr,k0[3])+np.multiply(broadjump_wr,k0[4])+np.multiply(cone_3_wr,k0[5])+np.multiply(shuttle_wr,k0[6])
metric=fit_metric_wr-np.ones(length_wr)*k0[0]
r2_wr_metric=r2(performance_wr,fit_metric_wr)

plt.figure()
print("Metric: ", r2_wr_metric)
plt.scatter(metric, performance_wr)
plt.plot(metric,fit_metric_wr)
plt.xlabel("Metric for WR")  
plt.ylabel("Receiving Yards for WR")


fit_metric_new_wr=np.ones(length_wr)*k1[0]+np.multiply(yd40_wr,k1[1])+np.multiply(vert_wr,k1[2])+np.multiply(bench_wr,k1[3])+np.multiply(broadjump_wr,k1[4])+np.multiply(cone_3_wr,k1[5])+np.multiply(shuttle_wr,k1[6])+np.multiply(draftposition_wr,k1[7])
metric_new=fit_metric_new_wr-np.ones(length_wr)*k1[0]
r2_wr_metric_new=r2(performance_wr,fit_metric_new_wr)

plt.figure()
print("New Metric: ", r2_wr_metric_new)
plt.scatter(metric_new, performance_wr)
plt.plot(metric_new,fit_metric_new_wr)
plt.xlabel("New Metric for WR")  
plt.ylabel("Receiving Yards for WR")

#RB
print("RB R2 values")
draftposition_rb=np.array(draftposition_rb,dtype=float)
parameters_pos, covariant_matrix_pos=curve_fit(linear_fit, draftposition_rb, performance_rb)
m_pos_rb=parameters_pos[0]
c_pos_rb=parameters_pos[1]
fit_pos_rb=m_pos_rb*draftposition_rb+c_pos_rb
r2_rb_pos=r2(performance_rb,fit_pos_rb)

plt.figure()
print("Draft Position: ", r2_rb_pos)
plt.scatter(draftposition_rb, performance_rb)
plt.plot(draftposition_rb,fit_pos_rb)
plt.xlabel("Draft Position for RB")  
plt.ylabel("Rushing Yards for RB")

fit_metric_rb=np.ones(length_rb)*k2[0]+np.multiply(yd40_rb,k2[1])+np.multiply(vert_rb,k2[2])+np.multiply(bench_rb,k2[3])+np.multiply(broadjump_rb,k2[4])+np.multiply(cone_3_rb,k2[5])+np.multiply(shuttle_rb,k2[6])
metric=fit_metric_rb-np.ones(length_rb)*k2[0]
r2_rb_metric=r2(performance_rb,fit_metric_rb)

plt.figure()
print("Metric: ", r2_rb_metric)
plt.scatter(metric, performance_rb)
plt.plot(metric,fit_metric_rb)
plt.xlabel("Metric for RB")  
plt.ylabel("Rushing Yards for RB")

fit_metric_new_rb=np.ones(length_rb)*k3[0]+np.multiply(yd40_rb,k3[1])+np.multiply(vert_rb,k3[2])+np.multiply(bench_rb,k3[3])+np.multiply(broadjump_rb,k3[4])+np.multiply(cone_3_rb,k3[5])+np.multiply(shuttle_rb,k3[6])+np.multiply(draftposition_rb,k3[7])
metric_new=fit_metric_new_rb-np.ones(length_rb)*k3[0]
r2_rb_metric_new=r2(performance_rb,fit_metric_new_rb)

plt.figure()
print("New Metric: ", r2_rb_metric_new)
plt.scatter(metric_new, performance_rb)
plt.plot(metric_new,fit_metric_new_rb)
plt.xlabel("New Metric for RB")  
plt.ylabel("Rushing Yards for RB")

#Using the lines of best fit to predict performances for the years 2016-2019
    
combine=[]
wrstats=[]
rbstats=[]

playernames=[]
position=[]
yd40=[]
vert=[]
bench=[]
broadjump=[]
cone_3=[]
shuttle=[]
drafted=[]

yd40_wr=[]
vert_wr=[]
bench_wr=[]
broadjump_wr=[]
cone_3_wr=[]
shuttle_wr=[]
draftposition_wr=[]
performance_wr=[]

yd40_rb=[]
vert_rb=[]
bench_rb=[]
broadjump_rb=[]
cone_3_rb=[]
shuttle_rb=[]
draftposition_rb=[]
performance_rb=[]

for i in range(4):
    year=2016+i
    filename_combine=str(year)+"_combine.csv"
    filename_wr=str(year)+"_wrstats.csv"
    filename_rb=str(year)+"_rushingstats.csv"
    combine.append(pd.read_csv(filename_combine))
    wrstats.append(pd.read_csv(filename_wr))
    rbstats.append(pd.read_csv(filename_rb))

for i in range(4):
    indexlist=[]
    combineadd=combine[i]
    playernames_new=combineadd["Player"].values.astype(str)
    position_new=combineadd["Pos"].values.astype(str)
    yd40_new=combineadd["40yd"].values
    vert_new=combineadd["Vertical"].values
    bench_new=combineadd["Bench"].values
    broadjump_new=combineadd["Broad Jump"].values
    cone_3_new=combineadd["3Cone"].values
    shuttle_new=combineadd["Shuttle"].values
    drafted_new=combineadd["Drafted (tm/rnd/yr)"].values
    for j in range(len(playernames_new)):
        if  math.isnan(yd40_new[j]) or math.isnan(vert_new[j]) or math.isnan(bench_new[j]) or math.isnan(broadjump_new[j]) or math.isnan(cone_3_new[j]) or math.isnan(shuttle_new[j]) or not isinstance(drafted_new[j],str): 
            indexlist.append(j)
    
    playernames_new=np.delete(playernames_new,indexlist)
    position_new=np.delete(position_new,indexlist)
    yd40_new=np.delete(yd40_new,indexlist)
    vert_new=np.delete(vert_new,indexlist)
    bench_new=np.delete(bench_new,indexlist)
    broadjump_new=np.delete(broadjump_new,indexlist)
    cone_3_new=np.delete(cone_3_new,indexlist)
    shuttle_new=np.delete(shuttle_new,indexlist)
    drafted_new=np.delete(drafted_new,indexlist)

    playernames.append(playernames_new)
    position.append(position_new)
    yd40.append(yd40_new)
    vert.append(vert_new)
    bench.append(bench_new)
    broadjump.append(broadjump_new)
    cone_3.append(cone_3_new)
    shuttle.append(shuttle_new)
    drafted.append(drafted_new)

for i in range(4):
    wrstats_check=wrstats[i]
    wr_names=wrstats_check["Player"].values
    wr_yards=wrstats_check["Yds"].values
    rbstats_check=rbstats[i]
    rb_names=rbstats_check["Player"].values
    rb_yards=rbstats_check["Yds"].values
    
    for j, char1 in enumerate(playernames[i]):
        if position[i][j]=="WR":
            for k, char2 in enumerate(wr_names):
                if char1==char2:
                    counterslash=0
                    index1=0
                    counter=0
                    while counterslash<2:
                        if drafted[i][j][index1]=="/":
                            counterslash+=1
                        index1+=1
                    index1+=1
                    index2=index1
                    while counter==0:
                        if drafted[i][j][index2]=="p":
                            counter=1
                        else:
                            index2+=1
                    index2=index2-3
                    draftposition=drafted[i][j][index1:index2]
                    draftposition=int(draftposition)
                    yd40_wr.append(yd40[i][j])
                    vert_wr.append(vert[i][j])
                    bench_wr.append(bench[i][j])
                    broadjump_wr.append(broadjump[i][j])
                    cone_3_wr.append(cone_3[i][j])
                    shuttle_wr.append(shuttle[i][j])
                    draftposition_wr.append(draftposition)
                    performance_wr.append(wr_yards[k])
                    break
        elif position[i][j]=="RB":
            for k, char2 in enumerate(rb_names):
                if char1==char2:
                    counterslash=0
                    index1=0
                    counter=0
                    while counterslash<2:
                        if drafted[i][j][index1]=="/":
                            counterslash+=1
                        index1+=1
                    index1+=1
                    index2=index1
                    while counter==0:
                        if drafted[i][j][index2]=="p":
                            counter=1
                        else:
                            index2+=1
                    index2=index2-3
                    draftposition=drafted[i][j][index1:index2]
                    draftposition=int(draftposition)
                    yd40_rb.append(yd40[i][j])
                    vert_rb.append(vert[i][j])
                    bench_rb.append(bench[i][j])
                    broadjump_rb.append(broadjump[i][j])
                    cone_3_rb.append(cone_3[i][j])
                    shuttle_rb.append(shuttle[i][j])
                    draftposition_rb.append(draftposition)
                    performance_rb.append(rb_yards[k])
                    break

print()
print("Values for years 2016-2019:")

#WR
print()
print("WR R2 values")
length_wr=len(yd40_wr)
draftposition_wr=np.array(draftposition_wr,dtype=float)
fit_pos_wr=m_pos_wr*draftposition_wr+c_pos_wr
r2_wr_pos=r2(performance_wr,fit_pos_wr)
plt.figure()
print("Draft Position: ", r2_wr_pos)
plt.scatter(draftposition_wr, performance_wr)
plt.plot(draftposition_wr,fit_pos_wr)
plt.xlabel("Draft Position for WR")  
plt.ylabel("Receiving Yards for WR")

fit_metric_wr=np.ones(length_wr)*k0[0]+np.multiply(yd40_wr,k0[1])+np.multiply(vert_wr,k0[2])+np.multiply(bench_wr,k0[3])+np.multiply(broadjump_wr,k0[4])+np.multiply(cone_3_wr,k0[5])+np.multiply(shuttle_wr,k0[6])
metric=fit_metric_wr-np.ones(length_wr)*k0[0]
r2_wr_metric=r2(performance_wr,fit_metric_wr)
plt.figure()
print("Metric: ", r2_wr_metric)
plt.scatter(metric, performance_wr)
plt.plot(metric,fit_metric_wr)
plt.xlabel("Metric for WR")  
plt.ylabel("Receiving Yards for WR")

fit_metric_new_wr=np.ones(length_wr)*k1[0]+np.multiply(yd40_wr,k1[1])+np.multiply(vert_wr,k1[2])+np.multiply(bench_wr,k1[3])+np.multiply(broadjump_wr,k1[4])+np.multiply(cone_3_wr,k1[5])+np.multiply(shuttle_wr,k1[6])+np.multiply(draftposition_wr,k1[7])
metric_new=fit_metric_new_wr-np.ones(length_wr)*k1[0]
r2_wr_metric_new=r2(performance_wr,fit_metric_new_wr)
plt.figure()
print("New Metric: ", r2_wr_metric_new)
plt.scatter(metric_new, performance_wr)
plt.plot(metric_new,fit_metric_new_wr)
plt.xlabel("New Metric for WR")  
plt.ylabel("Receiving Yards for WR")

#RB
print()
print("RB R2 values")
length_rb=len(yd40_rb)
draftposition_rb=np.array(draftposition_rb,dtype=float)
fit_pos_rb=m_pos_rb*draftposition_rb+c_pos_rb
r2_rb_pos=r2(performance_rb,fit_pos_rb)
plt.figure()
print("Draft Position: ", r2_rb_pos)
plt.scatter(draftposition_rb, performance_rb)
plt.plot(draftposition_rb,fit_pos_rb)
plt.xlabel("Draft Position for RB")  
plt.ylabel("Rushing Yards for RB")

fit_metric_rb=np.ones(length_rb)*k2[0]+np.multiply(yd40_rb,k2[1])+np.multiply(vert_rb,k2[2])+np.multiply(bench_rb,k2[3])+np.multiply(broadjump_rb,k2[4])+np.multiply(cone_3_rb,k2[5])+np.multiply(shuttle_rb,k2[6])
metric=fit_metric_rb-np.ones(length_rb)*k2[0]
r2_rb_metric=r2(performance_rb,fit_metric_rb)
plt.figure()
print("Metric: ", r2_rb_metric)
plt.scatter(metric, performance_rb)
plt.plot(metric,fit_metric_rb)
plt.xlabel("Metric for RB")
plt.ylabel("Rushing Yards for RB")

fit_metric_new_rb=np.ones(length_rb)*k3[0]+np.multiply(yd40_rb,k3[1])+np.multiply(vert_rb,k3[2])+np.multiply(bench_rb,k3[3])+np.multiply(broadjump_rb,k3[4])+np.multiply(cone_3_rb,k3[5])+np.multiply(shuttle_rb,k3[6])+np.multiply(draftposition_rb,k3[7])
metric_new=fit_metric_new_rb-np.ones(length_rb)*k3[0]
r2_rb_metric_new=r2(performance_rb,fit_metric_new_rb)
plt.figure()
print("New Metric: ", r2_rb_metric_new)
plt.scatter(metric_new, performance_rb)
plt.plot(metric_new,fit_metric_new_rb)
plt.xlabel("New Metric for RB")
plt.ylabel("Rushing Yards for RB")
plt.show()
plt.pause(120)