#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from data_collection.receptors_function import receptors

def receptor_df(receptor_data):
    labels = sorted(set(receptor_data.keys())) 
    proteins = set()
    for ls in receptor_data.values():
        proteins.update(ls)
    proteins = sorted(proteins)

    df = pd.DataFrame(index = labels, columns = proteins)

    for sp in df.index:
        df.loc[sp] = df.columns.isin(receptor_data.get(sp, False)).astype(int)
    return df

def membership(target, df):
    if target in df.index:
        return True
    else:
        return False
        
def produce_array(target, df):
    if membership(target, df):
        return None
    else:
        targetdict = {}
        targetdict[target] = receptors(target)
        target_conf = df.columns.isin(targetdict.get(target, False)).astype(int)
        target_features = target_conf.reshape(1, -1)
        return target_features 
    
def remove_ifmember(target_features, target, df):

    if target_features is None:
        target_row = df.loc[target]
        target_features = target_row.values.reshape(1, -1)
        features_data = df.drop(target, axis = 0).values
    else:
        features_data = df.values
        
    return target_features, features_data   
        
    
