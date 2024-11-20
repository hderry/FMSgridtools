import click
from .lazy_group import LazyGroup

@click.group(
    cls = LazyGroup,
    lazy_subcommands = {"make_grid" : "make_grid.make_grid",
                        "regrid" : "regrid.regrid",
                        "make_mosaic" : "make_mosaic.make_mosaic"},
    help = click.style("help")
)

def gridtools() :
    pass

if __name__ == '__main__' :
    gridtools()
    

