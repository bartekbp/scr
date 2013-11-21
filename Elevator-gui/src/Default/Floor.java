/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: Floor
//!	Generated Date	: Thu, 21, Nov 2013 
	File Path	: exe/DefaultConfig/Default/Floor.java
*********************************************************************/

package Default;


//----------------------------------------------------------------------------
// Default/Floor.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class Floor 
public class Floor {
    
    protected boolean areDoorsOpened;		//## attribute areDoorsOpened 
    
    protected boolean isOverloaded;		//## attribute isOverloaded 
    
    protected Elevator el;		//## link el 
    
    
    // Constructors
    
    //## auto_generated 
    public  Floor() {
    }
    
    //## auto_generated 
    public boolean getAreDoorsOpened() {
        return areDoorsOpened;
    }
    
    //## auto_generated 
    public void setAreDoorsOpened(boolean p_areDoorsOpened) {
        areDoorsOpened = p_areDoorsOpened;
    }
    
    //## auto_generated 
    public boolean getIsOverloaded() {
        return isOverloaded;
    }
    
    //## auto_generated 
    public void setIsOverloaded(boolean p_isOverloaded) {
        isOverloaded = p_isOverloaded;
    }
    
    //## auto_generated 
    public Elevator getEl() {
        return el;
    }
    
    //## auto_generated 
    public void __setEl(Elevator p_Elevator) {
        el = p_Elevator;
    }
    
    //## auto_generated 
    public void _setEl(Elevator p_Elevator) {
        if(el != null)
            {
                el._removeFl(this);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._addFl(this);
            }
        _setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void _clearEl() {
        el = null;
    }
    
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/Floor.java
*********************************************************************/

