# data from https://neurodata.io/project/connectomes/

class config:
    FILE_LOCATION = './data/mixed.species_brain_1.graphml'
    FILE_TYPE = 'graphml'

    # Flags to enable/disable functions
    RUN_EDA = True
    RUN_DEGREE_DIST = False
    RUN_CLUSTERING_COEFF = False
    RUN_COMMUNITY_DETECTION = True
    RUN_COMMUNITY_DETECTION_PLOT = True
    RUN_3D_VISUALIZATION = False
    CENTRALITY = False