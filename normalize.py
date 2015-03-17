'''
A Python program to normalize a dataset.
Accepts a comma separated list of numbers then asks for the lowest and 
highest values to consider, and the minimum and maximum values to normalize to.
Hitting ENTER at any of the prompts after the data have been loaded will set a sensible default value.
'''

# from __future__ import division

def main():
    # Get some data to normalize
    # my_data = (0,1,2,3,4,5,6,7,8,9,10,11)
    my_data = read_my_data(get_file())
    print 'My data:', my_data, '\n'

    # Get the smallest and largest data to use in the normalization
    # Smallest
    my_default = str(min(my_data))
    minData = get_parameter('What is the smallest value to consider? [Enter to use smallest datum]:', my_default, 'float')
    # Largest
    my_default = str(max(my_data))
    maxData = get_parameter('What is the largest value to consider? [Enter to use largest datum]:', my_default, 'float')
    print 'Data range to normalize:', minData, '-', maxData, '\n'


    # Get the smallest and largest normalized values
    minNorm = get_parameter('What is the smallest value to normalize to? [Enter to use 0]:', '0', 'float')
    maxNorm = get_parameter('What is the largest value to normalize to? [Enter to use 1]:', '1', 'float')
    print 'Normalized range: ', minNorm, '-', str(maxNorm), '\n'
    
    # Should we print the data out?
    verbose_flag = get_parameter('Do you want to see the data while saving? (y/N) ', False, 'bool')

    # Normalize the data using the supplied parameters
    my_norm_data = normalize(my_data, minData, maxData, minNorm, maxNorm)
#    print 'Normalized data:', my_norm_data

    # Save in a file
    save_my_data('normalized', my_norm_data, verbose_flag)  


def get_file() :
    '''
    Get a file name to examine
    '''
    my_file = raw_input('Enter a file name: ')
    try:
        fhandle = open(my_file, 'r')
        return fhandle
    except:
        print 'Invalid file name:', my_file
        quit()


def read_my_data(fhandle):
    '''
    Read the data into a list
    '''
    print 'Loading data...'
    my_data = list()
    for line in fhandle:
        data_items = line.split(',')
        for datum in data_items:
            datum = float(datum)
            my_data.append(datum)
    print 'Done.'
    return my_data


def get_parameter(prompt, val_default, val_type='str'):
    '''
    Needs prompt, val_default and val_type as strings.
    val_type can be 'str', 'int', 'bool' or 'float'
    Returns val converted to val_type
    '''
    while True:
        val = raw_input(prompt)
        if val == '':
            val = val_default
        try:
            if val_type == 'float':
                val = float(val)
            elif val_type == 'int' :
                val = int(val)
            elif val_type == 'bool' :
                if val in ['Y','Yes','y','yes','true','True']:
                    val = True
                else:
                    val = False
            return val
        except:
            print 'Wrong type of data entered.'
            continue
    
    
def normalize(my_data, minData, maxData, min_norm=0, max_norm=1):
    '''
    Normalizes data from minData-maxData to the range min_norm-max-norm
    Builds a list of (datum, norm_datum) tuples
    '''
    my_list = list()
    for datum in my_data:
        norm_datum = (min_norm + (datum - minData) * (max_norm - min_norm)) / (maxData - minData)
        my_list.append((datum, norm_datum))
    return(my_list)
    

def save_my_data(my_file, my_data, verbose_flag = False):
    '''
    Save in a csv file
    '''
    print 'Saving data...'
    my_output_file = my_file + '_out.csv'
    output_handle = open(my_output_file, 'w')
    output_handle.write('Data' + ',' + 'Transformed Data\n')
    for datum, output_datum in my_data[:]:
        next_line = str(datum) + ',' + str(output_datum) + '\n'
        if verbose_flag:
            print next_line.rstrip()
        output_handle.write(next_line)
    output_handle.close()
    print 'Done.'



    
if __name__ == '__main__':
    main()

    
    
 



