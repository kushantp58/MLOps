WANDB_PROJECT = "mlops"
WANDB_ENTITY = "ktest123"
BDD_CLASSES = {i:c for i,c in enumerate (['background','road','traffic light', 'traffic sign', 'person','vehicle','bicycle'])}
RAW_DATA_ARTIFACT = "bdd_simple_1k"
PROCESSED_DATA_ARTIFACT = "bdd_simple_1k_split"