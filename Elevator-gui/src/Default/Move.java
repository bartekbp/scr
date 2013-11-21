/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: Move
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/Move.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.RiJEvent;

//----------------------------------------------------------------------------
// Default/Move.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## event Move(int,int) 
public class Move extends RiJEvent {
    
    public static final int Move_Default_id = 18620;		//## ignore 
    
    public int level;
    public int origin;
    
    // Constructors
    
    public  Move(int p_level, int p_origin) {
        lId = Move_Default_id;
        level = p_level;
        origin = p_origin;
    }
    
    public boolean isTypeOf(long id) {
        return (Move_Default_id==id);
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/Move.java
*********************************************************************/

