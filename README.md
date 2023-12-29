# leetcode-notebook-generator

A Python script to simplify LeetCode problem-solving by generating a Jupyter Notebook template from problem URLs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ixora-0/leetcode-notebook-generator.git
   cd leetcode-notebook-generator
   ```
2. Install dependencies
### Using [poetry](https://python-poetry.org/docs/)
   ```bash
   poetry install
   ```
### Using pip
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Using [poetry](https://python-poetry.org/docs/)
```bash
poetry run generate <url> -d <path>
```

### Without [poetry](https://python-poetry.org/docs/)
```bash
python -m leetcode_notebook_generator <url> -d <path>
```

Replace `<url>` with the URL of the LeetCode problem you want to generate a Jupyter Notebook for. Replace `<path>` with th edestination folder, default is `./output/`.

### Example
```bash
poetry run generate https://leetcode.com/problems/two-sum/ -d ./sample_output/
```
or
```bash
python -m leetcode_notebook_generator https://leetcode.com/problems/two-sum/ -d ./sample_output/
```
This will generate a [Jupyter Notebook](sample_output/1-%20Two%20Sum.ipynb) with a template for the [Two Sum](https://leetcode.com/problems/two-sum/) problem.
![Example Notebook](sample_output/Two%20Sum%20screenshot.png)

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). See the [LICENSE](LICENSE) file for details.
