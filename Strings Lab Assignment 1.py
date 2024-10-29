#Christopher Kenny
#CS 175
#Strings Lab Assignment 1; May be useful for quiz

def main():
  with open('test_scores.csv', 'r') as data:
    rows = data.readlines()

    all_data = []

    for row in rows: 
      values = row.strip().split(',')
      scores = [int(score) for score in values[0:]]
      all_data.append(scores)
      total = sum(scores)
      average = sum(scores) / len(scores)
      print(row.split())
      print(f'Average: {average}')

main()
