import os
import zipfile

def make_zip(source_dir, output_filename):
    ignored_patterns = {
        'node_modules',
        '.git',
        'dist',
        '.gradle',
        'build',
        '.DS_Store',
        'bun.lockb',
        '__pycache__'
    }
    
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    
    count = 0
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Prune ignored directories (allow .github)
            dirs[:] = [d for d in dirs if d not in ignored_patterns and (d == '.github' or not d.startswith('.'))]
            
            for file in files:
                if file in ignored_patterns or file.endswith('.zip') or file.endswith('.log'):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
                count += 1
                
    file_size_mb = os.path.getsize(output_filename) / (1024 * 1024)
    print(f"Successfully archived {count} files into {output_filename} ({file_size_mb:.2f} MB)")

if __name__ == '__main__':
    source = '/app/applet'
    out = '/app/applet/public/a1-live-cricket-project.zip'
    make_zip(source, out)
