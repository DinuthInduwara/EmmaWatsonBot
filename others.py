from telegram.ext import *
from telegram import *


# Main Menu
Photos = "1.All Officialy Relesed Photos"
Interviews = "2.Emma Watson Interviews"
Tiktok_And_Others = "3.TikTok And Other Short Videos"
Movies = "4.Emma Watson Acted Movies"
Random_Photos_And_Videos = "5.Random HighQuality Photos And Videos"
Watch_And_Download_All = "6.Watch All And Download"




#Back

imgback = "🔙Back To Years List🔙"
backmain = "🔙🔙Back To Main Menu🔙🔙"


#Main Menu

firstbuttonset = [[KeyboardButton(Photos)], [KeyboardButton(Interviews)],[KeyboardButton(Tiktok_And_Others)],[KeyboardButton(Movies)],[KeyboardButton(Random_Photos_And_Videos)],[KeyboardButton(Watch_And_Download_All)]]



#URL Button

yearsbuttonph = [[KeyboardButton("🖼 2000 🖼")],[KeyboardButton("🖼 2002 🖼")],[KeyboardButton("🖼 2003 🖼")],[KeyboardButton("🖼 2004 🖼")],[KeyboardButton("🖼 2005 🖼")],[KeyboardButton("🖼 2006 🖼")],[KeyboardButton("🖼 2007 🖼")],[KeyboardButton("🖼 2008 🖼")],[KeyboardButton("🖼 2009 🖼")],[KeyboardButton("🖼 2010 🖼")],[KeyboardButton("🖼 2011 🖼")],[KeyboardButton("🖼 2012 🖼")],[KeyboardButton("🖼 2013 🖼")],[KeyboardButton("🖼 2014 🖼")],[KeyboardButton("🖼 2015 🖼")],[KeyboardButton("🖼 2016 🖼")],[KeyboardButton("🖼 2017 🖼")],[KeyboardButton("🖼 2018 🖼")],[KeyboardButton("🖼 2019 🖼")],[KeyboardButton("🖼 2020 🖼")],[KeyboardButton("🖼 2021 🖼")],[KeyboardButton(backmain)]]

#Years Keyboard button

දෙදස්දෙක  = [[KeyboardButton("2002 Octomber")], [KeyboardButton("2002 November")],[KeyboardButton("2002 july")],[KeyboardButton(imgback)]]
දෙදාස්තුන  = [[KeyboardButton("2003 April")], [KeyboardButton("2003 Spetember")],[KeyboardButton("2003 November")], [KeyboardButton("2003 December")],[KeyboardButton(imgback)]]
දෙදස්හතර  = [[KeyboardButton("2004 January")], [KeyboardButton("2004 May 1")], [KeyboardButton("2004 May 2")], [KeyboardButton("2004 May 3")], [KeyboardButton("2004 May 4")], [KeyboardButton("2004 May 5")], [KeyboardButton("2004 May 6")],[KeyboardButton("2004 September")], [KeyboardButton("2004 November")],[KeyboardButton(imgback)]]
dedaspaha   = [[KeyboardButton("2005 Feburary")], [KeyboardButton("2005 March")],[KeyboardButton("2005 July")],[KeyboardButton("2005 Octomber 1")], [KeyboardButton("2005 Octomber 2")], [KeyboardButton("2005 November 1")],[KeyboardButton("2005 November 2")],[KeyboardButton("2005 November 3")],[KeyboardButton("2005 November 4")],[KeyboardButton("2005 November 5")],[KeyboardButton(imgback)]]
දෙදාස්හය  = [[KeyboardButton("2006 March")], [KeyboardButton("2006 Juni")],[KeyboardButton("2006 September")],[KeyboardButton(imgback)]]
දෙදස්හත  = [[KeyboardButton("2007 July 1")], [KeyboardButton("2007 July 2")],[KeyboardButton("2007 July 3")],[KeyboardButton("2007 July 4")],[KeyboardButton("2007 July 5")],[KeyboardButton("2007 July 6")],[KeyboardButton("2007 July 7")],[KeyboardButton("2007 July 8")],[KeyboardButton("2007 September")],[KeyboardButton("2007 October")],[KeyboardButton("2007 November")],[KeyboardButton("2007 December")],[KeyboardButton(imgback)]]
දෙදසඇට  = [[KeyboardButton("2008 February")], [KeyboardButton("2008 March")],[KeyboardButton("2008 September 1")],[KeyboardButton("2008 September 2")],[KeyboardButton("2008 September 3")],[KeyboardButton("2008 September 4")],[KeyboardButton("2008 Octomber 1")],[KeyboardButton("2008 Octomber 2")],[KeyboardButton("2008 Octomber 3")],[KeyboardButton("2008 November")],[KeyboardButton("2008 December 1")],[KeyboardButton("2008 December 2")],[KeyboardButton(imgback)]]
දේදාස්නවය  = [[KeyboardButton("2009 Feb07")],[KeyboardButton("2009 Feb08")], [KeyboardButton("2009 Jul05")], [KeyboardButton("2009 Jul06")], [KeyboardButton("2009 Jul07")],[KeyboardButton("2009 Jul08 - 1")],[KeyboardButton("2009 Jul08 - 2")],[KeyboardButton("2009 Jul08 - 3")],[KeyboardButton("2009 Jun03")],[KeyboardButton("2009 Jul09 - 1")],[KeyboardButton("2009 Jul09 - 2")],[KeyboardButton("2009 Jul11 - 1")], [KeyboardButton("2009 Jul11 - 2")], [KeyboardButton("2009 Mar10")], [KeyboardButton("2009 Sep22")],[KeyboardButton(imgback)]]
දෙදස්දහය  = [[KeyboardButton("2010 Mar03")], [KeyboardButton("2010 May20")], [KeyboardButton("2010 Mar25")], [KeyboardButton("2010 May26")],[KeyboardButton("2010 Nov10")],[KeyboardButton("2010 Nov15 - 1")],[KeyboardButton("2010 Nov15 - 2")],[KeyboardButton("2010 Nov13")],[KeyboardButton("2010 Nov16")], [KeyboardButton(imgback)]]
දෙදස්දොළහ  = [[KeyboardButton("2012 April-14")], [KeyboardButton("2012 April-21")], [KeyboardButton("2012 Sep05")], [KeyboardButton("2012 Oct15")],[KeyboardButton("2012 Jun03")], [KeyboardButton("2012 Feb10-2")],[KeyboardButton("2012 Feb10-1")],[KeyboardButton("2012 May01")],[KeyboardButton("2012 Sep06")], [KeyboardButton("2012 Sep26")], [KeyboardButton("2012 Spe07")], [KeyboardButton("2012 Spe08")], [KeyboardButton("2012 Sep11")], [KeyboardButton("2012 Sep13-1")], [KeyboardButton("2012 Sep-2")], [KeyboardButton("2012 Sep17")], [KeyboardButton("2012 Sep30")], [KeyboardButton(imgback)]]
දෙදසේකොළහ = [[KeyboardButton("2011 Feb-11")],[KeyboardButton("2011 Feb-12")],[KeyboardButton("2011 Feb13-1")],[KeyboardButton("2011 Feb13-2")],[KeyboardButton("2011 Feb14")],[KeyboardButton("2011 Apr-28")],[KeyboardButton("2011 Jul06")],[KeyboardButton("2011 Jul07-1")],[KeyboardButton("2011 Jul07-2")],[KeyboardButton("2011 Jul07-3")],[KeyboardButton("2011 Jul11-1")],[KeyboardButton("2011 Jul11-2")],[KeyboardButton("2011 Jul1-3")],[KeyboardButton("2011 Jul-12")],[KeyboardButton("2011 Jun05-01 ")],[KeyboardButton("2011 Jun05-02")],[KeyboardButton("2011 Sep-06")],[KeyboardButton("2011 Nov-20")],[KeyboardButton("2011 Dec07-1")],[KeyboardButton("2011 Dec07-2")], [KeyboardButton(imgback)]]



















#________________________Inline Buttons_____________________
#________________________     2004     _____________________
INLINE_2004_May_1_Next      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2004_May_1_Next_CALLBACK')]]
INLINE_2004_May_4_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2004_May_4_1_Next_CALLBACK')]]
INLINE_2004_May_5_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2004_May_5_1_Next_CALLBACK')]]
INLINE_2004_May_5_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2004_May_5_2_Next_CALLBACK')]]
INLINE_2004_May_5_3         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2004_May_5_3_Next_CALLBACK')]]
INLINE_2004_September       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2004_September_CALLBACK')]]
#________________________     2005     _____________________
INLINE_2005_Feburary_1      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2005_Feburary_1_CALLBACK')]]
INLINE_2005_Feburary_2      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='INLINE_2005_Feburary_2_CALLBACK')]]
Inline_2005_March_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_March_1_CALLBACK')]]
Inline_2005_March_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_March_2_CALLBACK')]]
Inline_2005_November1_1     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November1_1_CALLBACK')]]
Inline_2005_November1_2     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November1_2_CALLBACK')]]
Inline_2005_November1_3     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November1_3_CALLBACK')]]
Inline_2005_November1_4     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November1_4_CALLBACK')]]
Inline_2005_November1_5     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November1_5_CALLBACK')]]
Inline_2005_November_3_1    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November_3_1_CALLBACK')]]
Inline_2005_November_3_2    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November_3_2_CALLBACK')]]
Inline_2005_November_3_3    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November_3_3_CALLBACK')]]
Inline_2005_November_4      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November_4_CALLBACK')]]
Inline_2005_November_5      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_November_5_CALLBACK')]]
Inline_2005_Octomber_2      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2005_Octomber_2_CALLBACK')]]
#________________________     2006     _____________________
Inline_2006_March_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2006_March_1_CALLBACK')]]
Inline_2006_March_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2006_March_2_CALLBACK')]]
Inline_2006_March_3         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2006_March_3_CALLBACK')]]
#________________________     2007     _____________________
Inline_2007_July_1_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_1_1_CALLBACK')]]
Inline_2007_July_1_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_1_2_CALLBACK')]]
Inline_2007_July_1_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_1_3_CALLBACK')]]
Inline_2007_July_1_4        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_1_4_CALLBACK')]]
Inline_2007_July_4_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_4_1_CALLBACK')]]
Inline_2007_July_4_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_4_2_CALLBACK')]]
Inline_2007_July_4_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_4_3_CALLBACK')]]
Inline_2007_July_4_4        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_4_4_CALLBACK')]]
Inline_2007_July_4_5        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_4_5_CALLBACK')]]
Inline_2007_July_4_6        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_4_6_CALLBACK')]]
Inline_2007_July_5_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_5_1_CALLBACK')]]
Inline_2007_July_5_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_5_2_CALLBACK')]]
Inline_2007_July_6_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_6_1_CALLBACK')]]
Inline_2007_July_6_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_6_2_CALLBACK')]]
Inline_2007_July_6_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_6_3_CALLBACK')]]
Inline_2007_July_7_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_7_1_CALLBACK')]]
Inline_2007_July_7_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_7_2_CALLBACK')]]
Inline_2007_July_7_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_7_3_CALLBACK')]]
Inline_2007_July_7_4        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_7_4_CALLBACK')]]
Inline_2007_July_8_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_8_1_CALLBACK')]]
Inline_2007_July_8_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_8_2_CALLBACK')]]
Inline_2007_July_8_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_8_3_CALLBACK')]]
Inline_2007_July_8_4        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_July_8_4_CALLBACK')]]
Inline_2007_September_1     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_September_1_CALLBACK')]]
Inline_2007_September_2     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_September_2_CALLBACK')]]
Inline_2007_October_1       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_October_1_CALLBACK')]]
Inline_2007_October_2       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_October_2_CALLBACK')]]
Inline_2007_December        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2007_December_CALLBACK')]]
#________________________     2008     _____________________
Inline_2008_September_1     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_September_1_CALLBACK')]]
Inline_2008_September_2     =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_September_2_CALLBACK')]]
Inline_2008_September3_1    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_September3_1_CALLBACK')]]
Inline_2008_September3_2    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_September3_2_CALLBACK')]]
Inline_2008_September4_1    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_September4_1_CALLBACK')]]
Inline_2008_September4_2    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_September4_2_CALLBACK')]]
Inline_2008_Octomber_2_1    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_Octomber_2_1_CALLBACK')]]
Inline_2008_Octomber_2_2    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_Octomber_2_2_CALLBACK')]]
Inline_2008_Octomber_3_1    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_Octomber_3_1_CALLBACK')]]
Inline_2008_February_1      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_February_1_CALLBACK')]]
Inline_2008_February_2      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_February_2_CALLBACK')]]
Inline_2008_March_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_March_1_CALLBACK')]]
Inline_2008_March_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_March_2_CALLBACK')]]
Inline_2008_March_3         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_March_3_CALLBACK')]]
Inline_2008_December_2_1    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_1_CALLBACK')]]
Inline_2008_December_2_2    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_2_CALLBACK')]]
Inline_2008_December_2_3    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_3_CALLBACK')]]
Inline_2008_December_2_4    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_4_CALLBACK')]]
Inline_2008_December_2_5    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_5_CALLBACK')]]
Inline_2008_December_2_6    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_6_CALLBACK')]]
Inline_2008_December_2_7    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_7_CALLBACK')]]
Inline_2008_December_2_8    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_8_CALLBACK')]]
Inline_2008_December_2_9    =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_9_CALLBACK')]]
Inline_2008_December_2_10   =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_December_2_10_CALLBACK')]]
Inline_2008_November        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2008_November_CALLBACK')]]
#________________________     2009     _____________________
Inline_2009_Feb08_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Feb08_1_CALLBACK')]]
Inline_2009_Feb08_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Feb08_2_CALLBACK')]]

Inline_2009_Jul07_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_1_CALLBACK')]]
Inline_2009_Jul07_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_2_CALLBACK')]]
Inline_2009_Jul07_3         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_3_CALLBACK')]]
Inline_2009_Jul07_4         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_4_CALLBACK')]]
Inline_2009_Jul07_5         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_5_CALLBACK')]]
Inline_2009_Jul07_6         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_6_CALLBACK')]]
Inline_2009_Jul07_7         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_7_CALLBACK')]]
Inline_2009_Jul07_8         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul07_8_CALLBACK')]]
Inline_2009_Jul08_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul08_2_CALLBACK')]]
Inline_2009_Jul08_3_1       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul08_3_1_CALLBACK')]]
Inline_2009_Jul08_3_2       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul08_3_2_CALLBACK')]]
Inline_2009_Jul08_3_3       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul08_3_3_CALLBACK')]]
Inline_2009_Jul08_3_4       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul08_3_4_CALLBACK')]]
Inline_2009_Jul08_3_5       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul08_3_5_CALLBACK')]]
Inline_2009_Jul09_1_1       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul09_1_1_CALLBACK')]]
Inline_2009_Jul09_1_2       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul09_1_2_CALLBACK')]]
Inline_2009_Jul09_1_3       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul09_1_3_CALLBACK')]]
Inline_2009_Jul09_1_4       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul09_1_4_CALLBACK')]]
Inline_2009_Jul09_1_5       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009_Jul09_1_5_CALLBACK')]]
Inline_2009Sep22            =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2009Sep22_CALLBACK')]]
#________________________     2010     _____________________
Inline_2010_Mar25           =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Mar25_CALLBACK')]]
Inline_2010_Mar03_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Mar03_1_CALLBACK')]]
Inline_2010_Mar03_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Mar03_2_CALLBACK')]]
Inline_2010_May26           =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_May26_CALLBACK')]]
Inline_2010_Nov10_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Nov10_1_CALLBACK')]]
Inline_2010_Nov10_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Nov10_2_CALLBACK')]]
Inline_2010_Nov10_3         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Nov10_3_CALLBACK')]]
Inline_2010_Nov13_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Nov13_1_CALLBACK')]]
Inline_2010_Nov15_2_1       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Nov15_2_1_CALLBACK')]]
Inline_2010_Nov15_2_2       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2010_Nov15_2_2_CALLBACK')]]
#________________________     2011     _____________________
Inline_2011_Feb13_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb13_1_CALLBACK')]]
Inline_2011_Feb13_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb13_2_CALLBACK')]]
Inline_2011_Feb14_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb14_1_CALLBACK')]]
Inline_2011_Feb14_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb14_2_CALLBACK')]]
Inline_2011_Feb14_3         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb14_3_CALLBACK')]]
Inline_2011_Feb14_4         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb14_4_CALLBACK')]]
Inline_2011_Feb14_5         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Feb14_5_CALLBACK')]]
Inline_2011_Jul06_1         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul06_1_CALLBACK')]]
Inline_2011_Jul06_2         =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul06_2_CALLBACK')]]
Inline_2011_Jul07_3_1       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_1_CALLBACK')]]
Inline_2011_Jul07_3_2       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_2_CALLBACK')]]
Inline_2011_Jul07_3_3       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_3_CALLBACK')]]
Inline_2011_Jul07_3_4       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_4_CALLBACK')]]
Inline_2011_Jul07_3_5       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_5_CALLBACK')]]
Inline_2011_Jul07_3_6       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_6_CALLBACK')]]
Inline_2011_Jul07_3_7       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_7_CALLBACK')]]
Inline_2011_Jul07_3_8       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_8_CALLBACK')]]
Inline_2011_Jul07_3_9       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_9_CALLBACK')]]
Inline_2011_Jul07_3_10      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_10_CALLBACK')]]
Inline_2011_Jul07_3_11      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul07_3_11_CALLBACK')]]
Inline_2011_Jul11_1_1       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_1_CALLBACK')]]
Inline_2011_Jul11_1_2       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_2_CALLBACK')]]
Inline_2011_Jul11_1_3       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_3_CALLBACK')]]
Inline_2011_Jul11_1_4       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_4_CALLBACK')]]
Inline_2011_Jul11_1_5       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_5_CALLBACK')]]
Inline_2011_Jul11_1_6       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_6_CALLBACK')]]
Inline_2011_Jul11_1_7       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_7_CALLBACK')]]
Inline_2011_Jul11_1_8       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_8_CALLBACK')]]
Inline_2011_Jul11_1_9       =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul11_1_9_CALLBACK')]]
Inline_2011_Jul1_3_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul1_3_1_CALLBACK')]]
Inline_2011_Jul1_3_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jul1_3_2_CALLBACK')]]
Inline_2011_Jun05_01_1      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jun05_01_1_CALLBACK')]]
Inline_2011_Jun05_01_2      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jun05_01_2_CALLBACK')]]
Inline_2011_Jun05_01_3      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jun05_01_3_CALLBACK')]]
Inline_2011_Jun05_01_4      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jun05_01_4_CALLBACK')]]
Inline_2011_Jun05_01_5      =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Jun05_01_5_CALLBACK')]]
Inline_2011_Sep_06_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Sep_06_1_CALLBACK')]]
Inline_2011_Sep_06_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Sep_06_2_CALLBACK')]]
Inline_2011_Sep_06_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Sep_06_3_CALLBACK')]]
Inline_2011_Nov_20_1        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Nov_20_1_CALLBACK')]]
Inline_2011_Nov_20_2        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Nov_20_2_CALLBACK')]]
Inline_2011_Nov_20_3        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Nov_20_3_CALLBACK')]]
Inline_2011_Nov_20_4        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Nov_20_4_CALLBACK')]]
Inline_2011_Nov_20_5        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='Inline_2011_Nov_20_5_CALLBACK')]]

#        =   [[InlineKeyboardButton(text= 'Next Page', callback_data='_CALLBACK')]]









හයකටකලින්එක = "Emma Watson launches  next phase of the HeForShe at World Economic Forum in Davos" #https://www.youtube.com/watch?v=0IS-9tI7-2o
හයකටකලින්දෙක = "Emma Watson Facebook Q&A about HeForShe - International Women's Day 2015"  #https://www.youtube.com/watch?v=n4xzvDzP-lA
හයකටකලින්තුන = "Regression Official Featurette #1 Emma Watson, Alejandro Amenábar"   #https://www.youtube.com/watch?v=s5LqlhRbQV4
පහකටකලින්එක = "Emma Watson interviews Malala Yousafzai Nobel Peace Prize"  #https://www.youtube.com/watch?v=NKckKStggSY
පහකටකලින්දෙක = "Emma Watson Backstage Vogue Italia 2015"  #https://www.youtube.com/watch?v=7AzSpttmlfI
පහකටකලින්තුන = "Emma Watson Introduces the new HeForShe"  #https://www.youtube.com/watch?v=u6iJN8OovWg
පහකටකලින්හතර = "Emma Watson interview in Scoop With Raya"  #https://www.youtube.com/watch?v=LKerYFqqmpM&t=7s
පහකටකලින්පහ = "Emma Watson interviews Lin-Manuel Miranda for HeForShe Arts Week"  #https://www.youtube.com/watch?v=-NbEbkVrVWY
පහකටකලින්හය = "Emma Watson - HITRECORD, Technology is like a Superpower"   #https://www.youtube.com/watch?v=1jxAsYdxhqw
පහකටකලින්හත = "Emma Watson interview for Colonia"  #https://www.youtube.com/watch?v=OBywDqT5PeY
පහකටකලින්අට =  "Emma Watson dons dress made of this (Met Gala 2016)"  #https://www.youtube.com/watch?v=t2j4hsQdMs0
පහකටකලින්නවය = "Emma Watson interview: Gripping new drama, media scrutiny and playing Belle"  #https://www.youtube.com/watch?v=TH0WGanHJf8&t=5s
පහකටකලින්දහය = "Emma Watson & Caitlin Moran - In Conversation for Our Shared Shelf" #https://www.youtube.com/watch?v=CynzW9Kz7Ds
පහකටකලින්එකොළහ = "Emma Watson - One Young World 2016"  #https://www.youtube.com/watch?v=elbqER_ZrLQ
පහකටකලින්දොළහ = "Emma Watson speech for HeForShe Second Year Anniversary"   #https://www.youtube.com/watch?v=mEjUcd33bCc
පහකටකලින්දහතුන = "Emma Watson speech at United Nations - HeForShe IMPACT 10x10x10 University Parity Report"  #https://www.youtube.com/watch?v=_vzb7Io7oQ0
පහකටකලින්දාහතර = "Emma Watson - Harper's Bazaar Women of the Year Awards 2016" #https://www.youtube.com/watch?v=XOKrdlZyF1Q
පහකටකලින්පහළොව = "Emma Watson - Harpers Bazaar Women of the Year Awards 2016 speech"  #https://www.youtube.com/watch?v=mzPMIHAfUcw
හතරකටකලින්එක = "Beauty and the Beast cast live chat on Facebook" #https://www.youtube.com/watch?v=TtlDoajvUvc
හතරකටකලින්දෙක = "Emma Watson answers questions from kids | Entertainment Weekly" #https://www.youtube.com/watch?v=YxPD6R-OlQI
හතරකටකලින්තුන් =  "Beauty and the Beast cast at Paris premiere"  #https://www.youtube.com/watch?v=ZAZqFgJ_tlw
හතරකටකලින්හතර = "Beauty and the Beast: press conference with cast in Paris" #https://www.youtube.com/watch?v=bfcka4GQsUw
හතරකටකලින්පහ = "Beauty and the Beast - Behind the scenes with Emma Watson" #https://www.youtube.com/watch?v=g9J1bRRxD_Q
හතරකටකලින්හය = "Beauty and the Beast - Emma Watson Interview #1" #https://www.youtube.com/watch?v=POvGKnq1d60
හතරකටකලින්හත = "Emma Watson at Los Angeles premiere of Beauty and the Beast" #https://www.youtube.com/watch?v=Exid3xOUzsY
හතරකටකලින්අට = "Beauty and the Beast cast live Q&A on Facebook" #https://www.youtube.com/watch?v=4h_YllMlUkc
හතරකටකලින්නවය = "Beauty and the Beast - Emma Watson Interview #2" #https://www.youtube.com/watch?v=MrBftDdA_aU
හතරකටකලින්දහය = "Emma Watson live chat for EW on facebook"  #https://www.youtube.com/watch?v=dSMr0JN0w1A
හතරකටකලින්එකොළහ = "Emma Watson and Dan Stevens dish on work and life | USA TODAY" #https://www.youtube.com/watch?v=bU7IzNB4LBQ
හතරකටකලින්දොළහ ="The Circle - Emma Watson interview #1" #https://www.youtube.com/watch?v=YlOPNGnPPS4
හතරකටකලින්දහතුන = "The Circle cast live chat on Twitter" #https://www.youtube.com/watch?v=4NISy3EFbNY
හතරකටකලින්දාහතර = "Emma Watson live on facecbook for TF1" #https://www.youtube.com/watch?v=jhfP7VHMo6I
තුනකටකලින්එක = "Emma Watson about anti-bullying and harassment" #https://www.youtube.com/watch?v=W4mlXlBH53Q
තුනකටකලින්දෙක = "Emma Watson Interviews Rupi Kaur for Our Shared Shelf" #https://www.youtube.com/watch?v=mkw1S1eqNBI
තුනකටකලින්තුන = "Emma Watson Interviews Reni Eddo Lodge" #https://www.youtube.com/watch?v=AwWCZl_OUsY
තුනකටකලින්හතර =  "Emma Watson In Conversation with Dr Denis Mukwege Nobel Peace Price" #https://www.youtube.com/watch?v=o2MkmSCYs0I
තුනකටකලින්පහ = "Emma Watson - In The Bag | British Vogue" #https://www.youtube.com/watch?v=NX2EYRAlYHw
තුනකටකලින්හය = "Emma Watson Interviews Author Rebecca Solnit" #https://www.youtube.com/watch?v=qdNHZDq7XHQ
තුනකටකලින්හත = "Emma Watson in Coversation with Steve Chbosky" #https://www.youtube.com/watch?v=dYDZWUmUdxI





harry = "Harry Potter"
beautyandthebeast = "Beauty And The Beast"
MyWeekwithMarilyn = "My Week with Marilyn"
TheBlingRing = "The Bling Ring"
ThisIstheEnd = "This Is the End"
Noah = "Noah"
Colonia = "Colonia"
Regression = "Regression"
TheCircle = "The Circle"
LittleWomen = "Little Women" 
harry1 = "/_Philosophers_Stone"
harry2 = "Harry Potter and the Chamber of Secrets"
harry3 = "Harry Potter and the Prisoner of Azkaban"
harry4 = "Harry Potter and the Goblet of Fire"
harry5 = "Harry Potter and the Order of the Phoenix"
harry6 = "Harry Potter and the Half-Blood Prince"
harry7 = "Harry Potter and the Deathly Hallows – Part 1"
harry8 = "Harry Potter and the Deathly Hallows – Part 2"










    




