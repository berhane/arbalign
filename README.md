# Purpose
ArbAlign is a small tool for optimally aligning two arbitrarily ordered isomers using the
Hungarian or Kuhn-Munkres algorithm. The final ordering of the two isomers should give the lowest
root mean-square distance (RMSD) between the two structures.

# Contents
The repo contains the following items:
* Code -  a folder containing the following items:
* ArbAlign-driver.py - a Python source code for the munkresRMSD script,
* ArbAlign.py - a Python source code for the munkresRMSD script,
* PrinCoords.py - a Python source code for calculating principal coordinates
* genTypes.csh – a shell script to use OpenBabel to convert a Cartesian (XYZ) file to a SYBYL Mol2 file formatted as a conventional XYZ file
* genConn.csh – a shell script to use OpenBabel to convert a Cartesian (XYZ) file to a NMA connectivity file formatted as a conventional XYZ file
* RMSD-Kabsch.py - a Python script for calculating RMSDs by Jimmy Charnley Kromann
            (jimmy@charnley.dk) and Lars Bratholm's script from
            https://github.com/charnley/rmsd - Accessed on Nov 10, 2015. Please see
            rmsd-script/LICENSE for usage rights.

# Usage
ArbAlign-driver.py is a Python driver script to run Kuhn-Munkres optimal RMSD matching
ArbAlign can be used either as a command line or web tool. The command line tool has a driver script
that can take in many options or resort to sensible defaults when necessary.
<pre>
Usage: ArbAlign-driver.py [-b/--by {l, t, c}] [-n/--noHydrogens] [-s/--simple] A.xyz B.xyz

   -b {l,t,c}, --by {l,t,c}
     Match atoms by l-label, SYBYL t-type, or NMA connectivity (-c).
     The default is by atom label (-l)
   -s, --simple
     Perform Kuhn-Munkres assignment reordering without axes swaps and reflections.
     The default is to perform axes swaps and reflections
   -n, --noHydrogens
     Ignore hydrogens.
     The default is to include all atoms
   </pre>
Examples
<pre>
ArbAlign-driver.py  A.xyz B.xyz
ArbAlign-driver.py --by c --noHydrogens A.xyz B.xyz
ArbAlign-driver.py --simple --noHydrogens A.xyz B.xyz
</pre>

## Alignment by label, atom type or NMA connectivity
<pre>
   -b {l,t,c},
   --by {l,t,c}
</pre>
The default is to align the isomers by element or atom label (-l). If one wants to align the isomers
by the elements' SYBYL atom type or NMA connectivity, the driver needs to interface with OpenBabel.
Match atoms by l-label, SYBYL t-type, or NMA connectivity (-c).

## Consider all axes swaps and reflections or original axes only
<pre>
   -s,
   --simple
</pre>
Perform Kuhn-Munkres assignment reordering without axes swaps and reflections.
The default is to perform axes swaps and reflections

## Consider all atoms or heavy atoms only
<pre>
   -n,
   --noHydrogens
</pre>
Ignore hydrogens.
The default is to include all atoms

# Requirements
## Python 2.7+
* Python Numpy module. If you don't have it already, you can install it using `pip`
 * `pip install numpy`
* Python Hungarian module by Harold Cooper
  * Hungarian: Munkres' Algorithm for the Linear Assignment Problem in Python (https://github.com/Hrldcpr/Hungarian)
  * This is a wrapper to a fast C++ implementation of the Kuhn-Munkres algorithm. The installation instructions are described clearly at https://github.com/Hrldcpr/Hungarian.
  * In short, one would need to go into the `hungarian` directory and
    * `python setup.py build`  
    * `python setup.py install`
    * You would either want to copy the file `build/lib-XXX/hungarian.so` into a location that's
      included in your `$PYTHONPATH` or whatever directory you are running ArbAlign from.
* Alternatively, you can use Brian Clapper's Munkres module or another similar module includeded in SciNumpy. This could require you to make small changes to the current script. We'll provide an version that uses SciNumpy's Munkres module at a later time.

## Other Tools Needed to Align by Atom Type or Connectivity
* OpenBabel - We use OpenBabel to convert Cartesian coordinates (XYZ) to formats containing atmm types including connectivity and hybridization information. It is necessary to use OpenBabel to convert the Cartesian coordinates to SYBYL Mol2 (sy2) and MNA (mna) formats.
* genTypes.csh - a small shell script which converts XYZ file to SYBYL Mol2 (sy2) format and recasts the atom label to contain atom type information.
* genConn.csh - a small shell script which converts XYZ file to NMA (nma) format and recasts the atom label to contain atom's bonding/connectivity information.


# Output
If the pairs of structures pass a sanity test, the tool will align them optimally and provide the
following information.
* The initial Kabsch RMSD,
* The Kuhn-Munkres reorderings for each atom and the corresponding RMSDs,
* The final Kabsch RMSD after the application of the Kuhn-Munkres algorithm, and
* The coordinates corresponding to the best alignment of the second structure with the first.

# Citation
If you find this tool useful for any publishable work, please cite the companion paper:

Berhane Temelso, Joel M. Mabey, Toshiro Kubota, Nana Appiah-padi, George C. Shields.  `J. Chem. Info. Model.` **2017**, 57 (5), 1045–1054

http://doi.org/10.1021/acs.jcim.6b00546
