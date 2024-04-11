# colab-git-integration
Example repo to demonstrate git folder structure having jupyter notebooks with colab

Here is the structure:

```console

- Repo/Project folder
    |- src
        |- package(sampleProject)
            |- __main__.py
            |- common
            |- models
            |- utility
        |- Jupyter notebooks
    |- tests
    |- docs
    |- README
    |- requirements.txt


```


Jupyter notebooks needs to be placed at package level 

## Running the package and Jupyter notebook 

- Use absolute import like : from sampleProject.utility import myUtility everywhere in code and also in Jupyter notebook


### Running the package independent from notebook 

Go to /src

> python -m sampleProject


### Running the Jupyter notebook

- You can reference any module as run as you want


## Importing and running Jupyter notebook in google colab

1. 
2. 

