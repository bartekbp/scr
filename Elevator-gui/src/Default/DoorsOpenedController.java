/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: DoorsOpenedController
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/DoorsOpenedController.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/DoorsOpenedController.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event DoorsOpenedController(boolean) 
public class DoorsOpenedController extends RiJEvent {
    
    public static final int DoorsOpenedController_Default_id = 18629;		//## ignore 
    
    public boolean areOpened;
    
    // Constructors
    
    public  DoorsOpenedController(boolean p_areOpened) {
        lId = DoorsOpenedController_Default_id;
        areOpened = p_areOpened;
    }
    
    public boolean isTypeOf(long id) {
        return (DoorsOpenedController_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/DoorsOpenedController.java
*********************************************************************/

