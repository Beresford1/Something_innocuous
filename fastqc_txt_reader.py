import os
import re

# This is a script to read things from the .txt files generated by fastqc analysis. These files contain all of the
# informative statistics about read quality etc per file. The key piece of information that I'm after is percentage
# of sequence duplication, which is the number of sequences that are duplicated in the files.

# The line in the txt file that I'm after is, verbatum, as follows:

# Total Duplication Percentage   <x>
# Although it's prefixed by an annoying hash(#)

# I need to read the txt file, read that line specifically, and record all four values for each library in another file
# I'm going to need to use a dictionary per sample, then print that dictionary.

# This is a list of the paths to the raw files from the home dir, need to add a line about each dir ending with *...
dirs = ['/fastdata/bop15job/160204_FastQ/cat_sequences/fastqc/',
        '/fastdata/bop15job/160204_FastQ/cat_trsequences/fastqc/',
        '/fastdata/bop15job/160208_FastQ/cat_sequences/fastqc/',
        '/fastdata/bop15job/160204_FastQ/cat_trsequences/fastqc/']

# creates a new txt file if there isn't one in the home dir since I didn't specify a path, specifying w' so that the
# contents can be overwritten (specify 'a' if this file exists already & you want to keep it!)
summary_stats = open('fastqc_1_sum.txt', 'w')
# This could easily become modular, e.g. user specified name for a txt file...

# We'll need this dictionary later
summary_dict = {}

for directory in dirs:
    fastqc_dirs = [x for x in os.listdir(directory) if x.endswith('fastqc')]
    # This bit finds & lists all of the fastqc files in the directories specified above in the dirs[] list

    for dir in fastqc_dirs:
        each_dir_path = [directory + dir + '/']
        # This bit makes a list of new paths from the original 4 dirs, adding the fastqc files & a '/'

        for path in each_dir_path:
            txt_file = [x for x in os.listdir(path) if x.endswith('a.txt')]
            # Here we find all of the txt files within the fastqc files

            for file in txt_file:
                txt_paths = [path + file]
                # Then generate yet another list of txt files & their pathways

                for summary_file in txt_paths:
                    # And now here is where things really kick off

                    # Openning all of the txt files,
                    file_name = open(summary_file)

                    # reading them all,
                    file_contents = file_name.read()

                    # and then searching for the #Total duplication percentage line, '#Total' is unique enough.
                    pdsl = file_contents.find('#Total Duplicate Percentage')

                    # From this we define the location of the percentage which has way too many numbers after the '.'
                    location = pdsl + 28

                    # Then here we read the percentage to 3 decimal places.
                    percentage_duplication = file_contents[location : location + 6]

                    #print(dir + ' ' + percentage_duplication + '\n')

                    if dir in summary_dict.keys():
                        summary_dict[dir].append(percentage_duplication)
                    else:
                        summary_dict[dir] = [percentage_duplication]

for entry in summary_dict.keys():
    summary_stats.write(entry + '\n')

summary_stats.close()