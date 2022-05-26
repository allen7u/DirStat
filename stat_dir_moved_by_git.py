





import PySimpleGUI as sg
import sys,os,re,math
from datetime import datetime
from shutil import copy,copytree

copy_long_path_folder = False

class stat_dir:
    def __init__(self) -> None:
        self.copy_long_path_folder = False
        self.path = self.draw_input_path_dialog()
        self.config()
        self.append_files_and_folders_to_list()
        self.Total_File_Num()
        self.by_file_path_length()
        self.sort_files_names_against_folder_path_list()
        self.by_total_size()
        self.file_num_by_folder()
        
    def draw_input_path_dialog(self):
        layout = [
        [sg.Text('Path')],
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
        return path

    def config(self):
        # self.root = sys.argv[1]
        self.root = self.path
        # self.root_ = re.sub(r'\\','∕',sys.argv[1])
        self.root_ = re.sub(r'\\','∕',self.root)
        self.root_ = re.sub(r':','：',self.root_)
        print(self.root_)
        # print(self.root)
        with open( 'output\\' + 'Just_timestamp_for_start - ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write('')

        if len(sys.argv) > 2:
            self.ext_includes = sys.argv[2]
        else:
            self.ext_includes = ''

        if len(sys.argv) > 3:
            self.file_name_includes = sys.argv[3]
        else:
            self.file_name_includes = ''

    def append_files_and_folders_to_list(self):
        # print(os.walk(self.root))
        self.folder_and_file_path_list = []
        self.file_path_list = []

        self.file_names_against_folder_path_list = []

        if self.ext_includes:

            for p,d,f in os.walk(self.root,):
                if f:
                    for ff in f:
                        if self.file_name_includes:
                            if ff.endswith(self.ext_includes) and self.file_name_includes in ff:
                                self.folder_and_file_path_list.append(os.path.join(p,ff))
                                self.file_path_list.append(os.path.join(p,ff))
                                # break
                        
                        elif ff.endswith(self.ext_includes):
                            self.folder_and_file_path_list.append(os.path.join(p,ff))
                            self.file_path_list.append(os.path.join(p,ff))

        else:

            for p,d,f in os.walk(self.root,):
                # print(p,d,f)
                if d:
                    for dd in d:
                        # print(os.path.join(p,dd))
                        self.folder_and_file_path_list.append(os.path.join(p,dd))
                if f:
                    for ff in f:
                        # print(os.path.join(p,ff))
                        self.folder_and_file_path_list.append(os.path.join(p,ff))
                        self.file_path_list.append(os.path.join(p,ff))
                    self.file_names_against_folder_path_list.append( [p,f])

    def Total_File_Num(self):
        if self.ext_includes and self.file_name_includes:
            buf = 'Total File Num:' + str(len(self.file_path_list)) + '\n'
            with open( 'output\\' + self.ext_includes + ' with `' + self.file_name_includes + '`' + ' files_list - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
                f.write( buf + '\n'.join(self.file_path_list))
        elif self.ext_includes:
            buf = 'Total File Num:' + str(len(self.file_path_list)) + '\n'
            with open( 'output\\' + self.ext_includes + ' files_list - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
                f.write( buf + '\n'.join(self.file_path_list))
        else:
            buf = 'Total File Num:' + str(len(self.file_path_list)) + '\n'
            with open( 'output\\' + 'Folders_and_files_list - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
                f.write( buf + '\n'.join(self.folder_and_file_path_list))

    def by_file_path_length(self):
        # File_name_by_file_path_length
        self.file_path_list = sorted(self.file_path_list, key = lambda x: len(x), reverse = True)
        with open( 'output\\' + 'File_name_by_file_path_length - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write( '\n'.join( ': '.join( [ file_path, str(len(file_path)) ] ) for file_path in self.file_path_list  ) ) 
        with open( 'output\\' + 'File_name_by_file_path_length（260+） - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write( '\n'.join( ': '.join( [ file_path, str(len(file_path)) ] ) for file_path in self.file_path_list if len(file_path) >= 260 ) ) 

        self.folder_with_long_file_path = sorted( list( set( [ os.path.dirname(file_path) for file_path in self.file_path_list if len(file_path) >= 260] ) ), key = lambda x: len(x), reverse = True)
        with open( 'output\\' + 'Folder_name_by_file_path_length（260+） - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write( '\n'.join( ': '.join( [ folder_path, str(len( folder_path )) ] ) for folder_path in self.folder_with_long_file_path ) ) 
        with open( 'output\\' + 'Folder_name_by_file_path_length（260+） - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
            f.write( 'Filename,Length\n' +      '\n'.join(    ','.join( [    '"' + folder_path + '"'  , str(len( folder_path )) ] )     for folder_path in self.folder_with_long_file_path )            ) 

    def by_total_size(self):
        convert_size = self.convert_size
        get_size = self.get_size

        with open( 'output\\' + 'File_total_size_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write( '\n'.join( ': '.join( [ folder_path, convert_size(get_size( [folder_path, file_names_list])) ] ) for folder_path, file_names_list in self.file_names_against_folder_path_list  ) ) 
        with open( 'output\\' + 'File_total_size_by_folder - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
            f.write(    "Filename,Size\n"       +        '\n'.join(','.join( [    '"' +  folder_path  +'"'  , str(get_size( [folder_path, file_names_list])) ] )for folder_path, file_names_list in self.file_names_against_folder_path_list  ) ) 

        with open( 'output\\' + 'File_total_size_and_file_names_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            buf = []
            for folder_path, file_names_list in self.file_names_against_folder_path_list:
                file_paths_list = '\n'.join( '  ' + file_name for file_name in file_names_list )
                folder_path_and_size = ': '.join( [ folder_path, convert_size( get_size( [folder_path, file_names_list])) ] )
                
                buf.append( '\n'.join(   [ folder_path_and_size , file_paths_list ]   )  )

            f.write(  '\n\n'.join( buf )  )  

    def file_num_by_folder(self):
        self.file_names_against_folder_path_list = sorted( self.file_names_against_folder_path_list , key = lambda x: len( x[1] ) , reverse = True)
        with open( 'output\\' + 'File_num_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write( '\n'.join( ': '.join( [ folder_path, str(len(file_names_list)) ] )for folder_path, file_names_list in self.file_names_against_folder_path_list  ) ) 
        with open( 'output\\' + 'File_num_by_folder - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
            f.write("Filename,Filenum\n"+    '\n'.join( ','.join( [ '"'+folder_path+'"', str(len(file_names_list)) ] )for folder_path, file_names_list in self.file_names_against_folder_path_list  ) ) 

        with open( 'output\\' + 'File_name_by_folder - ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
            f.write( '\n\n'.join( '\n'.join( [ ': '.join( [ folder_path, str(len(file_names_list)) ] ) , '\n'.join( '  ' + file_name for file_name in file_names_list ) ] ) for folder_path, file_names_list in self.file_names_against_folder_path_list  ) ) 

    def get_size( self, arg ):
        dir_path, file_name_list = arg[0], arg[1]
        return sum( os.path.getsize(file_path) for file_path in [ os.path.join(dir_path, file_name) for file_name in file_name_list ] )
    
    def sort_files_names_against_folder_path_list(self):
        self.file_names_against_folder_path_list = sorted( self.file_names_against_folder_path_list , key = self.get_size , reverse = True)

    def convert_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def copy_long_path_folder(self):
        if copy_long_path_folder:
            error_counter = 1
            for folder_path in self.folder_with_long_file_path:
                # copytree(folder_path,'.'+folder_path.replace("F:\__books",''), dirs_exist_ok = True)
                try:
                    copytree(folder_path,'.'+folder_path.replace("F:\__books",''))
                except FileExistsError: 
                    copytree(folder_path,'./{}/'.format(error_counter) +folder_path.replace("F:\__books",''))
                    error_counter+=1

stat_dir()

input('raw')








# file_path_list = sorted(file_path_list, key = lambda x: len(x), reverse = True)
# copy( file_path_list[0], '.')
# xxx







# with open( 'output\\' + 'Folder_name_by_file_path_length（260+）_min - ' + str(datetime.now()).replace(':','-') + '.efu', 'w', encoding = 'utf-8') as f:
# 	f.write( 'Filename\n' +      '\n'.join(    ''.join( [    '"' + folder_path + '"' ] )     for folder_path in folder_with_long_file_path )            ) 





    # f.write( '\n\n'.join( '\n'.join( [ ': '.join( [ folder_path, str( get_size( [folder_path, file_names_list])) ] ) ] ) , '\n'.join( '  ' + file_name for file_name in file_names_list ) ] ) for folder_path, file_names_list in file_names_against_folder_path_list  )  





# buf1 = '\n'.join( ':'.join(folder_path, str(len(file_names_list))) for folder_path, file_names_list in file_names_against_folder_path_list)
# buf2 = '\n'.join( ':'.join(folder_path, file_names_list) for folder_path, file_names_list in file_names_against_folder_path_list)

ext_list = []
for fn in self.file_path_list:
    if re.findall(r'(?<=\.)\w{1,4}$',fn):
        ext_list.append( re.findall(r'(?<=\.)\w{1,4}$',fn)[0].lower() )

untypical_file_list = []
for fn in self.file_path_list:
    if not re.findall(r'(?<=\.)\w{1,4}$',fn):
        untypical_file_list.append( fn )

ext_type_list = list( set(ext_list) )
print(ext_type_list)
with open( 'output\\' + 'Ext_type_list - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write('\n'.join(ext_type_list))
# file_names_ext_wise_list = []
ext_type_and_file_name_list = []
counter = 0

for ext_type in ext_type_list:
    this_ext_type_fn_list = []
    for fn in self.file_path_list:
        if re.findall( r'(?i)\.' + ext_type + '$' ,fn):
            this_ext_type_fn_list.append(fn)
            counter += 1
    ext_type_and_file_name_list.append( [ext_type, this_ext_type_fn_list ] )

ext_type_and_file_name_list = sorted(ext_type_and_file_name_list, key = lambda x: len(x[1]), reverse = True )

self.folder_and_file_path_list = 'Total File Num:' + str(counter) + '\n'
output_ext_and_num_buf = 'Total File Num:' + str(counter) + '\n'
for ext_type, this_ext_type_fn_list in ext_type_and_file_name_list:
    self.folder_and_file_path_list += ext_type + ':\n' + str(len(this_ext_type_fn_list)) + '\n' + '\n'.join(this_ext_type_fn_list) + '\n\n'
    output_ext_and_num_buf += ext_type + ':' + str(len(this_ext_type_fn_list)) + '\n'
with open( 'output\\' + 'File_name_by_ext_type - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write(self.folder_and_file_path_list)
with open( 'output\\' + 'File_nums_by_exts_type - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write(output_ext_and_num_buf)

buf = 'Total File Num:' + str(len(untypical_file_list)) + '\n'
with open( 'output\\' + 'Untypical_files_list - ' + 'under ' + self.root_ + ' ' + str(datetime.now()).replace(':','-') + '.txt', 'w', encoding = 'utf-8') as f:
    f.write( buf + '\n'.join(untypical_file_list))

