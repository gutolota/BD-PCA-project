import random
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(sys.argv[0])
    parser.add_argument('-k', '--number_of_clusters', help='How many centroids will the data have?', default=5, nargs='?', type=int)
    parser.add_argument('-n', '--number_of_data', help='How many rows will be generated', default=1000, type=int, nargs='?')
    parser.add_argument('-o', '--output_file', help='The output file', nargs='?', default='data.csv', type=str)
    parser.add_argument('-nd', '--number_of_dimensions', help='How many features will it have?', default=3, type=int, nargs='?')
    args = parser.parse_args()

    file = open(args.output_file, 'w')
    
    file.write(f'{",".join([str(x) for x in range(args.number_of_dimensions)])[:-2]}\n')

    centroids = []
    for i, k in enumerate(range(args.number_of_clusters)):
        centroids.append([])
        for d in range(args.number_of_dimensions):
            centroids[i].append(random.randint(-200, 200))

    for i in range(args.number_of_data):
        for d in range(args.number_of_dimensions):
            file.write(str(random.gauss(centroids[random.randint(0, args.number_of_clusters-1)][d], random.randint(0, 20))))
            if(d < args.number_of_dimensions-1):
                file.write(',')
        file.write('\n')
    
    file.close()

if __name__ == '__main__':
    main()