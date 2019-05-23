"""
clicore module for command line implementation
"""
import sys
import platform
import click


try:
    from jxcore import JxCore
    from ctxcore import CtxCore
except ImportError:
    from .jxcore import JxCore
    from .ctxcore import CtxCore

# Globals
__author__ = "Deepankumar Loganathan"
__email__ = "deepan0433@gmail.com"
__version__ = "0.0.8a"
__pypi__ = "https://pypi.org/project/jxctl/"

# pylint:  disable=anomalous-backslash-in-string
BANNER = """

      _          __  __
     (_)_ ______/ /_/ /
    / /\ \ / __/ __/ /
 __/ //_\_\\\__/\__/_/
|___/

"""  # noqa


# pylint: disable=unused-argument
def print_help(ctx, param, value):
    """
    Print the help message in terminal when options not passed
    """
    if value is False:
        return
    click.echo(ctx.get_help())
    ctx.exit()


# pylint: disable=unnecessary-pass
@click.group()
def main():
    """
    jxctl - jenkins command line tool
    """
    pass


# pylint: disable=unnecessary-pass
@main.group()
def get():
    """
    Get the jenkins resources(jobs, plugin, nodes, etc.. ) from jenkins
    """
    pass

# pylint: disable=unnecessary-pass
@main.group()
def context():
    """
    Set and Get Jenkins context
    """
    pass


@main.command()
def version():
    """
    Show the version and info of jxctl
    """
    click.echo(BANNER)
    click.echo("=========================================")
    click.echo("A cli interface for your Jenkins Instance")
    click.echo("=========================================")
    click.echo("jxctl version : " + __version__)
    click.echo("Python version : " + platform.python_version())
    click.echo("OS Version: " + platform.system() + " - " + platform.version())
    click.echo("Author: " + __author__)
    click.echo("Email: " + __email__)
    click.echo("PyPI: " + __pypi__)
    click.echo("=========================================")

# pylint: disable=redefined-builtin
@context.command("list")
@click.argument("context_name", required=False)
@click.option("-a", "--all", is_flag=True, required=False)
def list_context(all, context_name):
    """
    List available jenkins context
    """
    CtxCore().list_context(all, context_name)


@context.command("set")
@click.argument("context_name")
@click.option("--url",
              type=str,
              help="URL of the Jenkins instance")
@click.option("--user",
              type=str,
              help="Username of the Jenkins instance")
@click.option("--token", "--password",
              type=str,
              nargs=1,
              help="Access token / password of the username")
@click.option("--default",
              is_flag=True,
              help="Set as current context")
def set_context(context_name,
                url,
                user,
                token,
                default):  # pylint: disable=redefined-builtin
    """
    Set jenkins Context
    """
    CtxCore().set_context(context_name, url, user, token, default)


@context.command("delete")
@click.argument("context_name", type=str, nargs=1)
def delete_context(context_name):
    """
    Delete a jenkins context
    """
    CtxCore().delete_context(context_name)


@context.command()
def info():
    """
    Show the infomation about jenkins
    """
    click.echo(BANNER)
    JxCore().info()


@context.command("rename")
@click.argument("context_from")
@click.argument("context_to")
def rename_context(context_from, context_to):
    """
    Rename the jenkins context
    """
    CtxCore().rename_context(context_from, context_to)


@context.command("set-current")
@click.argument("context_name")
def set_current(context_name):
    """
    Set the current jenkins context
    """
    CtxCore().set_current_context(context_name)


@get.command()
@click.option("--count", "-c",
              is_flag=True,
              help="Returns number of jobs")
@click.option("--all",
              is_flag=True,
              help="List all(maven, \
                freestly, pipeline, \
                multi-branch, matrix and org) jobs")
@click.option("--maven",
              is_flag=True,
              help="List all maven style jobs")
@click.option("--freestyle",
              is_flag=True,
              help="List all freestyle jobs")
@click.option("--pipeline",
              is_flag=True,
              help="List all pipeline jobs")
@click.option("--multi-branch",
              is_flag=True,
              help="List all multi-branch pipeline jobs")
@click.option("--matrix",
              is_flag=True,
              help="List all matrix jobs")
@click.option("--org",
              is_flag=True,
              help="List all Organization jobs")
@click.option("-f", "--format", nargs=1, required=False,
              help="Display format(json/table). Default=json")
@click.option("--help",
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
         org,
         format):
    """
    Get list of job from jenkins
    """
    option_dist = {"all": all,
                   "maven": maven,
                   "freestyle": freestyle,
                   "pipeline": pipeline,
                   "multi-branch": multi_branch,
                   "matrix": matrix,
                   "org": org}
    option_list = []
    if any(option_dist.values()):
        if count:
            if not all:
                for item in option_dist:
                    if option_dist[item]:
                        option_list.append(item)
                JxCore().list_jobs(option_list, format, count=True)
            else:
                JxCore().list_all_jobs(format, count=True)
        elif all:
            JxCore().list_all_jobs(format)
        else:
            for item in option_dist:
                if option_dist[item]:
                    option_list.append(item)
            JxCore().list_jobs(option_list, format)
    else:
        print_help(ctx, None, value=True)


@get.command("folders")
@click.option("--format", "-f",
              nargs=1,
              required=False,
              help="Display format(json/table). Default=json")
@click.option("--count", "-c",
              is_flag=True,
              help="Returns the number of plugin installed")
def folders(format, count):
    """
    Get all folders from jenkins
    """
    JxCore().list_all_folders(format, count)


@get.command("plugins")
@click.option("--format", "-f",
              nargs=1,
              required=False,
              help="Display format(json/table). Default=json")
@click.option("--count", "-c",
              is_flag=True,
              help="Returns the number of plugin installed")
def plugins(format, count):
    """
    List all installed plugins from jenkins
    """
    if count:
        JxCore().list_all_plugins(format, count=True)
    else:
        JxCore().list_all_plugins(format)


@get.command("nodes")
@click.option("-f", "--format", nargs=1, required=False)
def nodes(format):
    """
    Get list of nodes from jenkins
    """
    JxCore().list_nodes(format)


@main.command()
@click.argument("node_name")
@click.option("--make-offline", is_flag=True)
@click.option("--make-online", is_flag=True)
@click.option("-m", "--message", required=False, help="Offline reason")
@click.option("-f", "--format", nargs=1, required=False,
              help="Display format(json/table). Default=json")
def node(node_name, make_offline, make_online, message, format):
    """
    Get node info and operation
    """
    if make_offline and not make_online:
        JxCore().node_action(node_name, "offline", message)
    elif not make_offline and make_online:
        JxCore().node_action(node_name, "online")
    else:
        JxCore().node_info(node_name, format)

# pylint:  disable=too-many-arguments
@main.command("job")
@click.argument("job_name")
@click.option("--build", is_flag=True, help="Triggers the build")
@click.option("--params",
              nargs=1,
              type=dict,
              help="Trigger build with params in Key:Value pair")
@click.option("--abort", nargs=1, type=int, help="Abort the build")
@click.option("--buildinfo", nargs=1, type=int, help="Get build info")
@click.option("--delete", "-d", is_flag=True, help="Delete a job")
@click.option("-f", "--format", nargs=1, required=False,
              help="Display format(json/table). Default=json")
def job(job_name, build, params, abort, buildinfo, delete, format):
    """
    Job info and operation
    """
    if buildinfo:
        JxCore().build_info(job_name, buildinfo, format)
    elif build:
        JxCore().trigger_job(job_name, params)
    elif delete:
        if click.confirm("Are you sure want to delete '{0}'".format("y" if delete else "N")):
            click.echo("Existing without deleting - {0}.".format(job_name))
            sys.exit(1)
        else:
            JxCore().delete_job(job_name)
    elif abort:
        JxCore()
    else:
        JxCore().job_info(job_name, format)


@main.command("plugin")
@click.argument("plugin_name")
def plugin(plugin_name):
    """
    Get plugin information
    """
    JxCore().get_plugin_info(plugin_name)


if __name__ == "__main__":
    main()


def start():
    """
    start method for cli to start with click top level command group
    """
    main()
