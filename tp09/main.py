from glob import glob
import re

def main():
    log_files = glob('*.log')
    
    for log_file in log_files:
        with open(log_file) as f:
            for line in f:
                line = line.strip()
                # pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                pattern = r"^(.+?)\s"
                pattern = r"HTTPS?/\d\.\d+\" 404"
                result = re.findall(pattern, line)
                if result:
                    print(line)
                    print(result)   


if __name__=='__main__':
    main()
