# phagepickr: phage cocktail design based on bacterial receptor configurations  

## Introduction
`phagepickr` is a tool aimed at the design of evolution-proof bacteriophage cocktails targeting multiple receptors proteins in bacteria. The workflow used to generate the database of protein receptors and phage-host information is available in `bacteria`.

## Installation
### MacOS / Linux
1. Create the new environment:
```
conda env create -f environment.yml
```
2. Activate the environment:
```
conda activate phagepickr
```
3. Install MAFFT (brew is required on macOS Apple Silicon where conda MAFFT is unavailable):
```
conda install -c bioconda mafft  # macOS Intel/Linux
```
```
brew install mafft  # macOS Apple Silicon (arm64)
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
