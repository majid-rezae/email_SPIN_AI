import smtplib, ssl
import sys
 
 
 
from Extensions.TKDataAccess import TKDataAccess

dataAccess = TKDataAccess()
connectionStatus = dataAccess.Connect("127.0.0.1:3101", "guest", "")
yy=str(dataAccess.GetObjectValue("Tag.taglist.name1"))

 
if yy  != '8cf9574000000012':
    message = """\
    ALERT SENSOR SPIN

    
    Dear Team,

    The Sensor ID: {0} does not working. please make a contact with Spin hardware team.
    
    Regards,
    Spin Team
    """.format(yy)
elif yy  == '8cf9574000000012':
    message = """\
    ALERT SENSOR SPIN

    
    Dear Team,

    The Sensor ID: {0} is working. OK.
    
    Regards,
    Spin Team
    """.format(yy)

dataAccess.SetObjectValue("Tag.taglistout.nameou1", message);