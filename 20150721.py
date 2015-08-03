
from things import Map

def Make_two_cluster(Map, target, start_point, end_point):
    
    cluster_s = []
    cluster_e = []
    
    for i in target:
        
        if Map.cal_distance(start_point,i) > Map.cal_distance(end_point,i):
            cluster_e.append(i)
        else:
            cluster_s.append(i)
    return cluster_s , cluster_e

def find_end_of_s(Map, cluster_s, end_point):
    
    e_s = []
    
    for i in cluster_s:
        if len(e_s) > 0:
            if Map.cal_distance(i, end_point) < e_s[1]:
                e_s = [i , Map.cal_distance(i, end_point)]
        else:
            e_s = [i , Map.cal_distance(i, end_point)] 
        
        #print e_s
    return e_s[0]
    
def eliminate_one(list, one):
    dummy = []
    for i in list:
        if i != one:
            dummy.append(i)
    return dummy

import itertools
def get_route(Map, start, cluster, end):
    result = []
    for subset in itertools.permutations(cluster, len(cluster)):
        result.append(subset)
    comp = []
    for i in result:
        dummy = [start]
        
        for j in i:
            dummy.append(j)
        dummy_dist = 0
        
        for k in range(len(dummy)-1):
            dummy_dist = dummy_dist + Map.cal_distance(dummy[k:k+2][0],dummy[k:k+2][1])
            #print dummy[k:k+2] , dummy[k:k+2][0], dummy[k:k+2][1] , Map.cal_distance(dummy[k:k+2][0],dummy[k:k+2][1]) 
        #print Map.cal_distance(dummy[len(dummy)-1],end) 
        dummy_dist = dummy_dist + Map.cal_distance(dummy[len(dummy)-1],end)
        dummy.append(end)
        comp.append([dummy_dist, dummy])
    comp.sort()
    return comp[0][1]
    
a = Map()

order_list = ['a1','a2','a3','a4','a5','a6']

cl1, cl2 = Make_two_cluster(a, order_list, 's' , 'e')

cl1_e = find_end_of_s(a, cl1, 'e')

cl1 = eliminate_one(cl1, cl1_e)

result = []

for i in get_route(a, 's', cl1, cl1_e)[0:len(get_route(a, 's', cl1, cl1_e))-1]:
    result.append(i)

for i in get_route(a, cl1_e, cl2, 'e'):
    result.append(i)
    
print result

a.printmap()

