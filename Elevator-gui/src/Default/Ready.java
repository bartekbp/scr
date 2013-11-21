/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: Ready
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/Ready.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/Ready.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event Ready(int) 
public class Ready extends RiJEvent {
    
    public static final int Ready_Default_id = 18623;		//## ignore 
    
    public int level;
    
    // Constructors
    
    public  Ready(int p_level) {
        lId = Ready_Default_id;
        level = p_level;
    }
    
    public boolean isTypeOf(long id) {
        return (Ready_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/Ready.java
*********************************************************************/

