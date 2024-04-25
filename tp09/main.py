from glob import glob

def main():
    log_files = glob('*.log')
    
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                line = line.strip()
                print(line)


if __name__=='__main__':
    main()
