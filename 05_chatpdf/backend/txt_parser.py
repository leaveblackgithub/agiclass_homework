def read_from_txt(file_path):
    result=[]
    row_count=0
    with open(file_path, 'r',encoding='utf-8') as file:
        for row in file.readlines():
            row_read=row.strip()
            if(len(row_read)>0):
                result.append(row_read)
                row_count+=1
    print( f"\nread {row_count} rows from {file_path}")
    return result
        
def write_to_txt(file_path, data):
    with open(file_path, 'w',encoding='utf-8') as file:
        row_count=0
        for row in data:
            row_to_write=row.strip()
            if(len(row_to_write)>0):
                file.write(row_to_write+'\n')
                row_count+=1
    print(  f"\nwrite {row_count} rows to {file_path}")