#!/bin/sh
for map in $(cat Reference/CellGrid_3_75Minute_TEM.txt | sed -e 's/ /_/g') ; do
map2=$(echo $map| sed -e 's/_/ /g')
map3=$(echo $map| sed 's/$/_Mask/g')
v.extract --o input="cellgrid_3_75minute_tem" where="cell_name='$map2'" output="$map3"
g.region -p -a vect=$map3 res=3.125
r.mask vect=$map3
g.copy --overwrite raster=MASK,$map3 
r.mask -r
done
