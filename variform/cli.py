import defopt


def variant_stats():
    pass


def main(argv=None):
    if isinstance(argv, str):
        argv = argv.split()

    defopt.run({"variant-stats": variant_stats}, argv=argv)
