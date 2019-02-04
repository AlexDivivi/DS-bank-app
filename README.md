# Bank App

## Setup

```sh
git clone https://github.com/neuefische/DS-bank-app.git
```

```sh
conda env create --file environment.yml
source activate neue-fische-bank-app
```

## Usage

```sh
conda env update --file environment.yml
source activate neue-fische-bank-app
jupyter notebook
```

## Tests

```sh
pytest # tests
```

```sh
flake8 # codestyle - Should return `0` if all checks are passed successfully.
```
