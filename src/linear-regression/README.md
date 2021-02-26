# Linear Regression

## Data Preparation

This repository doesn't contain dataset. Download boston house prices data from [Kaggle](https://www.kaggle.com/vikrishnan/boston-house-prices) and place it to `src/linear-regression/dataset/housing.csv`.

## How to build and start

Images will be created in `images` directory.

### With Docker

Run following command to build and run.

```bash
cd src/linear-regression
# build
docker image build -t linear-reg .
# run
docker container run --rm -v /$(PWD)/images:/src/images linear-reg
```

Shell script can also be used instead.

```bash
bash build.sh
bash start.sh
```

### Without Docker

Install following 3 modules which are specified in Dockerfile. Version of Python is 3.9.1.

```bash
pip install numpy==1.20.1
pip install matplotlib==3.3.4
pip install seaborn==0.11.1
```

Run process.py

```bash
python process.py
```
