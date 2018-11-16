#!/bin/csh

rm -f rmsd-2017.dat
touch rmsd-2017.dat
foreach FILE (`cat list `)
   setenv FILE1  `echo $FILE | awk -F"_" '{print $1}'`
   setenv FILE2  `echo $FILE | awk -F"_" '{print $2}'`
   #setenv NATOMS `head -1 $FILE1.xyz`
   ArbAlign-driver.py $FILE1.xyz $FILE2.xyz | tail -n 4 | grep -e "Best " -e "Initial and " -e "Initial unsorted RMSD" | awk '{printf "%-6s\t", $NF}' >> rmsd-2017.dat
   ArbAlign-driver.py -b t $FILE1.xyz $FILE2.xyz | tail -n 2 | grep RMSD | awk '{printf "%-6s\t", $NF}' >> rmsd-2017.dat
   ArbAlign-driver.py -b c $FILE1.xyz $FILE2.xyz | tail -n 2 | grep RMSD | awk '{printf "%-6s\t", $NF} END {print "\n"}' >> rmsd-2017.dat
end
