



























import PySimpleGUI as sg
import sys,os,re,math
from datetime import datetime
from shutil import copy,copytree

layout = [
    [sg.Text('Path')],
    # [sg.Input(sys.argv[1],key='path')],
    [sg.Input('F:\\Anaconda_Play\\DirStat\\asd',key='path')],
    # [sg.Input(key='path')],
    [sg.Button('submit'), sg.Button('cancel')],
    # [sg.Text('输出：'), sg.Text(key='OUTPUT')]
]
window = sg.Window('Tree Maker GUI', layout)
while True:
    event, values = window.read()
    # print(event)
    # print(values)
    if event in (None, 'submit', 'cancel'):
        path = values['path']
        break
    # else:
        # window['OUTPUT'].update(values['INPUT1'])

copy_long_path_folder = False

# root = sys.argv[1]
root = path
# root_ = re.sub(r'\\','∕',sys.argv[1])
root_ = re.sub(r'\\','∕',root)
root_ = re.sub(r':','：',root_)
print(root_)
# print(root)
with open( 'Just_timestamp_for_start - ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write('')

if len(sys.argv) > 2:
    ext_includes = sys.argv[2]
else:
    ext_includes = ''

if len(sys.argv) > 3:
    file_name_includes = sys.argv[3]
else:
    file_name_includes = ''


# print(os.walk(root))
folder_and_file_path_list = []
file_path_list = []

file_names_against_folder_path_list = []

if ext_includes:

    for p,d,f in os.walk(root,):
        if f:
            for ff in f:
                if file_name_includes:
                    if ff.endswith(ext_includes) and file_name_includes in ff:
                        folder_and_file_path_list.append(os.path.join(p,ff))
                        file_path_list.append(os.path.join(p,ff))
                        # break
                
                elif ff.endswith(ext_includes):
                    folder_and_file_path_list.append(os.path.join(p,ff))
                    file_path_list.append(os.path.join(p,ff))

else:

    for p,d,f in os.walk(root,):
        # print(p,d,f)
        if d:
            for dd in d:
                # print(os.path.join(p,dd))
                folder_and_file_path_list.append(os.path.join(p,dd))
        if f:
            for ff in f:
                # print(os.path.join(p,ff))
                folder_and_file_path_list.append(os.path.join(p,ff))
                file_path_list.append(os.path.join(p,ff))
            file_names_against_folder_path_list.append( [p,f])



# file_path_list = sorted(file_path_list, key = lambda x: len(x), reverse = True)
# copy( file_path_list[0], '.')
# xxx

if ext_includes and file_name_includes:
    buf = 'Total File Num:' + str(len(file_path_list)) + '\n'
    with open( ext_includes + ' with `' + file_name_includes + '`' + ' files_list - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
        f.write( buf + '\n'.join(file_path_list))
elif ext_includes:
    buf = 'Total File Num:' + str(len(file_path_list)) + '\n'
    with open( ext_includes + ' files_list - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
        f.write( buf + '\n'.join(file_path_list))
else:
    buf = 'Total File Num:' + str(len(file_path_list)) + '\n'
    with open( 'Folders_and_files_list - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
        f.write( buf + '\n'.join(folder_and_file_path_list))

# File_name_by_file_path_length
file_path_list = sorted(file_path_list, key = lambda x: len(x), reverse = True)
with open( 'File_name_by_file_path_length - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( '\n'.join( ': '.join( [ file_path, str(len(file_path)) ] ) for file_path in file_path_list  ) ) 
with open( 'File_name_by_file_path_length（260+） - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( '\n'.join( ': '.join( [ file_path, str(len(file_path)) ] ) for file_path in file_path_list if len(file_path) >= 260 ) ) 

folder_with_long_file_path = sorted( list( set( [ os.path.dirname(file_path) for file_path in file_path_list if len(file_path) >= 260] ) ), key = lambda x: len(x), reverse = True)
with open( 'Folder_name_by_file_path_length（260+） - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( '\n'.join( ': '.join( [ folder_path, str(len( folder_path )) ] ) for folder_path in folder_with_long_file_path ) ) 
with open( 'Folder_name_by_file_path_length（260+） - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
    f.write( 'Filename,Length\n' +      '\n'.join(    ','.join( [    '"' + folder_path + '"'  , str(len( folder_path )) ] )     for folder_path in folder_with_long_file_path )            ) 

if copy_long_path_folder:
    error_counter = 1
    for folder_path in folder_with_long_file_path:
        # copytree(folder_path,'.'+folder_path.replace("F:\__books",''), dirs_exist_ok = True)
        try:
            copytree(folder_path,'.'+folder_path.replace("F:\__books",''))
        except FileExistsError: 
            copytree(folder_path,'./{}/'.format(error_counter) +folder_path.replace("F:\__books",''))
            error_counter+=1

# with open( 'Folder_name_by_file_path_length（260+）_min - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
# 	f.write( 'Filename\n' +      '\n'.join(    ''.join( [    '"' + folder_path + '"' ] )     for folder_path in folder_with_long_file_path )            ) 


def get_size( arg ):
    dir_path, file_name_list = arg[0], arg[1]
    return sum( os.path.getsize(file_path) for file_path in [ os.path.join(dir_path, file_name) for file_name in file_name_list ] )
file_names_against_folder_path_list = sorted( file_names_against_folder_path_list , key = get_size , reverse = True)


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

with open( 'File_total_size_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( '\n'.join( ': '.join( [ folder_path, convert_size(get_size( [folder_path, file_names_list])) ] ) for folder_path, file_names_list in file_names_against_folder_path_list  ) ) 
with open( 'File_total_size_by_folder - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
    f.write(    "Filename,Size\n"       +        '\n'.join(','.join( [    '"' +  folder_path  +'"'  , str(get_size( [folder_path, file_names_list])) ] )for folder_path, file_names_list in file_names_against_folder_path_list  ) ) 

with open( 'File_total_size_and_file_names_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    buf = []
    for folder_path, file_names_list in file_names_against_folder_path_list:
        file_paths_list = '\n'.join( '  ' + file_name for file_name in file_names_list )
        folder_path_and_size = ': '.join( [ folder_path, convert_size( get_size( [folder_path, file_names_list])) ] )
        
        buf.append( '\n'.join(   [ folder_path_and_size , file_paths_list ]   )  )

    f.write(  '\n\n'.join( buf )  )  
    # f.write( '\n\n'.join( '\n'.join( [ ': '.join( [ folder_path, str( get_size( [folder_path, file_names_list])) ] ) ] ) , '\n'.join( '  ' + file_name for file_name in file_names_list ) ] ) for folder_path, file_names_list in file_names_against_folder_path_list  )  



file_names_against_folder_path_list = sorted( file_names_against_folder_path_list , key = lambda x: len( x[1] ) , reverse = True)

with open( 'File_num_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( '\n'.join( ': '.join( [ folder_path, str(len(file_names_list)) ] )for folder_path, file_names_list in file_names_against_folder_path_list  ) ) 
with open( 'File_num_by_folder - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
    f.write("Filename,Filenum\n"+    '\n'.join( ','.join( [ '"'+folder_path+'"', str(len(file_names_list)) ] )for folder_path, file_names_list in file_names_against_folder_path_list  ) ) 

with open( 'File_name_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( '\n\n'.join( '\n'.join( [ ': '.join( [ folder_path, str(len(file_names_list)) ] ) , '\n'.join( '  ' + file_name for file_name in file_names_list ) ] ) for folder_path, file_names_list in file_names_against_folder_path_list  ) ) 

# buf1 = '\n'.join( ':'.join(folder_path, str(len(file_names_list))) for folder_path, file_names_list in file_names_against_folder_path_list)
# buf2 = '\n'.join( ':'.join(folder_path, file_names_list) for folder_path, file_names_list in file_names_against_folder_path_list)

ext_list = []
for fn in file_path_list:
    if re.findall(r'(?<=\.)\w{1,4}$',fn):
        ext_list.append( re.findall(r'(?<=\.)\w{1,4}$',fn)[0].lower() )

untypical_file_list = []
for fn in file_path_list:
    if not re.findall(r'(?<=\.)\w{1,4}$',fn):
        untypical_file_list.append( fn )

ext_type_list = list( set(ext_list) )
print(ext_type_list)
with open( 'Ext_type_list - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write('\n'.join(ext_type_list))
# file_names_ext_wise_list = []
ext_type_and_file_name_list = []
counter = 0

for ext_type in ext_type_list:
    this_ext_type_fn_list = []
    for fn in file_path_list:
        if re.findall( r'(?i)\.' + ext_type + '$' ,fn):
            this_ext_type_fn_list.append(fn)
            counter += 1
    ext_type_and_file_name_list.append( [ext_type, this_ext_type_fn_list ] )

ext_type_and_file_name_list = sorted(ext_type_and_file_name_list, key = lambda x: len(x[1]), reverse = True )

folder_and_file_path_list = 'Total File Num:' + str(counter) + '\n'
output_ext_and_num_buf = 'Total File Num:' + str(counter) + '\n'
for ext_type, this_ext_type_fn_list in ext_type_and_file_name_list:
    folder_and_file_path_list += ext_type + ':\n' + str(len(this_ext_type_fn_list)) + '\n' + '\n'.join(this_ext_type_fn_list) + '\n\n'
    output_ext_and_num_buf += ext_type + ':' + str(len(this_ext_type_fn_list)) + '\n'
with open( 'File_name_by_ext_type - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write(folder_and_file_path_list)
with open( 'File_nums_by_exts_type - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write(output_ext_and_num_buf)

buf = 'Total File Num:' + str(len(untypical_file_list)) + '\n'
with open( 'Untypical_files_list - ' + 'under ' + root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( buf + '\n'.join(untypical_file_list))

