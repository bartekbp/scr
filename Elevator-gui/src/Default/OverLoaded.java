/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: OverLoaded
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/OverLoaded.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/OverLoaded.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event OverLoaded(boolean) 
public class OverLoaded extends RiJEvent {
    
    public static final int OverLoaded_Default_id = 18626;		//## ignore 
    
    public boolean isOverloaded;
    
    // Constructors
    
    public  OverLoaded(boolean p_isOverloaded) {
        lId = OverLoaded_Default_id;
        isOverloaded = p_isOverloaded;
    }
    
    public boolean isTypeOf(long id) {
        return (OverLoaded_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/OverLoaded.java
*********************************************************************/

