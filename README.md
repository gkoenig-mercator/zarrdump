#zarrdump.py — Zarr Metadata Dumper

A simple Python script that prints metadata from a Zarr dataset to the command line, similar to ncdump for NetCDF files.
## Requirements

pip install xarray zarr

## Usage

python zarrdump.py <path_to_zarr>

## Output

    Global attributes

    Variable names, dimensions, shapes, dtypes, and attributes

## Example

python zarrdump.py data/example.zarr
