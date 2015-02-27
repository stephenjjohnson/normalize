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
    my_data = list()
    for line in fhandle:
        data_items = line.split(',')
        for datum in data_items:
            datum = float(datum)
            my_data.append(datum)
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
    my_output_file = my_file + '_normalized.csv'
    output_handle = open(my_output_file, 'w')
    output_handle.write('Data' + ',' + 'Normalized\n')
    for datum, norm_datum in my_norm_data[:]:
        next_line = str(datum) + ',' + str(norm_datum) + '\n'
        output_handle.write(next_line)
    output_handle.close()

    
    

# Get some data to normalize
# my_data = (0,1,2,3,4,5,6,7,8,9,10,11)
my_data = read_my_data(get_file())
print 'My data:', my_data, '\n'

# Get the smallest datum to use in the normalization
my_default = str(min(my_data))
floor = get_parameter('What is the smallest value you wish to consider? [Enter to use smallest datum]:', my_default, 'float')

# floor = raw_input('What is the smallest value you wish to consider? [Enter to use smallest datum]:')
# if floor == '':
    # floor = min(my_data)
# else:
    # try:
        # floor = float(floor)
    # except:
        # print 'Not a number. Using smallest datum...'
        # floor = min(my_data)

        
# Get the largest datum to use in the normalization
my_default = str(max(my_data))
ceiling = get_parameter('What is the largest value you wish to consider? [Enter to use largest datum]:', my_default, 'float')

# ceiling = raw_input('What is the largest value you wish to consider? [Enter to use largest datum]:')
# if ceiling == '':
    # ceiling = max(my_data)
# else:
    # try:
        # ceiling = float(ceiling)
    # except:
        # print 'Not a number. Using largest datum...'
        # ceiling = max(my_data)        

print 'Data range to normalize:', floor, '-', ceiling, '\n'


# Get the smallest normalized value
min = get_parameter('What is the smallest value you wish to normalize to? [Enter to use 0]:', '0', 'float')

# min = raw_input('What is the smallest value you wish to normalize to? [Enter to use 0]:')
# if min == '':
    # min = 0
# else:
    # try:
        # min = float(min)
    # except:
        # print 'Not a number. Using zero...\n'
        # min = 0
        
# Get the largest normalized value
max = get_parameter('What is the smallest value you wish to normalize to? [Enter to use 1]:', '1', 'float')

# max = raw_input('What is the largest value you wish to normalize to? [Enter to use 1]:')
# if max == ''
    # max = 1
# else:
    # try:
        # max = float(max)
    # except:
        # print 'Not a number. Using 1...\n'
        # max = 1

print 'Normalized range: ', min, '-', str(max), '\n'

my_norm_data = normalize(my_data, floor, ceiling, min, max)
print 'Normalized data:', my_norm_data


save_my_norm_data('', my_norm_data)
    

    
 



