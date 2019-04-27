"""
jxctl - command line implementations
"""
import platform
import click

# sys.path.append("..")

from pyfiglet import Figlet

try:
    from jxcore import JxCore
    from ctxcore import CtxCore
except ImportError:
    from .jxcore import JxCore
    from .ctxcore import CtxCore

# Globals
__author__ = 'Deepankumar Loganathan'
__email__ = 'deepan0433@gmail.com'
__version__ = '0.0.6'
__pypi__ = 'https://pypi.org/project/jxctl/'


def print_help(ctx, param, value):  # pylint: disable=unused-argument
    """
    Print the help message in terminal when options not passed
    """
    if value is False:
        return
    click.echo(ctx.get_help())
    ctx.exit()


@click.group()
def main():
    """
    Jenkins cli interface for Jenkins Instance
    """
    pass  # pylint: disable=unnecessary-pass


@main.command()
def version():
    """
    Show the version and info of jxctl
    """
    figlet = Figlet(font='smslant')
    click.echo(figlet.renderText('jxctl'))
    click.echo('A cli interface for your Jenkins Instance')
    click.echo("=========================================")
    click.echo('jxctl version : ' + __version__)
    click.echo('Python version : ' + platform.python_version())
    click.echo('OS Version: ' + platform.system() + ' - ' + platform.version())
    click.echo("Author: " + __author__)
    click.echo("Email: " + __email__)
    click.echo("PyPI: " + __pypi__)
    click.echo("=========================================")


@main.group()
def context():
    """
    Set and Get Jenkins context
    """
    pass  # pylint: disable=unnecessary-pass


@main.group()
def get():
    """
    List the Resources(jobs, plugin, build, nodes, etc.. ) from Jenkins context
    """
    pass  # pylint: disable=unnecessary-pass


@context.command()
@click.option('--url',
              type=str,
              help='URL of the Jenkins Instance')
@click.option('--user',
              type=str,
              help='Username of the Jenkins Instance')
@click.option('--token', '--password',
              type=str,
              nargs=1,
              help='Access Token / Password of the Username')
@click.option('--name',
              type=str,
              help='Name of the Jenkins Context')
def set(url, user, token, name):  # pylint: disable=redefined-builtin
    """
    Set Jenkins Context
    """
    CtxCore().set_context(url, user, token, name)


@context.command()
def info():
    """
    Show the infomation about your Jenkins Context
    """
    figlet = Figlet(font='smslant')
    click.echo(figlet.renderText('jxctl'))
    JxCore().info()


@get.command()
@click.option('--count', '-c',
              is_flag=True,
              help='Returns number of jobs')
@click.option('--all',
              is_flag=True,
              help='List all(maven, \
                freestly, pipeline, \
                multi-branch, matrix and org) jobs')
@click.option('--maven',
              is_flag=True,
              help='List all maven style jobs')
@click.option('--freestyle',
              is_flag=True,
              help='List all freestyle jobs')
@click.option('--pipeline',
              is_flag=True,
              help='List all pipeline jobs')
@click.option('--multi-branch',
              is_flag=True,
              help='List all multi-branch pipeline jobs')
@click.option('--matrix',
              is_flag=True,
              help='List all matrix jobs')
@click.option('--folders',
              is_flag=True,
              help='List all folders in Jenkins context')
@click.option('--org',
              is_flag=True,
              help='List all Organization jobs')
@click.option('--help',
              is_flag=True,
              expose_value=False,
              is_eager=False,
              callback=print_help,
              help="Print help message")
@click.pass_context
def jobs(ctx,  # pylint: disable=too-many-arguments
         count,
         all,  # pylint: disable=redefined-builtin
         maven,
         freestyle,
         pipeline,
         multi_branch,
         matrix,
         folders,
         org):
    """
    List Jenkins Context jobs
    """
    option_dist = {"all": all,
                   "maven": maven,
                   "freestyle": freestyle,
                   "pipeline": pipeline,
                   "multi-branch": multi_branch,
                   "matrix": matrix,
                   "folders": folders,
                   "org": org}
    option_list = []
    if any(option_dist.values()):
        if count:
            if not all:
                for item in option_dist:
                    if option_dist[item]:
                        option_list.append(item)
                JxCore().list_jobs(option_list, count=True)
            else:
                JxCore().list_all_jobs(count=True)
        elif all:
            JxCore().list_all_jobs()
        else:
            for item in option_dist:
                if option_dist[item]:
                    option_list.append(item)
            JxCore().list_jobs(option_list)
    else:
        print_help(ctx, None, value=True)


@main.command()
@click.argument('jobName')
@click.option('--debug', is_flag=True, help='Returns complete job info')
@click.option('--build', is_flag=True, help='Triggers the build')
@click.option('--report', is_flag=True, help='Generate HTML report')
@click.option('--buildinfo', nargs=1, type=int)
def job(jobname, debug, build, report, buildinfo):
    """
    Job level Operations
    """
    if buildinfo:
        JxCore().build_info(jobname, buildinfo)
    elif build:
        JxCore().job_build(jobname)
    else:
        JxCore().job_info(jobname, debug, report)


@get.command()
@click.option('--count', '-c',
              is_flag=True,
              help='Returns the number of plugin installed')
def plugins(count):
    """
    List all installed plugins of Jenkins Context
    """
    if count:
        JxCore().list_all_plugins(count=True)
    else:
        JxCore().list_all_plugins()


if __name__ == '__main__':
    main()


def start():
    """
    start jxctl
    """
    main()
