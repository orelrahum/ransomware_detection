# in this File we will make Unencrypted Text file
import glob
import random

global number_files
global name_file

# ADD all your VARS here
text_name = 'total.txt'
folder_output_name = 'total'
file_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET_Small\\" + text_name
output_path = "E:\\Dropbox\\Orel\\Ariel University\\final Project\\DATASET_Small\\Unencrypted\\"
start_random = 150
end_random = 400
number_files = 838

if __name__ == "__main__":
    with open(file_path, 'r') as file:
        num_of_lines = random.randint(start_random, end_random)
        num_total_lines = sum(1 for line in open(file_path))
        x = 0
        final_text = ""
        for lines in file.readlines():
            if x < num_of_lines:
                final_text = final_text + lines + "\n"
                #print(lines)
            if x == num_of_lines:
                name_file = output_path + "Unencrypted{}.txt ".format(number_files)
                write_file = open(name_file, "a+")
                write_file.write(final_text)
                write_file.close()
                num_total_lines = num_total_lines - num_of_lines
                num_of_lines = random.randint(start_random, end_random)
                if num_total_lines <= num_of_lines:
                    num_of_lines = num_total_lines
                number_files = number_files + 1
                x = 0
                final_text = ""
            x = x + 1
