import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

import weka.attributeSelection.InfoGainAttributeEval;
import weka.attributeSelection.Ranker;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.BayesNet;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.evaluation.NominalPrediction;
import weka.classifiers.functions.Logistic;
import weka.classifiers.functions.MultilayerPerceptron;
import weka.classifiers.functions.RBFNetwork;
//import weka.classifiers.functions.SMO;  // I am using SMO.Java
import weka.classifiers.meta.AdaBoostM1;
import weka.classifiers.meta.Bagging;
import weka.classifiers.meta.Stacking;
import weka.classifiers.meta.Vote;
import weka.classifiers.rules.DecisionTable;
import weka.classifiers.rules.ZeroR;
import weka.classifiers.trees.ADTree;
import weka.classifiers.trees.J48;
import weka.classifiers.trees.RandomForest;
import weka.classifiers.trees.RandomTree;
import weka.core.FastVector;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.SelectedTag;
import weka.core.converters.ArffSaver;
import weka.core.converters.ConverterUtils.DataSource;
import weka.filters.Filter;
import weka.filters.supervised.attribute.AttributeSelection;
import weka.filters.supervised.attribute.Discretize;
import weka.filters.unsupervised.attribute.Normalize;
import weka.filters.unsupervised.attribute.Standardize;
import weka.filters.unsupervised.attribute.StringToWordVector;



/*
 * @Author: Sangeeta
 * 1. This is the simple log prediction code that is used to predict logging using LogIm model classifier
 * 2.
 * 3. Using SMO. java in whihc I have modified following two things:
 *   1. m_fitLogisticModels = **true.** 
 *   2. smo.buildClassifier(train, cl1, cl2, **true**, -1, -1)
 *   
 *   
 *   Code Version  =  baseline + +ensemble + 1 feature selection techniqie (we create one file for each feature selection technique)
 * 

 * */
public class log_pred_baseline_LOGIM_70_30_NEW_rc_feb9_roc
{

	/*
	 String path = "E:\\Sangeeta\\Research\\L5IMBAL\\dataset\\";
	 String user_name =  "sangeetal";
	 String password = "sangeetal";
	 String url = "jdbc:mysql://localhost:3307/";
	 String driver = "com.mysql.jdbc.Driver"; 
	  
	// */
	
	/*
	String path = "F:\\Research\\L5IMBAL\\dataset\\";
	String user_name =  "root";
	String password = "1234";
	String url = "jdbc:mysql://localhost:3306/";
	String driver = "com.mysql.jdbc.Driver";
	//*/
	 

	// jiit server
	///*
	String path = "D:\\Sangeeta\\Research\\L5IMBAL\\dataset\\";
	String user_name =  "root";
	String password = "1234";
	String url = "jdbc:mysql://localhost:3306/";
	String driver = "com.mysql.jdbc.Driver";
	//*/
	int iterations=10;	
	String type = "catch";
	//String type ="if";

	String source_project="tomcat";	
	//String source_project="cloudstack";	
	//String source_project="hd";
	
	
	//String db_name ="logging5_imbal";
	
	String  db_name = "logging5_imbal_rc_feb9";
	String result_table = "result_baseline_logim_"+type;
	//String result_table = "temp_threshold";

	
	// we are using balanced files for with-in project logging prediction		
   	String train_file_path = path+source_project+"-arff"+"\\" +type+"\\train";
   	String test_file_path = path +source_project +"-arff"+"\\"+type+"\\test";
		
	//DataSource trainsource;
	DataSource train_data_source;
	DataSource test_data_source;
	
	Instances trains;
	Instances tests;
	
	Evaluation result;
		
	int instance_count_train = 0;
	int instance_count_test= 0;
	 

	//Connection conn=null;	
	//java.sql.Statement stmt = null;
   
	double precision[][];
	double recall[][];
	double fmeasure[][];
	double accuracy[][];
	double roc_auc[][];
	
	long trainbegin ;
	long trainend ;
	long testbegin ;
	long testend ;
	
	long train_time[][] ;
	long test_time[][];
	
	double no_of_features[];
	
	// This function uses dataset from the ARFF files
	public void read_file(int i)
	 { 
		try 
			{
			
				train_data_source = new DataSource(train_file_path+"_"+i+"\\k1\\"+source_project+"_train.arff");
				//System.out.println("File path = "+ train_file_path+"_"+i+"\\k1\\"+source_project+"_train.arff");
				trains = train_data_source.getDataSet();
				trains.setClassIndex(0);
				
				
				test_data_source = new DataSource(test_file_path+"_"+i+"\\"+source_project+"_test.arff");
				tests = test_data_source.getDataSet();
				tests.setClassIndex(0);	
								
				
				instance_count_train = trains.numInstances();
				instance_count_test = tests.numInstances();
				
				System.out.println("Instance count Train ="+ instance_count_train+"   Instance count Test="+ instance_count_test);// + "  Instance count target="+ instance_count_target);
		    
			} catch (Exception e) 
			{
			
				e.printStackTrace();
			}	  
			
		}	
	

// This function is used to pre-process the dataset
public void pre_process_data()
	{
		
		  try
		    {
			 
			   //1. TF-IDF
			  StringToWordVector tfidf_filter = new StringToWordVector();
			  tfidf_filter.setIDFTransform(true);
			  tfidf_filter.setInputFormat(trains);
	     	  trains = Filter.useFilter(trains, tfidf_filter);  
	     	  
	     	  tests = Filter.useFilter(tests, tfidf_filter);
	     	  

	 	     //2. Standarize  (not normalize because normalization is affected by outliers very easily)   	  
	     	 // Standardize  std_filter =  new Standardize();
	     	 // std_filter.setInputFormat(trains);
	     	 // trains= Filter.useFilter(trains,std_filter);  
	     	  
	     	 // tests =  Filter.useFilter(tests, std_filter);
	     	
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
//This method will divide the data in =to two parts: Not used i this work
public void create_train_and_test_split(double train_size, double test_size) 
{
	all_data.randomize(new java.util.Random(0));
	int trainSize = (int) Math.round(all_data.numInstances() * train_size);
	int testSize = all_data.numInstances() - trainSize;
	trains = new Instances(all_data, 0, trainSize);
	tests = new Instances(all_data, trainSize, testSize);

}*/


// This function is used to train and test a using a given classifier
/*public Evaluation pred(Classifier model) 
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

//Mjority Vote
public Evaluation pred2_info_gain_maj_vote( int itr, int p_of_features) 
{

	// classifier_name = "J48-RF-SVM";	
	// Feature selection = "info gain";
	
	Evaluation evaluation = null;
	//double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
	
	try {
		
		//======================================//
		//Newly added code:  Feature selection  //
		
		 int total_features = trains.numAttributes();
		/* int select_feature_count =  (total_features*p_of_features)/100;
		 AttributeSelection attributeSelection = new  AttributeSelection(); 
	     Ranker ranker = new Ranker(); 
	     ranker.setNumToSelect(select_feature_count-1);
	     InfoGainAttributeEval infoGainAttributeEval = new InfoGainAttributeEval(); 
	     attributeSelection.setEvaluator(infoGainAttributeEval); 
	     attributeSelection.setSearch(ranker); 
	     attributeSelection.setInputFormat(trains); 
	     
	     trains = Filter.useFilter(trains, attributeSelection); 
	     
	     tests= Filter.useFilter(tests, attributeSelection);*/
		
		//======================================//
	      
		trainbegin = System.currentTimeMillis();
		
		//================================//
		
		Vote voter =  new Vote();  
		Classifier classif[] = {new RandomForest(), new J48(), new SMO()};
		voter.setClassifiers(classif); 
		voter.setCombinationRule(new SelectedTag(Vote.MAJORITY_VOTING_RULE, Vote.TAGS_RULES));
		evaluation= new Evaluation(trains);
	    voter.buildClassifier(trains);
		
		//===============================//
		
		
		trainend = System.currentTimeMillis();
		
		int thres_itr= 0;
		for(double thres=0.1; thres<=0.9; thres=thres+0.1)
		 {
			double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
			
			//evaluation.evaluateModel(model, tests);	
			testbegin = System.currentTimeMillis();
			for (int j = 0; j < tests.numInstances(); j++) 
			 {
			     
				double score[] ;
				Instance curr  =  tests.instance(j);  
				double actual = curr.classValue();
			 
			  
				score= voter.distributionForInstance(curr);
				 
			 
				// Find index of the model giving maximum value for the test instance
			 
				double predicted = 0;
				if ( score[1] <= thres) 
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

			  // System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
		   }//for

		
			testend = System.currentTimeMillis();

			util5_met ut =  new util5_met();
	 
			precision[itr][thres_itr]=ut.compute_precision(tp, fp, tn, fn);
			double temp = ut.compute_precision(tp, fp, tn, fn);
		
			recall[itr][thres_itr]= ut.compute_recall(tp, fp, tn, fn);
			fmeasure[itr][thres_itr]=ut.compute_fmeasure(tp, fp, tn, fn);
			accuracy[itr][thres_itr]=ut.compute_accuracy(tp, fp, tn, fn);
			// rc feb 9 start
			
			// @old code roc_auc[itr][thres_itr] =0.0;// call some method here if possible	
						
				evaluation.evaluateModel(voter, tests);
				roc_auc[itr][thres_itr] = evaluation.areaUnderROC(1)*100;
			// rc feb 9 end
						
			//System.out.println("precision ["+itr+"]["+thres_itr+"]="+ precision[itr][thres_itr]+ "  temp="+temp+ " thres= "+ thres + " tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
	
			train_time[itr][thres_itr] = trainend -trainbegin;
			test_time[itr][thres_itr] = testend-testbegin;
	
			no_of_features[itr] =  trains.numAttributes();

			//System.out.println("Pre="+ precision[]+"  rec="+ recall+"   fm="+ fmeasure+ "  acc="+ accuracy);
	
			thres_itr =  thres_itr + 1;
	  }// Thresh
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}



// Average Vote
public Evaluation pred2_info_gain_avg_vote( int itr, int p_of_features) 
{

	
	Evaluation evaluation = null;
	//double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
	
	try {
		
		//======================================//
		//Newly added code:  Feature selection  //
		
		 int total_features = trains.numAttributes();
		 /*int select_feature_count =  (total_features*p_of_features)/100;
		 AttributeSelection attributeSelection = new  AttributeSelection(); 
	     Ranker ranker = new Ranker(); 
	     ranker.setNumToSelect(select_feature_count-1);
	     InfoGainAttributeEval infoGainAttributeEval = new InfoGainAttributeEval(); 
	     attributeSelection.setEvaluator(infoGainAttributeEval); 
	     attributeSelection.setSearch(ranker); 
	     attributeSelection.setInputFormat(trains); 
	     
	     trains = Filter.useFilter(trains, attributeSelection); 
	     
	     tests= Filter.useFilter(tests, attributeSelection);*/
		
		//======================================//
	      
		trainbegin = System.currentTimeMillis();
		
		//================================//
		
		Vote voter =  new Vote();  
		Classifier classif[] = {new RandomForest(), new J48(), new SMO()};
		voter.setClassifiers(classif); 
		voter.setCombinationRule(new SelectedTag(Vote.AVERAGE_RULE, Vote.TAGS_RULES));
		evaluation= new Evaluation(trains);
	    voter.buildClassifier(trains);
		
		//===============================//
		
		
		trainend = System.currentTimeMillis();
		
		int thres_itr= 0;
		for(double thres=0.1; thres<=0.9; thres=thres+0.1)
		 {
			double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
			
			//evaluation.evaluateModel(model, tests);	
			testbegin = System.currentTimeMillis();
			for (int j = 0; j < tests.numInstances(); j++) 
			 {
			     
				double score[] ;
				Instance curr  =  tests.instance(j);  
				double actual = curr.classValue();
			 
			  
				score= voter.distributionForInstance(curr);
				 
			 
				// Find index of the model giving maximum value for the test instance
			 
				double predicted = 0;
				if ( score[1] <= thres) 
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

			  // System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
		   }//for

		
			testend = System.currentTimeMillis();

			util5_met ut =  new util5_met();
	 
			precision[itr][thres_itr]=ut.compute_precision(tp, fp, tn, fn);
			double temp = ut.compute_precision(tp, fp, tn, fn);
		
			recall[itr][thres_itr]= ut.compute_recall(tp, fp, tn, fn);
			fmeasure[itr][thres_itr]=ut.compute_fmeasure(tp, fp, tn, fn);
			accuracy[itr][thres_itr]=ut.compute_accuracy(tp, fp, tn, fn);
			
			// rc feb 9 start
			
			// @old code roc_auc[itr][thres_itr] =0.0;// call some method here if possible	
							
			 evaluation.evaluateModel(voter, tests);
			roc_auc[itr][thres_itr] = evaluation.areaUnderROC(1)*100;
			// rc feb 9 end
									
						
			//System.out.println("precision ["+itr+"]["+thres_itr+"]="+ precision[itr][thres_itr]+ "  temp="+temp+ " thres= "+ thres + " tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
	
			train_time[itr][thres_itr] = trainend -trainbegin;
			test_time[itr][thres_itr] = testend-testbegin;
	
			no_of_features[itr] =  trains.numAttributes();

			//System.out.println("Pre="+ precision[]+"  rec="+ recall+"   fm="+ fmeasure+ "  acc="+ accuracy);
	
			thres_itr =  thres_itr + 1;
	  }// Thresh
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}


//max Vote
public Evaluation pred2_info_gain_max_vote( int itr, int p_of_features) 
{

	// classifier_name = "J48-RF-SVM";	
	// Feature selection = "info gain";
	
	Evaluation evaluation = null;
	//double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
	
	try {
		
		//======================================//
		//Newly added code:  Feature selection  //
		
		 int total_features = trains.numAttributes();
		 /*int select_feature_count =  (total_features*p_of_features)/100;
		 AttributeSelection attributeSelection = new  AttributeSelection(); 
	     Ranker ranker = new Ranker(); 
	     ranker.setNumToSelect(select_feature_count-1);
	     InfoGainAttributeEval infoGainAttributeEval = new InfoGainAttributeEval(); 
	     attributeSelection.setEvaluator(infoGainAttributeEval); 
	     attributeSelection.setSearch(ranker); 
	     attributeSelection.setInputFormat(trains); 
	     
	     trains = Filter.useFilter(trains, attributeSelection); 
	     
	     tests= Filter.useFilter(tests, attributeSelection);*/
		
		//======================================//
	      
		trainbegin = System.currentTimeMillis();
		
		//================================//
		
		Vote voter =  new Vote();  
		Classifier classif[] = {new RandomForest(), new J48(), new SMO()};
		voter.setClassifiers(classif); 
		voter.setCombinationRule(new SelectedTag(Vote.MAX_RULE, Vote.TAGS_RULES));
		evaluation= new Evaluation(trains);
	    voter.buildClassifier(trains);
		
		//===============================//
		
		
		trainend = System.currentTimeMillis();
		
		int thres_itr= 0;
		for(double thres=0.1; thres<=0.9; thres=thres+0.1)
		 {
			double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
			
			//evaluation.evaluateModel(model, tests);	
			testbegin = System.currentTimeMillis();
			for (int j = 0; j < tests.numInstances(); j++) 
			 {
			     
				double score[] ;
				Instance curr  =  tests.instance(j);  
				double actual = curr.classValue();
			 
			  
				score= voter.distributionForInstance(curr);
				 
			 
				// Find index of the model giving maximum value for the test instance
			 
				double predicted = 0;
				if ( score[1] <= thres) 
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

			  // System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
		   }//for

		
			testend = System.currentTimeMillis();

			util5_met ut =  new util5_met();
	 
			precision[itr][thres_itr]=ut.compute_precision(tp, fp, tn, fn);
			double temp = ut.compute_precision(tp, fp, tn, fn);
		
			recall[itr][thres_itr]= ut.compute_recall(tp, fp, tn, fn);
			fmeasure[itr][thres_itr]=ut.compute_fmeasure(tp, fp, tn, fn);
			accuracy[itr][thres_itr]=ut.compute_accuracy(tp, fp, tn, fn);
			// rc feb 9 start
			
			// @old code roc_auc[itr][thres_itr] =0.0;// call some method here if possible	
										
			 evaluation.evaluateModel(voter, tests);
			roc_auc[itr][thres_itr] = evaluation.areaUnderROC(1)*100;
			// rc feb 9 end
						
			//System.out.println("precision ["+itr+"]["+thres_itr+"]="+ precision[itr][thres_itr]+ "  temp="+temp+ " thres= "+ thres + " tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
	
			train_time[itr][thres_itr] = trainend -trainbegin;
			test_time[itr][thres_itr] = testend-testbegin;
	
			no_of_features[itr] =  trains.numAttributes();

			//System.out.println("Pre="+ precision[]+"  rec="+ recall+"   fm="+ fmeasure+ "  acc="+ accuracy);
	
			thres_itr =  thres_itr + 1;
	  }// Thresh
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}


//Stacking Vote
public Evaluation pred2_info_gain_stack( int itr, int p_of_features) 
{

	// classifier_name = "J48-RF-SVM";	
	// Feature selection = "info gain";
	
	Evaluation evaluation = null;
	//double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
	
	try {
		
		//======================================//
		//Newly added code:  Feature selection  //
		
		 int total_features = trains.numAttributes();
		 /*int select_feature_count =  (total_features*p_of_features)/100;
		 AttributeSelection attributeSelection = new  AttributeSelection(); 
	     Ranker ranker = new Ranker(); 
	     ranker.setNumToSelect(select_feature_count-1);
	     InfoGainAttributeEval infoGainAttributeEval = new InfoGainAttributeEval(); 
	     attributeSelection.setEvaluator(infoGainAttributeEval); 
	     attributeSelection.setSearch(ranker); 
	     attributeSelection.setInputFormat(trains); 
	     
	     trains = Filter.useFilter(trains, attributeSelection); 
	     
	     tests= Filter.useFilter(tests, attributeSelection);*/
		
		//======================================//
	      
		trainbegin = System.currentTimeMillis();
		
		//================================//
		
		 Classifier[] cfsArray = new Classifier[3]; 
		 Classifier classif[] = {new RandomForest(), new J48(), new SMO()};
		  
		  cfsArray[0]=classif[0];
		  cfsArray[1]=classif[1];
		  cfsArray[2]=classif[2];
		  
		  Logistic cfsm =  new Logistic();
		  
		  Stacking stack_model= new Stacking();
		  stack_model.setClassifiers(cfsArray);
		  stack_model.setMetaClassifier(cfsm);
		  stack_model.setSeed(1);
		  
		  stack_model.buildClassifier(trains);
	      evaluation= new Evaluation(trains);
		//===============================//
		
		
		trainend = System.currentTimeMillis();
		
		int thres_itr= 0;
		for(double thres=0.1; thres<=0.9; thres=thres+0.1)
		 {
			double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
			
			//evaluation.evaluateModel(model, tests);	
			testbegin = System.currentTimeMillis();
			for (int j = 0; j < tests.numInstances(); j++) 
			 {
			     
				double score[] ;
				Instance curr  =  tests.instance(j);  
				double actual = curr.classValue();
			 
			  
				score= stack_model.distributionForInstance(curr);
				 
			 
				// Find index of the model giving maximum value for the test instance
			 
				double predicted = 0;
				if ( score[1] <= thres) 
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

			  // System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
		   }//for

		
			testend = System.currentTimeMillis();

			util5_met ut =  new util5_met();
	 
			precision[itr][thres_itr]=ut.compute_precision(tp, fp, tn, fn);
			double temp = ut.compute_precision(tp, fp, tn, fn);
		
			recall[itr][thres_itr]= ut.compute_recall(tp, fp, tn, fn);
			fmeasure[itr][thres_itr]=ut.compute_fmeasure(tp, fp, tn, fn);
			accuracy[itr][thres_itr]=ut.compute_accuracy(tp, fp, tn, fn);
			
			// rc feb 9 start
			// @old code roc_auc[itr][thres_itr] =0.0;// call some method here if possible	
							
			 evaluation.evaluateModel(stack_model, tests);
			roc_auc[itr][thres_itr] = evaluation.areaUnderROC(1)*100;
			// rc feb 9 end
						
			//System.out.println("precision ["+itr+"]["+thres_itr+"]="+ precision[itr][thres_itr]+ "  temp="+temp+ " thres= "+ thres + " tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
	
			train_time[itr][thres_itr] = trainend -trainbegin;
			test_time[itr][thres_itr] = testend-testbegin;
	
			no_of_features[itr] =  trains.numAttributes();

			//System.out.println("Pre="+ precision[]+"  rec="+ recall+"   fm="+ fmeasure+ "  acc="+ accuracy);
	
			thres_itr =  thres_itr + 1;
	  }// Thresh
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}


//Bagging Vote
public Evaluation pred2_info_gain_bagging( int itr, int p_of_features, Classifier  classif) 
{

	// classifier_name = "J48-RF-SVM";	
	// Feature selection = "info gain";
	
	Evaluation evaluation = null;
	//double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
	
	try {
		
		//======================================//
		//Newly added code:  Feature selection  //
		
		 int total_features = trains.numAttributes();
		/* int select_feature_count =  (total_features*p_of_features)/100;
		 AttributeSelection attributeSelection = new  AttributeSelection(); 
	     Ranker ranker = new Ranker(); 
	     ranker.setNumToSelect(select_feature_count-1);
	     InfoGainAttributeEval infoGainAttributeEval = new InfoGainAttributeEval(); 
	     attributeSelection.setEvaluator(infoGainAttributeEval); 
	     attributeSelection.setSearch(ranker); 
	     attributeSelection.setInputFormat(trains); 
	     
	     trains = Filter.useFilter(trains, attributeSelection); 
	     
	     tests= Filter.useFilter(tests, attributeSelection);*/
		
		//======================================//
	      
		trainbegin = System.currentTimeMillis();
		
		//================================//
		
		Bagging bag_model =  new Bagging();	
		
	    bag_model.setClassifier(classif);
	    bag_model.setNumIterations(20);
		
	    evaluation= new Evaluation(trains);		
		bag_model.buildClassifier(trains);
		
		//===============================//
		
		
		trainend = System.currentTimeMillis();
		
		int thres_itr= 0;
		for(double thres=0.1; thres<=0.9; thres=thres+0.1)
		 {
			double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
			
			//evaluation.evaluateModel(model, tests);	
			testbegin = System.currentTimeMillis();
			for (int j = 0; j < tests.numInstances(); j++) 
			 {
			     
				double score[] ;
				Instance curr  =  tests.instance(j);  
				double actual = curr.classValue();
			 
			  
				score= bag_model.distributionForInstance(curr);
				 
			 
				// Find index of the model giving maximum value for the test instance
			 
				double predicted = 0;
				if ( score[1] <= thres) 
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

			  // System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
		   }//for

		
			testend = System.currentTimeMillis();

			util5_met ut =  new util5_met();
	 
			precision[itr][thres_itr]=ut.compute_precision(tp, fp, tn, fn);
			double temp = ut.compute_precision(tp, fp, tn, fn);
		
			recall[itr][thres_itr]= ut.compute_recall(tp, fp, tn, fn);
			fmeasure[itr][thres_itr]=ut.compute_fmeasure(tp, fp, tn, fn);
			accuracy[itr][thres_itr]=ut.compute_accuracy(tp, fp, tn, fn);
			// rc feb 9 start
			
			// @old code roc_auc[itr][thres_itr] =0.0;// call some method here if possible	
							
				 evaluation.evaluateModel(bag_model, tests);
				roc_auc[itr][thres_itr] = evaluation.areaUnderROC(1)*100;
			// rc feb 9 end
						
			//System.out.println("precision ["+itr+"]["+thres_itr+"]="+ precision[itr][thres_itr]+ "  temp="+temp+ " thres= "+ thres + " tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
	
			train_time[itr][thres_itr] = trainend -trainbegin;
			test_time[itr][thres_itr] = testend-testbegin;
	
			no_of_features[itr] =  trains.numAttributes();

			//System.out.println("Pre="+ precision[]+"  rec="+ recall+"   fm="+ fmeasure+ "  acc="+ accuracy);
	
			thres_itr =  thres_itr + 1;
	  }// Thresh
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}


//Boosting Vote
public Evaluation pred2_info_gain_boosting( int itr, int p_of_features, Classifier  classif) 
{

	// classifier_name = "J48-RF-SVM";	
	// Feature selection = "info gain";
	
	Evaluation evaluation = null;
	//double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
	
	try {
		
		//======================================//
		//Newly added code:  Feature selection  //
		
		 int total_features = trains.numAttributes();
		 /*int select_feature_count =  (total_features*p_of_features)/100;
		 AttributeSelection attributeSelection = new  AttributeSelection(); 
	     Ranker ranker = new Ranker(); 
	     ranker.setNumToSelect(select_feature_count-1);
	     InfoGainAttributeEval infoGainAttributeEval = new InfoGainAttributeEval(); 
	     attributeSelection.setEvaluator(infoGainAttributeEval); 
	     attributeSelection.setSearch(ranker); 
	     attributeSelection.setInputFormat(trains); 
	     
	     trains = Filter.useFilter(trains, attributeSelection); 
	     
	     tests= Filter.useFilter(tests, attributeSelection);*/
		
		//======================================//
	      
		trainbegin = System.currentTimeMillis();
		
		//================================//
		
		AdaBoostM1 boost_model =  new AdaBoostM1();	
	    boost_model.setClassifier(classif);
	    boost_model.setNumIterations(20);
		
	    evaluation= new Evaluation(trains);		
		boost_model.buildClassifier(trains);
		
		//=================================//
		
		trainend = System.currentTimeMillis();
		
		int thres_itr= 0;
		for(double thres=0.1; thres<=0.9; thres=thres+0.1)
		 {
			double tp=0.0, fp=0.0, tn =0.0,fn=0.0;
			
			//evaluation.evaluateModel(model, tests);	
			testbegin = System.currentTimeMillis();
			for (int j = 0; j < tests.numInstances(); j++) 
			 {
			     
				double score[] ;
				Instance curr  =  tests.instance(j);  
				double actual = curr.classValue();
			 
			  
				score= boost_model.distributionForInstance(curr);
				 
			 
				// Find index of the model giving maximum value for the test instance
			 
				double predicted = 0;
				if ( score[1] <= thres) 
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

			  // System.out.println("tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
		   }//for

		
			testend = System.currentTimeMillis();

			util5_met ut =  new util5_met();
	 
			precision[itr][thres_itr]=ut.compute_precision(tp, fp, tn, fn);
			double temp = ut.compute_precision(tp, fp, tn, fn);
		
			recall[itr][thres_itr]= ut.compute_recall(tp, fp, tn, fn);
			fmeasure[itr][thres_itr]=ut.compute_fmeasure(tp, fp, tn, fn);
			accuracy[itr][thres_itr]=ut.compute_accuracy(tp, fp, tn, fn);
			
			// rc feb 9 start
			
			// @old code roc_auc[itr][thres_itr] =0.0;// call some method here if possible	
			
			evaluation.evaluateModel(boost_model, tests);
			roc_auc[itr][thres_itr] = evaluation.areaUnderROC(1)*100;
			// rc feb 9 end
			
			//System.out.println("precision ["+itr+"]["+thres_itr+"]="+ precision[itr][thres_itr]+ "  temp="+temp+ " thres= "+ thres + " tp="+ tp+ "  fp"+ fp +" fn="+fn+" tn="+tn);
			 
	
			train_time[itr][thres_itr] = trainend -trainbegin;
			test_time[itr][thres_itr] = testend-testbegin;
	
			no_of_features[itr] =  trains.numAttributes();

			//System.out.println("Pre="+ precision[]+"  rec="+ recall+"   fm="+ fmeasure+ "  acc="+ accuracy);
	
			thres_itr =  thres_itr + 1;
	  }// Thresh
	
	} catch (Exception e) {
	
		e.printStackTrace();
	}

	return evaluation;
	
	//http://www.programcreek.com/2013/01/a-simple-machine-learning-example-in-java/
}




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
public void compute_avg_stdev_and_insert(String classifier_name, String ensemble_tech, double thres, String feature_sel_tech, int p_of_features, double[] precision, double[] recall, double[] accuracy, double[] fmeasure, double[] roc_auc , long train_time[], long test_time[]) 
{

	 // computes following metrics:
		/*
		 * 1. Precision
		 * 2. Recall
		 * 3. Accuracy
		 * 4. F measure
		 * 5. ROC-AUC
		 * */

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
		
		double avg_train_time= ut.compute_time_avg(train_time);	
		double avg_test_time = ut.compute_time_avg(test_time);
		double std_train_time= ut.compute_time_std(train_time);
		double std_test_time =ut.compute_time_std(test_time);
			
		double avg_features = ut.compute_mean(no_of_features);
		double std_features = ut.compute_stddev(no_of_features);
		
	   // System.out.println("model ="+classifier_name +"   Acc = "+ avg_accuracy + "  size="+ pred_10_db.size());
		
		String insert_str =  " insert into "+ result_table +"  values("+ "'"+ source_project+"','"+ "same_as_source" +"','"+ classifier_name+"','"+ensemble_tech+"',"+thres+",'"+feature_sel_tech+"',"+p_of_features+"," +trains.numInstances() + ","+ tests.numInstances()+","
		                       + iterations+","+avg_features+ ","+ std_features +","+avg_precision+","+ std_precision+","+ avg_recall+","+ std_recall+","+avg_fmeasure+","+std_fmeasure+","+ avg_accuracy 
		                       +","+std_accuracy+","+ avg_roc_auc+","+ std_roc_auc+ ","+avg_train_time+ ","+std_train_time+","+ avg_test_time+","+ std_test_time+ " )";
		
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

// This is the function created to store the files to help in debugging
  public void save_file_temp_location(Instances trains2, Instances tests2)
  	{
	 
	  try
	  {
	       ArffSaver saver = new ArffSaver();
           saver.setInstances(trains);
       
		   saver.setFile(new File("F:\\result\\logging5_imbal_logg_pred_baseline.arff"));
		
		   saver.writeBatch();
	
	 } catch (IOException e) 
	{
	
	 	e.printStackTrace();
	}
       
}


//This is the main function
public static void main(String args[])
	{
	
	 
		log_pred_baseline_LOGIM_70_30_NEW_rc_feb9_roc clp = new log_pred_baseline_LOGIM_70_30_NEW_rc_feb9_roc();
		String classifier_name= "";
		String ensemble_tech = "";
		String feature_selection_tech= "no-feature-selection";
			
			for(int p_of_features=100; p_of_features>=100; p_of_features=p_of_features-10)
			{
				clp.precision   = new double[clp.iterations][9];
				clp.recall      = new double[clp.iterations][9];
				clp.accuracy    = new double[clp.iterations][9];
				clp.fmeasure    = new double[clp.iterations][9];	
				clp.roc_auc     = new double[clp.iterations][9];
			    
				clp.train_time= new long[clp.iterations][9];
				clp.test_time= new long[clp.iterations][9];
				
				clp.no_of_features = new double[clp.iterations];
			
				for(int i=0; i<clp.iterations; i++)
					{
				    	clp.read_file(i+1);
				   
				    	clp.pre_process_data();
				    	
				    	 //classifier_name = "J48-RF-SVM";
				    	 //ensemble_tech= "Majority Vote";
					     //clp.result = clp.pred2_info_gain_maj_vote(i, p_of_features);	
				    
					     //classifier_name = "J48-RF-SVM";
				    	//ensemble_tech= "Average Vote";
					    //clp.result = clp.pred2_info_gain_avg_vote(i, p_of_features);	
				    
				    	  //classifier_name = "J48-RF-SVM";
				    	  //ensemble_tech= "Max Vote";
					      //clp.result = clp.pred2_info_gain_max_vote(i, p_of_features);	
				    
				    	  // classifier_name = "J48-RF-SVM";
				    	   //ensemble_tech= "Stacking";
					     //  clp.result = clp.pred2_info_gain_stack(i, p_of_features);	
				   
					     
				    	  //classifier_name = "J48";
				    	  //ensemble_tech= "Bagging";
					      //clp.result = clp.pred2_info_gain_bagging(i, p_of_features, new J48());	
					      
					      classifier_name = "RF";
				    	  ensemble_tech= "Bagging";
					      clp.result = clp.pred2_info_gain_bagging(i, p_of_features, new RandomForest());	
					   
				    	
					    //  classifier_name = "SMO";
				    	 // ensemble_tech= "Bagging";
					     // clp.result = clp.pred2_info_gain_bagging(i, p_of_features, new SMO());	
					    
					      //classifier_name = "J48";
				    	  //ensemble_tech= "BoosTing";
					      //clp.result = clp.pred2_info_gain_boosting(i, p_of_features, new J48());	
					    
					      //classifier_name = "RF";
				    	  //ensemble_tech= "Boosting";
					      //clp.result = clp.pred2_info_gain_boosting(i, p_of_features, new RandomForest());	
					     
					      //classifier_name = "SMO";
				    	  //ensemble_tech= "Boosting";
					      //clp.result = clp.pred2_info_gain_boosting(i, p_of_features, new SMO());	
					      
					      System.out.println("Project="+ clp.source_project+ " Classifier name:"+ classifier_name+"  ensem tech:"+ ensemble_tech+" itr="+ clp.iterations);
						
					}
					    
				
				// define some temporary parameters
				double temp_thres= 0.1;
				double temp_precision[] =  new double[clp.iterations];
				double temp_recall[]    =  new double[clp.iterations];
				double temp_fmeasure[] 	=  new double[clp.iterations];
				double temp_accuracy[]	=  new double[clp.iterations];
				double temp_roc_auc[] 	=  new double[clp.iterations];
				
				long temp_train_time[] =  new long[10];
				long temp_test_time[]  = new long[10];
				
				for(int k=0; k<9; k++)
				{
					for(int l = 0; l<clp.iterations; l++)
					{
					  temp_precision[l]  = clp.precision[l][k];	
					  temp_recall[l]     = clp.recall[l][k];	
					  temp_fmeasure[l]   = clp.fmeasure[l][k];						
					  temp_accuracy[l]   = clp.accuracy[l][k];						
					  temp_roc_auc[l]    = clp.roc_auc[l][k];	
						
					  temp_train_time[l] = clp.train_time[l][k];
					  temp_test_time[l]  =  clp.test_time[l][k];
					  
					}// for
			      clp.compute_avg_stdev_and_insert(classifier_name, ensemble_tech, temp_thres, feature_selection_tech,  p_of_features, temp_precision, temp_recall, temp_accuracy, temp_fmeasure , temp_roc_auc, temp_train_time,temp_test_time );
			   
			      temp_thres  =  temp_thres +0.1;
			      
				}// for
			
			} //p of featuers
					
	}// main

	
}// class


