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

1. Use git repo HTTPS link to search for pytorch file
2. Open the Pytorch file and clone repository by adding code line in starting:
    - !git clone "https://github.com/some-repo.git"
3. Now we have downloaded the complete repo. But to execute the our Jupyter notebook , we should be able to find correct package. So we need to move to specific directory inside source which Jupyter notebook references
    - %cd /content/colab-git-integration/<repo-name>/src

4. Install the requirements 
    - !pip install -r ../requirements.txt

5. Now you should be able to execute rest of the jupyter notebook program

### Directly running code without any modification 

- For this your repo should have only contents present inside src at repo level. So when you clone git repo, you may not need to change any path
- Execute above steps 4 and 5 as needed,

