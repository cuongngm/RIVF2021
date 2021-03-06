from pathlib import Path
Path('dataset').mkdir(parents=True, exist_ok=True)
Path('dataset/task1_diqa').mkdir(parents=True, exist_ok=True)
Path('dataset/task1_diqa/image').mkdir(parents=True, exist_ok=True)
Path('dataset/task1_diqa/label').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect/images').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect/images/train').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect/images/val').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect/labels').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect/labels/train').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_detect/labels/val').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_ocr').mkdir(parents=True, exist_ok=True)
Path('dataset/task2_ocr/img').mkdir(parents=True, exist_ok=True)
Path('result').mkdir(parents=True, exist_ok=True)
Path('weights').mkdir(parents=True, exist_ok=True)
