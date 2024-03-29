import defopt

def variant_stats():
    pass

def main(argv=None):
    if type(argv) is str:
        argv = argv.split()
        
    defopt.run({
        "variant-stats": variant_stats}, argv=argv)
    