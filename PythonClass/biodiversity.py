{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone 2: Biodiversity Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.\n",
    "\n",
    "Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1\n",
    "Import the modules that you'll be using in this assignment:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2\n",
    "You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:\n",
    "- The scientific name of each species\n",
    "- The common names of each species\n",
    "- The species conservation status\n",
    "\n",
    "Load the dataset and inspect it:\n",
    "- Load `species_info.csv` into a DataFrame called `species`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "species = pd.read_csv('species_info.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Inspect each DataFrame using `.head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  category                scientific_name  \\\n",
      "0   Mammal  Clethrionomys gapperi gapperi   \n",
      "1   Mammal                      Bos bison   \n",
      "2   Mammal                     Bos taurus   \n",
      "3   Mammal                     Ovis aries   \n",
      "4   Mammal                 Cervus elaphus   \n",
      "\n",
      "                                        common_names conservation_status  \n",
      "0                           Gapper's Red-Backed Vole                 NaN  \n",
      "1                              American Bison, Bison                 NaN  \n",
      "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...                 NaN  \n",
      "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)                 NaN  \n",
      "4                                      Wapiti Or Elk                 NaN  \n"
     ]
    }
   ],
   "source": [
    "print(species.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 3\n",
    "Let's start by learning a bit more about our data.  Answer each of the following questions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many different species are in the `species` DataFrame?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Clethrionomys gapperi gapperi', 'Bos bison', 'Bos taurus', ...,\n",
       "       'Parthenocissus vitacea', 'Vitis californica',\n",
       "       'Tribulus terrestris'], dtype=object)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.scientific_name.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `category` in `species`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Mammal', 'Bird', 'Reptile', 'Amphibian', 'Fish', 'Vascular Plant',\n",
       "       'Nonvascular Plant'], dtype=object)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.category.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `conservation_status`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([nan, 'Species of Concern', 'Endangered', 'Threatened',\n",
       "       'In Recovery'], dtype=object)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.conservation_status.unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Let's start doing some analysis!\n",
    "\n",
    "The column `conservation_status` has several possible values:\n",
    "- `Species of Concern`: declining or appear to be in need of conservation\n",
    "- `Threatened`: vulnerable to endangerment in the near future\n",
    "- `Endangered`: seriously at risk of extinction\n",
    "- `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range\n",
    "\n",
    "We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>scientific_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Endangered</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>In Recovery</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>161</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Threatened</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  conservation_status  scientific_name\n",
       "0          Endangered               16\n",
       "1         In Recovery                4\n",
       "2  Species of Concern              161\n",
       "3          Threatened               10"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.groupby(['conservation_status']).scientific_name.count().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.\n",
    "\n",
    "Paste the following code and run it to see replace `None` with `No Intervention`:\n",
    "```python\n",
    "species.fillna('No Intervention', inplace=True)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "species.fillna('No Intervention', inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now run the same `groupby` as before to see how many species require `No Intervention`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>scientific_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Endangered</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>In Recovery</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>No Intervention</td>\n",
       "      <td>5633</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>161</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Threatened</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  conservation_status  scientific_name\n",
       "0          Endangered               16\n",
       "1         In Recovery                4\n",
       "2     No Intervention             5633\n",
       "3  Species of Concern              161\n",
       "4          Threatened               10"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.groupby(['conservation_status']).scientific_name.count().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.\n",
    "\n",
    "Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:\n",
    "```python\n",
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  conservation_status  scientific_name\n",
      "1         In Recovery                4\n",
      "4          Threatened               10\n",
      "0          Endangered               16\n",
      "3  Species of Concern              161\n",
      "2     No Intervention             5633\n"
     ]
    }
   ],
   "source": [
    "protection_counts = species.groupby('conservation_status')\\\n",
    ".scientific_name.count().reset_index()\\\n",
    ".sort_values(by='scientific_name')\n",
    "print(protection_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's create a bar chart!\n",
    "1. Start by creating a wide figure with `figsize=(10, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `conservation_status` in `protection_counts`\n",
    "5. Label the y-axis `Number of Species`\n",
    "6. Title the graph `Conservation Status by Species`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2bdfb276940>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax = plt.subplots(figsize=(10,4))\n",
    "x = protection_counts['conservation_status']\n",
    "y = species.groupby('conservation_status').scientific_name.count()\n",
    "#plt.bar(protection_counts['conservation_status'],species.groupby('conservation_status').scientific_name.count())\n",
    "plt.bar(x, y)\n",
    "plt.xticks(protection_counts['conservation_status'])\n",
    "plt.ylabel('Number of Spcies')\n",
    "plt.title('Conservation Status by Speices')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Are certain types of species more likely to be endangered?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  category                scientific_name  \\\n",
      "0   Mammal  Clethrionomys gapperi gapperi   \n",
      "1   Mammal                      Bos bison   \n",
      "2   Mammal                     Bos taurus   \n",
      "3   Mammal                     Ovis aries   \n",
      "4   Mammal                 Cervus elaphus   \n",
      "5   Mammal         Odocoileus virginianus   \n",
      "6   Mammal                     Sus scrofa   \n",
      "7   Mammal                  Canis latrans   \n",
      "8   Mammal                    Canis lupus   \n",
      "9   Mammal                    Canis rufus   \n",
      "\n",
      "                                        common_names conservation_status  \\\n",
      "0                           Gapper's Red-Backed Vole     No Intervention   \n",
      "1                              American Bison, Bison     No Intervention   \n",
      "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...     No Intervention   \n",
      "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "4                                      Wapiti Or Elk     No Intervention   \n",
      "5                                  White-Tailed Deer     No Intervention   \n",
      "6                                Feral Hog, Wild Pig     No Intervention   \n",
      "7                                             Coyote  Species of Concern   \n",
      "8                                          Gray Wolf          Endangered   \n",
      "9                                           Red Wolf          Endangered   \n",
      "\n",
      "  is_protected  \n",
      "0        False  \n",
      "1        False  \n",
      "2        False  \n",
      "3        False  \n",
      "4        False  \n",
      "5        False  \n",
      "6        False  \n",
      "7         True  \n",
      "8         True  \n",
      "9         True  \n"
     ]
    }
   ],
   "source": [
    "is_protected = []\n",
    "for row in species['conservation_status']:\n",
    "    if row != 'No Intervention':\n",
    "        is_protected.append('True')\n",
    "    else:\n",
    "        is_protected.append('False')\n",
    "        \n",
    "species['is_protected'] = is_protected\n",
    "print(species.head(10))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's group by *both* `category` and `is_protected`.  Save your results to `category_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_counts = species.groupby(['category','is_protected']).count().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_counts` using `head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    category is_protected  scientific_name  common_names  conservation_status\n",
      "0  Amphibian        False               73            73                   73\n",
      "1  Amphibian         True                7             7                    7\n",
      "2       Bird        False              442           442                  442\n",
      "3       Bird         True               79            79                   79\n",
      "4       Fish        False              116           116                  116\n"
     ]
    }
   ],
   "source": [
    "print(category_counts.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:\n",
    "- `columns` is `is_protected`\n",
    "- `index` is `category`\n",
    "- `values` is `scientific_name`\n",
    "\n",
    "Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot = category_counts.pivot(\n",
    "    index='category', \n",
    "    columns='is_protected', \n",
    "    values='scientific_name').reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_protected           category  False  True\n",
      "0                     Amphibian     73     7\n",
      "1                          Bird    442    79\n",
      "2                          Fish    116    11\n",
      "3                        Mammal    176    38\n",
      "4             Nonvascular Plant    328     5\n",
      "5                       Reptile     74     5\n",
      "6                Vascular Plant   4424    46\n"
     ]
    }
   ],
   "source": [
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `.columns` property to  rename the categories `True` and `False` to something more description:\n",
    "- Leave `category` as `category`\n",
    "- Rename `False` to `not_protected`\n",
    "- Rename `True` to `protected`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category  not_protected  protected\n",
      "0          Amphibian             73          7\n",
      "1               Bird            442         79\n",
      "2               Fish            116         11\n",
      "3             Mammal            176         38\n",
      "4  Nonvascular Plant            328          5\n",
      "5            Reptile             74          5\n",
      "6     Vascular Plant           4424         46\n"
     ]
    }
   ],
   "source": [
    "category_pivot.columns = ['category','not_protected','protected']\n",
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            category  not_protected  protected  percent_protected\n",
      "0          Amphibian             73          7           0.087500\n",
      "1               Bird            442         79           0.151631\n",
      "2               Fish            116         11           0.086614\n",
      "3             Mammal            176         38           0.177570\n",
      "4  Nonvascular Plant            328          5           0.015015\n",
      "5            Reptile             74          5           0.063291\n",
      "6     Vascular Plant           4424         46           0.010291\n"
     ]
    }
   ],
   "source": [
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:\n",
    "- Is the data numerical or categorical?\n",
    "- How many pieces of data are you comparing?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:\n",
    "\n",
    "||protected|not protected|\n",
    "|-|-|-|\n",
    "|Mammal|?|?|\n",
    "|Bird|?|?|\n",
    "\n",
    "Create a table called `contingency` and fill it in with the correct numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[38, 176], [79, 442]]\n"
     ]
    }
   ],
   "source": [
    "contingency = [[38, 176],\n",
    "              [79, 442]]\n",
    "print(contingency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:\n",
    "```py\n",
    "from scipy.stats import chi2_contingency\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now run `chi2_contingency` with `contingency`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(0.5810483277947567, 0.445901703047197, 1, array([[ 34.06530612, 179.93469388],\n",
       "        [ 82.93469388, 438.06530612]]))"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chi2_contingency(contingency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like this difference isn't significant!\n",
    "\n",
    "Let's test another.  Is the difference between `Reptile` and `Mammal` significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(5.139702724228909,\n",
       " 0.02338465214871547,\n",
       " 1,\n",
       " array([[ 11.59385666,  67.40614334],\n",
       "        [ 31.40614334, 182.59385666]]))"
      ]
     },
     "execution_count": 149,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "contingency = [[5, 74],\n",
    "               [38, 176]]\n",
    "chi2_contingency(contingency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "            scientific_name                            park_name  observations\n",
      "0        Vicia benghalensis  Great Smoky Mountains National Park            68\n",
      "1            Neovison vison  Great Smoky Mountains National Park            77\n",
      "2         Prunus subcordata               Yosemite National Park           138\n",
      "3      Abutilon theophrasti                  Bryce National Park            84\n",
      "4  Githopsis specularioides  Great Smoky Mountains National Park            85\n"
     ]
    }
   ],
   "source": [
    "observation = pd.read_csv('observations.csv')\n",
    "print(observation.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str1 = 'This string contains Sheep'\n",
    "'Sheep' in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 152,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str2 = 'This string contains Cows'\n",
    "'Sheep' in str2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  category                scientific_name  \\\n",
      "0   Mammal  Clethrionomys gapperi gapperi   \n",
      "1   Mammal                      Bos bison   \n",
      "2   Mammal                     Bos taurus   \n",
      "3   Mammal                     Ovis aries   \n",
      "4   Mammal                 Cervus elaphus   \n",
      "\n",
      "                                        common_names conservation_status  \\\n",
      "0                           Gapper's Red-Backed Vole     No Intervention   \n",
      "1                              American Bison, Bison     No Intervention   \n",
      "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...     No Intervention   \n",
      "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
      "4                                      Wapiti Or Elk     No Intervention   \n",
      "\n",
      "  is_protected  is_sheep  \n",
      "0        False     False  \n",
      "1        False     False  \n",
      "2        False     False  \n",
      "3        False      True  \n",
      "4        False     False  \n"
     ]
    }
   ],
   "source": [
    "species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)\n",
    "print(species.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Select the rows of `species` where `is_sheep` is `True` and examine the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1139</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex acetosella</td>\n",
       "      <td>Sheep Sorrel, Sheep Sorrell</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2233</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Festuca filiformis</td>\n",
       "      <td>Fineleaf Sheep Fescue</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3014</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3758</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex acetosella</td>\n",
       "      <td>Common Sheep Sorrel, Field Sorrel, Red Sorrel,...</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3761</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex paucifolius</td>\n",
       "      <td>Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4091</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Carex illota</td>\n",
       "      <td>Sheep Sedge, Smallhead Sedge</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4383</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Potentilla ovina var. ovina</td>\n",
       "      <td>Sheep Cinquefoil</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4446</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            category              scientific_name  \\\n",
       "3             Mammal                   Ovis aries   \n",
       "1139  Vascular Plant             Rumex acetosella   \n",
       "2233  Vascular Plant           Festuca filiformis   \n",
       "3014          Mammal              Ovis canadensis   \n",
       "3758  Vascular Plant             Rumex acetosella   \n",
       "3761  Vascular Plant            Rumex paucifolius   \n",
       "4091  Vascular Plant                 Carex illota   \n",
       "4383  Vascular Plant  Potentilla ovina var. ovina   \n",
       "4446          Mammal      Ovis canadensis sierrae   \n",
       "\n",
       "                                           common_names conservation_status  \\\n",
       "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "1139                        Sheep Sorrel, Sheep Sorrell     No Intervention   \n",
       "2233                              Fineleaf Sheep Fescue     No Intervention   \n",
       "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "3758  Common Sheep Sorrel, Field Sorrel, Red Sorrel,...     No Intervention   \n",
       "3761   Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock     No Intervention   \n",
       "4091                       Sheep Sedge, Smallhead Sedge     No Intervention   \n",
       "4383                                   Sheep Cinquefoil     No Intervention   \n",
       "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "\n",
       "     is_protected  is_sheep  \n",
       "3           False      True  \n",
       "1139        False      True  \n",
       "2233        False      True  \n",
       "3014         True      True  \n",
       "3758        False      True  \n",
       "3761        False      True  \n",
       "4091        False      True  \n",
       "4383        False      True  \n",
       "4446         True      True  "
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species[species.is_sheep == True]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [],
   "source": [
    "sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "      <th>category</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>219</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>109</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>117</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>48</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>67</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>39</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>22</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>25</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>126</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>76</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>119</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>221</td>\n",
       "      <td>Mammal</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            scientific_name                            park_name  \\\n",
       "0           Ovis canadensis            Yellowstone National Park   \n",
       "1           Ovis canadensis                  Bryce National Park   \n",
       "2           Ovis canadensis               Yosemite National Park   \n",
       "3           Ovis canadensis  Great Smoky Mountains National Park   \n",
       "4   Ovis canadensis sierrae            Yellowstone National Park   \n",
       "5   Ovis canadensis sierrae               Yosemite National Park   \n",
       "6   Ovis canadensis sierrae                  Bryce National Park   \n",
       "7   Ovis canadensis sierrae  Great Smoky Mountains National Park   \n",
       "8                Ovis aries               Yosemite National Park   \n",
       "9                Ovis aries  Great Smoky Mountains National Park   \n",
       "10               Ovis aries                  Bryce National Park   \n",
       "11               Ovis aries            Yellowstone National Park   \n",
       "\n",
       "    observations category                                       common_names  \\\n",
       "0            219   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "1            109   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "2            117   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "3             48   Mammal                       Bighorn Sheep, Bighorn Sheep   \n",
       "4             67   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "5             39   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "6             22   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "7             25   Mammal                        Sierra Nevada Bighorn Sheep   \n",
       "8            126   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "9             76   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "10           119   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "11           221   Mammal  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)   \n",
       "\n",
       "   conservation_status is_protected  is_sheep  \n",
       "0   Species of Concern         True      True  \n",
       "1   Species of Concern         True      True  \n",
       "2   Species of Concern         True      True  \n",
       "3   Species of Concern         True      True  \n",
       "4           Endangered         True      True  \n",
       "5           Endangered         True      True  \n",
       "6           Endangered         True      True  \n",
       "7           Endangered         True      True  \n",
       "8      No Intervention        False      True  \n",
       "9      No Intervention        False      True  \n",
       "10     No Intervention        False      True  \n",
       "11     No Intervention        False      True  "
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sheep_observations = observation.merge(sheep_species)\n",
    "sheep_observations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.\n",
    "\n",
    "This is the total number of sheep observed in each park over the past 7 days."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>282</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             park_name  observations\n",
       "0                  Bryce National Park           250\n",
       "1  Great Smoky Mountains National Park           149\n",
       "2            Yellowstone National Park           507\n",
       "3               Yosemite National Park           282"
      ]
     },
     "execution_count": 199,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()\n",
    "obs_by_park"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a bar chart showing the different number of observations per week at each park.\n",
    "\n",
    "1. Start by creating a wide figure with `figsize=(16, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `park_name` in `obs_by_park`\n",
    "5. Label the y-axis `Number of Observations`\n",
    "6. Title the graph `Observations of Sheep per Week`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2bdfcedbc18>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16, 4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(obs_by_park)), obs_by_park.observations.values)\n",
    "ax.set_xticks(range(len(obs_by_park)))\n",
    "ax.set_xticklabels(obs_by_park.park_name.values)\n",
    "plt.ylabel('Number of Observations')\n",
    "plt.title('Observations of Sheep per Week')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage points.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.\n",
    "\n",
    "Use <a href=\"https://s3.amazonaws.com/codecademy-content/courses/learn-hypothesis-testing/a_b_sample_size/index.html\">Codecademy's sample size calculator</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).\n",
    "\n",
    "Remember that \"Minimum Detectable Effect\" is a percent of the baseline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33.333333333333336\n",
      "15\n",
      "890\n"
     ]
    }
   ],
   "source": [
    "min_detectable_effect = (100 * 0.05) / 0.15\n",
    "print(min_detectable_effect)\n",
    "baseline = 15\n",
    "print(baseline)\n",
    "sample_size = 890\n",
    "print(sample_size)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>282</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             park_name  observations\n",
       "0                  Bryce National Park           250\n",
       "1  Great Smoky Mountains National Park           149\n",
       "2            Yellowstone National Park           507\n",
       "3               Yosemite National Park           282"
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obs_by_park"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.56\n",
      "1.755424063116371\n"
     ]
    }
   ],
   "source": [
    "bryce_nation_park = sample_size / 250\n",
    "print(bryce_nation_park)\n",
    "yellowstone_nation_park = sample_size / 507\n",
    "print(yellowstone_nation_park)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
