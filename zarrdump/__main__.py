import sys
import xarray as xr

def main():
    if len(sys.argv) != 2:
        print("Usage: zarrdump <zarr_path>")
        sys.exit(1)

    zarr_path = sys.argv[1]

    try:
        ds = xr.open_zarr(zarr_path, consolidated=True)
    except ValueError:
        ds = xr.open_zarr(zarr_path, consolidated=False)
    except Exception as e:
        print(f"Error opening Zarr dataset: {e}")
        sys.exit(1)

    print("netcdf-like output of Zarr metadata:\n")
    print("global attributes:")
    for key, value in ds.attrs.items():
        print(f"\t:{key} = {value!r}")

    for var_name, da in ds.data_vars.items():
        dims = ", ".join(da.dims)
        print(f"\n{var_name}({dims})")
        for attr_name, attr_val in da.attrs.items():
            print(f"\t:{attr_name} = {attr_val!r}")
        print(f"\tshape = {da.shape}")
        print(f"\tdtype = {da.dtype}")

if __name__ == "__main__":
    main()
