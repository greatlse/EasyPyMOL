from __future__ import division
from pymol import stored,cmd

def roundview(StoredView = 0, sig_digits = 2, 
    outname = "roundedview.txt" ):
    """
DESCRIPTION

Adds the command "roundview" that gets a view (default is 0,
the current view; you can get a stored view assigned to some
other digit with the view command) and rounds to two
significant digits (default) the viewpoint matrix elements
and rewrites the matrix elements on a single line with no
whitespaces and a semicolon at the end. The saved space
eases the making of a single line of PyMOL commands
separated by semicolons. This enables rapid and interactive
editing of chunks of PyMOL commands. The viewpoints are
appended to the bottom of a text file in the present working
directory called "roundedview.txt". The line could be easier
to copy from this file than from the command history window
in the external gui. A semicolon with nothing to the right
of it at the end of a line of grouped commands is harmless.

Usage: roundview [view, significant digits, outname] 

    Note that the values in the [] are optional.

The default argument values are 0,2, roundedview.txt

Examples: run roundview.py and then call with "roundview" or
store in .pymol/startup/ and then quit and restart pymol and
you will find the function listed in the list of plugins.

Then invoke by typing roundview

            roundview # typical use roundview 0,3  

# current view with three significant digits

Copy roundview.py to the folder ~/.pymol/startup and then
the command will always be accessible.

18 elements of the view matrix (0-17)

0 - 8 = column-major 3x3 matrix that rotates the model axes 
to camera axes 

9 - 11 = origin of rotation relative to the camera 
in camera space

12 - 14 = origin of rotation in model space 

15 = front plane distance from the camera 

16 = rear plane distance from the camera 

17 = orthoscopic flag 
(not implemented in older versions)



26 October 2015

  Copyright Notice
  ================
  
  The PyMOL function source code in this file is copyrighted, but you can
  freely use and copy it as long as you don't change or remove any of
  the copyright notices.
  
  ----------------------------------------------------------------------
  This PyMOL script is Copyright (C) 2015 by 
  Blaine Mooers , PhD <blaine-mooers@ouhsc.edu>
  University of Oklahoma Health Sciences Center, Oklahoma City, OK, USA
  
                         All Rights Reserved
  
  Permission to use, copy, modify, distribute, and distribute modified
  versions of this software and its documentation for any purpose and
  without fee is hereby granted, provided that the above copyright
  notice appear in all copies and that both the copyright notice and
  this permission notice appear in supporting documentation, and that
  the name(s) of the author(s) not be used in advertising or publicity
  pertaining to distribution of the software without specific, written
  prior permission.
  
  THE AUTHOR(S) DISCLAIM ALL WARRANTIES WITH REGARD TO THIS
  SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF
  MERCHANTABILITY AND FITNESS.  IN NO EVENT SHALL THE
  AUTHOR(S) BE LIABLE FOR ANY SPECIAL, INDIRECT OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
  FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF
  CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
  OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.
  ----------------------------------------------------------------------
 """
#convert the commandline arguments from strings to integers
    StoredView = int(StoredView) sig_digits =
    int(sig_digits)

#call the get_view function
    m = cmd.get_view(StoredView)

#Make a list of the elements in the orientation matrix. 
    myList = [m[0], m[1], m[2], m[3], m[4], m[5], m[6],
    m[7], m[8], m[9], m[10], m[11], m[12], m[13], m[14],
    m[15], m[16], m[17]]

#Round of to two significant digits the matrix elements.
#This rounding approach solved the problem of unwanted
#whitespaces when I tried using a string format statement
    myRoundedList = [ round(elem, sig_digits) for elem in
    myList ]

#x is the format of the output. The whitespace is required
#between the "set_view" and "(". 
    x = 'set_view ({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},
    {10},{11},{12},{13},{14},{15},{16},{17});' 
#print to the external gui.
    print x.format(*myRoundedList)

#Write to a text file. 
    myFile = open("roundedview.txt", "a") myFile.write(
    x.format(*myRoundedList) + "\n" ) myFile.close() return

#The extend command makes roundview into a PyMOL command.
cmd.extend("roundview",roundview)
