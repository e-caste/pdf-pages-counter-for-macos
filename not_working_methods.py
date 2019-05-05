# NOT WORKING METHODS FOR FUTURE REFERENCE:

# with sp.Popen(["mdls", "-name", "kMDItemFSName", "-name", "kMDItemNumberOfPages", path, "|", "cut", "-d=", "-f", "2", "|", "paste", "-", "-", "|", "cut", "-f", "2"], shell=True, stdout=sp.PIPE, stdin=sp.PIPE) as p:
#     p.wait(10)
#     lines = p.stdout.read().decode("ascii").splitlines()
#     print(lines)
#     for num in lines:
#         sum += int(num)


# mdls = sp.Popen(["mdls", "-name", "kMDItemFSName", "-name", "kMDItemNumberOfPages", path], stdout=sp.PIPE)
# cut1 = sp.Popen(["cut", "-d=", "-f", "2"], stdin=mdls.stdout, stdout=sp.PIPE)
# paste = sp.Popen(["paste", "-", "-"], stdin=cut1.stdout, stdout=sp.PIPE)
# cut2 = sp.Popen(["cut", "-f", "2"], stdin=paste.stdout, stdout=sp.PIPE)
# mdls.wait()
# cut1.wait()
# paste.wait()
#
# for line in cut2.stdout.read().decode("ascii").splitlines():
#     # sum += int(line)
#     print(line)


# from glob import glob as __g
# import re
# import sys
#
# if len(sys.argv[1:]) != 1:
#     print("Usage: pdf_pages_counter.py /path/to/folder")
#     exit(-1)
#
# path = str(sys.argv[1])
# pattern = re.compile(r"/Count\s+(\d+)")
#
# def count(path):
#     """
#     Takes one argument: the path where you want to search the files.
#     Returns a dictionary with the file name and number of pages for each file.
#     source: https://www.daniweb.com/programming/software-development/threads/152831/read-number-of-pages-in-pdf-files
#     """
#     pdf_files = __g(path + "\\" + '*.pdf')
#     vMsg = {}
#     for vPDFfile in pdf_files:
#         vPages = 0
#         content = open(vPDFfile, 'rb', 1).read().decode("ascii")
#         for match in pattern.finditer(content):
#             vPages = int(match.group(1))
#         vMsg[vPDFfile] = vPages
#     return vMsg
#
# if __name__ == '__main__':
#     print("The total number of pages of all PDFs in the given directory is " + str(len(count(path))))