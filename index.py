from pandas import DataFrame, read_csv

def main():
  df = read_csv(r'./beers.csv')
  print('Mean IBU', df['ibu'].mean())
  
  maxName = df['name'][df['ibu'] == df['ibu'].max()].values[0]
  print('Name of beer with highest IBU', maxName)

  print(df.axes)

if __name__ == "__main__":
  main()
