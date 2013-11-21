/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: DoorsOpened
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/DoorsOpened.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/DoorsOpened.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event DoorsOpened(int,boolean) 
public class DoorsOpened extends RiJEvent {
    
    public static final int DoorsOpened_Default_id = 18627;		//## ignore 
    
    public int level;
    public boolean areOpened;
    
    // Constructors
    
    public  DoorsOpened(int p_level, boolean p_areOpened) {
        lId = DoorsOpened_Default_id;
        level = p_level;
        areOpened = p_areOpened;
    }
    
    public boolean isTypeOf(long id) {
        return (DoorsOpened_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/DoorsOpened.java
*********************************************************************/

