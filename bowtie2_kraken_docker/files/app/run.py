#!/usr/bin/python
import os
import re

# Lectura de parametros desde el fichero properties
import json

def parseParameters(properties):
    f = open(properties, 'r')
    try:
        parameters = json.loads(f.read())
    except ValueError:
        array = {}
        print 'Parameters could not be read. Will exit with status 102'
        f.close()
        sys.exit(102)
    f.close()
    return parameters

# Ejecucion del programa con los Browseparametros del fichero properties 


def run_programs(properties):
    parameters = parseParameters(properties)
    input_path = "/data/input/"
    output_path = "/data/output/"
    tmp_output_path = "/tmp/"
    bowtie_path = "/bowtie_db/"
    kraken_output_raw = "krak.txt"
    kraken_output_file = "kraken.txt"
    bowtie_output_file = "bowtie.txt"
    bowtie_1 = "bowtie.1.txt"
    bowtie_2 = "bowtie.2.txt"
    final = ".output"
    zipp = "\*.zip"
    
 
    bashCommand = "unzip %s -d %s && rm -rf /data/input/*zip" %(input_path + zipp, input_path)
    os.system(bashCommand)
        
    if parameters['input_type'] == "PE":
       input_file = parameters['input1']
       input_file2 = parameters['input2']
    
       match = re.search(r'.gz', input_path + input_file)

       if match:
          bashCommand = "gunzip %s" %(input_path + input_file)
          os.system(bashCommand)
          split_list_3 = input_file.split(".gz")
          input_file = split_list_3[0]

       match2 = re.search(r'.gz', input_path + input_file2)

       if match2:
          bashCommand = "gunzip %s" %(input_path + input_file2)
          os.system(bashCommand)
          split_list_4 = input_file2.split(".gz")
          input_file2 = split_list_4[0]

    else:
       input_file = parameters['input']
    
       match = re.search(r'.gz', input_path + input_file)

       if match:
          bashCommand = "gunzip %s" %(input_path + input_file)
          os.system(bashCommand)
          split_list_2 = input_file.split(".gz")
          input_file = split_list_2[0]



    if parameters['input_type'] == "FASTA":


        if parameters['use_bowtie'] == "true":
           
            # bowtie2
             bashCommand = "/app/bowtie2/bowtie2 -x %s -f -U %s --un %s --threads %s > /dev/null" %(bowtie_path + parameters['bowtie_db_files'], input_path + input_file,\
	                                    tmp_output_path + bowtie_output_file, os.environ['BATCH_CPU'])
	
             os.system(bashCommand)


             # kraken    
             bashCommand = "/app/kraken/kraken --db /kraken_db %s --threads %s --output %s" %(tmp_output_path + bowtie_output_file,\
                                            os.environ['BATCH_CPU'],\
                                            tmp_output_path + kraken_output_raw)
        
             os.system(bashCommand)
             
             # kraken scores
             bashCommand = "/app/kraken/kraken-filter --db /kraken_db %s > %s" %(tmp_output_path + kraken_output_raw, output_path + kraken_output_file)
        
             os.system(bashCommand)
          
             # kraken report
             bashCommand = "perl /app/kraken_parser.pl %s %s" %(output_path + kraken_output_file, output_path + input_file + final)
        
             os.system(bashCommand)
 

        else:
             # kraken    
             bashCommand = "/app/kraken/kraken --db /kraken_db %s --threads %s --output %s" %(input_path + input_file,\
                                            os.environ['BATCH_CPU'],\
                                            tmp_output_path + kraken_output_raw)
        
             os.system(bashCommand)
             
             # kraken scores
             bashCommand = "/app/kraken/kraken-filter --db /kraken_db %s > %s" %(tmp_output_path + kraken_output_raw, output_path + kraken_output_file)
        
             os.system(bashCommand)

             # kraken-report
             bashCommand = "perl /app/kraken_parser.pl %s %s" %(output_path + kraken_output_file, output_path + input_file + final)
        
             os.system(bashCommand)


    elif parameters['input_type'] == "SE":


        if parameters['use_bowtie'] == "true":
           
             # bowtie2
              # bowtie2
             bashCommand = "/app/bowtie2/bowtie2 -x %s -U %s --un %s --threads %s > /dev/null" %(bowtie_path + parameters['bowtie_db_files'], input_path + input_file,\
	                                    tmp_output_path + bowtie_output_file, os.environ['BATCH_CPU'])
	
             os.system(bashCommand)


             # kraken    
             bashCommand = "/app/kraken/kraken --db /kraken_db --fastq-input %s --threads %s --output %s" %(tmp_output_path + bowtie_output_file,\
                                            os.environ['BATCH_CPU'],\
                                            tmp_output_path + kraken_output_raw)
        
             os.system(bashCommand)
             
              # kraken scores
             bashCommand = "/app/kraken/kraken-filter --db /kraken_db %s > %s" %(tmp_output_path + kraken_output_raw, output_path + kraken_output_file)
        
             os.system(bashCommand)
          
             # kraken report
             bashCommand = "perl /app/kraken_parser.pl %s %s" %(output_path + kraken_output_file, output_path + input_file + final)
        
             os.system(bashCommand)
 

        else:
             # kraken    
             bashCommand = "/app/kraken/kraken --db /kraken_db --fastq-input %s --threads %s --output %s" %(input_path + input_file,\
                                            os.environ['BATCH_CPU'],\
                                            tmp_output_path + kraken_output_raw)
        
             os.system(bashCommand)
             
             # kraken scores
             bashCommand = "/app/kraken/kraken-filter --db /kraken_db %s > %s" %(tmp_output_path + kraken_output_raw, output_path + kraken_output_file)
        
             os.system(bashCommand)

             # kraken-report
             bashCommand = "perl /app/kraken_parser.pl %s %s" %(output_path + kraken_output_file, output_path + input_file + final)
        
             os.system(bashCommand)


    elif parameters['input_type'] == "PE":


        if parameters['use_bowtie'] == "true":
           
             # bowtie2
             # bowtie2
             bashCommand = "/app/bowtie2/bowtie2 -x %s -1 %s -2 %s --un-conc %s --threads %s > /dev/null" %(bowtie_path + parameters['bowtie_db_files'], input_path + input_file, \
                                            input_path + input_file2,\
	                                    tmp_output_path + bowtie_output_file, os.environ['BATCH_CPU'])
	
             os.system(bashCommand)


             # kraken    
             bashCommand = "/app/kraken/kraken --db /kraken_db --fastq-input --paired %s %s --threads %s --output %s" %(tmp_output_path + bowtie_1,\
                                            tmp_output_path + bowtie_2,\
                                            os.environ['BATCH_CPU'],\
                                            tmp_output_path + kraken_output_raw)
        
             os.system(bashCommand)
             
              # kraken scores
             bashCommand = "/app/kraken/kraken-filter --db /kraken_db %s > %s" %(tmp_output_path + kraken_output_raw, output_path + kraken_output_file)
        
             os.system(bashCommand)
          
             # kraken report
             bashCommand = "perl /app/kraken_parser.pl %s %s" %(output_path + kraken_output_file, output_path + input_file + final)
        
             os.system(bashCommand)
 

        else:
             # kraken    
             bashCommand = "/app/kraken/kraken --db /kraken_db --fastq-input --paired %s %s --threads %s --output %s" %(input_path + input_file,\
                                            input_path + input_file2,\
                                            os.environ['BATCH_CPU'],\
                                            tmp_output_path + kraken_output_raw)
        
             os.system(bashCommand)
             
              # kraken scores
             bashCommand = "/app/kraken/kraken-filter --db /kraken_db %s > %s" %(tmp_output_path + kraken_output_raw, output_path + kraken_output_file)
        
             os.system(bashCommand)

             # kraken-report
             bashCommand = bashCommand = "perl /app/kraken_parser.pl %s %s" %(output_path + kraken_output_file, output_path + input_file + final)
        
             os.system(bashCommand)





def main():    
    prop_file = '/data/parameters.txt'   
    run_programs(prop_file)
     
if __name__ == "__main__":
    main()

