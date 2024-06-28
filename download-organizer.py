import os
import shutil

# If you need to change your downloads folder route change in this line.
downloads_folder = os.path.expanduser('~/Downloads')

# These are some common extensions and the names of the folders that they are going to be saved in.
extensions_folders = {
    'jpg': 'Imágenes',
    'jpeg': 'Imágenes',
    'png': 'Imágenes',
    'gif': 'Imágenes',
    'mp4': 'Videos',
    'mov': 'Videos',
    'mkv': 'Videos',
    'mp3': 'Música',
    'wav': 'Música',
    'pdf': 'Documentos',
    'doc': 'Documentos',
    'docx': 'Documentos',
    'ppt': 'Presentaciones',
    'pptx': 'Presentaciones',
    'xls': 'Hojas de Cálculo',
    'xlsx': 'Hojas de Cálculo',
    'zip': 'Archivos Comprimidos',
    'rar': 'Archivos Comprimidos',
    'kra': 'Dibujos Krita',
}

def organize_downloads(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            if ext in extensions_folders:
                dest_folder = os.path.join(folder, extensions_folders[ext])
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                shutil.move(file_path, os.path.join(dest_folder, filename))

if __name__ == "__main__":
    organize_downloads(downloads_folder)
