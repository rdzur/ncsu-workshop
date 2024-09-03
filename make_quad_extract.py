import sys
import grass.script as gs

try:
    with open("Reference/CellGrid_3_75Minute_TEM.txt", "r") as cell_grid_file:
        for map in cell_grid_file:
            
            map = map.strip() # Remove leading/trailing whitespace
            print(f"Processing: {map}") # Print the map name

            map2 = map.replace("_", " ") # Replace underscores with spaces
            map3 = map + "_Mask" # Append "_Mask" to the map name

            # Extract the cell from the vector map
            result = gs.run_command('v.extract', input="cellgrid_3_75minute_tem", where=f"cell_name='{map2}'", output=map3)
            print(f"v.extract result: {result}")

            # Check if the vector map was created successfully
            gs.run_command('g.region', flags='pa', vector=map3, res=3.125)
            print("Region info:", gs.region())

            # Mask the raster map using the extracted vector map
            gs.run_command('r.mask', vector=map3)
            print("Mask status:", gs.raster_info('MASK'))

            # Export the masked raster map
            gs.run_command('g.copy', raster=f"MASK,{map3}", overwrite=True)

            # Remove the mask
            gs.run_command('r.mask', flags='r')

            print(f"Finished processing: {map}")

    print("\nCreated vector maps:")
    print(gs.list_strings('vect', pattern='*_Mask'))
    print("\nCreated raster maps:")
    print(gs.list_strings('rast', pattern='*_Mask'))

except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)
    sys.exit(1)