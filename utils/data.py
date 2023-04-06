from datasets import load_dataset, concatenate_datasets


def combine(data_path: str, shuffle=True, seed=42):
    data = None
    dataset_names = data_path.split(",")
    for i, dataset_name in enumerate(dataset_names):
        dataset_name = dataset_name.strip()
        ds = load_dataset(dataset_name)
        for split in ds.keys():
            print(f"Dataset {split}: {len(ds[split])}")
        if data is None:
            data = ds
        else:
            for split in ds.keys():
                data[split] = concatenate_datasets([data[split], ds[split]])
    for split in data.keys():
        print(f"Dataset {split}: {len(data[split])}")
    if shuffle:
        data = data.shuffle(seed=seed)
    return data
