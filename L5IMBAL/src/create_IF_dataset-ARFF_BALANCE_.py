import MySQLdb
import numpy as np

import utill5


"""=====================================================================================================
@ Author: Sangeeta
@Uses:
1. This file will be used to create dataset from the main training table "project_Training5_IF.java
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

#"""
port=3306
user="root"
password="1234"
database="logging5_imbal"
main_source_table = project+"_if_training5"  # from this table we have to take the data
path = "F:\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\if\\"
test_file_path = path+ project+"-arff\\if\\"

"""


port=3307
user="sangeetal"
password="sangeetal"
database="logging5_imbal"
main_source_table = project+"_if_training5"  # from this table we have to take the data
path = "E:\\Sangeeta\\Research\\L5IMBAL\\dataset\\"
train_file_path=path+project+"-arff\\if\\"
test_file_path = path+ project+"-arff\\if\\"
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
    file_obj.write("@attribute is_if_logged {0,1}  "+"\n")    
    file_obj.write("@attribute loc_till_if numeric "+"\n")
    file_obj.write("@attribute is_till_if_logged {0,1} "+"\n")
    file_obj.write("@attribute till_if_log_count numeric "+"\n")
    file_obj.write("@attribute operators_count_till_if numeric "+"\n")
    file_obj.write("@attribute variables_count_till_if numeric "+"\n")
    file_obj.write("@attribute method_call_count_till_if numeric "+"\n")
    file_obj.write("@attribute is_return_in_till_if {0,1} "+"\n")
    file_obj.write("@attribute throw_throws_till_if {0,1} "+"\n")
    file_obj.write("@attribute if_in_till_if {0,1} "+"\n")
    file_obj.write("@attribute if_count_in_till_if numeric "+"\n")
    file_obj.write("@attribute is_assert_till_if {0,1} "+"\n")
    file_obj.write("@attribute is_method_have_param {0,1} "+"\n")
    file_obj.write("@attribute method_param_count numeric "+"\n")
    file_obj.write("@attribute is_return_in_if {0,1} "+"\n")
    file_obj.write("@attribute throw_throws_if {0,1} "+"\n")
    file_obj.write("@attribute is_assert_if {0,1} "+"\n")
    file_obj.write("@attribute is_null_condition_if {0,1} "+"\n")
    file_obj.write("@attribute is_instance_of_condition_if {0,1} "+"\n")
    file_obj.write("@attribute all_text_features_cleaned string "+"\n")
        
    file_obj.write("\n")
    file_obj.write("@data " +"\n")
    
        
    
#=======================================================#
# @uses: Function to write in file ceate arff files
#=======================================================#
def write_in_file(file_obj, tuple_val):
    
    
    t_if_expr                  = tuple_val[0]
    n_loc_till_if              =  tuple_val[1]
    n_is_till_if_logged        = tuple_val[2]
    n_till_if_log_count        = tuple_val[3]
    t_till_if_log_levels       = tuple_val[4]
    t_operators_till_if        = tuple_val[5]
    n_operators_count_till_if  = tuple_val[6]
    t_variables_till_if          = tuple_val[7]
    n_variables_count_till_if    = tuple_val[8]
    t_method_call_names_till_if   =tuple_val[9]
    n_method_call_count_till_if   = tuple_val[10]
    n_is_return_in_till_if        =tuple_val[11]
    n_throw_throws_till_if        =tuple_val[12]
    n_if_in_till_if               =tuple_val[13]
    n_if_count_in_till_if         =tuple_val[14]
    n_is_assert_till_if          =tuple_val[15]
    n_is_method_have_param        =tuple_val[16] 
    t_method_param_type          =tuple_val[17]
    t_method_param_name         =tuple_val[18]
    n_method_param_count        =tuple_val[19]
    n_is_return_in_if           = tuple_val[20]
    n_throw_throws_if          = tuple_val[21]
    n_is_assert_if              =tuple_val[22]
    n_is_null_condition_if          = tuple_val[23] 
    n_is_instance_of_condition_if = tuple_val[24] 
    t_package_name               =tuple_val[25]
    t_class_name                =tuple_val[26]
    t_method_name                =tuple_val[27]
           
    is_if_logged = tuple_val[28]
    
    
    operator_feature =  t_operators_till_if
    
    text_features =      t_if_expr + " "+            t_till_if_log_levels   +" "                  +    t_variables_till_if +" "        +  t_method_call_names_till_if +" "+\
             t_method_param_type + " " +  t_method_param_name +" " +  t_package_name+" "+ t_class_name + " "+ t_method_name         
    
    #Applying camel casing
    text_features = utill5.camel_case_convert(text_features)
    text_features = utill5.remove_stop_words(text_features)
    text_features = utill5.stem_it(text_features)
    
    text_features =  text_features +" " + operator_feature
    
    text_features =  text_features.strip()
    
    #print "writing if:"   
   
    
    #=== write the data in the file=====================#
    write_str =""+ (str)(is_if_logged )+","+  (str)(n_loc_till_if)  +","+ (str)(n_is_till_if_logged ) +","+ (str)(n_till_if_log_count) +","+(str)( n_operators_count_till_if) +","+ \
    (str)(n_variables_count_till_if) +","+ (str)( n_method_call_count_till_if)  +","+ (str)(n_is_return_in_till_if)+","+ (str)(n_throw_throws_till_if)  +","+ \
    (str)(n_if_in_till_if) +","+ (str)(n_if_count_in_till_if) +","+ (str)(n_is_assert_till_if ) +","+  (str)(n_is_method_have_param )      +","+ \
    (str)( n_method_param_count)  +","+ (str)(n_is_return_in_if ) +","+ (str)(n_throw_throws_if)  +","+    (str)( n_is_assert_if  )           +","+ \
    (str)(n_is_null_condition_if)  +","+    (str)( n_is_instance_of_condition_if) +",'"+ text_features+"')"
      
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
#  This function will read all the logged if blocks                #
#=====================================================================#    
def read_logged_data():
    #===========Read the logged if blocks===============================#
   
    str_logged_data = "select  if_expr, loc_till_if, is_till_if_logged, till_if_log_count, till_if_log_levels, operators_till_if, operators_count_till_if, variables_till_if,  \
                       variables_count_till_if,method_call_names_till_if, method_call_count_till_if,  is_return_in_till_if, throw_throws_till_if, \
                       if_in_till_if, if_count_in_till_if, is_assert_till_if, is_method_have_param,  method_param_type, method_param_name, method_param_count,\
                       is_return_in_if, throw_throws_if, is_assert_if, is_null_condition_if, is_instance_of_condition_if, package_name, class_name, method_name, is_if_logged\
                       from "+ main_source_table +" where if_expr not like '%isTraceEnabled()'  and \
                       if_expr not like '%isDebugEnabled()'  and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'  \
                       and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and if_expr!=''  and is_if_logged=1"
        

    select_cursor.execute(str_logged_data)
    logged_data = select_cursor.fetchall()
    
    return logged_data



#==========================================================================#
#  This function will read all the non logged if blocks                 #
#==========================================================================#    
def read_non_logged_data():
    #===========Read the non logged if blocks===============================#
    str_non_logged_data = "select  if_expr, loc_till_if, is_till_if_logged, till_if_log_count, till_if_log_levels, operators_till_if, operators_count_till_if, variables_till_if,  \
                       variables_count_till_if,method_call_names_till_if, method_call_count_till_if,  is_return_in_till_if, throw_throws_till_if, \
                       if_in_till_if, if_count_in_till_if, is_assert_till_if, is_method_have_param,  method_param_type, method_param_name, method_param_count,\
                       is_return_in_if, throw_throws_if, is_assert_if, is_null_condition_if, is_instance_of_condition_if, package_name, class_name, method_name, is_if_logged\
                       from "+ main_source_table +" where if_expr not like '%isTraceEnabled()'  and \
                       if_expr not like '%isDebugEnabled()'  and if_expr not like '%isInfoEnabled()' and if_expr not like '%isWarnEnabled()'  \
                       and if_expr not like '%isErrorEnabled()'  and if_expr not like '%isFatalEnabled()'  and if_expr!=''  and is_if_logged=0"
         
 
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
    
   # train_file_path=path+project+"-arff\\if\\train_1\\k1\\"+project+"_train.arff"  # Complete taining file, its subsects will be create for ensemble creation
   #test_file_path = path+ project+"-arff\\if\\test_1\\"+project+"_test.arff"

    
    file_train =  open(train_file_path, 'w+')
    file_test  =  open(test_file_path,  'w+')
   
    # 1. Write header in the file
    train_relation_name =  project +"_if_train"
    write_header(file_train, train_relation_name)
    
    test_relation_name =  project +"_if_test"
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




