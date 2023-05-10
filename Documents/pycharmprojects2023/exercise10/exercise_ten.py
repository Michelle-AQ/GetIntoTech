import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)
len(pattern)
# pattern = os.path.join(hdir,'desktop')
# print(pattern, "*")

# TODO: Use the glob.glob() function to obtain the list of filenames

print(os.environ)

files = glob.glob(pattern)
print(files)
# add a 'for' loop to iterate each individual file - instead of a whole list


# pattern = find any file that is in the

# glob.glob appears to be activated already from the start and we believe this is what provided our list results

print(os.path.getsize(hdir))
# This retrieves the file size of the home directory (in bytes?)

path = glob.glob(hdir)
print(os.path.getsize('exercise_ten.py'))


# TODO: use os.path.getsize to find each file's size

file_name = 'exercise_ten.py'
file_stats = os.stat(file_name)
print(file_stats)
print(str(os))
# this appears to find the file size in bytes

byte_size = os.path.getsize(file_name)
mb_size = byte_size / (1024 * 1024)
print(mb_size)
# Result: '0.001049041748046875'



# Unable to check file sizes for files that are not in the Exercise 10 folder/directory


# TODO: Add a test to only display files that are not zero length
# notes as above
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename() - notes as above




