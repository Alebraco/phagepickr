#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.neighbors import NearestNeighbors

def nearest_bacteria(target_features, features_data, neighbors = 1):
    nn_model = NearestNeighbors(n_neighbors = neighbors, metric = 'hamming')
    nn_model.fit(features_data)

    distances, indices = nn_model.kneighbors(target_features)

    return distances, indices
    
def nearest_names(indices, df):
    similar = list(df.index[indices[0]].values)
    
    return similar

def nearest_phages(similar, phageinfo):
    similar_phages = {host:[record['acc'] for record in phageinfo if record['host'] == host] for host in similar}

    return similar_phages
