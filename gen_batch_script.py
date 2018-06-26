# -*- coding: utf-8 -*-
def main():
    gen_batch_script(hardware_constraint='knl')

def gen_batch_script(
        batch_fname='batch_test.sh',
        job_name='newjob',  # this determines output file name too
        module_str='',
        cores_count=1,
        cores_per_node=16,
        hardware_constraint='',
        time='1:00:00',
        ):
    """
    Construct batch script.
    This function accepts keyword arguments.
    
    Kevin Rosa
    June 26, 2018
    Los Alamos National Laboratory
    """
    import math
    
    ''' Setting variable values for testing
    import datetime
    time_str = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
    
    # Inputs:
    batch_fname = 'batch_'+time_str+'.sh'
    job_name = 'antelope'
    hardware_constraint = 'knl'
    module_str = 'module load deer_creek\nmodule unload coventry'
    cores_count = '32'
    cores_per_node = 15.0
    '''
    
    # calculations
    nodes_count = int(math.ceil(float(cores_count)/float(cores_per_node)))
    
    output = '\n'.join((
            "#! /bin/bash",
            "#SBATCH --partition=regular",
            "#SBATCH --nodes="+str(nodes_count),
            "#SBATCH --time="+time,
            "#SBATCH --job_name="+job_name,
            "#SBATCH --output="+job_name+".out",
            "#SBATCH --license=SCRATCH"
            ))
    
    # append a hardware constraint if given
    if not hardware_constraint == '':
        output = '\n'.join((
                output,
                "#SBATCH --constraint="+hardware_constraint
                ))
    
    
    
    # append module loading
    output = '\n'.join((
            output,
            '',
            module_str
            ))
    
    # append srun command
    output = '\n'.join((
            output,
            '',
            "srun --ntasks="+str(cores_count)
            ))
    
    print(output)

if __name__ == '__main__':
    main()