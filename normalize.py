#  Normalize a dataset

from __future__ import division

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
    val_type can be 'str', 'int' or 'float'
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
            return val
        except:
            print 'Wrong type of data entered.'
            continue
    
    
def normalize(my_data, floor, ceiling, min_norm=0, max_norm=1):
    '''
    Normalizes data from floor-ceiling to the range min_norm-max-norm
    Builds a list of (datum, norm_datum) tuples
    '''
    my_list = list()
    for datum in my_data:
        norm_datum = (min_norm + (datum - floor) * (max_norm - min_norm)) / (ceiling - floor)
        my_list.append((datum, norm_datum))
    return(my_list)
    

def save_my_norm_data(my_file, my_norm_data):
    '''
    Save in a csv file
    '''
    print 'Saving data...'
    my_output_file = my_file + '_normalized.csv'
    output_handle = open(my_output_file, 'w')
    output_handle.write('Data' + ',' + 'Normalized\n')
    for datum, norm_datum in my_norm_data[:]:
        next_line = str(datum) + ',' + str(norm_datum) + '\n'
        output_handle.write(next_line)
    output_handle.close()
    print 'Done.'

    
    

# Get some data to normalize
# my_data = (0,1,2,3,4,5,6,7,8,9,10,11)
my_data = read_my_data(get_file())
print 'My data:', my_data, '\n'

# Get the smallest and largest data to use in the normalization
my_default = str(min(my_data))
floor = get_parameter('What is the smallest value to consider? [Enter to use smallest datum]:', my_default, 'float')

my_default = str(max(my_data))
ceiling = get_parameter('What is the largest value to consider? [Enter to use largest datum]:', my_default, 'float')

print 'Data range to normalize:', floor, '-', ceiling, '\n'


# Get the smallest and largest normalized values
min = get_parameter('What is the smallest value to normalize to? [Enter to use 0]:', '0', 'float')
max = get_parameter('What is the largest value to normalize to? [Enter to use 1]:', '1', 'float')
print 'Normalized range: ', min, '-', str(max), '\n'

# Normalize the data using the supplied parameters
my_norm_data = normalize(my_data, floor, ceiling, min, max)
print 'Normalized data:', my_norm_data

# Save in a file
save_my_norm_data('', my_norm_data)

    
 



