
```
# install requirements
sudo apt install miller

# download data
wget https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv

# install termboxplot
pip3 install termboxplot

# make box plots from data
cat mpg_ggplot2.csv | termbox  --g class --y hwy --option 4
``
