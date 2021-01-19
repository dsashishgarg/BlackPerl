## Setup

### Setting up environment

- Create conda environment

```ssh
$ conda env create -f environment.yml
```

- To activate environment ()

```ssh
$ conda activate blackperl

// all commands after activation will have the right binaries references. You must always be in this environment to run and debug this project
```

- To deactivate environment

```ssh
$ conda deactivate namekoexample
```

- Unit Test

```ssh
(blackperl) python -m pytest -v
```

- Coverage

```ssh
(blackperl) python -m pytest --cov
```
