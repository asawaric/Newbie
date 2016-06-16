
Jupyter Notebook formerly known as IPython Notebook is an interactive computational environment, in which you can combine code execution, equations, plots, visualizations and explanatory text for data cleaning and transformation, numerical simulation, statistical modeling, machine learning etc.

Jupyter Architecture

The Jupyter Notebook is based on a set of open standards for interactive computing. These open standards can be leveraged by third party developers to build customized applications with interactive computing.

Notebook Document

'Notebook Documents' or 'notebooks' are documents produced by the Jupyter Notebook App which contain both computer code(e.g.Python) and rich text elements (paragraph, equations, figures, links etc.) Notebook documents are both human-readable documents containing the analysis description and the results(figures, tables, etc...)as well as executable documents which can be run to perform data analysis.

The Notebook document format

Jupyter Notebooks are an open document format based on JSON (JavaScript Object Notation). They contain complete record of the user's sessions and embed code, narrative text, equations and output.

Interactive computing protocol

The Notebook communicates with computational Kernels using the Interactive Computing Protocol, an open network protocol based on JSON data.

The Kernel

Kernels are processes that run interactive code in a particular programming language and return output to the user. Kernels also respond to tab completion and interospection requests.

Notebook dashboard

Notebook dashboard is the component which is shown first when launching Jupyter Notebook. It is mainly used to open notebook documents and to manage the running kernels (Visualize and Shutdown). It also has other features similar to a file manager, namely navigating folders and renaming/deleting files.

The information given on this page is sourced from following links. Check these links for more details.
http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html
http://jupyter.org/

Installing Jupyter Notebook

To install Jupyter, Python (Python 2.7 or Python 3.3 or greater) is a required. For this tutorial, Python 2.7.11 is recommended. On Debian-based systems (e.g.Ubuntu), install Jupyter with following command: apt-get install build-essential python-dev
For more details, see http://jupyter.readthedocs.io/en/latest/install.html

Launching Jupyter Notebook To launch Jupyter Notebook App:

1.Open terminal to open a terminal window.

2.Change the directory to one where you want to have your Jupyter Notebooks e.g. cd ~/My_local_repo/Python_Tyro

3.Type jupyter notebook to launch the Jupyter Notebook App (it will appear in a new browser window or tab).
