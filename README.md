# phagetool: phage cocktail design based on bacterial receptor configurations  

## Introduction
'' is a tool aimed at the design of evolution-proof bacteriophage cocktails targeting multiple receptors proteins in bacteria. The workflow used to generate the database of protein receptors and phage-host information is available in 'submodule'.

## Installation
### MacOS / Linux
1. Create the new environment:
```
mamba env create -f phagetool.yml
```
2. Activate the environment:
```
mamba activate phagetool
```

### Windows
1. Install Ubuntu on the terminal:  
    ```bash
    wsl --install
    ```
2. Start Ubuntu:  
    ```bash
    wsl
    ```

3. Install [Miniforge](https://github.com/conda-forge/miniforge):  
    ```bash
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

4. Follow steps 1 and 2 from MacOS / Linux (environment setup)
