import argh 

from .version import version_string 


def main(argv=None):
    if isinstance(argv, str):
        argv = argv.split()
    parser = argh.ArghParser()
    parser.prog = 'variform'
    parser.add_argument("--version", action="version", version=version_string)
    # parser.add_commands([])
    parser.dispatch(argv=argv, output_file=None)
    