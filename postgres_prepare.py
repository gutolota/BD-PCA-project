import json
import sys
from time import sleep
import psycopg2
import psycopg2.extensions
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(sys.argv[0])
    parser.add_argument('-cf', '--credential_file', help='File with database credentials', default='credentials.json')
    args = parser.parse_args()

    subprocess.Popen('docker stop postgres_server 2> /dev/null', shell=True).wait()
    sleep(0.5)
    subprocess.Popen('docker rm postgres_server 2> /dev/null', shell=True).wait()
    sleep(0.5)
    subprocess.Popen('docker run -p 5432:5432 -e POSTGRES_PASSWORD=teste123!@#321#@! --name postgres_server -d postgres 2> /dev/null', shell=True).wait()
    sleep(0.5)
    subprocess.Popen('docker start postgres_server 2> /dev/null', shell=True).wait()
    sleep(0.5)
    

    credential_file = json.load(open(args.credential_file, 'r'))
    connection = psycopg2.connect(f'dbname=postgres host={credential_file["host"]} port={credential_file["port"]} user={credential_file["user"]} password={credential_file["password"]}')
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(f'DROP DATABASE IF EXISTS {credential_file["dbname"]};')
    cursor.execute(f'CREATE DATABASE {credential_file["dbname"]};')
    connection.commit()
    connection.close()
    sleep(0.5)

    connection = psycopg2.connect(f'dbname={credential_file["dbname"]} host={credential_file["host"]} port={credential_file["port"]} user={credential_file["user"]} password={credential_file["password"]}')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS pca_data;')
    cursor.execute('CREATE TABLE pca_data(feature_1 FLOAT, feature_2 FLOAT, feature_3 FLOAT, feature_4 FLOAT);')
    connection.commit()

    with open('./data/example_data1.csv', 'r') as file:
        next(file)
        cursor.copy_from(file, 'pca_data', ',')
        connection.commit()
    connection.close()


if __name__ == '__main__':
    main()