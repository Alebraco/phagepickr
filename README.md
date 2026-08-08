# phagepickr: phage cocktail design based on bacterial receptor configurations  

A tool to design evolution-proof bacteriophage cocktails against pathogenic bacteria.

## Installation

```bash
# 1. Clone and create environment
git clone https://github.com/Alebraco/phagepickr
cd phagepickr
conda env create
# 2. Activate the environment
conda activate phagepickr
```

## Usage

Once installed, `phagepickr` can be run from the command line.

```bash
phagepickr --target <SPECIES> --email <EMAIL> [options]
```

### Arguments

| Argument | Short | Required | Description |
| :--- | :--- | :---: | :--- |
| `--target` | `-t` | Yes | Name of the target species (e.g., "Escherichia coli"). |
| `--email` | `-e` | Yes | Your email address (required for NCBI Entrez access). |
| `--strategy` | `-s` | No | Selection strategy: `'diverse'` for maximum diversity or `'random'` (default: `diverse`). |
| `--neighbors` | `-n` | No | Number of nearest neighbors to consider (default: `3`). |
| `--k_value` | `-k` | No | Number of most distant phage pairs that maximize diversity per neighbor (default: `1`). |
| `--explore_only`| `-i` | No | If set, excludes known infecting phages and selects only potential infectors. |
| `--threads` | `-T` | No | Number of threads passed to MAFFT for the alignment step. `-1` uses all available cores (default: `1`). |
| `--api_key` | `-a` | No | NCBI API key (optional but recommended for higher rate limits). |
| `--lifestyle` | `-l` | No | Predict phage lifestyle with BACPHLIP: `'annotate'` scores the selected phages, `'exclude'` scores the whole pool and discards temperate phages before selection (requires optional environment below). |

### Examples

**Basic usage for *E. coli*:**
```bash
phagepickr --target "Escherichia coli" --email <EMAIL>
```

**Select a random set of phages:**
```bash
phagepickr -t "Salmonella enterica" -e <EMAIL> --strategy random
```

**Explore potential infectors only (excluding known ones):**
```bash
phagepickr -t "Pseudomonas aeruginosa" -e <EMAIL> --explore_only
```

**Advanced usage with specific neighbor and pair counts:**
```bash
phagepickr -t "Klebsiella pneumoniae" -e <EMAIL> --neighbors 5 -k 2
```

**Speed up the alignment step on a multi-core machine:**
```bash
phagepickr -t "Escherichia coli" -e <EMAIL> --threads 8
```
> The built-in datasets for bacterial receptors and phage-host information were generated using the workflow available in [bacteria](phagepickr/bacteria/).

### Optional Lifestyle Prediction

`--lifestyle` annotates the cocktail with lytic/temperate predictions from [BACPHLIP](https://github.com/adamhockenberry/bacphlip). `annotate` scores only the selected phages and does not modify phage selection. `exclude` scores the whole candidate pool and removes temperate phages *before* selection, so the cocktail is drawn from the remaining lytic candidates. Both print P(virulent) and P(temperate) beside each phage.

```bash
phagepickr -t "Escherichia coli" -e <EMAIL> --lifestyle annotate
phagepickr -t "Escherichia coli" -e <EMAIL> --lifestyle exclude
```

BACPHLIP needs a separate environment as its dependencies conflict with those of phagepickr:

```bash
conda env create -f environment-bacphlip.yml
```

If BACPHLIP cannot be run, `annotate` reports the error and the cocktail is returned unannotated, while `exclude` stops rather than returning an unfiltered cocktail.

This feature remains experimental, as lifestyle prediction does not rely on any single standard method.

## Dependencies

All dependencies and their versions are defined in `environment.yml`.

* **Python:** 3.11
* **BioPython:** 1.83
* **NumPy:** 1.26.0
* **Pandas:** 2.1.1
* **Scikit-learn:** 1.2.2
* **SciPy:** 1.13.1
* **MAFFT** (via `conda-forge`)

Optional, for `--lifestyle` only, defined in `environment-bacphlip.yml` (separate environment):

* **BACPHLIP:** 0.9.6 (Python 3.8, scikit-learn 0.23.1)
* **HMMER** ≥ 3.3 (via `bioconda`)

## License
MIT - see [LICENSE](LICENSE) for details.
