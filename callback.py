from telegram.ext import *
from telegram import *
from telegram.ext import callbackcontext
from others import *
from url_img_callback import *
from callback import *
from Other_imgs import *






#def queryHandler(update: Update, context: CallbackContext):
 #   query = update.callback_query.data
 #   update.callback_query.answer()

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

    if "INLINE_2004_May_1_Next_CALLBACK" in query:
        INLINE_2004_May_1_Next_command(update, context)
 
    if "INLINE_2004_May_4_1_Next_CALLBACK" in query:
        INLINE_2004_May_4_1_Next_command(update, context)
        
    if "INLINE_2004_May_5_1_Next_CALLBACK" in query:
        INLINE_2004_May_5_1_Next_command(update, context)

    if "INLINE_2004_May_5_2_Next_CALLBACK" in query:
        INLINE_2004_May_5_2_Next_command(update, context)


    if "INLINE_2004_May_5_3_Next_CALLBACK" in query:
        INLINE_2004_May_5_3_Next_command(update, context)

        
    if "INLINE_2004_September_CALLBACK" in query:
        INLINE_2004_September_command(update, context)

#_________________________2005_______________________
    if "INLINE_2005_Feburary_1_CALLBACK" in query:
        INLINE_2005_Feburary_1_command(update, context)


    if "INLINE_2005_Feburary_2_CALLBACK" in query:
        INLINE_2005_Feburary_2_command(update, context)

        
    if "Inline_2005_March_1_CALLBACK" in query:
        Inline_2005_March_1_command(update, context)

        
    if "Inline_2005_March_2_CALLBACK" in query:
        Inline_2005_March_2_command(update, context)

    
    if "Inline_2005_November1_1_CALLBACK" in query:
        Inline_2005_November1_1_command(update, context)
        
    
    if "Inline_2005_November1_2_CALLBACK" in query:
        Inline_2005_November1_2_command(update, context)
        
    
    if "Inline_2005_November1_3_CALLBACK" in query:
        Inline_2005_November1_3_command(update, context)
        
    
    if "Inline_2005_November1_4_CALLBACK" in query:
        Inline_2005_November1_4_command(update, context)
        
    
    if "Inline_2005_November1_5_CALLBACK" in query:
        Inline_2005_November1_5_command(update, context)

    
    if "Inline_2005_November_3_1_CALLBACK" in query:
        Inline_2005_November_3_1_command(update, context)


            
    if "Inline_2005_November_3_2_CALLBACK" in query:
        Inline_2005_November_3_2_command(update, context)


            
    if "Inline_2005_November_3_3_CALLBACK" in query:
        Inline_2005_November_3_3_command(update, context)

        

                
    if "Inline_2005_November_4_CALLBACK" in query:
        Inline_2005_November_4_command(update, context)    


    if "Inline_2005_November_5_CALLBACK" in query:
        Inline_2005_November_5_command(update, context)    

    
    if "Inline_2005_Octomber_2_CALLBACK" in query:
        Inline_2005_Octomber_2_command(update, context)  


            
    if "Inline_2006_March_1_CALLBACK" in query:
        Inline_2006_March_1_command(update, context)  

            
    if "Inline_2006_March_2_CALLBACK" in query:
        Inline_2006_March_2_command(update, context)  

            
    if "Inline_2006_March_3_CALLBACK" in query:
        Inline_2006_March_3_command(update, context)  

                    
    if "Inline_2007_July_1_1_CALLBACK" in query:
        Inline_2007_July_1_1_command(update, context)  

                            
    if "Inline_2007_July_1_2_CALLBACK" in query:
        Inline_2007_July_1_2_command(update, context)  


                            
    if "Inline_2007_July_1_3_CALLBACK" in query:
        Inline_2007_July_1_3_command(update, context)  

                            
    if "Inline_2007_July_1_4_CALLBACK" in query:
        Inline_2007_July_1_4_command(update, context)  

        
                            
    if "Inline_2007_July_4_1_CALLBACK" in query:
        Inline_2007_July_4_1_command(update, context) 

                                    
    if "Inline_2007_July_4_2_CALLBACK" in query:
        Inline_2007_July_4_2_command(update, context)  

                                    
    if "Inline_2007_July_4_3_CALLBACK" in query:
        Inline_2007_July_4_3_command(update, context)   

                                    
    if "Inline_2007_July_4_4_CALLBACK" in query:
        Inline_2007_July_4_4_command(update, context)  

                                    
    if "Inline_2007_July_4_5_CALLBACK" in query:
        Inline_2007_July_4_5_command(update, context)  

                                    
    if "Inline_2007_July_4_6_CALLBACK" in query:
        Inline_2007_July_4_6_command(update, context)  

    if "Inline_2007_July_5_1_CALLBACK" in query:
        Inline_2007_July_5_1_command(update, context)  


    if "Inline_2007_July_5_2_CALLBACK" in query:
        Inline_2007_July_5_2_command(update, context) 

        
    if "Inline_2007_July_6_1_CALLBACK" in query:
        Inline_2007_July_6_1_command(update, context)   

        
    
    if "Inline_2007_July_6_2_CALLBACK" in query:
        Inline_2007_July_6_2_command(update, context)   
        
        
    if "Inline_2007_July_6_3_CALLBACK" in query:
        Inline_2007_July_6_3_command(update, context)   


    if "Inline_2007_July_7_1_CALLBACK" in query:
        Inline_2007_July_7_1_command(update, context)   

        
    if "Inline_2007_July_7_2_CALLBACK" in query:
        Inline_2007_July_7_2_command(update, context)   

        
    if "Inline_2007_July_7_3_CALLBACK" in query:
        Inline_2007_July_7_3_command(update, context)   

        
    if "Inline_2007_July_7_4_CALLBACK" in query:
        Inline_2007_July_7_4_command(update, context)   


    if "Inline_2007_July_8_1_CALLBACK" in query:
        Inline_2007_July_8_1_command(update, context)  

        
    if "Inline_2007_July_8_2_CALLBACK" in query:
        Inline_2007_July_8_2_command(update, context)  

        
    if "Inline_2007_July_8_3_CALLBACK" in query:
        Inline_2007_July_8_3_command(update, context)  

        
    if "Inline_2007_July_8_4_CALLBACK" in query:
        Inline_2007_July_8_4_command(update, context)  

                
    if "Inline_2007_September_1_CALLBACK" in query:
        Inline_2007_September_1_command(update, context) 

                
    if "Inline_2007_September_2_CALLBACK" in query:
        Inline_2007_September_2_command(update, context) 
        
                
    if "Inline_2007_October_1_CALLBACK" in query:
        Inline_2007_October_1_command(update, context) 
        
                
    if "Inline_2007_October_2_CALLBACK" in query:
        Inline_2007_October_2_command(update, context) 

                        
    if "Inline_2007_December_CALLBACK" in query:
        Inline_2007_December_command(update, context) 
        
                        
    if "Inline_2008_September_1_CALLBACK" in query:
        Inline_2008_September_1_command(update, context) 
                
                        
    if "Inline_2008_September_2_CALLBACK" in query:
        Inline_2008_September_2_command(update, context) 

                                
    if "Inline_2008_September3_1_CALLBACK" in query:
        Inline_2008_September3_1_command(update, context) 

                                
    if "Inline_2008_September3_2_CALLBACK" in query:
        Inline_2008_September3_2_command(update, context) 
        
                                
    if "Inline_2008_September4_1_CALLBACK" in query:
        Inline_2008_September4_1_command(update, context)

                
                                
    if "Inline_2008_September4_2_CALLBACK" in query:
        Inline_2008_September4_2_command(update, context)

                        
                                
    if "Inline_2008_Octomber_2_1_CALLBACK" in query:
        Inline_2008_Octomber_2_1_command(update, context)

                        
                                
    if "Inline_2008_Octomber_2_2_CALLBACK" in query:
        Inline_2008_Octomber_2_2_command(update, context)

                        
                                
    if "Inline_2008_Octomber_3_1_CALLBACK" in query:
        Inline_2008_Octomber_3_1_command(update, context)     

                                
                                
    if "Inline_2008_February_1_CALLBACK" in query:
        Inline_2008_February_1_command(update, context)    

                                
                                
    if "Inline_2008_February_2_CALLBACK" in query:
        Inline_2008_February_2_command(update, context) 
                                        
                                
    if "Inline_2008_March_1_CALLBACK" in query:
        Inline_2008_March_1_command(update, context) 
                                        
                                
    if "Inline_2008_March_2_CALLBACK" in query:
        Inline_2008_March_2_command(update, context) 
                                        
                                
    if "Inline_2008_March_3_CALLBACK" in query:
        Inline_2008_March_3_command(update, context) 

                                                        
    if "Inline_2008_December_2_1_CALLBACK" in query:
        Inline_2008_December_2_1_command(update, context) 
        
                                                        
    if "Inline_2008_December_2_2_CALLBACK" in query:
        Inline_2008_December_2_2_command(update, context) 

                                                                
    if "Inline_2008_December_2_3_CALLBACK" in query:
        Inline_2008_December_2_3_command(update, context) 

                                                                
    if "Inline_2008_December_2_4_CALLBACK" in query:
        Inline_2008_December_2_4_command(update, context) 

                                                                
    if "Inline_2008_December_2_5_CALLBACK" in query:
        Inline_2008_December_2_5_command(update, context) 

                                                                
    if "Inline_2008_December_2_6_CALLBACK" in query:
        Inline_2008_December_2_6_command(update, context) 

                                                                
    if "Inline_2008_December_2_7_CALLBACK" in query:
        Inline_2008_December_2_7_command(update, context) 

                                                                
    if "Inline_2008_December_2_8_CALLBACK" in query:
        Inline_2008_December_2_8_command(update, context) 

                                                                
    if "Inline_2008_December_2_9_CALLBACK" in query:
        Inline_2008_December_2_9_command(update, context) 

                                                                
    if "Inline_2008_December_2_10_CALLBACK" in query:
        Inline_2008_December_2_10_command(update, context) 

                                                                        
    if "Inline_2008_November_CALLBACK" in query:
        Inline_2008_November_command(update, context)

        

    if "Inline_2009_Feb08_1_CALLBACK" in query:
        Inline_2009_Feb08_1_command(update, context) 

        

    if "Inline_2009_Feb08_2_CALLBACK" in query:
        Inline_2009_Feb08_2_command(update, context)  
        

    if "Inline_2009_Jul07_1_CALLBACK" in query:
        Inline_2009_Jul07_1_command(update, context) 


    if "Inline_2009_Jul07_2_CALLBACK" in query:
        Inline_2009_Jul07_2_command(update, context) 
        

    if "Inline_2009_Jul07_3_CALLBACK" in query:
        Inline_2009_Jul07_3_command(update, context) 
        

    if "Inline_2009_Jul07_4_CALLBACK" in query:
        Inline_2009_Jul07_4_command(update, context) 
        

    if "Inline_2009_Jul07_5_CALLBACK" in query:
        Inline_2009_Jul07_5_command(update, context) 
        

    if "Inline_2009_Jul07_6_CALLBACK" in query:
        Inline_2009_Jul07_6_command(update, context) 
        

    if "Inline_2009_Jul07_7_CALLBACK" in query:
        Inline_2009_Jul07_7_command(update, context) 
    

    if "Inline_2009_Jul07_8_CALLBACK" in query:
        Inline_2009_Jul07_8_command(update, context) 
        

    if "Inline_2009_Jul08_2_CALLBACK" in query:
        Inline_2009_Jul08_2_command(update, context) 
        


    if "Inline_2009_Jul08_3_1_CALLBACK" in query:
        Inline_2009_Jul08_3_1_command(update, context) 



    if "Inline_2009_Jul08_3_2_CALLBACK" in query:
        Inline_2009_Jul08_3_2_command(update, context) 



    if "Inline_2009_Jul08_3_3_CALLBACK" in query:
        Inline_2009_Jul08_3_3_command(update, context) 



    if "Inline_2009_Jul08_3_4_CALLBACK" in query:
        Inline_2009_Jul08_3_4_command(update, context) 



    if "Inline_2009_Jul08_3_5_CALLBACK" in query:
        Inline_2009_Jul08_3_5_command(update, context) 




    if "Inline_2009_Jul09_1_1_CALLBACK" in query:
        Inline_2009_Jul09_1_1_command(update, context) 
        



    if "Inline_2009_Jul09_1_2_CALLBACK" in query:
        Inline_2009_Jul09_1_2_command(update, context) 
                



    if "Inline_2009_Jul09_1_3_CALLBACK" in query:
        Inline_2009_Jul09_1_3_command(update, context)         



    if "Inline_2009_Jul09_1_4_CALLBACK" in query:
        Inline_2009_Jul09_1_4_command(update, context)         



    if "Inline_2009_Jul09_1_5_CALLBACK" in query:
        Inline_2009_Jul09_1_5_command(update, context) 
        

   
    if "Inline_2009Sep22_CALLBACK" in query:
        Inline_2009Sep22_command(update, context) 



    if "Inline_2010_Mar25_CALLBACK" in query:
        Inline_2010_Mar25_command(update, context) 
       



    if "Inline_2010_Mar03_1_CALLBACK" in query:
        Inline_2010_Mar03_1_command(update, context) 

        

    if "Inline_2010_Mar03_2_CALLBACK" in query:
        Inline_2010_Mar03_2_command(update, context) 



    if "Inline_2010_May26_CALLBACK" in query:
        Inline_2010_May26_command(update, context) 




    if "Inline_2010_Nov10_1_CALLBACK" in query:
        Inline_2010_Nov10_1_command(update, context) 
        



    if "Inline_2010_Nov10_2_CALLBACK" in query:
        Inline_2010_Nov10_2_command(update, context) 
        



    if "Inline_2010_Nov10_3_CALLBACK" in query:
        Inline_2010_Nov10_3_command(update, context) 

        

        

    if "Inline_2010_Nov13_1_CALLBACK" in query:
        Inline_2010_Nov13_1_command(update, context) 


        

    if "Inline_2010_Nov15_2_1_CALLBACK" in query:
        Inline_2010_Nov15_2_1_command(update, context) 
       
       


    if "Inline_2010_Nov15_2_2_CALLBACK" in query:
        Inline_2010_Nov15_2_2_command(update, context) 
       
       

    if "Inline_2011_Feb13_1_CALLBACK" in query:
        Inline_2011_Feb13_1_command(update, context) 

        

    if "Inline_2011_Feb13_2_CALLBACK" in query:
        Inline_2011_Feb13_2_command(update, context) 


    if "Inline_2011_Feb14_1_CALLBACK" in query:
        Inline_2011_Feb14_1_command(update, context) 
       


    if "Inline_2011_Feb14_2_CALLBACK" in query:
        Inline_2011_Feb14_2_command(update, context) 
       

       

    if "Inline_2011_Feb14_3_CALLBACK" in query:
        Inline_2011_Feb14_3_command(update, context) 
       

       

    if "Inline_2011_Feb14_4_CALLBACK" in query:
        Inline_2011_Feb14_4_command(update, context) 
       

       

    if "Inline_2011_Feb14_5_CALLBACK" in query:
        Inline_2011_Feb14_5_command(update, context) 
       

       
       
    if "Inline_2011_Jul06_1_CALLBACK" in query:
        Inline_2011_Jul06_1_command(update, context) 




              
    if "Inline_2011_Jul06_2_CALLBACK" in query:
        Inline_2011_Jul06_2_command(update, context) 
       


    if "Inline_2011_Jul07_3_1_CALLBACK" in query:
        Inline_2011_Jul07_3_1_command(update, context) 
       

    if "Inline_2011_Jul07_3_2_CALLBACK" in query:
        Inline_2011_Jul07_3_2_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_3_CALLBACK" in query:
        Inline_2011_Jul07_3_3_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_4_CALLBACK" in query:
        Inline_2011_Jul07_3_4_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_5_CALLBACK" in query:
        Inline_2011_Jul07_3_5_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_6_CALLBACK" in query:
        Inline_2011_Jul07_3_6_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_7_CALLBACK" in query:
        Inline_2011_Jul07_3_7_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_8_CALLBACK" in query:
        Inline_2011_Jul07_3_8_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_9_CALLBACK" in query:
        Inline_2011_Jul07_3_9_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_10_CALLBACK" in query:
        Inline_2011_Jul07_3_10_command(update, context) 
       
       


    if "Inline_2011_Jul07_3_11_CALLBACK" in query:
        Inline_2011_Jul07_3_11_command(update, context) 
       
       

       

    if "Inline_2011_Jul11_1_1_CALLBACK" in query:
        Inline_2011_Jul11_1_1_command(update, context) 
       
       
       

    if "Inline_2011_Jul11_1_2_CALLBACK" in query:
        Inline_2011_Jul11_1_2_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_3_CALLBACK" in query:
        Inline_2011_Jul11_1_3_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_4_CALLBACK" in query:
        Inline_2011_Jul11_1_4_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_5_CALLBACK" in query:
        Inline_2011_Jul11_1_5_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_6_CALLBACK" in query:
        Inline_2011_Jul11_1_6_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_7_CALLBACK" in query:
        Inline_2011_Jul11_1_7_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_8_CALLBACK" in query:
        Inline_2011_Jul11_1_8_command(update, context) 
       
       


       

    if "Inline_2011_Jul11_1_9_CALLBACK" in query:
        Inline_2011_Jul11_1_9_command(update, context) 
       
       

    if "Inline_2011_Jul1_3_1_CALLBACK" in query:
        Inline_2011_Jul1_3_1_command(update, context) 
       
       
    if "Inline_2011_Jul1_3_2_CALLBACK" in query:
        Inline_2011_Jul1_3_2_command(update, context) 
       
       


    if "Inline_2011_Jun05_01_1_CALLBACK" in query:
        Inline_2011_Jun05_01_1_command(update, context) 
       
       

    if "Inline_2011_Jun05_01_2_CALLBACK" in query:
        Inline_2011_Jun05_01_2_command(update, context) 
       
       


    if "Inline_2011_Jun05_01_3_CALLBACK" in query:
        Inline_2011_Jun05_01_3_command(update, context) 
       
       


    if "Inline_2011_Jun05_01_4_CALLBACK" in query:
        Inline_2011_Jun05_01_4_command(update, context) 
       
       


    if "Inline_2011_Jun05_01_5_CALLBACK" in query:
        Inline_2011_Jun05_01_5_command(update, context) 
       
       

    if "Inline_2011_Sep_06_1_CALLBACK" in query:
        Inline_2011_Sep_06_1_command(update, context) 
       
              

    if "Inline_2011_Sep_06_2_CALLBACK" in query:
        Inline_2011_Sep_06_2_command(update, context) 
       
       
       

       

    if "Inline_2011_Sep_06_3_CALLBACK" in query:
        Inline_2011_Sep_06_3_command(update, context) 
       
       
       

       

    if "Inline_2011_Sep_06_4_CALLBACK" in query:
        Inline_2011_Sep_06_4_command(update, context) 
       
       
       


    if "Inline_2011_Nov_20_1_CALLBACK" in query:
        Inline_2011_Nov_20_1_command(update, context) 
       
       

    if "Inline_2011_Nov_20_2_CALLBACK" in query:
        Inline_2011_Nov_20_2_command(update, context) 
       
       
       


    if "Inline_2011_Nov_20_3_CALLBACK" in query:
        Inline_2011_Nov_20_3_command(update, context) 
       
       
       


    if "Inline_2011_Nov_20_4_CALLBACK" in query:
        Inline_2011_Nov_20_4_command(update, context) 
       
       
       


    if "Inline_2011_Nov_20_5_CALLBACK" in query:
        Inline_2011_Nov_20_5_command(update, context) 
       
       
       

       

       




'''   


    if "" in query:
        (update, context) 
       
       
       
        '''
       








