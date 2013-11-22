/*********************************************************************
	Rhapsody	: 8.0.3
	Login		: janiec
	Component	: exe
	Configuration 	: DefaultConfig
	Model Element	: LoadController
//!	Generated Date	: Fri, 22, Nov 2013 
	File Path	: exe/DefaultConfig/Default/LoadController.java
*********************************************************************/

package Default;

//## auto_generated
import com.ibm.rational.rhapsody.oxf.*;
//## auto_generated
import com.ibm.rational.rhapsody.oxf.states.*;

//----------------------------------------------------------------------------
// Default/LoadController.java                                                                  
//----------------------------------------------------------------------------

//## package Default 


//## class LoadController 
public class LoadController implements RiJStateConcept {
    
    public Reactive reactive;		//## ignore 
    
    protected boolean isOverloaded;		//## attribute isOverloaded 
    
    protected Elevator el;		//## link el 
    
    //#[ ignore 
    public static final int RiJNonState=0;
    public static final int Waiting=1;
    //#]
    protected int rootState_subState;		//## ignore 
    
    protected int rootState_active;		//## ignore 
    
    
    //## statechart_method 
    public RiJThread getThread() {
        return reactive.getThread();
    }
    
    //## statechart_method 
    public void schedTimeout(long delay, long tmID, RiJStateReactive reactive) {
        getThread().schedTimeout(delay, tmID, reactive);
    }
    
    //## statechart_method 
    public void unschedTimeout(long tmID, RiJStateReactive reactive) {
        getThread().unschedTimeout(tmID, reactive);
    }
    
    //## statechart_method 
    public boolean isIn(int state) {
        return reactive.isIn(state);
    }
    
    //## statechart_method 
    public boolean isCompleted(int state) {
        return reactive.isCompleted(state);
    }
    
    //## statechart_method 
    public RiJEventConsumer getEventConsumer() {
        return (RiJEventConsumer)reactive;
    }
    
    //## statechart_method 
    public void gen(RiJEvent event) {
        reactive._gen(event);
    }
    
    //## statechart_method 
    public void queueEvent(RiJEvent event) {
        reactive.queueEvent(event);
    }
    
    //## statechart_method 
    public int takeEvent(RiJEvent event) {
        return reactive.takeEvent(event);
    }
    
    // Constructors
    
    //## auto_generated 
    public  LoadController(RiJThread p_thread) {
        reactive = new Reactive(p_thread);
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
                el.__setLc(null);
            }
        __setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void setEl(Elevator p_Elevator) {
        if(p_Elevator != null)
            {
                p_Elevator._setLc(this);
            }
        _setEl(p_Elevator);
    }
    
    //## auto_generated 
    public void _clearEl() {
        el = null;
    }
    
    //## auto_generated 
    public boolean startBehavior() {
        boolean done = false;
        done = reactive.startBehavior();
        return done;
    }
    
    //## ignore 
    public class Reactive extends RiJStateReactive {
        
        // Default constructor 
        public Reactive() {
            this(RiJMainThread.instance());
        }
        
        
        // Constructors
        
        public  Reactive(RiJThread p_thread) {
            super(p_thread);
            initStatechart();
        }
        
        //## statechart_method 
        public boolean isIn(int state) {
            if(rootState_subState == state)
                {
                    return true;
                }
            return false;
        }
        
        //## statechart_method 
        public boolean isCompleted(int state) {
            return true;
        }
        
        //## statechart_method 
        public void rootState_entDef() {
            {
                rootState_enter();
                rootStateEntDef();
            }
        }
        
        //## statechart_method 
        public int rootState_dispatchEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(rootState_active == Waiting)
                {
                    res = Waiting_takeEvent(id);
                }
            return res;
        }
        
        //## auto_generated 
        protected void initStatechart() {
            rootState_subState = RiJNonState;
            rootState_active = RiJNonState;
        }
        
        //## statechart_method 
        public void Waiting_enter() {
            rootState_subState = Waiting;
            rootState_active = Waiting;
            WaitingEnter();
        }
        
        //## statechart_method 
        public int WaitingTakeOverLoaded() {
            OverLoaded params = (OverLoaded) event;
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            //#[ transition 1 
            if(el.effectors != null) {
            	el.effectors.debugMessage("overload contr");
            }
            int level = el.hc.getLevel();  
            isOverloaded = params.isOverloaded;
            el.gen(new OverLoadedController(level, params.isOverloaded));
            //#]
            res = RiJStateReactive.TAKE_EVENT_COMPLETE;
            return res;
        }
        
        //## statechart_method 
        public void Waiting_entDef() {
            Waiting_enter();
        }
        
        //## statechart_method 
        public int rootState_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            return res;
        }
        
        //## statechart_method 
        public void WaitingEnter() {
        }
        
        //## statechart_method 
        public void rootState_enter() {
            rootStateEnter();
        }
        
        //## statechart_method 
        public void rootStateEnter() {
        }
        
        //## statechart_method 
        public int Waiting_takeEvent(short id) {
            int res = RiJStateReactive.TAKE_EVENT_NOT_CONSUMED;
            if(event.isTypeOf(OverLoaded.OverLoaded_Default_id))
                {
                    res = WaitingTakeOverLoaded();
                }
            
            return res;
        }
        
        //## statechart_method 
        public void Waiting_exit() {
            WaitingExit();
        }
        
        //## statechart_method 
        public void rootStateEntDef() {
            Waiting_entDef();
        }
        
        //## statechart_method 
        public void WaitingExit() {
        }
        
        //## statechart_method 
        public void rootStateExit() {
        }
        
    }
}
/*********************************************************************
	File Path	: exe/DefaultConfig/Default/LoadController.java
*********************************************************************/

