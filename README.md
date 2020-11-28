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
cat mpg_ggplot2.csv | termbox  --g class --y hwy --option 1

1  │                     ──────◖──◦───◗─────────────────────────────
2  │                     ──────◖──◦───◗──────
3  │ ─────────◖──◦──◗───────────────
4  │                     ──◖──◦──◗
5  │          ─────────◖──◦──◗
6  │ ───────◖──◦──◗───────
7  │                ───────◖────◦───────────◗───────────────────────
+------------+---------+---------+---------+---------+---------+
| class      | hwy_min | hwy_p25 | hwy_p50 | hwy_p75 | hwy_max |
+------------+---------+---------+---------+---------+---------+
| compact    | 23      | 26      | 27      | 29      | 44      |
| midsize    | 23      | 26      | 27      | 29      | 32      |
| suv        | 12      | 17      | 18      | 19      | 27      |
| 2seater    | 23      | 24      | 25      | 26      | 26      |
| minivan    | 17      | 22      | 23      | 24      | 24      |
| pickup     | 12      | 16      | 17      | 18      | 22      |
| subcompact | 20      | 24      | 26      | 32      | 44      |
+------------+---------+---------+---------+---------+---------+

get help with `termbox --help`
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

