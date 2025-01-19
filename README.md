# TOPSIS Package for Multiple Criteria Decision Making

## Introduction to TOPSIS

TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a popular multi-criteria decision analysis (MCDA) method used to rank alternatives based on their distance from an ideal solution. The primary goal of the method is to find the option that has the shortest distance from the ideal solution (ideal best) while being the farthest from the negative ideal solution (ideal worst).

This package implements the TOPSIS method to help users easily evaluate and rank alternatives based on their performance across multiple criteria.

## Features of the Package

- Provides an easy-to-use interface to apply TOPSIS.
- Requires a .csv file as the input file.
- Handles decision matrices with various scales and criteria.
- Validates the input data to ensure all criteria are correctly provided.
- Supports normalization and weighted scoring.
- Allows for both maximization(+) and minimization(-) of criteria.

## Installation

To install the latest version of the TOPSIS package, run the following command:

```bash
pip install Topsis-Rishika-102203128
```

## Usage
This package is designed to be used as a command-line tool for easy integration into your decision-making workflows.

```bash
python <program.py> <InputDataFile> <Weights> <Impacts> <OutputFileName>
```
### Parameter Description

```<InputDataFile>:``` The path to the input file (in .csv) containing the decision matrix.
```<Weights>:``` A comma-separated list of weights for the criteria (e.g., 1,1,2,1).
```<Impacts>:``` A comma-separated list of impacts for the criteria (+ for maximization and - for minimization) (e.g., +,+,-,+).
```<ResultFileName>:``` The name of the output file where the results will be saved (e.g., result.csv).

## Important Notes

1. The input file must contain at least two sections:
    a. Object/alternative names: The first column should have the names of the alternatives (e.g., M1, M2, M3).
    b Criteria values: The remaining columns should contain numeric values representing the performance of each alternative across the criteria.
2. The input file must be in .csv format only.
3. The number of weights and impacts must match the number of criteria.

## Exception Handling

This package includes robust exception handling to ensure smooth execution and to provide clear feedback to users. The following error scenarios are handled:

    File Not Found: If the input file cannot be found, an error message will be displayed, and the process will terminate.

    Mismatched Parameters: If the number of weights or impacts does not match the number of criteria in the input file, an error will be thrown.

    Non-Numeric Values: The package ensures that all criteria columns contain numeric values only. If any non-numeric value is encountered, an error will be raised.
    
    Invalid Impacts: The impacts provided must be either + (for maximization) or - (for minimization). If any invalid characters are provided, an error will be thrown.

This makes it easier for users to identify and resolve issues in their input data and ensures the correctness of the decision-making process.

## License

This package is distributed under the MIT License, which allows you to freely use, modify, and distribute the software. However, it comes with no warranty, and the authors are not responsible for any damages that may result from its use.

You can find the full text of the MIT License in the LICENSE file.

## Contributing
Contributions are welcome! If you'd like to contribute to the development of this package, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make the necessary changes and commit them.
4. Open a pull request with a description of the changes.

Please make sure to include tests for any new functionality or bugfixes. For major changes, open an issue first to discuss what you’d like to change.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository or reach out to the package maintainer.