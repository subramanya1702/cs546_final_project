# Download from https://snap.stanford.edu/biodata/datasets/10023/10023-CC-Neuron.html
class Config:
    FILE_LOCATION = "./data/CC-Neuron_cci.tsv"
    FILE_TYPE = 'tsv'
    #NOTE: This is a large file. Not recommended to visualize unless you have a powerful system.
    # Flags to enable/disable functions
    RUN_EDA = True
    RUN_DEGREE_DIST = False
    RUN_CLUSTERING_COEFF = False
    RUN_COMMUNITY_DETECTION = True
    RUN_COMMUNITY_DETECTION_PLOT = False
    RUN_3D_VISUALIZATION = False
    CENTRALITY = False