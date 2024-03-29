import defopt

def variant_stats():
    pass

def main(argv=None):
    defopt.run({
        "variant-stats": variant_stats}, argv=argv)
    