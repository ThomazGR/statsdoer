<title>Stats doer Docs</title>
<link rel="shortcut icon" href="favicon.ico">  
<link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicons/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicons/favicon-16x16.png">

# Welcome to my documentation!

Hiya, my name is Stats doer. How ya doin'? I am a Discord bot created with [discord.py](https://discordpy.readthedocs.io/en/latest/index.html)!

My main purpose in this world is to give a little easier path to anyone on a Discord server that wants to run statistical tests without having to code or use an statistical software. With my help you can run some (by now) statistical tests with a simple command, passing me the parameters so I can do all the math-statistics for you in the background while you enjoy a cup of coffee (or tea if you prefer (or water if you prefer)).

If you arrived here in this documentation but hasn't seen my code, you can checkout on my [Github repo](https://github.com/ThomazGR/statsdoer).

If you really want to read my documentation then take a seat and enjoy everything that my [creator](thomazgr.github.io) has written about me but be careful because some things may or may not be true (**just kidding**).

## How to use

First of all, you need to call me onto your own Discord server.
You can call my through this [link](https://discord.com/api/oauth2/authorize?client_id=805567313398726698&permissions=8&scope=bot).

After calling me I will be able to answer all your calls!
Ask for help typing +help and I will show you all I can do for you!
Call me typing +help command_name and I will give you a brief description of the command!

If you need further help and want to read about the commands, the statistic behind and even more, take some time and read my command list down below!

You still need more help? No worries, contact my founder and maintainer, he is always ready to answer your questions no matter what.

## Installing and running locally

If you don't want to call me into your own server it's ok, but you will need to follow some steps to have my source code running locally on your machine.

First you need to create a Discord bot account on your own. That can be achieved read the [Discord Developer documentation](https://discord.com/developers/docs/intro) or the [discord.py guide](https://discordpy.readthedocs.io/en/latest/discord.html).

After that, download/clone the source code from my [Github repo](https://github.com/ThomazGR/statsdoer) and open the `.env` file changing `DISCORD_TOKEN` to your bot's own token.

You will also need to install all the requirements from **requirements.txt**. Open Terminal, navigate to the directory that you downloaded/cloned the source code and run on terminal `pip install -r requirements.txt` or `pip3 install -r requirements.txt` if you are using pip3 as default for python3.

Finishing installation run on Terminal `python bot.py` or `python3 bot.py` if you are using python3 on $PATH.

This is the end of configuration and installation to get the bot running. Now you can use your own bot OAuth2, get him to join the server you want and enjoy the commands!

## Commands and parameters

| COMMAND NAME | PARAMETER | RETURN |
| -------------|-----------|------- |
| +help | **command_name**: _str, optional_<br>Requieres a command name from the list | Help section from specific command name if passed |
| +mean | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Mean from given array or mean for every column if dataframe has been passed |
| +mode | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Mode from given array or mean for every column if dataframe has been passed |
| +median | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Median from given array or mean for every column if dataframe has been passed |
| +describe | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN value |
| +plot_mean | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Mean calculated for every column of given dataframe and line plot with mean in dataframe's own order |
| +correlation | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**m_used**: _str_<br> > Method used for correlation. Available options: kendall, pearson and spearman<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Correlation matrix containing r values |
| +normal | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | k2 and p values for every colum tested from dataframe |
| +anova1w | **dataframe**: _str_<br> > Complete link for a RAW .csv file from a Github repository<br><br>**fcai**: _bool, optional_<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>**tpose**: _bool, optional_<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False<br><br>**colunas**: _str_<br> > String containing list of columns referring as each group to be compared in the test separated by comma without spaces e.g. `colunas=colunaG,colunaF,colunaR` | F statistics and p value from One-way ANOVA using groups passed in colunas |

## Contact Information
My maintainer's name is Thomaz Guadagnini, you can see him clicking [here](http://thomazgr.github.io) or contact through his email [here](mailto:thomaz@vivaldi.net) which is thomaz@vivaldi.net.