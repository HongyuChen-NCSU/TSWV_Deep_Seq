'''
Using fastQC to check raw sequencing reads in mutiple files
Writed on Jun 25th 2020 
Author: Hongyu Chen
'''
import os
import sys
import subprocess


# FastQC_out_path = /mnt/c/Users/Na/Desktop/TSWV_Deep_seq/FastQC_out
# Raw_data_path = /mnt/c/Users/Na/Desktop/TSWV_Deep_seq/TSWV_vector_alt_data_L1
# Cmd = fastqc --outdir FastQC_out_path Raw_data_path/*.fastq 

if __name__ == '__main__':
    
    batch = False # processing multiple samples?
        
    main_path = '/mnt/c/Users/Na/Desktop/TSWV_Deep_seq/TSWV_vector_alt_data_L1/'
    out_dir = '/mnt/c/Users/Na/Desktop/TSWV_Deep_seq/FastQC_out/'
        
    '''Get all directories in main_path'''
    dir_list = os.listdir(main_path)
    # print(dir_list)
    

    for dir in dir_list:
        os.chdir(out_dir)
        cmd1 = 'mkdir ' + dir
        subprocess.run(cmd1, shell = True)  
        os.chdir(main_path + dir)
        cmd = 'fastqc --outdir ' + out_dir + dir + ' *.fastq'  
        subprocess.run(cmd, shell = True)
        os.chdir(main_path)