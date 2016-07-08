import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.BayesNet;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.evaluation.NominalPrediction;
import weka.classifiers.functions.Logistic;
import weka.classifiers.functions.MultilayerPerceptron;
import weka.classifiers.functions.RBFNetwork;
import weka.classifiers.meta.AdaBoostM1;
import weka.classifiers.rules.DecisionTable;
import weka.classifiers.trees.ADTree;
import weka.classifiers.trees.J48;
import weka.classifiers.trees.RandomForest;
import weka.core.FastVector;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.ArffSaver;
import weka.core.converters.ConverterUtils.DataSource;
import weka.filters.Filter;
import weka.filters.supervised.attribute.Discretize;
import weka.filters.unsupervised.attribute.Normalize;
import weka.filters.unsupervised.attribute.Standardize;
import weka.filters.unsupervised.attribute.StringToWordVector;



/*
 * @Author: Sangeeta
 * 1. This is the simple log prediction code that is used to predict logging using ensemble of classifier
 * */
public class log_pred_ensemble_not_used
{

	/*
	 String path = "E:\\Sangeeta\\Research\\L5IMBAL\\dataset\\";
	 String user_name =  "sangeetal";
	 String password = "sangeetal";
	 String url = "jdbc:mysql://localhost:3307/";
	 String driver = "com.mysql.jdbc.Driver"; 
	  
	// */
	
	///*
	String path = "F:\\Research\\L5IMBAL\\dataset\\";
	String user_name =  "root";
	String password = "1234";
	String url = "jdbc:mysql://localhost:3306/";
	String driver = "com.mysql.jdbc.Driver";
	//*/
	 

	int iterations=1;	
	String type = "catch";
	//String type ="if";

	String source_project="tomcat";	
	//String source_project="cloudstack";	
	//String source_project="hd";
	
	
	String db_name ="logging5_imbal";
	String result_table = "result_ensemble_"+type;

		
	//DataSource trainsource;
	DataSource train_data_source[];
	DataSource test_data_source;
	
	Instances trains[];
	Instances tests[];
	
	Evaluation result;
		
	int instance_count_train = 0;
	int instance_count_test= 0;
	 
	double precision[] ;
	double recall[]   ;
	double accuracy[]  ;
	double fmeasure[]  ;
	double roc_auc[] ;
	   	
	
	//Connection conn=null;	
	//java.sql.Statement stmt = null;
   
	
	
	// This function uses dataset from the ARFF files
	public void read_file(int i, String train_file_path, String test_file_path)
	 { 
		try 
			{
			
				train_data_source[i] = new DataSource(train_file_path);
				
				trains[i] = train_data_source[i].getDataSet();
				trains[i].setClassIndex(0);
				
				
				test_data_source = new DataSource(test_file_path);
				tests[i] = test_data_source.getDataSet();
				tests[i].setClassIndex(0);	
								
				
				instance_count_train = trains[i].numInstances();
				instance_count_test = tests[i].numInstances();
				
				System.out.println("Instance count Train ="+ instance_count_train+"   Instance count Test="+ instance_count_test);// + "  Instance count target="+ instance_count_target);*/
		    
			} catch (Exception e) 
			{
			
				e.printStackTrace();
			}	  
			
		}	
	
	
	
// This is the main function that is used to  call the important function for classification
	 private void ensemble_prediction(Classifier model[]) 
	 {
	  	int k=10; //No of subsets
	  	for(int i=2; i<=k;i++)
	  	{

			 precision   = new double[iterations];
			 recall     = new double[iterations];
			 accuracy    = new double[iterations];
			 fmeasure    = new double[iterations];	
			 roc_auc     = new double[iterations];
	  	   	
			 for(double thres =0.1; thres<=1.0;thres=thres+0.1)
			 {
				 for(int itr=0; itr<iterations;itr++) 
				 	{
					 train_data_source = new DataSource[i];
					 test_data_source = test_data_source;// Its not an array test set is same for all the training subsets  						

					 trains= new Instances[i];
					 tests = new  Instances[i];
				
					 //Set train and test data source
					 for(int j=1;j<=i;j++)
					 	{
					
						 	// file path  subset = i, and iteration = itr
						 	String train_file_path = path+ source_project+"-arff\\"+ type+"\\train_"+(itr+1)+"\\k"+i+"\\"+source_project+"_train_sub_"+j+".arff";
						 	String test_file_path = path+ source_project+"-arff\\"+ type+"\\test_"+(itr+1)+"\\"+source_project+"_test.arff";
						
						 	// System.out.println("test file path="+ test_file_path);
						 	//DataSource trainsource;						
						 	read_file(j-1, train_file_path, test_file_path);
						
						 	pre_process_data(j-1);  
						
					 	}// j
				
					 //pre-dict usinensemble
					 compute_results_of_ensemble(trains, tests, i, model, itr, thres);
								
				 	}// itr
	  	
			 
			  String classifier_name = model[0].getClass().getSimpleName();
			  compute_avg_stdev_and_insert(classifier_name,i, thres, precision,  recall,  accuracy,  fmeasure,  roc_auc);
			 }//thres
			
	  	}// for i
	  	
	 }	


// This file will compute the results of ensemble creation using the specified classifier model
private void compute_results_of_ensemble(Instances[] trains2, Instances[] tests2, int no_of_subsets, Classifier model[], int itr, double thres) 
{
	 
	int tp=0, fp = 0, tn = 0, fn=0;
	
	try
	{
		for(int i=0;i<no_of_subsets; i++)
		{
			model[i].buildClassifier(trains2[i]);
			//System.out.println(model[0].getClass().getSimpleName());
		}		
		
	 for (int j = 0; j < tests2[0].numInstances(); j++) 
	 {
		     
		 double score[][] =  new double[no_of_subsets][2];
		 Instance curr  =  tests2[0].instance(j);  //tests2[0]  is not an error as number of instance in same in all tests2[0], tests2[1]..., any one can be used
		 double actual = curr.classValue();
		 
		 for(int i=0; i<no_of_subsets;i++)
		 { 
			 
			 score[i]= model[i].distributionForInstance(curr);
			
		 }
		// System.out.println(" actual="+actual+ "  mode 0=" +  score[0][1]+   " model 1="+ score[1][1]);
		 
		 // Find index of the model giving maximum valaue for the test instance
		 double avg_score = 0.0;
		 for(int i=0;i<no_of_subsets;i++)
		 {
			 
			 
				 avg_score= avg_score+ score[i][1];
			 
			 
		 }
		 
		 avg_score = (1.0*avg_score)/no_of_subsets;
		 
		 double predicted = 0;
	     if ( avg_score <= thres) 
	     {
	      predicted = 0;
	     } else 
	     {
	      predicted = 1;
	     }
		 
	     if (actual == 1) 
	       {
		      if (predicted == 1) 
		      {
		       tp++;
		      } else
		      {
		       fn++;
		      }
		     }

		 else if (actual == 0)
		   {
		      if (predicted == 0) 
		      {
		       tn++;
		      } else 
		      {
		       fp++;
		      }
		     }//else if

		 System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
		 
	 }//for

	} catch (Exception e) 
	{
		e.printStackTrace();
	}
	

 util5_met ut =  new util5_met();
 precision[itr]=ut.compute_precision(tp, fp, tn, fn);
 recall[itr]= ut.compute_recall(tp, fp, tn, fn);
 fmeasure[itr]=ut.compute_fmeasure(tp, fp, tn, fn);
 accuracy[itr]=ut.compute_accuracy(tp, fp, tn, fn);
 roc_auc[itr] =0.0;// call some method here if possible	
		
}// function



// This function is used to pre-process the dataset
public void pre_process_data(int i)
	{
		
		  try
		    {			 
			   //1. TF-IDF
			  StringToWordVector tfidf_filter = new StringToWordVector();
			  tfidf_filter.setIDFTransform(true);
			  tfidf_filter.setInputFormat(trains[i]);
	     	  trains[i] = Filter.useFilter(trains[i], tfidf_filter);  
	     	  
	     	  tests[i] = Filter.useFilter(tests[i], tfidf_filter);
	     	  

	 	     //2. Standarize  (not normalize because normalization is affected by outliers very easily)   	  
	     	//  Standardize  std_filter =  new Standardize();
	     	 // std_filter.setInputFormat(trains[i]);
	     	//  trains[i] =  Filter.useFilter(trains[i],std_filter);  
	     	  
	     	 // tests[i]  =  Filter.useFilter(tests[i], std_filter);
	     	
	 	     //3. Discretizations
	     	 // Discretize dfilter = new Discretize();
		      //dfilter.setInputFormat(trains);
		     // trains = Filter.useFilter(trains, dfilter);
		      
		      //tests = Filter.useFilter(tests, dfilter);
		      
		
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

}
	
/*
// This function is used to train and test a using a given classifier
public Evaluation pred(Classifier model) 
{
	Evaluation evaluation = null;
	
	try {
	      
		evaluation= new Evaluation(trains);		
		model.buildClassifier(trains);
		evaluation.evaluateModel(model, tests);
	
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}*/


public Connection initdb(String db_name)
{
	Connection conn= null;
	
	try {
		      Class.forName(driver).newInstance();
		       conn = DriverManager.getConnection(url+db_name,user_name,password);
		      //System.out.println(" dbname="+ db_name+ "user name"+ userName+ " password="+ password);
		      if(conn==null)
		      {
		    	  System.out.println(" Database connection is null. Check it.");
		      }
		      
		 } catch (Exception e) 
		 {
		      e.printStackTrace();
		 }
		return conn;
}


// This method computes the average value  and std. deviation and inserts them in a db
public void compute_avg_stdev_and_insert(String classifier_name, int no_of_subsets, double thres, double[] precision, double[] recall, double[] accuracy, double[] fmeasure, double[] roc_auc) 
{

	 // computes following metrics:
		
		// * 1. Precision
		// * 2. Recall
		 //* 3. Accuracy
		 //* 4. F measure
		 //* 5. ROC-AUC
		 

		double avg_precision = 0.0;
		double avg_recall = 0.0;
		double avg_accuracy = 0.0;
		double avg_fmeasure = 0.0;	
		double avg_roc_auc = 0.0;
		
		double std_precision = 0.0;
		double std_recall = 0.0;
		double std_accuracy = 0.0;
		double std_fmeasure = 0.0;	
		double std_roc_auc = 0.0;
		//double total_instances = 0.0;
		
		util5_met  ut = new util5_met();
		
		avg_precision   = ut.compute_mean(precision);
		avg_recall      = ut.compute_mean(recall);
		avg_fmeasure    = ut.compute_mean(fmeasure);
		avg_accuracy    = ut.compute_mean(accuracy);
		avg_roc_auc     = ut.compute_mean(roc_auc);
		
		std_precision   = ut.compute_stddev(precision);
		std_recall      = ut.compute_stddev(recall);
		std_fmeasure    = ut.compute_stddev(fmeasure);
		std_accuracy    = ut.compute_stddev(accuracy);
		std_roc_auc     = ut.compute_stddev(roc_auc);
		
		
		String insert_str =  " insert into "+ result_table +"  values("+ "'"+ source_project+"','"+ source_project +"',"+no_of_subsets+",'"+ classifier_name+"',"+thres+","+ trains[0].numInstances() + ","+ tests[0].numInstances()+","
		                       + iterations+","+trains[0].numAttributes() +","+avg_precision+","+ std_precision+","+ avg_recall+","+ std_recall+","+avg_fmeasure+","+std_fmeasure+","+ avg_accuracy 
		                       +","+std_accuracy+","+ avg_roc_auc+","+ std_roc_auc+" )";
		System.out.println("Inserting="+ insert_str);
		
		Connection conn2 = initdb(db_name);
		if(conn2==null)
		{
			System.out.println(" Databasse connection is null");
			
		}
		
		try 
		{
			Statement stmt2 = conn2.createStatement();
			stmt2.executeUpdate(insert_str);
			stmt2.close();
			conn2.close();
			
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
	
}



//This is the main function
public static void main(String args[])
	{
	
	  
	/*  Classifier models [] = {  new RandomForest(),
			                    new Logistic(),
			  					new J48()};*/
	  
	  
	 RandomForest rf[] = new RandomForest[10];
	 for(int i=0; i<10;i++)
	 {
		rf[i]= new RandomForest(); 
	 }
	 
	 log_pred_ensemble_not_used clp = new log_pred_ensemble_not_used();	
	 clp.ensemble_prediction(rf);
		
	}
	
}


