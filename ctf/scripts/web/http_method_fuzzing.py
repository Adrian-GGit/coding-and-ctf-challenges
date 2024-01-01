import uuid
import requests
import argparse
from tqdm import tqdm

HTTP_VERBS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "HEAD",
    "CONNECT",
    "OPTIONS",
    "TRACE",
]
IDENT = 0
TAB = "\t"
NEWLINE = "\n"

def beautiful_output(result_dict):
    output_string = ""
    for key, value in result_dict.items():
        output_string += TAB * IDENT + str(key) + NEWLINE
        if isinstance(value, dict):
            output_string += beautiful_output(value, IDENT + 1)
        elif isinstance(value, list):
            for el in value:
                if isinstance(value, dict):
                    output_string += beautiful_output(value, IDENT + 1)
                else:
                    output_string += TAB * (IDENT + 1) + str(el) + NEWLINE
        else:
            output_string += TAB * (IDENT + 1) + str(value) + NEWLINE
    return output_string

def write_to_output_file(output_file_path, output_string):
    wrote_to_file = True
    try:
        with open(output_file_path, "w") as file:
            file.write(output_string)
            file.close()
    except IOError:
        print("[!] Couldn't access output file - printing results directly:")
        wrote_to_file = False
    return wrote_to_file

def print_to_console(output_string):
    print("[*] Successful fuzzed url:")
    print(output_string)


def setup_parameters(args):
    error_message = args.errormessage
    error_code = args.errorcode
    url = args.url
    output_file_path = args.outputnormalfile
    directories = ["/"]
    if args.directories:
        dirs = args.directories
        dirs.replace(" ", "")
        dirs = dirs.split(",")
        directories.extend(dirs)

    if not error_message:
        rand_uuid_dir = "/" + str(uuid.uuid4())
        res = requests.get(url=url + rand_uuid_dir)
        error_message = res.text

    return {
        "error_message": error_message,
        "error_code": error_code,
        "url": url,
        "output_file_path": output_file_path,
        "directories": directories,
    }

def fuzz(error_message, error_code, url, output_file_path, directories):
    result_dict = {}
    for http_method in tqdm(HTTP_VERBS):
        for dir in tqdm(directories, leave=False):
            directory = dir if "/" in dir else "/" + dir
            res = requests.request(
                method=http_method,
                url=url + directory,
            )
            status_code = res.status_code

            if error_message not in res.text and str(status_code) != error_code:
                to_add = http_method + ": " + str(status_code)
                if directory in result_dict:
                    result_dict[directory].append(to_add)
                else:
                    result_dict[directory] = [to_add]

    output_string = beautiful_output(result_dict)
    if output_file_path:
        wrote_to_file = write_to_output_file(output_file_path, output_string)
        if not wrote_to_file:
            print_to_console(output_string)
    else:
        print_to_console(output_string)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="HTTPVFuzzer",
        description="HTTP method fuzzing",
        epilog="Have fun",
    )
    parser.add_argument("-u", "--url", required=True, help="Base url to fuzz")
    parser.add_argument("-d", "--directories", help="Directories to fuzz - separated with ',' - spaces don't matter")
    parser.add_argument("-eM", "--errormessage", help="Error message popping up on not existing dir")
    parser.add_argument("-eC", "--errorcode", help="Error code on not existing dir", default="404")
    parser.add_argument("-oN", "--outputnormalfile", help="Output file to which result is being written")
    # TODO: implement threading
    parser.add_argument("-t", "--threads", help="Number of threads", default=10)
    # TODO: read from /usr/share/wordlists/wfuzz/general/http_methods.txt if "only_conventional" is set on False
    parser.add_argument("-oC", "--onlyconventional", help="Only fuzz conventional http methods", default=True)
    args = parser.parse_args()

    fuzz_kwargs = setup_parameters(args)
    fuzz(**fuzz_kwargs)