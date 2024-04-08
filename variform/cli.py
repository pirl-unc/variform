import argh 
from .version import print_version 


def main(argv=None):
    if isinstance(argv, str):
        argv = argv.split()
    
    parser = argh.ArghParser()
    parser.prog = 'variform'
    parser.add_commands([print_version])
    parser.dispatch(argv=argv, output_file=None)
    