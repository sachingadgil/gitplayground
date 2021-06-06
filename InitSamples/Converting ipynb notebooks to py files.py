# Remove all special Charators using powershell using this command
# Dir | Rename-Item -NewName { $_.name -replace "&",""}
# Replace & with any charactor you want to replace
# Second argument is charactor to be replaced - in this case nothign to replace
# command doesnot work for full stop as first argument

# Use Jupyter notebook for executing following <- This did not work reliably
# import nbconvert
# import os
# os.chdir('C:\\Users\\your\\directory')
#
# !jupyter nbconvert --to script *.ipynb
# exclamation runs this cell as command line

# Open Anaconda Python environemnt in Terminal <- This worked :)
# Navigate to your directory
# Use following command
# jupyter nbconvert --to script *.ipynb