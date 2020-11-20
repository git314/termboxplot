# termboxplot

Terminal boxplots with UTF-8 characters.

```
1:◖─◦─◗ 
2:▁╭─╴╶─╮▁ 
3:▁▂ ▂▁
4:[=*=] 
```

# Features

1. Works with tidy data
2. Tufte inspired
3. One line only - making a nice display in Cloudwatch or other logging tools
4. Uses data piped with stdout making it compatable with a wider range of unix tools.

# Example 

```
# install requirements
sudo apt install miller

# download data
wget https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv

# install termboxplot
pip3 install termboxplot

# make box plots from data
cat mpg_ggplot2.csv | termbox  --g class --y hwy --option 4
```

# Install

## Dependancies

1. `miller`

```
sudo apt install miller
```

## Pip install

```
pip3 install termboxplot
```

