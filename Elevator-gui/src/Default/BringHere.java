/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: BringHere
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/BringHere.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/BringHere.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event BringHere(int) 
public class BringHere extends RiJEvent {
    
    public static final int BringHere_Default_id = 18619;		//## ignore 
    
    public int level;
    
    // Constructors
    
    public  BringHere(int p_level) {
        lId = BringHere_Default_id;
        level = p_level;
    }
    
    public boolean isTypeOf(long id) {
        return (BringHere_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/BringHere.java
*********************************************************************/

