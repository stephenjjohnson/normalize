#    normalize.py A Python program to normalize a dataset
#    Copyright (C) 2016 Stephen J. Johnson
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
A Python program to normalize a dataset.
Accepts a comma separated list of numbers then asks for the lowest and 
highest values to consider, and the minimum and maximum values to normalize to.
Hitting ENTER at any of the prompts after the data have been loaded will set a sensible default value.
'''

# from __future__ import division

def main():
    # Get some data to normalize
    # myData = (0,1,2,3,4,5,6,7,8,9,10,11)
    myData = read_my_data(get_file())
    print 'My data:', myData, '\n'

    # Get the smallest and largest data to use in the normalization
    # Smallest
    my_default = str(min(myData))
    minData = get_parameter('What is the smallest value to consider? [Enter to use smallest datum]:', my_default, 'float')
    # Largest
    my_default = str(max(myData))
    maxData = get_parameter('What is the largest value to consider? [Enter to use largest datum]:', my_default, 'float')
    print 'Data range to normalize:', minData, ' to ', maxData, '\n'


    # Get the smallest and largest normalized values
    minNorm = get_parameter('What is the value to normalize the smallest datum to? [Enter to use 0]:', '0', 'float')
    maxNorm = get_parameter('What is the value to normalize the largest datum to? [Enter to use 1]:', '1', 'float')
    print 'Normalized range: ', minNorm, ' to ', str(maxNorm), '\n'
    
    # Should we print the data out?
    verboseFlag = get_parameter('Do you want to see the data while saving? (y/N) ', False, 'bool')

    # Normalize the data using the supplied parameters
    my_norm_data = normalize(myData, minData, maxData, minNorm, maxNorm)
#    print 'Normalized data:', my_norm_data

    # Save in a file
    save_my_data('normalized', my_norm_data, verboseFlag)  


def get_file() :
    '''
    Get a file name to examine
    '''
    myFile = raw_input('Enter a file name: ')
    try:
        fhandle = open(myFile, 'r')
        return fhandle
    except:
        print 'Invalid file name:', myFile
        quit()


def read_my_data(fhandle):
    '''
    Read the data into a list
    '''
    print 'Loading data...'
    myData = list()
    for line in fhandle:
        data_items = line.split(',')
        for datum in data_items:
            datum = float(datum)
            myData.append(datum)
    print 'Done.'
    return myData


def get_parameter(prompt, valDefault, valType='str'):
    '''
    Needs prompt, valDefault and valType as strings.
    valType can be 'str', 'int', 'bool' or 'float'
    Returns val converted to valType
    '''
    while True:
        val = raw_input(prompt)
        if val == '':
            val = valDefault
        try:
            if valType == 'float':
                val = float(val)
            elif valType == 'int' :
                val = int(val)
            elif valType == 'bool' :
                if val in ['Y','Yes','y','yes','true','True']:
                    val = True
                else:
                    val = False
            return val
        except:
            print 'Wrong type of data entered.'
            continue
    
    
def normalize(myData, minData, maxData, minNorm=0, maxNorm=1):
    '''
    Normalizes data from minData-maxData to the range minNorm-max-norm
    Builds a list of (datum, norm_datum) tuples
    '''
    my_list = list()
    for datum in myData:
        norm_datum = minNorm + ((datum - minData) * (maxNorm - minNorm) / (maxData - minData))
        my_list.append((datum, norm_datum))
    return(my_list)


def save_my_data(myFile, myData, verboseFlag = False):
    '''
    Save in a csv file
    '''
    print 'Saving data...'
    my_output_file = myFile + '_out.csv'
    output_handle = open(my_output_file, 'w')
    output_handle.write('Data' + ',' + 'Transformed Data\n')
    for datum, output_datum in myData[:]:
        next_line = str(datum) + ',' + str(output_datum) + '\n'
        if verboseFlag:
            print next_line.rstrip()
        output_handle.write(next_line)
    output_handle.close()
    print 'Done.'




if __name__ == '__main__':
    main()
