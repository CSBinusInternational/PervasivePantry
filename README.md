# PervasivePantry
PROJECT DESCRIPTIONS
The  idea  behind  the  project  is  to  create a smart  pantry  that  could notify the  owner  if  their  egg  or 
ingredient  is  running  out  via  email.  At  first  we  choose  a  moving  sensor  that  would  act  as  a  trigger  that 
keeping  track  of  the  ingredient  place  under  the  tray  and  connect  to  the  raspberry  pi. Unfortunately,because we don't have any necessary tools and skill to assemble the prototype. Our  teacher recommends another  component  that  could  use  as  the  trigger.  We  come  out  an  idea  to  use Gyroscope  application  that  available  in  Android  application  (Wireless  IMU). According  to  the  official website of the Wireless IMU, this app sends the measurements from your phone inertial sensors via UDP 
as CSV (Comma-Separated Values) to a computer in your network.

COMPONENTS REQUIRED (INCLUDE THE QUANTITY OF EACH COMPONENT)
The components required for this project are as follows
• Raspberry Pi 3 model B
• Wireless IMU adaptor in Android
• A handmade scale 
• Basket 

HOW DOES IT WORK?
The Raspberry Pi will open UDP server simultaneously and continuously along with the IMU adapter that will  send  UDP  packet  containing  Gyroscope  data.  It  is  worth  to  mention  that  the  Wireless  IMU  adapter also sending Accelerometer and Magnetometer data along with the Gyroscope data so we need to cut the other  two  data  and  only  take  the  Gyroscope  data.  We  put  the  Gyroscope  at  the  end  of  the  scale  and  the basket the other end. At this state Gyroscope will contain only zero value because it doesn’t move due the stable weight. If we take some ingredient,for example egg from the basket,it will 
change the latitude of the Gyroscope position because the weight is not in a stable position. Now at this state the X, Y, Z
-axis will change, the author warned the user of the code to pay attention of the cellphone position if the initial position  of  the  cell  phone  (Wireless  IMU)  is  flat  with  back  of  the  phone  touch  the  ground  the  reader should only care about the y value of the data that have been received. we create a Python code inside the UDP  server  if  the  data  from  the  IMU  adapter  is  change  to  certain limit.  In  this  scenario  we  put  0.10 latitude  to  act  as  the  limitation  if  the  data  supposed  to  go  beyond  the  limitation  the  Raspberry  Pi  will create  an  email  notification  using  SMTP  Library  from  Python library  and  after  user  receive  the  email notification they can see the warning if the ingredient is running low.

CIRCUIT DIAGRAM
Overall in the part of assembly is fast and easy as long the base of the 3D print is solid and can handle weight  and  another  problem  that  could  arise  when  try  to  attach  the  Gyroscope  (smartphone)  to  the  end and make it hang vertically. In the end we try to use a book clip as an attachment of the Gyroscope and the stick and turns out the it could handle the Gyroscope but because the book clip is not long enough we put a box as a stool to close the gap between the Gyroscope and the stick.


