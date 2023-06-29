import click
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader
import os
import logging


@click.group()
def main():
    pass


@main.command()
@click.argument("folder")
@click.option(
    "-f", "--file", "file", help="Only render specified file", default=None, type=str
)
@click.option(
    "-v",
    "--verbose",
    "verbose",
    help="Debug render values, don't write to file",
    is_flag=True,
    default=False,
    type=bool,
)
def render(folder, file, verbose):
    """render a folder"""
    env = Environment(
        loader=FileSystemLoader(folder),
        variable_start_string="{|",
        variable_end_string="|}",
    )

    if file:
        relative_path = os.path.join(folder, file)
        if os.path.exists(relative_path):
            print(env.get_template(file).render(**os.environ))
        else:
            logging.debug("file {} not exist".format(relative_path))
        return

    for sub_file in os.listdir(folder):
        relative_path = os.path.join(folder, sub_file)
        if os.path.isfile(relative_path):
            result = env.get_template(sub_file).render(**os.environ)
            if verbose:
                print(result)
            else:
                output_path = os.path.join("values", relative_path)
                output_dirpath = os.path.dirname(output_path)
                if not os.path.exists(output_dirpath):
                    os.makedirs(output_dirpath)
                with open(output_path, "w") as output_write:
                    output_write.writelines(result)


if __name__ == "__main__":
    load_dotenv()
    main()
