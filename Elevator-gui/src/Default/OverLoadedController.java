/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: OverLoadedController
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/OverLoadedController.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/OverLoadedController.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event OverLoadedController(int,boolean) 
public class OverLoadedController extends RiJEvent {
    
    public static final int OverLoadedController_Default_id = 18628;		//## ignore 
    
    public int level;
    public boolean isOverloaded;
    
    // Constructors
    
    public  OverLoadedController(int p_level, boolean p_isOverloaded) {
        lId = OverLoadedController_Default_id;
        level = p_level;
        isOverloaded = p_isOverloaded;
    }
    
    public boolean isTypeOf(long id) {
        return (OverLoadedController_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/OverLoadedController.java
*********************************************************************/

