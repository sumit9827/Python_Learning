import zipapp

file_1 = open('tar_file_1.txt', 'w')
file_1.write("this is File 1 TXT file")

file_2 = open('tar_file_2.txt', 'w')
file_2.write("this is File 2 TXT file")

file_3 = open('tar_file_3.txt', 'w')
file_3.write("this is File 3 TXT file")

file_1 = open('tar_file_1.txt', 'r')
file_2 = open('tar_file_2.txt', 'r')
file_3 = open('tar_file_3.txt', 'r')
print(file_1.read())
print(file_2.read())
print(file_3.read())

file_1.close()
file_2.close()
file_3.close()

my_tar_file = zip.open('mytar.tar', 'w')
my_tar_file.add('tar_file_1.txt')
my_tar_file.add('tar_file_2.txt')
my_tar_file.add('tar_file_3.txt')


my_tar_file = tarfile.open('mytar.tar', 'r')

file_extract_1 = my_tar_file.extractfile("tar_file_1.txt")
print("File1 has been extracted")

print("Content of the file")
print(file_extract_1.read())
my_tar_file.close()
file_extract_1.close()
