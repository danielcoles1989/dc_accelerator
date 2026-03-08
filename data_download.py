import os
import requests
from stream_unzip import stream_unzip

def download_and_extract_gravity_data(url, output_dir):
    
    # function for yielding files
    def zipped_chunks():
        # stream=True ensures we don't load the massive ZIP into memory
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            
            # Yield bytes in 64KB chunks
            for chunk in response.iter_content(chunk_size=65536):
                if chunk:
                    yield chunk

    print(f"Downloading from: {url}")
    print(f"Destination dir: {os.path.abspath(output_dir)}\n")
    
    # pass each file from stream_unzip
    for file_name, file_size, unzipped_chunks in stream_unzip(zipped_chunks()):
        
        # stream_unzip bytes so we decode it to a string
        if isinstance(file_name, bytes):
            file_name_str = file_name.decode('utf-8', errors='replace')
        else:
            file_name_str = file_name
            
        file_name_str = file_name_str.lstrip('/')
        file_path = os.path.join(output_dir, file_name_str)
        
        # check for subfolder in the downloaded zipfile
        if file_name_str.endswith('/'):
            os.makedirs(file_path, exist_ok=True)
            
            for _ in unzipped_chunks:
                pass
            continue
            
        # make files
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        print(f"Unzipping file: {file_name_str}.")
        
        # write paths to files
        with open(file_path, 'wb') as f:
            for chunk in unzipped_chunks:
                f.write(chunk)
                
    print("\nDownload and unzip complete.")

if __name__ == '__main__':
    # directory for full raw data
    DATA_URL = "https://www.cepii.fr/DATA_DOWNLOAD/gravity/data/Gravity_csv_V202211.zip"
    
    # Llocal data folder
    DEST_DIR = "./data"
    
    # try incase link fails
    try:
        download_and_extract_gravity_data(DATA_URL, DEST_DIR)
    except:
        print(f"File cannot be downloaded please download gravity csv from: https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=8")