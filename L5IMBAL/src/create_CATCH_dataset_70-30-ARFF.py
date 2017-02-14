import MySQLdb
import numpy as np

import utill5


"""=====================================================================================================
@ Author: Sangeeta
@Uses:
1. This file will be used to create dataset from the main training table "project_Training5_Catch.java
2. It will create 2 ARFF Files

    a. One training
    b. One testing
    c. train -test size is 70-30%
======================================================================================================"""

#Project
#"""
project= "tomcat"
title = 'Tomcat'
#"""
"""
project =  "cloudstack"
title = 'CloudStack'
#"""

"""
project =  "hd"
title = 'Hadoop'
#"""

"""
port=3306
user="root"
password="1234"
database="logging5_imbal"
main_source_table = project+"_catch_training5"  # from this table we have to take the data
path = "F:\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\catch\\"
test_file_path = path+ project+"-arff\\catch\\"

#logged_indices_file_path =  path+project+"-arff\\catch\\train_1\\logged_indices.txt"
#non_logged_indices_file_path =  path+project+"-arff\\catch\\train_1\\non_logged_indices.txt"
"""

"""
port=3307
user="sangeetal"
password="sangeetal"
database="logging5_imbal"
main_source_table = project+"_catch_training5"  # from this table we have to take the data
path = "E:\\Sangeeta\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\catch\\"
test_file_path = path+ project+"-arff\\catch\\"
#"""
 
# JIIT Server #
"""
port=3306
user="root"
password="1234"
database="logging5_imbal_rc_feb9"
main_source_table = project+"_catch_training5"  # from this table we have to take the data
path = "D:\\Sangeeta\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\catch\\"
test_file_path = path+ project+"-arff\\catch\\"
#"""


##  feb9 ###
"""
port=3306
user="root"
password="1234"
database="logging5_imbal_rc_feb9"
main_source_table = project+"_catch_training5"  # from this table we have to take the data
path = "F:\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\catch\\"
test_file_path = path+ project+"-arff\\catch\\"

#logged_indices_file_path =  path+project+"-arff\\catch\\train_1\\logged_indices.txt"
#non_logged_indices_file_path =  path+project+"-arff\\catch\\train_1\\non_logged_indices.txt"

"""
port=3306
user="root"
password="1234"
database="logging5_imbal_rc_feb9"
main_source_table = project+"_catch_training5"  # from this table we have to take the data
path = "D:\\Sangeeta\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\catch\\"
test_file_path = path+ project+"-arff\\catch\\"
#"""

db1= MySQLdb.connect(host="localhost",user=user, passwd=password, db=database, port=port)
select_cursor = db1.cursor()
insert_cursor = db1.cursor()
logged_train_indices = list()
non_logged_train_indices= list()

logged_test_indices = list()
non_logged_test_indices = list()


#=======================================================#
#  @Uses:Write_header() is a function that is used toinsert
# the ARFF header in the file.
#=======================================================#
def write_header(file_obj,relation_name):
    
    file_obj.write("@relation    "  + relation_name+"\n" )
    file_obj.write("@attribute is_catch_logged {0,1}  "+"\n")
    file_obj.write("@attribute try_loc numeric "+"\n")
    file_obj.write("@attribute is_try_logged {0,1}"+"\n")
    file_obj.write("@attribute try_log_count numeric "+"\n")
    file_obj.write("@attribute have_previous_catches {0,1} "+"\n")
    file_obj.write("@attribute previous_catches_logged {0,1} "+"\n")
    file_obj.write("@attribute is_return_in_try {0,1} "+"\n")
    file_obj.write("@attribute is_return_in_catch {0,1} "+"\n")
    file_obj.write("@attribute is_catch_object_ignore {0,1} "+"\n")
    file_obj.write("@attribute is_interrupted_exception {0,1} "+"\n")
    file_obj.write("@attribute is_thread_sleep_try {0,1} "+"\n")
    file_obj.write("@attribute throw_throws_try {0,1} "+"\n")
    file_obj.write("@attribute throw_throws_catch {0,1} "+"\n")
    file_obj.write("@attribute if_in_try {0,1} "+"\n")
    file_obj.write("@attribute if_count_in_try numeric "+"\n")
    file_obj.write("@attribute is_assert_in_try {0,1} "+"\n")
    file_obj.write("@attribute is_assert_in_catch {0,1} "+"\n")
    file_obj.write("@attribute is_method_have_param {0,1} "+"\n")
    file_obj.write("@attribute method_param_count numeric "+"\n")
    file_obj.write("@attribute method_call_count_try numeric "+"\n")
    file_obj.write("@attribute operators_count_in_try numeric "+"\n")
    file_obj.write("@attribute variables_count_try numeric "+"\n")
    file_obj.write("@attribute method_call_count_till_try numeric "+"\n")
    file_obj.write("@attribute operators_count_till_try numeric "+"\n")
    file_obj.write("@attribute variables_count_till_try numeric "+"\n")
    file_obj.write("@attribute loc_till_try numeric "+"\n")
    file_obj.write("@attribute is_till_try_logged {0,1} "+"\n")
    file_obj.write("@attribute till_try_log_count numeric "+"\n")
    file_obj.write("@attribute is_return_till_try {0,1} "+"\n")
    file_obj.write("@attribute throw_throws_till_try {0,1} "+"\n")
    file_obj.write("@attribute if_in_till_try {0,1} "+"\n")
    file_obj.write("@attribute if_count_in_till_try numeric "+"\n")
    file_obj.write("@attribute is_assert_till_try {0,1} "+"\n")
    file_obj.write("@attribute all_text_feature_cleaned string "+"\n")
    
    file_obj.write("\n")
    file_obj.write("@data " +"\n")
        
    
#=======================================================#
# @uses: Function to write in file ceate arff files
#=======================================================#
def write_in_file(file_obj, tuple_val):
    
    t_catch_exc     = tuple_val[0]
    t_package_name  = tuple_val[1]
    t_class_name    = tuple_val[2]
    t_method_name   = tuple_val[3]

    n_try_loc       = tuple_val[4]
    n_is_try_logged = tuple_val[5]
    n_try_log_count  =tuple_val[6]

    t_try_log_levels = tuple_val[7]

    n_have_previous_catches=tuple_val[8]
    n_previous_catches_logged =tuple_val[9]
    n_is_return_in_try =tuple_val[10]                     
    n_is_return_in_catch  = tuple_val[11]
    n_is_catch_object_ignore = tuple_val[12]
    n_is_interrupted_exception = tuple_val[13]
    n_is_thread_sleep_try = tuple_val[14]
    n_throw_throws_try = tuple_val[15]                             
    n_throw_throws_catch= tuple_val[16]
    n_if_in_try =tuple_val[17]
    n_if_count_in_try = tuple_val[18]
    n_is_assert_in_try = tuple_val[19]
    n_is_assert_in_catch = tuple_val[20]
    n_is_method_have_param = tuple_val[21]
    
    t_method_param_type = tuple_val[22]
    t_method_param_name = tuple_val[23]

    n_method_param_count = tuple_val[24]
    
    t_method_call_names_try = tuple_val[25]
    
    n_method_call_count_try= tuple_val[26]
    
    t_operators_in_try = tuple_val[27]
    
    n_operators_count_in_try =tuple_val[28]
    
    t_variables_in_try =tuple_val[29]
    
    n_variables_count_try =tuple_val[30]
    
    t_method_call_names_till_try =tuple_val[31]
    
    n_method_call_count_till_try =tuple_val[32]
    
    t_operators_till_try  =tuple_val[33]
    
    n_operators_count_till_try =tuple_val[34]
    
    t_variables_till_try =tuple_val[35]
    
    n_variables_count_till_try =tuple_val[36] 
    n_loc_till_try =tuple_val[37]
    n_is_till_try_logged =tuple_val[38] 
    n_till_try_log_count =tuple_val[39]

    t_till_try_log_levels =tuple_val[40]
    
    n_is_return_till_try =tuple_val[41]
    n_throw_throws_till_try =tuple_val[42]
    n_if_in_till_try =tuple_val[43]
    n_if_count_in_till_try =tuple_val[44] 
    n_is_assert_till_try =tuple_val[45]
   
    try_id    = tuple_val[46]
    catch_id = tuple_val[47]
    is_catch_logged  = tuple_val[48]
    
    
    text_features =      t_catch_exc+ " "+            t_package_name +" "                  + t_class_name+" "        + t_method_name  +" "+\
                 t_method_param_type + " " +  t_method_param_name +" " +            t_method_call_names_try +" " +\
                 t_variables_in_try  +" " +   t_try_log_levels +" "+                  t_method_call_names_till_try +" "+   t_variables_till_try +"  "+\
                 t_till_try_log_levels

    #Applying camel casing
    text_features = utill5.camel_case_convert(text_features)
    text_features =  utill5.remove_stop_words(text_features)
    text_features = utill5.stem_it(text_features)
    
    operator_string =  t_operators_in_try +" "+ t_operators_till_try
    
    text_features =  text_features +" " + operator_string
    
    text_features =  text_features.strip()
    
    #print "writing try id=", try_id   #Note: Uncomment to see which ids its writing
    
    #====Insert the data in the table=====#
    write_str =  ""+ (str)(is_catch_logged) +","+ (str)(n_try_loc) +","+ (str)(n_is_try_logged)  +","+ (str)(n_try_log_count)\
    +","+ (str)(n_have_previous_catches) +","+ (str)(n_previous_catches_logged)  +","+ (str)(n_is_return_in_try) +","+ (str)(n_is_return_in_catch) +","+ (str)(n_is_catch_object_ignore) +","+ (str)(n_is_interrupted_exception)\
    +","+ (str)(n_is_thread_sleep_try)  +","+ (str)(n_throw_throws_try)  +","+ (str)(n_throw_throws_catch) +","+ (str)(n_if_in_try) +","+ (str)(n_if_count_in_try) +","+ (str)(n_is_assert_in_try)\
    +","+ (str)(n_is_assert_in_catch) +","+ (str)(n_is_method_have_param) +","+ (str)(n_method_param_count)  +","+ (str)(n_method_call_count_try) +","+ (str)(n_operators_count_in_try)\
    +","+ (str)(n_variables_count_try) +","+ (str)(n_method_call_count_till_try) +","+ (str)(n_operators_count_till_try)\
    +","+ (str)(n_variables_count_till_try) +","+ (str)(n_loc_till_try) +","+ (str)(n_is_till_try_logged) +","+ (str)(n_till_try_log_count)\
    +","+ (str)(n_is_return_till_try) +","+ (str)(n_throw_throws_till_try) +","+ (str)(n_if_in_till_try) +","+ (str)(n_if_count_in_till_try)\
    +","+ (str)(n_is_assert_till_try)  +",'"+  text_features+"')"
      
    # ==write in the file======#  
    file_obj.write(write_str+"\n")       
                
    
    #target.append(0)  Removing from here moving up                  
    #db1.commit()           
    
    
#=====================================================#
#  This function is used to creat indices 
#=====================================================#
def write_indices_in_file(indices, indices_file_path):
    file_obj =  open(indices_file_path, 'w+')
    for i in indices:
        file_obj.write((str)(i)+ "\n")
        
    file_obj.close();    
        

#=====================================================================#
#  This function will read all the logged catch blocks                #
#=====================================================================#    
def read_logged_data():
    #===========Read the logged catch blocks===============================#
    str_logged_data = "select  catch_exc, package_name, class_name, method_name, try_loc, is_try_logged, try_log_count, try_log_levels, have_previous_catches, previous_catches_logged, \
                      is_return_in_try, is_return_in_catch, is_catch_object_ignore, is_interrupted_exception, is_thread_sleep_try,\
                       throw_throws_try,  throw_throws_catch, if_in_try, if_count_in_try, is_assert_in_try, is_assert_in_catch, \
                      is_method_have_param, method_param_type, method_param_name, method_param_count, method_call_names_try, \
                      method_call_count_try, operators_in_try, operators_count_in_try, variables_in_try, variables_count_try,\
                      method_call_names_till_try, method_call_count_till_try, operators_till_try, operators_count_till_try, variables_till_try,\
                      variables_count_till_try, loc_till_try, is_till_try_logged, till_try_log_count, till_try_log_levels,is_return_till_try, throw_throws_till_try, \
                     if_in_till_try, if_count_in_till_try,  is_assert_till_try, try_id, catch_id, is_catch_logged  from  "+ main_source_table +" where catch_exc!=''  and is_catch_logged=1 "
   

    select_cursor.execute(str_logged_data)
    logged_data = select_cursor.fetchall()
    
    return logged_data



#==========================================================================#
#  This function will read all the non logged catch blocks                 #
#==========================================================================#    
def read_non_logged_data():
    #===========Read the non logged catch blocks===============================#
    str_non_logged_data = "select  catch_exc, package_name, class_name, method_name, try_loc, is_try_logged, try_log_count, try_log_levels, have_previous_catches, previous_catches_logged, \
                      is_return_in_try, is_return_in_catch, is_catch_object_ignore, is_interrupted_exception, is_thread_sleep_try,\
                       throw_throws_try,  throw_throws_catch, if_in_try, if_count_in_try, is_assert_in_try, is_assert_in_catch, \
                      is_method_have_param, method_param_type, method_param_name, method_param_count, method_call_names_try, \
                      method_call_count_try, operators_in_try, operators_count_in_try, variables_in_try, variables_count_try,\
                      method_call_names_till_try, method_call_count_till_try, operators_till_try, operators_count_till_try, variables_till_try,\
                      variables_count_till_try, loc_till_try, is_till_try_logged, till_try_log_count, till_try_log_levels,is_return_till_try, throw_throws_till_try, \
                     if_in_till_try, if_count_in_till_try,  is_assert_till_try, try_id, catch_id, is_catch_logged  from  "+ main_source_table +" where catch_exc!=''  and is_catch_logged=0 "
   

    select_cursor.execute(str_non_logged_data)
    non_logged_data = select_cursor.fetchall()
    
    return non_logged_data
        
#=========================================================================#
#  This function creates an array having  size of each of the subset      #
#=========================================================================#
def compute_subset_size_array(total_data_points, no_of_subsets):
    
    size_list  = list()
    size= total_data_points/no_of_subsets
    
    i=1
    data_points_added = 0
    while i<no_of_subsets:
        size_list.append(size)
        data_points_added = data_points_added + size
        i=i+1
        
    remaining_data_points = total_data_points -data_points_added
    size_list.append(remaining_data_points)    
    
    return size_list

#=========================================================================#
#  This function creates an subsets from the training dataset             #
#=========================================================================#
def create_train_subsets_k(k, logged_size_array, non_logged_size_array, logged_train_indices, non_logged_test_indices,  logged_data, non_logged_data):
    
    j=0
    
    logged_start = 0
    logged_end   = 0
    
    non_logged_start = 0
    non_logged_end   = 0
    
    while(j<k):
        
        print "\n K=", j+1
        
        
        logged_start = logged_end
        logged_end   = logged_end+ logged_size_array[j]
    
        non_logged_start = non_logged_end
        non_logged_end   = non_logged_end + non_logged_size_array[j]
    
        
        logged_sub_train_indices = logged_train_indices[logged_start:logged_end] 
        non_logged_sub_train_indices = non_logged_train_indices[non_logged_start:non_logged_end]   
        
        print " Logged subset =", j, "  th train indices= ", logged_sub_train_indices
        print " Non Logged subset =", j, "  th train indices= ", non_logged_sub_train_indices
        
        
        train_subset_file_path  = path + project+"-arff\\catch\\train_1\\k"+(str)(k)+"\\"+project+"_train_sub_"+(str)(j+1)+".arff"
        file_sub_train =  open(train_subset_file_path, 'w+')
    
        # 1. Write header in the file
        train_subset_relation_name =  project +"_catch_train_subset_"+(str)(j+1)
        write_header(file_sub_train, train_subset_relation_name)
        
        valid_index=-1
        for d in logged_data:
            valid_index= valid_index+1
            if valid_index in logged_sub_train_indices: 
                write_in_file(file_sub_train, d)   
        
        valid_index=-1
        for d in non_logged_data:
            valid_index= valid_index+1
            if valid_index in non_logged_sub_train_indices: 
                write_in_file(file_sub_train, d)  
                
        file_sub_train.close()
            
        j=j+1 
    
#===========================================================================#
#    Creating train and test dataset                                        #
#===========================================================================#    
def create_complete_train_and_test_file_logged(train_file_path, test_file_path, i):

    logged_data = read_logged_data()   
    non_logged_data = read_non_logged_data()

    
    #===============================================================#
    #@ 1. Create one complete  train and test database (logged data)   
    #===============================================================#
   
    train_file_path = train_file_path+"train_"+(str)(i)+"\\k1\\"+project+"_train.arff"
    test_file_path  = test_file_path+"test_"+(str)(i)+"\\"+project+"_test.arff"
    
   # train_file_path=path+project+"-arff\\catch\\train_1\\k1\\"+project+"_train.arff"  # Complete taining file, its subsects will be create for ensemble creation
   #test_file_path = path+ project+"-arff\\catch\\test_1\\"+project+"_test.arff"

    
    file_train =  open(train_file_path, 'w+')
    file_test  =  open(test_file_path,  'w+')
   
    # 1. Write header in the file
    train_relation_name =  project +"_catch_train"
    write_header(file_train, train_relation_name)
    
    test_relation_name =  project +"_catch_test"
    write_header(file_test, test_relation_name)       
     
            
    np.random.seed(i-1)
    
    logged_train_indices = list()
    logged_test_indices = list()
    
    total_logged_data_points =  len(logged_data)
    logged_indices = np.random.permutation(len(logged_data))
    logged_per_70  = (total_logged_data_points * 70)/100
    logged_per_30 = total_logged_data_points-logged_per_70    
    
    global logged_train_indices 
    logged_train_indices= logged_indices[:logged_per_70]
    
    global logged_test_indices
    logged_test_indices= logged_indices[-logged_per_30:]
    
    #============ Write training indices (logged) in file for ensemble creation=======#
    # write_indices_in_file(logged_train_indices, logged_indices_file_path)  # Not required
    #=========================================================================#
    
    print "len logged tuples=", len(logged_data),  "per_70=", logged_per_70, "  per_30=", logged_per_30    
    print " all indices = ", logged_indices
    print " train =", logged_train_indices,  "  test =", logged_test_indices
    
    valid_index=-1
    for d in logged_data:
   
        valid_index= valid_index+1
        if valid_index in logged_train_indices: 
            write_in_file(file_train, d)   
    
    valid_index=-1
    for d in logged_data:
   
        valid_index= valid_index+1
        if valid_index in logged_test_indices: 
            write_in_file(file_test, d)          
    

    #===============================================================#
    # Create one complete  train and test database (non logged data)   
    #===============================================================#
   
    #non_logged_train_indices = list()
    #non_logged_test_indices = list()
    
    total_non_logged_data_points =  len(non_logged_data)
    non_logged_indices = np.random.permutation(len(non_logged_data))
    non_logged_per_70  = (total_non_logged_data_points * 70)/100
    non_logged_per_30 = total_non_logged_data_points-non_logged_per_70    
   
    global non_logged_train_indices 
    non_logged_train_indices = non_logged_indices[:non_logged_per_70]
    global non_logged_test_indices
    non_logged_test_indices = non_logged_indices[-non_logged_per_30:]
   
    #============ Write training indices (non-logged) in file for ensemble creation=======#
    # write_indices_in_file(non_logged_train_indices, non_logged_indices_file_path)  # Not required
    #====================================================================================#
    
    print "len non logged tuples=", len(non_logged_data),  "non logged per_70=", non_logged_per_70, " non logged  per_30=", non_logged_per_30    
    print " all indices (non logged) = ", non_logged_indices
    print " train (non logged) =", non_logged_train_indices,  "  test (non logged)=", non_logged_test_indices
    
    valid_index=-1
    for d in non_logged_data:
   
        valid_index= valid_index+1
        if valid_index in non_logged_train_indices: 
            write_in_file(file_train, d)   
    
    valid_index=-1
    for d in non_logged_data:
   
        valid_index= valid_index+1
        if valid_index in non_logged_test_indices: 
            write_in_file(file_test, d)          
    
    
    file_train.close()
    file_test.close()
    
    
#==================================================================================#
#  This function will bes used to create subsets of training dataset for ensemble 
#  creation
#==================================================================================#
def create_train_data_set_for_different_k(a,b):
    i=a
    j=b
    
    while(i<=j):
        print i
        
        logged_data =  read_logged_data()
        non_logged_data =  read_non_logged_data()
        
        logged_per_70       =   (len(logged_data) * 70)/100
        non_logged_per_70   =   (len(non_logged_data) * 70)/100
        logged_size_array   =   compute_subset_size_array(logged_per_70, i)
        non_logged_size_array =  compute_subset_size_array(non_logged_per_70, i)
        print "logged size array=", logged_size_array, " non logged size array=", non_logged_size_array, "logged train indices=", logged_train_indices, "  non logged train indices=", non_logged_train_indices
        
        create_train_subsets_k(i, logged_size_array, non_logged_size_array, logged_train_indices, non_logged_test_indices,  logged_data, non_logged_data)

        i=i+1
    



#=========== Run ========================#

i=1
while(i<=10):
    create_complete_train_and_test_file_logged(train_file_path, test_file_path, i)
    i=i+1



#create_train_data_set_for_different_k(2,10)  # @Note: This function is not modifed may be wrong please check for correctness

