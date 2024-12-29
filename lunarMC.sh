
#!/bin/bash

#------------------------------------------------------------------------
# VARIABLES
#------------------------------------------------------------------------

# FILES
rm sum_output_true.txt
cat tablehead.txt > sum_output_true.txt
rm sum_output_false.txt
cat tablehead.txt > sum_output_false.txt
rm sum_starting_true.txt
cat tablehead_starting.txt > sum_starting_true.txt
rm sum_starting_false.txt
cat tablehead_starting.txt > sum_starting_false.txt
# files that run melts 
batch_file=batch_exoplanets.txt

env_file=alphamelts_default_env.txt
melts_file=input.txt

# automatically generated melts output that needs to be read at each step to 
output=alphaMELTS_tbl.txt


#------------------------------------------------------------------------
# CALCULATION
#----------------------------------------------------------

# First loop for various starting compositions


a=1
while [ $a -le 100000 ]
do
python3 generate_input.py

# Run MELTS

    run_alphamelts.command -f $env_file -m $melts_file -b $batch_file

# Create output files


# cp alphaMELTS_tbl.txt Results_exoplanets${a}.txt
# cp Liquid_comp_tbl.txt Liquid_comp_tbl${a}.txt
# cp Phase_main_tbl.txt Phase_main_tbl${a}.txt
# cp System_main_tbl.txt System_main_tbl${a}.txt
# cp Solid_comp_tbl.txt Solid_comp_tbl${a}.txt
# cp Phase_mass_tbl.txt Phase_mass_tbl${a}.txt
# cp Phase_vol_tbl.txt Phase_vol_tbl${a}.txt

# Recreate the new Melts file for the next round of calculations

python3 generate_output.py


a=$(( a+1 ))
done
