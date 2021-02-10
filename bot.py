"""
This is the main file for running the bot on your local machine and also used for running on a server.
The bot needs a .env file for running as it asks for a DISCORD_TOKEN which needs to be written inside the .env file.
e.g. DISCORD_TOKEN=xyz
The bot file runs every command that a person asked in a server and for that it needs to be built in a asynchronous way but awaiting 
for a response to be given from that exact command.
"""
import os
from discord.ext import commands
from dotenv import load_dotenv
from scripts.mmm import media, mediana, moda, describe, plotmean
from scripts.corr import correlation
from scripts.normality import norm
from scripts.oneway import anova
import discord
import numpy as np
import distutils
import distutils.util

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="+", help_command=None)


@bot.command()
async def help(ctx, args=None):
    """
    +help command that returns all supported commands and details for each one of them if called passing the command name as an argument.
    e.g. +help describe
    """
    help_embed = discord.Embed(title=f"Hi {ctx.author.name}, this is my help section!")
    command_names_list = [x.name for x in bot.commands]

    if not args:
        """
        If there are no arguments, just list the commands:
        """
        help_embed.add_field(
            name="List of supported commands:",
            value="\n".join(
                [str(i + 1) + ". " + x.name for i, x in enumerate(bot.commands)]
            ),
            inline=False,
        )
        help_embed.add_field(
            name="Details",
            value="Type `+help <command name>` for more details about each command.",
            inline=False,
        )

    elif args in command_names_list:
        """
        If the argument is a command, get the help text from that command:
        """
        help_embed.add_field(name=args, value=bot.get_command(args).help)

    await ctx.send(embed=help_embed)


def check_args(param_rec: tuple, param_def: dict):
    lparam_rec = list(param_rec)
    param_name = list(param_def.keys())
    for algo in lparam_rec:
        if algo.partition("=")[0] in param_name:
            pass
        if algo.partition("=")[0] not in param_name:

            return "ERROR. Don't give me any argument cuz' I hate random things :rage:"
    dd_rec = [f.split("=") for f in lparam_rec]
    dd_rec = dict(dd_rec)
    param_def.update(dd_rec)
    for val in param_name:
        if bool(param_def.get(val)):
            pass
        if bool(param_def.get(val)) == False:

            return (
                "HEY. The parameter %s is needed but hasn't been given. C'mon, call me again and gimme :triumph:"
                % val
            )

    return param_def


@bot.command(name="mean", help="Generate mean from dataset.")
async def mean(ctx, *args):
    """
    Generate mean from given dataset.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False

    Returns
    -------
    dataframe
        Returns the mean for the given array or a dataframe containing means for every column
    """
    param_def = {"fcai": "False", "tpose": "False", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")

    avg = media(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
    )
    await ctx.send(avg)


@bot.command(name="median", help="Generate median from dataset.")
async def median(ctx, *args):
    """
    Generate median from given dataset.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False

    Returns
    -------
    dataframe
        Returns the median for the given array or a dataframe containing means for every column
    """
    param_def = {"fcai": "False", "tpose": "False", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")

    median = media(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
    )
    await ctx.send(median)


@bot.command(name="mode", help="Generate mode from the dataset.")
async def mode(ctx, *args):
    """
    Generate mode from given dataset.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False

    Returns
    -------
    dataframe
        Returns the mode for the given array or a dataframe containing means for every column
    """
    param_def = {"fcai": "False", "tpose": "False", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")

    mode = moda(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
    )
    await ctx.send(mode)


@bot.command(
    name="describe",
    help="Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.",
)
async def describe(ctx, *args):
    """
    Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False

    Returns
    -------
    dataframe
        Returns the descriptive statistics of the dataframe
    """
    param_def = {"fcai": "False", "tpose": "False", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")

    desc = describe(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
    )
    await ctx.send(desc)


@bot.command(name="plot_mean", help="Plot line from means.")
async def plot_mean(ctx, *args):
    """
    Generate mean for columns from given dataset and plot a line graph.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False

    Returns
    -------
    dataframe
        Returns the mean for every column and a figure with line plot for every mean calculated
    """
    param_def = {"fcai": "False", "tpose": "False", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")

    mean, idfig = plotmean(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
    )
    await ctx.send(mean)
    await ctx.send(file=discord.File(idfig))
    os.remove(idfig)


@bot.command(
    name="correlation",
    help="Compute pairwise correlation of columns, excluding NA/null values. Choose either pearson, kendall or spearman.",
)
async def correlation_matrix(ctx, *args):
    """
    Compute pairwise correlation of columns, excluding NA/null values. Choose either pearson, kendall or spearman.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    m_used : str
        Let user choose the method used for correlation. Options: pearson, kendall or spearman
    fcai: bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False

    Returns
    -------
    dataframe
        Returns the correlation matrix from a dataframe containing r value
    """
    param_def = {"fcai": "False", "tpose": "False", "m_used": "", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)
    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        m_used = argchecked.get("m_used")
        dataframe = argchecked.get("dataframe")

    corr_matrix = correlation(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
        m_used=m_used,
    )
    await ctx.send(corr_matrix)


@bot.command(
    name="normal", help="Test whether a sample differs from a normal distribution."
)
async def normality(ctx, *args):
    """
    Test whether a sample differs from a normal distribution.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False

    Returns
    -------
    dataframe
        Returns k2 and p value for each column tested for normality.
    """
    param_def = {"fcai": "False", "tpose": "False", "dataframe": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")

    tup = norm(
        sample=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
    )

    await ctx.send(f"k2 values and p values \n")

    for item in tup:
        np.set_printoptions(suppress=True)
        await ctx.send(item)


@bot.command(name="anova1w", help="Run 1-way ANOVA test")
async def oneway(ctx, *args):
    """
    Runs One-Way ANOVA for columns from a dataframe chosen by user. Each columns is a group.

    Parameters
    ----------
    dataframe : str
        Link for the dataframe chosen by user
    fcai : bool, optional
        Boolean that lets user choose if uses the First Columns As Index, defaults to False
    tpose: bool, optional
        Boolean that lets user choose whether the DF will transpose or not, defaults to False
    *colunas: str
        After tpose Boolean parameter, user will need to choose the columns from the dataframe to assign each group of ANOVA test. Columns must be separated by space and after tpose param.

    Returns
    -------
    dataframe
        Returns F statistics and p value.

    """
    param_def = {"dataframe": "", "fcai": "False", "tpose": "False", "colunas": ""}
    argchecked = check_args(param_rec=args, param_def=param_def)

    if type(argchecked) == str:
        await ctx.send(argchecked)
        return
    elif type(argchecked) == dict:
        fcai = argchecked.get("fcai")
        tpose = argchecked.get("tpose")
        dataframe = argchecked.get("dataframe")
        colunas = argchecked.get("colunas")
    anovar = anova(
        dataframe=dataframe,
        fcai=bool(distutils.util.strtobool(fcai)),
        tpose=bool(distutils.util.strtobool(tpose)),
        colunas=colunas.split(","),
    )

    await ctx.send(anovar)


bot.run(TOKEN)
