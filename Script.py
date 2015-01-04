import Source.ServerDataParser
import sys

parser = Source.ServerDataParser.logFile_parser()
try:
    parser.parse(str(sys.argv[1]))
except:
    print 'File not found'