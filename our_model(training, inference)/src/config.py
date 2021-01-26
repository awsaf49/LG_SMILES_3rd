from pathlib import Path

### Data provided by LG
# Head directory
data_dir = Path('/home/jaeho_ubuntu/SMILES/data/')
train_dir = data_dir / 'train'
test_dir = data_dir / 'test'
train_csv_dir = data_dir /'train.csv'
# train_modified contains information of the train/validation split in a pickle file format. I saved in pickle just for efficiency
train_pickle_dir = data_dir /'train_modified.pkl'
# Sample submission directory
sample_submission_dir = data_dir /'sample_submission.csv'


### Data directory generated by us
input_data_dir = data_dir / 'input_data'
base_file_name = 'seed_123_max75smiles'

### seed for train/val split
random_seed = 123

### Reversed_token_file used to map numbers to string. 
reversed_token_map_dir = input_data_dir/ f'REVERSED_TOKENMAP_{base_file_name}.json'