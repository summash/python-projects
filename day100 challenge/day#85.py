import argparse 
import requests
import shutil
parser=argparse.ArgumentParser()

#add command line arguments
parser.add_argument('url', help='url of the file to download')
parser.add_argument('output',help='by which name do you want to save your file')
parser.add_argument('-o','--optional',help='name of the file',default=None)


args=parser.parse_args()


def download_file(url,local_filename):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

print(args.url)
print(args.output)
download_file(args.url,args.output)