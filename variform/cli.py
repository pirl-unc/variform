import argh 


def main(argv=None):
    if isinstance(argv, str):
        argv = argv.split()
    argh.dispatch_command(lambda: None, argv=argv, output_file=None)
    