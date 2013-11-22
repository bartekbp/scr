/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: MoveControllerE
//!	Generated Date	: Fri, 22, Nov 2013 
	File Path	: exe/DefaultConfig/Default/MoveControllerE.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/MoveControllerE.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event MoveControllerE(int) 
public class MoveControllerE extends RiJEvent {
    
    public static final int MoveControllerE_Default_id = 18642;		//## ignore 
    
    public int level;
    
    // Constructors
    
    public  MoveControllerE(int p_level) {
        lId = MoveControllerE_Default_id;
        level = p_level;
    }
    
    public boolean isTypeOf(long id) {
        return (MoveControllerE_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/MoveControllerE.java
*********************************************************************/

