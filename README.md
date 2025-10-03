This repository contains a Python program that efficiently finds amicable number pairs up to a configurable limit. The code reads configuration from a YAML file, calculates the sum of proper divisors for numbers in parallel using multiprocessing, and identifies amicable pairs by comparing divisor sums.

Key features:

- Configurable maximum number via external YAML file

- Efficient divisor sum calculation using a square root optimization

- Parallelized computation leveraging all available CPU cores with multiprocessing.Pool

- Clear, modular function structure for easy maintenance and extension

This project serves as a practical example of combining mathematical algorithms with Python’s multiprocessing and configuration management for performance and flexibility. Ideal for those interested in number theory or Python parallel programming.
