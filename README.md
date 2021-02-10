# Stats doer
Hi! My name is BOT and I'm an Stats Doer type of BOT!
Yes, that's all I do, stats!

The main purpose of this bot is to run statistical tests and some descriptive statistic for a given dataset.

# How to use
First of all, you need to call me onto your own Discord server.
You can call my through this [LINK](https://discord.com/api/oauth2/authorize?client_id=805567313398726698&permissions=8&scope=bot).

After calling me I will be able to answer all your calls!
Ask for help typing +help and I will show you all I can do for you!
Call me typing +help commandname and I will give you a brief description of the command!

If you need further help and want to read about the commands, the statistic behind and even more, take some time and read my command list down below!

You still need more help? No worries, contact my founder and maintainer, he is always ready to answer your questions no matter what.

# Commands and parameters

| COMMAND NAME | PARAMETER | RETURN |
| -------------|-----------|------- |
| +help | <p>command_name: str, optional<br>Requieres a command name from the list | Help section from specific command name if passed |
| +mean | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Mean from given array or mean for every column if dataframe has been passed |
| +mode | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Mode from given array or mean for every column if dataframe has been passed |
| +median | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Median from given array or mean for every column if dataframe has been passed |
| +describe | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN value |
| +plot_mean | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Mean calculated for every column of given dataframe and line plot with mean in dataframe's own order |
| +correlation | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>m_used: str<br> > Method used for correlation. Available options: kendall, pearson and spearman<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | Correlation matrix containing r values |
| +normal | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False | k2 and p values for every colum tested from dataframe |
| +anova1w | <p>dataframe: str<br> > Complete link for a RAW .csv file from a Github repository<br><br>fcai: bool, optional<br> > Boolean that lets user choose if uses the First Columns As Index, defaults to False<br><br>tpose: bool, optional<br> > Boolean that lets user choose whether the DF will transpose or not, defaults to False<br><br>colunas: str<br> > String containing list of columns referring as each group to be compared in the test separated by comma without spaces e.g. colunas=colunaG,colunaF,colunaR | F statistics and p value from One-way ANOVA using groups passed in colunas |
  
# Contact Information
My maintainer's name is Thomaz Guadagnini, you can see him clicking [HERE](http://thomazgr.github.io) or contact through his email [HERE](mailto:thomaz@vivaldi.net) which is thomaz@vivaldi.net.
