# Activate python3.6
The following two commands activate python on the computer
in the computer room at the Innsbruck University.

```bash
module available

module load python/miniconda3
```

# create a working directory

```bash
mkdir PYTHON_COURSE

cd PYTHON_COURSE

```

# clone the git repository
**!!! you have to do this only the first time !!!**

```bash
git clone https://github.com/marcogullieuszik/astromundus2017_python.git
```


A new directory `astromundus2017_python` will be created. Here you have all the material we will use.

**DO NOT modify this directory**. Do not overwrite/delete/add files.

# create another direcory
where you can make experiments and copy the files that you need, for example:

```bash
mkdir WORK

cp -r astromundus2017_python/NOTEBOOKS/02_PYTHON_INTRO WORK

```

# update the `git` repository
When new material will be ready you have to add it to your
local copy of the repository.

get in the directory with the *ORIGINAL* repository
ad update the repository.

```bash
cd PYTHON_COURSE/astromundus2017_python

git pull origin master
```
now you can copy the new files in your working directory (`../WORK/` in the previous example)
